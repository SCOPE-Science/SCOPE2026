"""Exact symbolic checks for the zero-sum real ell-four Euclidean distortion formula.

This validates algebraic reductions. The global extremum and optimal-ellipsoid
steps are analytic, using the cited half-degree principle and a convex averaging
argument, not inferred from finite numerical tests.
"""
import random
from fractions import Fraction
from math import isclose
import sympy as s

n, k = s.symbols('n k', integer=True, positive=True)
a2 = (n-k)/(n*k)
b2 = k/(n*(n-k))
q = s.factor(k*a2**2 + (n-k)*b2**2)
assert s.factor(q - (n/(k*(n-k)) - s.Rational(3)/n)) == 0
q_hi = s.factor(q.subs(k, 1))
assert s.factor(q_hi - (n*n-3*n+3)/(n*(n-1))) == 0
q_even = s.factor(q.subs(k, n/2))
assert s.factor(q_even - 1/n) == 0
q_odd = s.factor(q.subs(k, (n-1)/2))
assert s.factor(q_odd - (n*n+3)/(n*(n*n-1))) == 0
ratio_even = s.factor(q_hi/q_even)
ratio_odd = s.factor(q_hi/q_odd)
assert s.factor(ratio_even - (n*n-3*n+3)/(n-1)) == 0
assert s.factor(ratio_odd - (n*n-3*n+3)*(n+1)/(n*n+3)) == 0

for nn in range(3, 151):
    ks = range(1, nn)
    values = [Fraction(nn, kk*(nn-kk)) - Fraction(3, nn) for kk in ks]
    assert max(values) == Fraction(nn*nn-3*nn+3, nn*(nn-1))
    expected_min = (Fraction(1, nn) if nn%2==0 else Fraction(nn*nn+3, nn*(nn*nn-1)))
    assert min(values) == expected_min

rng = random.Random(2026)
for nn in range(3, 17):
    lo = float(Fraction(1, nn) if nn%2==0 else Fraction(nn*nn+3, nn*(nn*nn-1)))
    hi = float(Fraction(nn*nn-3*nn+3, nn*(nn-1)))
    for _ in range(250):
        vals=[rng.uniform(-1.0,1.0) for _ in range(nn)]
        mean=sum(vals)/nn
        centered=[v-mean for v in vals]
        ss=sum(v*v for v in centered)
        if ss < 1e-15:
            continue
        qr=sum(v**4 for v in centered)/(ss**2)
        assert lo-1e-12 <= qr <= hi+1e-12

# The 3-atom section is exactly Hilbertian after scaling.
u,v = s.symbols('u v', real=True)
w = -u-v
assert s.expand(u**4+v**4+w**4-s.Rational(1,2)*(u*u+v*v+w*w)**2)==0
print('VERIFY_OK: two-level identities, parity formulas, and n=3 identity exact; finite diagnostics passed')
