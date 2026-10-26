#!/usr/bin/env python3
"""Reproduce the decimal minimizer and constant in RESULT.md (standard library only)."""
import math

def f(s):
    return math.log1p(2.0 * s) - math.log1p(-s)

def fp(s):
    return 3.0 / ((1.0 + 2.0 * s) * (1.0 - s))

def h(s):
    return s * fp(s) - f(s)

# h is strictly increasing on (1/4, 1), with opposite endpoint signs.
lo, hi = 0.25, 0.999999999999
assert h(lo) < 0.0 < h(hi)
for _ in range(100):
    mid = (lo + hi) / 2.0
    if h(mid) < 0.0:
        lo = mid
    else:
        hi = mid
s_star = (lo + hi) / 2.0
lambda_star = fp(s_star)
assert abs(h(s_star)) < 1e-12
assert 0.37720 < s_star < 0.37721
assert 2.74564 < lambda_star < 2.74565
print(f"s_star={s_star:.15f}")
print(f"lambda_star={lambda_star:.15f}")
print(f"stationarity_residual={h(s_star):.3e}")
