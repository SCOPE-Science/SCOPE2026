#!/usr/bin/env python3
"""Self-contained exact constants and finite-rectangle diagnostic sampling."""
from fractions import Fraction as F
from math import exp, log
from random import Random

# Integral over 0<b<a<t of b(a+b): (5/24)t^4.
half_square = F(1, 4) + F(1, 3) - F(3, 8)
assert half_square == F(5, 24)
full_square = 2 * half_square
assert full_square == F(5, 12)
vertical_one_sign = full_square / 5
assert vertical_one_sign == F(1, 12)
vertical_both_signs = 2 * vertical_one_sign
assert 6 * vertical_both_signs == 1
assert 6 * F(1, 12) == F(1, 2)
print('PASS exact: total mass 1, each logarithmic half mass 1/2')

# Importance sample zeta uniformly in (-2,1), s uniformly in (0,1).
# With u=h*exp(zeta*log(1/h)), v=h^2*s/u, the Jacobian is
# h^2 log(1/h). Because the zeta-interval has length 3 and
# the ordered horizontal gap density is 6*(1-u-v), the normalized
# estimator weight is 18*(1-u-v)*1_Acute.
# Sampling beyond (-1,1) retains lower-gap endpoint corrections.
rng = Random(87443021)
N = 400000
for h in (0.05, 0.01, 0.002, 0.0003, 1e-6, 1e-9):
    log_inv_h = log(1 / h)
    sum_w = 0.0
    sum_right = 0.0
    sum_height = 0.0
    cdf_bins = [0.0] * 4
    thresholds = (0.2, 0.4, 0.6, 0.8)
    for i in range(N):
        zeta = -2 + 3 * rng.random()
        s = rng.random()
        y1, y2, y3 = rng.random(), rng.random(), rng.random()
        u = h * exp(zeta * log_inv_h)
        v = h * h * s / u
        if u + v >= 1:
            continue
        a, b = y2 - y1, y2 - y3
        if u * v >= h * h * a * b:
            continue
        if u * (u + v) + h * h * a * (a-b) <= 0:
            continue
        if v * (u + v) + h * h * b * (b-a) <= 0:
            continue
        weight = 18 * (1 - u - v)
        sum_w += weight
        sum_right += weight if zeta > 0 else 0.0
        sum_height += weight * y2
        for j, t in enumerate(thresholds):
            if y2 <= t:
                cdf_bins[j] += weight
    ratio = sum_w / N
    right_share = sum_right / sum_w
    avg_height = sum_height / sum_w
    print(f'h={h:.5g}, normalized acute mass={ratio:.6f}, '
          f'log positive share={right_share:.5f}, vertical mean={avg_height:.5f}')
    assert abs(avg_height - 0.5) < 0.045
    if h <= 1e-6:
        assert abs(ratio - 1) < 0.045
        assert abs(right_share - 0.5) < 0.06
        for t, observed in zip(thresholds, cdf_bins):
            expected = (t**5 + 1 - (1-t)**5) / 2
            assert abs(observed / sum_w - expected) < 0.02
print('PASS finite-height diagnostics; limiting law is established analytically.')
