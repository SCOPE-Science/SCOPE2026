import sympy as sp

lam, d = sp.symbols("lam d")
J = sp.Matrix([
    [-40, 40, 0, 1],
    [10, 25, 0, 0],
    [0, 0, -3, 0],
    [d, 0, 0, 0],
])
expected = (lam + 3) * (lam**3 + 15*lam**2 - (1400 + d)*lam + 25*d)
actual = sp.expand(J.charpoly(lam).as_expr())
assert sp.expand(actual - expected) == 0
q = lam**3 + 15*lam**2 - (1400 + d)*lam + 25*d
assert sp.expand(q.subs(lam, -40) - (16000 + 65*d)) == 0
assert sp.expand(q.subs(lam, 0) - 25*d) == 0
assert sp.expand(q.subs(lam, 25) + 10000) == 0
assert sp.expand(q.subs(lam, -3) - (4308 + 28*d)) == 0
roots = sorted(float(sp.re(r)) for r in sp.nroots(q.subs(d, 15)))
reference = [-45.963082582082144, 0.2657797580076817, 30.697302824074466]
assert max(abs(a-b) for a,b in zip(roots, reference)) < 1e-10
assert roots[0] < -40 < 0 < roots[1] < 25 < roots[2]
print("VERIFY_OK")
