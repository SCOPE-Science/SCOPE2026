from sympy import Matrix, diff, exp, simplify, symbols

x, y, z = symbols("x y z")
a, b = symbols("a b", positive=True)
s, t, lam = symbols("s t lam", real=True)

F = Matrix([y, -a*x + y*z, x**2 - b*y**2])
vars_ = (x, y, z)

divF = simplify(sum(diff(F[i], vars_[i]) for i in range(3)))
assert divF == z

Es = {x: 0, y: 0, z: s}
assert F.subs(Es) == Matrix([0, 0, 0])

J = F.jacobian(vars_)
Js = J.subs(Es)
charpoly = simplify((lam*Matrix.eye(3) - Js).det())
assert simplify(charpoly - lam*(lam**2 - s*lam + a)) == 0

def lie(poly):
    return simplify(sum(diff(poly, vars_[i]) * F[i] for i in range(3)))

assert simplify(lie(z) - (x**2 - b*y**2)) == 0
assert simplify(lie(a*x**2 + y**2) - 2*y**2*z) == 0

volume_factor = exp(s*t)
assert simplify(diff(volume_factor, t) - s*volume_factor) == 0
assert volume_factor.subs(t, 0) == 1

print("divergence =", divF)
print("charpoly =", charpoly)
print("moment_balance =", lie(z))
print("weighted_balance =", lie(a*x**2 + y**2))
print("equilibrium_volume_factor =", volume_factor)
print("VERIFY_OK")
