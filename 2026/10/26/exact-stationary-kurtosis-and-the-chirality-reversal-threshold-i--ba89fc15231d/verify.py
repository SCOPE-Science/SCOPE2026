"""Exact symbolic checks for stationary kurtosis in the chirality-switching trapped swimmer.
Requires Python 3.10+ and sympy. Run: python verify.py
No external data or downloads are needed.
"""
import sympy as S
from functools import lru_cache

d, g, w = S.symbols('d g w', real=True)
I = S.I

@lru_cache(None)
def moment(p, q, sector):
    """Invariant harmonic moment; sector=0 or 1 denotes sigma exponent."""
    if p == q == 0:
        return S.Integer(1 if sector == 0 else 0)
    k = q - p
    c = p + q + d * k * k
    c1 = c + 2*g
    def rhs(s):
        ans = S.Integer(0)
        if p:
            ans += p * moment(p-1,q,s)
        if q:
            ans += q * moment(p,q-1,s)
        return ans
    r0, r1 = rhs(0), rhs(1)
    det = c*c1 + k*k*w*w
    return S.cancel(((c1*r0 + I*k*w*r1) if sector == 0 else
                     (c*r1 + I*k*w*r0))/det)

u = w*w
a = 1+d+2*g
L1 = (1+d)*a + u
L2 = u + d*d + 2*d*g + 6*d + 6*g + 9
L3 = u + 4*d*d + 2*d*g + 4*d + g + 1
A = (7*d+3)*a*a*(d+2*g+3)*(2*d+g+1)
B = -a*(10*d*d-7*d*g-2*d-14*g*g-27*g-10)
P = A+B*u+(1-4*g)*u*u
m2 = moment(1,1,0)
m4 = moment(2,2,0)
kurt = S.Rational(3,2)*m4/m2**2-3
assert S.cancel(m2-a/L1) == 0
assert S.cancel(m4-(2*a*a*L2*L3-P)/(L1*L1*L2*L3)) == 0
assert S.cancel(kurt+3*P/(2*a*a*L2*L3)) == 0
assert S.cancel(kurt.subs({d:0,g:0})+S.Rational(3,2)) == 0
# Positive / negative / positive: rigorous reentrant sample.
params={d:S.Integer(10),g:S.Rational(1,10)}
assert [S.sign(P.subs({**params,w:t})) for t in (0,30,200)] == [1,-1,1]
# Unique crossing when g>1/4: quadratic leading coefficient is negative.
params={d:S.Integer(0),g:S.Integer(1)}
assert [S.sign(P.subs({**params,w:t})) for t in (5,10)] == [1,-1]
print('PASS: exact second and fourth moments, kurtosis identity, boundary and samples')
