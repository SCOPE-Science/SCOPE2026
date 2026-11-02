"""Exact rational checks for quadratic statistics of the twisted baker map.

Run with Python 3 and SymPy: python verification/check_energy.py
This checker supplements the independent algebraic proof in RESULT.md.
"""
import sympy as S

u, v, z = S.symbols('u v z')
Q = S.Rational
mons = [S.Integer(1), u, v, u**2, u*v, v**2]


def P(f):
    """Normalized transfer of the two square branches."""
    return S.expand((f.subs({u: (u-1)/2, v: v}, simultaneous=True)
                     +f.subs({u: (v+1)/2, v: -u}, simultaneous=True))/2)


def coeffs(f):
    poly = S.Poly(S.expand(f), u, v)
    return S.Matrix([poly.coeff_monomial(m) for m in mons])


def mean(f):
    return S.simplify(S.integrate(S.integrate(f, (u,-1,1)), (v,-1,1))/4)


q = u*u + v*v - Q(2,3)
assert P(S.Integer(1)) == 1
assert mean(q) == 0
assert mean(q*q) == Q(8,45)
mat = S.Matrix.hstack(*(coeffs(P(m)) for m in mons))
assert S.factor(mat.charpoly().as_expr()) == S.factor(
    (S.Symbol('lambda')-1)*(S.Symbol('lambda')-Q(5,8))
    * (S.Symbol('lambda')**2-Q(3,4)*S.Symbol('lambda')+Q(1,4))
    * S.Symbol('lambda')**2)
assert S.factor(P(u)-u/4-v/4) == 0
assert S.factor(P(v)+u/2-v/2) == 0
E = q-Q(10,11)*u+Q(2,11)*v
assert S.simplify(P(E)-Q(5,8)*E) == 0
assert S.factor(q - E - Q(10,11)*u + Q(2,11)*v) == 0
assert mean(q*u) == 0 and mean(q*v) == 0

h = Q(5,3)*q-Q(4,3)*u+Q(2,3)*v
assert S.simplify((h-P(h))-P(q)) == 0
assert mean(h) == 0
L = {u: 1+2*u, v:v}
R = {u: -v, v: 2*u-1}
dL = S.expand(q+h-h.subs(L, simultaneous=True))
dR = S.expand(q+h-h.subs(R, simultaneous=True))
assert S.expand((dL.subs({u:(u-1)/2,v:v},simultaneous=True)+
                 dR.subs({u:(v+1)/2,v:-u},simultaneous=True))/2) == 0
sigma2 = S.simplify((S.integrate(S.integrate(dL**2,(u,-1,0)),(v,-1,1))+
                     S.integrate(S.integrate(dR**2,(u,0,1)),(v,-1,1)))/4)
assert sigma2 == Q(104,135)

# Exact infinite correlations via a finite transfer matrix (k=0 through 24).
for k in range(25):
    value = S.expand((S.Matrix(mons).T * (mat**k) * coeffs(q))[0])
    assert mean(q*value) == Q(8,45)*Q(5,8)**k

# Finite-sample variance closed form and asymptotic Green--Kubo variance.
for n in range(1,30):
    direct = n*Q(8,45) + 2*sum((n-k)*Q(8,45)*Q(5,8)**k for k in range(1,n))
    closed = n*Q(104,135)-Q(128,81)*(1-Q(5,8)**n)
    assert S.simplify(direct-closed) == 0
assert S.simplify(Q(8,45)*(1+2*Q(5,8)/(1-Q(5,8)))-sigma2) == 0

print('PASS: invariant transfer, exact polynomial spectrum, quadratic eigenvector,')
print('      25 covariances, 29 finite variances, martingale kernel and variance.')
