#!/usr/bin/env python3
import math
import random


def poly_add(a, b, sign=1):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + sign * (b[i] if i < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_scale(a, c):
    return [c * x for x in a]


def lam_star(h):
    s = math.hypot(1.0, h)
    if h <= 1.0:
        return s * (h + 2.0) / (2.0 * h)
    return (h * h + 5.0) / (2.0 * s)


def lam_liu(h):
    s = math.hypot(1.0, h)
    ma = 0.5 * math.sqrt(s * s + 8.0)
    wa = math.sqrt(8.0 * s * (s + 1.0)) / (s + 2.0)
    return 2.0 * ma / wa


def defect(h, x, y, lam):
    s = math.hypot(1.0, h)
    pa = math.hypot(x + 1.0, y)
    pb = math.hypot(x - 1.0, y)
    pc = math.hypot(x, h - y)
    ra = (h - y - h * x) / s
    rb = (h - y + h * x) / s
    rc = y
    return pa + pb + pc - lam * (ra + rb) - 2.0 * rc


# Exact polynomial identity:
# 2(s+1)(s^2+4)^2 - s(s^2+8)(s+2)^2
# = (s-2)^2(s^3+2s^2+8s+8).
s = [0, 1]
one_plus_s = [1, 1]
s2_plus_4 = [4, 0, 1]
s2_plus_8 = [8, 0, 1]
s_plus_2 = [2, 1]
s_minus_2 = [-2, 1]
cubic = [8, 8, 2, 1]
lhs = poly_add(
    poly_scale(poly_mul(one_plus_s, poly_mul(s2_plus_4, s2_plus_4)), 2),
    poly_mul(s, poly_mul(s2_plus_8, poly_mul(s_plus_2, s_plus_2))),
    sign=-1,
)
rhs = poly_mul(poly_mul(s_minus_2, s_minus_2), cubic)
assert lhs == rhs, (lhs, rhs)

# Deterministic parameter comparisons.
for i in range(1, 20001):
    h = math.exp(math.log(0.02) + (math.log(50.0) - math.log(0.02)) * i / 20001.0)
    assert lam_liu(h) <= lam_star(h) + 2e-13

# Deterministic interior-point stress test.
rng = random.Random(20261002)
min_sharp = float('inf')
min_liu = float('inf')
for _ in range(60000):
    h = math.exp(rng.uniform(math.log(0.02), math.log(50.0)))
    y = h * rng.random()
    xmax = 1.0 - y / h
    x = rng.uniform(-xmax, xmax)
    ds = defect(h, x, y, lam_star(h))
    dl = defect(h, x, y, lam_liu(h))
    min_sharp = min(min_sharp, ds)
    min_liu = min(min_liu, dl)
    if ds < -2e-11 or dl < -2e-11:
        raise AssertionError((h, x, y, ds, dl))

# Exact interior equality branch for h>1, checked numerically.
max_eq = 0.0
for h in (1.01, 1.1, 1.5, math.sqrt(3.0), 2.0, 5.0, 20.0):
    y = (h * h - 1.0) / (2.0 * h)
    max_eq = max(max_eq, abs(defect(h, 0.0, y, lam_star(h))))
assert max_eq < 2e-12

print('VERIFY_OK')
print('exact_factorization=OK')
print('parameter_grid=20000')
print('point_tests=60000')
print('min_sharp_defect={:.17g}'.format(min_sharp))
print('min_liu_defect={:.17g}'.format(min_liu))
print('max_equality_residual={:.17g}'.format(max_eq))
