import sympy as sp

a, x, y, q = sp.symbols("a x y q")
b = 2 - a
z = 1 - x - y

gx = sp.expand(1 - x - a*y - b*z)
expected = sp.expand((a - 1)*(z - y))
assert sp.simplify(gx - expected) == 0

cov = sp.Rational(1, 2) * (sp.Rational(1, 3) - q) - sp.Rational(1, 9)
sigma2 = q - sp.Rational(1, 9)
assert sp.simplify(cov + sigma2/sp.Integer(2)) == 0

print("ALGEBRA_OK")
