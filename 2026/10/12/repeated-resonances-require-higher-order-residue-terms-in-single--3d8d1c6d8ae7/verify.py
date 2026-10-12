import sympy as sp

alpha, z, w = sp.symbols("alpha z w")
r = -1 / sp.sqrt(6)
V = sp.Matrix([
    [sp.sqrt(3)/6, -sp.sqrt(6)/3, -sp.Rational(1,2)],
    [2*sp.sqrt(2)/3, sp.Rational(1,3), 0],
    [sp.Rational(1,6), -sp.sqrt(2)/3, sp.sqrt(3)/2],
])
assert sp.simplify(V.T*V) == sp.eye(3)
assert sp.simplify(V.det()) == 1

U = sp.Matrix([
    [0, 0, 0, alpha],
    [sp.sqrt(3)/6, -sp.sqrt(6)/3, -sp.Rational(1,2), 0],
    [2*sp.sqrt(2)/3, sp.Rational(1,3), 0, 0],
    [sp.Rational(1,6), -sp.sqrt(2)/3, sp.sqrt(3)/2, 0],
])
cp = sp.expand(U.charpoly(z).as_expr())
target = sp.expand(z**2*(z-r)**2 - alpha*(1-r*z)**2)
assert sp.simplify(cp-target) == 0

U0 = U.subs(alpha, 0)
M = U0-r*sp.eye(4)
assert 4-M.rank() == 1
assert 4-(M**2).rank() == 2

S = sp.simplify(w**2*(w-r)**2/(1-r*w)**2)
series = sp.series(S, w, 0, 13).removeO().expand()
for n in range(13):
    got = series.coeff(w, n)
    want = 0
    if n >= 2:
        want = (6 if n == 2 else 0) + sp.Rational(5,36)*(5*n-17)*r**(n-4)
    assert sp.simplify(got-want) == 0

print("VERIFY_OK orthogonal=1 double_root=-sqrt(6)/6 jordan_chain=2 coefficients=13")
