import sympy as sp

s = sp.sqrt(2)
x, y = sp.symbols("x y")
p3 = 1 - x - y
nodes = (-1, 0, 1)
weights = (x, y, p3)
mu = sp.expand(sum(w*z for w, z in zip(weights, nodes)))

raw = [sp.expand(w*(mu-z)**4) for w, z in zip(weights, nodes)]
den = sp.expand(sum(raw))
T = [sp.factor(r/den) for r in raw]
Txy = sp.Matrix(T[:2])
J = sp.simplify(Txy.jacobian((x, y)))

A = sp.Rational(3,8) + s/4
B = sp.Rational(3,8) - s/4
pminus = {x:A, y:sp.Rational(1,4)}
pplus = {x:B, y:sp.Rational(1,4)}

Tm = [sp.simplify(t.subs(pminus)) for t in T]
Tp = [sp.simplify(t.subs(pplus)) for t in T]
assert Tm == [B, sp.Rational(1,4), A]
assert Tp == [A, sp.Rational(1,4), B]

Jm = sp.simplify(J.subs(pminus))
Jp = sp.simplify(J.subs(pplus))

expected_m = sp.Matrix([
    [5-7*s/2, s/4],
    [7*s, 5+7*s/2],
])
expected_p = sp.Matrix([
    [5+7*s/2, -s/4],
    [-7*s, 5-7*s/2],
])

assert sp.simplify(Jm-expected_m) == sp.zeros(2)
assert sp.simplify(Jp-expected_p) == sp.zeros(2)
assert sp.simplify(Jp*Jm + 3*sp.eye(2)) == sp.zeros(2)
assert sp.simplify(Jm*Jp + 3*sp.eye(2)) == sp.zeros(2)

print("VERIFY_OK")
