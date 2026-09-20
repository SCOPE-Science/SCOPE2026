import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
a, b, c = sp.symbols('a b c', real=True)
R, m, w, th = sp.symbols('R m w th', real=True)

f = (y, z, -c*x - b*y - a*z + x**2)
J = y*z + sp.Rational(1, 2)*a*y**2 + sp.Rational(1, 2)*c*x**2 - sp.Rational(1, 3)*x**3
lie_J = sum(sp.diff(J, q)*fq for q, fq in zip((x, y, z), f))
balance_residual = sp.factor(lie_J - (z**2 - b*y**2))
assert balance_residual == 0

# Equality in the periodic Wirtinger step forces a pure first harmonic.
# Setting w^2=b cancels x''' + b x'.  The remaining equation is
# a*x'' + c*x - x^2 = 0.  For x=m+R*cos(th), only -x^2 contributes
# a second harmonic, with coefficient -R^2/2.
X = m + R*sp.cos(th)
remaining = sp.expand_trig(-a*w**2*R*sp.cos(th) + c*X - X**2)
second_harmonic_coefficient = sp.expand_trig(sp.integrate(remaining*sp.cos(2*th), (th, 0, 2*sp.pi))/sp.pi)
second_harmonic_coefficient = sp.simplify(second_harmonic_coefficient)
assert second_harmonic_coefficient == -R**2/2

print(f"balance_residual = {balance_residual}")
print(f"equality_second_harmonic_coefficient = {second_harmonic_coefficient}")
print("verification = PASS")
