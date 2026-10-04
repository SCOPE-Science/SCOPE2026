#!/usr/bin/env python3
import math

SQ2 = math.sqrt(2.0)
D = 2.0 - SQ2
TS = SQ2
TE = (3.0 + math.sqrt(21.0)) / 4.0

def tail_ratio(t, r):
    if r == 0.0:
        return 0.5 * math.exp(-SQ2*t)
    if r == 1.0:
        return 0.5 * (1.0+t) * math.exp(-2.0*t)
    c = SQ2*t*math.sqrt(1.0+r*r)
    return (math.exp(-c) - r*r*math.exp(-c/r)) / (2.0*(1.0-r*r))

def sparse_coeff(t):
    return 1.0 - t/SQ2

def equal_coeff_sign_poly(t):
    return 4.0*t*t - 6.0*t - 3.0

def endpoint_log_ratio(t):
    return math.log1p(t) - D*t

# The nonzero crossing lies on the strictly decreasing branch after 1/sqrt(2).
lo, hi = TS, TE
assert endpoint_log_ratio(lo) > 0.0
assert endpoint_log_ratio(hi) < 0.0
for _ in range(120):
    mid = (lo+hi)/2.0
    if endpoint_log_ratio(mid) > 0.0:
        lo = mid
    else:
        hi = mid
TSTAR = (lo+hi)/2.0

assert TS < TSTAR < TE
assert abs(endpoint_log_ratio(TSTAR)) < 5e-15
assert sparse_coeff(1.2) > 0.0
assert sparse_coeff(1.6) < 0.0
assert equal_coeff_sign_poly(1.6) < 0.0
assert equal_coeff_sign_poly(2.1) > 0.0

# Exact endpoint formulas agree with limiting evaluations close to each endpoint.
for t in (1.2, 1.5, 1.75, 2.1, 3.0):
    s0 = tail_ratio(t, 0.0)
    s_eps = tail_ratio(t, 1e-4)
    se = tail_ratio(t, 1.0)
    se_eps = tail_ratio(t, 0.99)
    if t < TS:
        assert s_eps > s0
    if t > TS:
        assert s_eps < s0
    if t < TE:
        assert se_eps < se
    if t > TE:
        assert se_eps > se

# In the coexistence window both endpoints descend under inward perturbation.
t = 1.6
assert TS < t < TE
assert tail_ratio(t, 1e-3) < tail_ratio(t, 0.0)
assert tail_ratio(t, 1.0-1e-4) < tail_ratio(t, 1.0)

print('VERIFY_OK')
print('t_sparse = %.15f' % TS)
print('t_cross  = %.15f' % TSTAR)
print('t_equal  = %.15f' % TE)
