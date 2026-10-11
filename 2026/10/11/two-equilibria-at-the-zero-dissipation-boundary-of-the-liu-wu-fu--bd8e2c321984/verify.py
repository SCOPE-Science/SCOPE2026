import sympy as sp

x, y, z = sp.symbols("x y z", real=True)
a, b, c, d = sp.symbols("a b c d", nonzero=True, real=True)
lam = sp.symbols("lam")

F = sp.Matrix([
    y * (a - z),
    z * (x - b),
    x * (c + y) - d * z,
])
vars_ = (x, y, z)
J = F.jacobian(vars_)

E0 = {x: 0, y: 0, z: 0, d: 0}
E1 = {x: b, y: -c, z: a, d: 0}

assert all(sp.simplify(v.subs(E0)) == 0 for v in F)
assert all(sp.simplify(v.subs(E1)) == 0 for v in F)

J0 = sp.simplify(J.subs(E0))
J1 = sp.simplify(J.subs(E1))

chi0 = sp.factor((lam * sp.eye(3) - J0).det())
chi1 = sp.factor((lam * sp.eye(3) - J1).det())

assert sp.expand(chi0 - (lam**3 + a*b*c)) == 0
assert sp.expand(chi1 - (lam**3 - a*b*c)) == 0
assert sp.simplify(sum(sp.diff(F[i], vars_[i]) for i in range(3)) + d) == 0

print("equilibrium_E0 =", sp.Matrix([0, 0, 0]).T)
print("equilibrium_E1 =", sp.Matrix([b, -c, a]).T)
print("chi_E0 =", chi0)
print("chi_E1 =", chi1)
print("divergence =", sp.simplify(sum(sp.diff(F[i], vars_[i]) for i in range(3))))
print("VERIFY_OK")
