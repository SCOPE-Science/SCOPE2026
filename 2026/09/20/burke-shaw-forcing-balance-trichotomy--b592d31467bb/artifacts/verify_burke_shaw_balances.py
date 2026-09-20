import sympy as sp

x, y, z, a, k, g, d = sp.symbols('x y z a k g d', nonzero=True)
xdot = -a*(x+y)
ydot = -k*x*z-y
zdot = g*x*y+d

W = y**2 + (k/g)*z**2
H = z + (g/(2*a))*x**2
x2 = x**2

D = lambda F: sp.expand(sp.diff(F,x)*xdot + sp.diff(F,y)*ydot + sp.diff(F,z)*zdot)

checks = {
    'dW': sp.simplify(D(W) - (-2*y**2 + 2*(k/g)*d*z)),
    'dH': sp.simplify(D(H) - (d-g*x**2)),
    'dx2': sp.simplify(D(x2) - (-2*a*x**2-2*a*x*y)),
    'xdot2': sp.simplify(xdot**2 - a**2*(x+y)**2),
}

for name, residual in checks.items():
    print(f'{name}: {sp.factor(residual)}')
    assert residual == 0

print('all symbolic balance identities verified')
