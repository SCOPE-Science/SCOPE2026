"""Supplementary deterministic finite checks of the arc-plane extremal ratios.
This file does not replace the all-parameter mathematical proof.
"""
import math
import random

rng = random.Random(20261008)
for theta in (0.17, 0.70, math.pi / 2, 2.2, 3.0):
    s = theta / 2
    c, h = math.cos(s), math.sin(s)
    y = min(math.tan(s)**2, 1.0)

    def sampled_norm_sq(u, v):
        angles = (-s, -s/2, 0, s/2, s, -math.pi/4, math.pi/4)
        return max(abs(u*math.cos(r) - 1j*v*math.sin(r))**2
                   for r in angles if -s <= r <= s)

    M = max(1.0, c*c + h*h / y)
    m = min(1.0 / (1.0 + y), h*h / y)
    assert abs(M / m - 2) < 1e-10
    assert abs(min(sampled_norm_sq(1, 1)/(1+y),
                   sampled_norm_sq(0, 1)/y)-m) < 1e-10
    assert abs(sampled_norm_sq(1, 1j/math.sqrt(y))/2-M) < 1e-10
    for _ in range(10000):
        u = complex(rng.gauss(0, 1), rng.gauss(0, 1))
        v = complex(rng.gauss(0, 1), rng.gauss(0, 1))
        r = sampled_norm_sq(u, v)/(abs(u)**2+y*abs(v)**2)
        assert m-1e-11 <= r <= M+1e-11
print("ARC_HILBERT_FINITE_CHECK_OK")
