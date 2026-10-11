import sympy as sp

x, y, z = sp.symbols("x y z", real=True)
a, b, c, d, eps = sp.symbols("a b c d eps", real=True)
xdot = y
ydot = z
zdot = eps - a*x - b**2*y - c*z + d*sp.sinh(x)
H = y*z + sp.Rational(1, 2)*a*x**2 + sp.Rational(1, 2)*c*y**2 - d*sp.cosh(x) - eps*x
Hdot = sp.diff(H, x)*xdot + sp.diff(H, y)*ydot + sp.diff(H, z)*zdot
assert sp.simplify(Hdot - (z**2 - b**2*y**2)) == 0

u, x0 = sp.symbols("u x0", real=True)
F = eps + (-a + c*b**2)*u - c*b**2*x0 + d*sp.sinh(u)
assert sp.simplify(sp.diff(F, u, 2) - d*sp.sinh(u)) == 0
print("VERIFY_OK")
