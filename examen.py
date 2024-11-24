from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para el menú principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el formulario de Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_por_tarro = 9000
        total_sin_descuento = precio_por_tarro * tarros

        # Cálculo del descuento
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)
        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')

# Ruta para el formulario de Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    if request.method == 'POST':
        usuarios = {'juan': 'admin', 'pepe': 'user'}
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username] == password:
            if username == 'juan':
                mensaje = f"Bienvenido administrador {username}"
            else:
                mensaje = f"Bienvenido usuario {username}"
        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
