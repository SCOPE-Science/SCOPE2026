"""Exact symbolic certificate for the heterogeneous Stuart-Landau triad.

Requires Python 3 and SymPy. Run: python verify.py
"""
import sympy as S

s, gamma, x = S.symbols('s gamma x')
B = S.sqrt(28083)
u = [S.Matrix([7, 0]), S.Matrix([S.Rational(71, 14), B/14]),
     S.Matrix([-S.Rational(169, 14), -B/14])]
assert sum(u, S.zeros(2, 1)) == S.zeros(2, 1)
assert [S.simplify(v.dot(v)) for v in u] == [49,169,289]
assert 169-49 == 289-169 == 120
K = S.Matrix([[1,-gamma],[gamma,1]])
J = S.zeros(6)
for j in range(3):
    for k in range(3):
        local = -2*u[j]*u[j].T if j == k else S.zeros(2)
        J[2*j:2*j+2, 2*k:2*k+2] = K+local
rotation = S.Matrix([-u[j][1] if v == 0 else u[j][0]
                     for j in range(3) for v in range(2)])
assert S.simplify(J*rotation) == S.zeros(6, 1)
Q = (s**5 + 1008*s**4 + (280071+9*gamma**2)*s**3
     + (18011228+6084*gamma**2)*s**2
     + (-56497371+939645*gamma**2)*s
     + 28476162*(1+gamma**2))
assert S.simplify(J.charpoly(s).as_expr() - s*Q) == 0
coeffs = S.Poly(Q,s).all_coeffs()
H = S.zeros(5)
for i in range(5):
    for j in range(5):
        k = 2*j-i+1
        if 0 <= k <= 5:
            H[i,j] = coeffs[k]
F = (1359668165778*x**3 + 52078596448637187*x**2
     + 197990312557568849400*x - 22858579814530283205625)
expected = [
    S.Integer(1008),
    4*(747*gamma**2+66075085),
    16*(1136187*gamma**4+45986583240*gamma**2+301112958309785),
    12*F.subs(x,gamma**2),
    341713944*(gamma**2+1)*F.subs(x,gamma**2)
]
for n in range(1,6):
    assert S.factor(H[:n,:n].det()-expected[n-1]) == 0
assert F.subs(x,112) < 0 < F.subs(x,113)
assert all(c > 0 for c in S.Poly(S.diff(F,x), x).all_coeffs())
assert S.simplify(coeffs[-1]-28476162*(1+gamma**2)) == 0
# Representative stable and unstable points: exact Hurwitz signs.
for t in (0,1,10):
    sig=[S.sign(a.subs(gamma,t)) for a in expected]
    assert sig == [1,1,1,-1,-1]
for t in (11,20):
    sig=[S.sign(a.subs(gamma,t)) for a in expected]
    assert sig == [1,1,1,1,1]
# Imaginary-pair frequency at the unique positive threshold.
xi = sorted([S.re(r) for r in S.nroots(F) if abs(float(S.im(r)))<1e-9 and S.re(r)>0])[0]
crit = float(S.sqrt(xi))
a5 = 28476162*(1+xi)
d2 = 4*(747*xi+66075085)
d3 = 16*(1136187*xi**2+45986583240*xi+301112958309785)
assert 10.58 < crit < 10.60
assert 13.18 < float(S.sqrt(a5*d2/d3)) < 13.20
print('EXACT_CERTIFICATE_OK', 'critical_gamma_approximately', crit)
