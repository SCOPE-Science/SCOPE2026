#!/usr/bin/env python3
"""Exact recurrence identities and reproducible supporting tests for BDF2 complete-graph diffusion.
The infinite all-parameter positivity theorem relies on the analytic proof in RESULT.md.
"""
from fractions import Fraction as F
from math import exp


def exp_bounds(q, terms=48):
    """Rigorous rational interval for exp(q), 0<=q<terms+2."""
    q = F(q)
    assert 0 <= q < terms + 2
    t = F(1)
    low = t
    for j in range(1, terms + 1):
        t *= q / j
        low += t
    first_omitted = t * q / (terms + 1)
    high = low + first_omitted / (1 - q / (terms + 2))
    return low, high


for s, low_expected, high_expected in [
    (F(3), F(16), F(22)),
    (F(5,2), F(12), F(13)),
    (F(3,4), F(2), F(5,2)),
    (F(5,4), F(3), F(4)),
    (F(11,6), F(6), F(7)),
    (F(1,2), F(8,5), F(2)),
    (F(1), F(2), F(10,3)),
]:
    low, high = exp_bounds(s)
    assert low_expected < low <= high < high_expected, (s, float(low), float(high))

# Represent u_k = A_k + B_k exp(-s), so every recurrence identity is exact rational arithmetic.
for s in (F(1,4), F(1,2), F(2,3), F(1), F(3), F(15,2), F(33,2)):
    d = 3 + 2*s
    u0 = (F(1), F(0))
    u1 = (F(0), F(1))
    arr = [u0, u1]
    for k in range(2, 5):
        a, b = arr[-1], arr[-2]
        arr.append(((4*a[0]-b[0])/d, (4*a[1]-b[1])/d))
    assert arr[2] == (-1/d, 4/d)
    assert arr[3] == (-4/d**2, (16-d)/d**2)
    assert arr[4] == ((d-16)/d**3, (64-8*d)/d**3)

# Rigorous exact-rational witness, not a floating-point sign test.
lo, hi = exp_bounds(F(3))
upper_e_minus3 = 1 / lo
u2_upper = (4*upper_e_minus3 - 1) / 9
assert u2_upper < F(-1, 12)

# Reproducible finite stress grid; not a substitute for the analytic all-step proof.
smallest = (0.0, 0.0, 0)
count = 0
for j in range(1, 30001):
    s = j / 1000.0
    old, current = 1.0, exp(-s)
    for k in range(2, 71):
        old, current = current, (4*current-old)/(3+2*s)
        assert current > -1/11 - 1e-13
        assert current <= 1 + 1e-13
        count += 1
        if current < smallest[0]:
            smallest = (current, s, k)
assert smallest[2] == 2
print('VERIFY_OK: exact identities, rational exponential certificates,', count,
      'finite recurrence checks; sampled minimum', smallest)
