#!/usr/bin/env python3
import math

EULER_GAMMA = 0.577215664901532860606512090082402431
A = math.pi / math.sqrt(6.0)
SQRT2 = math.sqrt(2.0)
SQRT2PI = math.sqrt(2.0 * math.pi)


def phi(x):
    return math.exp(-0.5*x*x) / SQRT2PI


def Phi(x):
    return 0.5 * (1.0 + math.erf(x / SQRT2))


def gumbel_cdf(y):
    return math.exp(-math.exp(-y))


def central_gumbel(c):
    return gumbel_cdf(EULER_GAMMA + A*c) - gumbel_cdf(EULER_GAMMA - A*c)


def central_normal(c):
    return 2.0*Phi(c) - 1.0


def tail_gumbel(c):
    return 1.0 - central_gumbel(c)


def tail_normal(c):
    return 1.0 - central_normal(c)


def lower_ratio_bound_to_mills(c):
    x = math.exp(-EULER_GAMMA - A*c)
    return c*x / (2.0*(1.0+x)*phi(c))


assert central_gumbel(1.0) > central_normal(1.0)
for c in (3.0, 4.0, 5.0, 6.0):
    assert central_gumbel(c) < central_normal(c)
assert lower_ratio_bound_to_mills(3.0) > 4.0
prev = lower_ratio_bound_to_mills(3.0)
for j in range(1, 341):
    c = 3.0 + j/20.0
    cur = lower_ratio_bound_to_mills(c)
    assert cur > prev
    prev = cur

lo, hi = 2.0, 2.5
for _ in range(80):
    mid = 0.5*(lo+hi)
    if central_gumbel(mid) - central_normal(mid) > 0.0:
        lo = mid
    else:
        hi = mid
root = 0.5*(lo+hi)
assert 2.05 < root < 2.06

for c in (4.0, 5.0, 6.0):
    asym = math.sqrt(math.pi/2.0)*c*math.exp(0.5*c*c - A*c - EULER_GAMMA)
    ratio = tail_gumbel(c)/tail_normal(c)
    assert ratio > 0.4*asym and ratio < 1.7*asym

print(f"VERIFY_OK root_locator={root:.15f} R3={lower_ratio_bound_to_mills(3.0):.12f}")
