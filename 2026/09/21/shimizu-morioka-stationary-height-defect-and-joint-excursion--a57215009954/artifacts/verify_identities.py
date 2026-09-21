import sympy as sp

x, y, z, a, b = sp.symbols("x y z a b")
f = sp.Matrix([y, x*(1-z)-a*y, x**2-b*z])

W = x*y - z + z**2/sp.Integer(2) + a*x**2/sp.Integer(2)
gradW = sp.Matrix([sp.diff(W, v) for v in (x, y, z)])
lie_W = sp.expand((gradW.T*f)[0])
target = y**2 - b*z*(z-1)

checks = {
    "lie_W_residual": sp.factor(lie_W-target),
    "equilibrium_plus": tuple(sp.simplify(q.subs({x:sp.sqrt(b), y:0, z:1})) for q in f),
    "equilibrium_minus": tuple(sp.simplify(q.subs({x:-sp.sqrt(b), y:0, z:1})) for q in f),
    "origin": tuple(sp.simplify(q.subs({x:0, y:0, z:0})) for q in f),
    "square_completion_residual": sp.expand((z-sp.Rational(1,2))**2-sp.Rational(1,4)-z*(z-1)),
}

for name, value in checks.items():
    print(f"{name}: {value}")
