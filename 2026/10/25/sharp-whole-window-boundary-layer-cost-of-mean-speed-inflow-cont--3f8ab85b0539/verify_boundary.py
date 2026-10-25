#!/usr/bin/env python3
"""Exact boundary coefficient checks and independent finite-width quadrature.
Uses only the Python standard library. This is a supplementary check;
the uniform boundary-layer limit is proved in RESULT.md.
"""
from fractions import Fraction as F
from math import log, log1p


def polyint(cs, a, b):
    return sum(c * (b ** (i + 1) - a ** (i + 1)) / (i + 1) for i, c in enumerate(cs))

# Left-side raw profile: (y/2)(1-y/2)^2 = y/2-y^2/2+y^3/8.
left_raw = polyint([F(0), F(1, 2), F(-1, 2), F(1, 8)], F(0), F(2))
# Left clipped profile on y in [0,1]: y^3/8;
# on y in [1,2] it agrees with the raw profile.
left_clip = polyint([F(0), F(0), F(0), F(1, 8)], F(0), F(1)) + polyint(
    [F(0), F(1, 2), F(-1, 2), F(1, 8)], F(1), F(2)
)
assert left_raw == F(1, 6), left_raw
assert left_clip == F(1, 12), left_clip
assert 2 * left_raw == F(1, 3)
assert 2 * left_clip == F(1, 6)
print('EXACT_BOUNDARY_COEFFICIENTS_OK', left_raw, left_clip)


def midpoint_integral(fun, a, b, n=20000):
    h = (b - a) / n
    return h * sum(fun(a + (i + .5) * h) for i in range(n))


def exact_excess(mu, eps, horizon, clipped):
    lo, hi = mu - eps, mu + eps
    a, b = 1 / hi, 1 / lo
    assert horizon > 2*b-a
    r0 = 1 / mu
    def integrand(t):
        if t < b-a:
            edge = 1 / (b-t)
            q = (edge-lo)/(2*eps)
            mean = log1p((edge-lo)/lo)/(edge-lo)
            l, r = b-t, b
        elif t > horizon-b:
            edge = 1 / (horizon-t)
            q = (hi-edge)/(2*eps)
            mean = -log1p((edge-hi)/hi)/(hi-edge)
            l, r = a, horizon-t
        else:
            q = 1.
            mean = log(hi/lo)/(2*eps)
            l, r = a, b
        delay = min(max(r0,l),r) if clipped else r0
        return q * (mean-delay)**2
    return sum(midpoint_integral(integrand, l, r) for l,r in
               [(0,b-a), (b-a,horizon-b), (horizon-b,horizon-a)])

for mu, horizon, eps_values in [(1.,4.,[.08,.04,.02,.01,.005]),
                                (2.,3.,[.08,.04,.02,.01])]:
    print('PARAMS', mu, horizon)
    for eps in eps_values:
        raw = exact_excess(mu,eps,horizon,False)
        clipped = exact_excess(mu,eps,horizon,True)
        scale = eps**3 / mu**6
        print('epsilon',eps,'raw/scale',f'{raw/scale:.9f}',
              'clip/scale',f'{clipped/scale:.9f}')
        assert raw > clipped > 0
        assert abs(raw/scale - 1/3) < 2*eps
        assert abs(clipped/scale - 1/6) < 2*eps
print('NUMERIC_CONVERGENCE_CHECKS_OK')
