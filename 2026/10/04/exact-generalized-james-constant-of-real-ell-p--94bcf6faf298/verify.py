#!/usr/bin/env python3
import math
import random

def norm(v, p):
    if p == math.inf:
        return max(abs(t) for t in v)
    return sum(abs(t) ** p for t in v) ** (1.0 / p)

def unit(v, p):
    n = norm(v, p)
    return [t / n for t in v]

def formula(p, lam):
    if p == math.inf:
        return 1.0
    if p <= 2.0:
        return (lam ** p + (1.0 - lam) ** p) ** (1.0 / p)
    return ((1.0 + abs(2.0 * lam - 1.0) ** p) / 2.0) ** (1.0 / p)

def pair_value(x, y, p, lam):
    a = [lam * u + (1.0 - lam) * v for u, v in zip(x, y)]
    b = [lam * u - (1.0 - lam) * v for u, v in zip(x, y)]
    return min(norm(a, p), norm(b, p))

def witness(p, lam):
    if p <= 2.0:
        x = [1.0, 0.0]
        y = [0.0, 1.0]
    else:
        c = 2.0 ** (-1.0 / p)
        x = [c, c]
        y = [c, -c]
    return pair_value(x, y, p, lam)

for lam in (0.2, 0.37, 0.5, 0.73):
    left = formula(2.0, lam)
    right = ((1.0 + abs(2.0 * lam - 1.0) ** 2) / 2.0) ** 0.5
    assert abs(left - right) < 1e-14
    for p in (1.0, 1.2, 1.5, 2.0, 3.0, 4.0, 8.0):
        assert abs(witness(p, lam) - formula(p, lam)) < 2e-13

x_inf = [1.0, 1.0]
y_inf = [1.0, -1.0]
for lam in (0.2, 0.37, 0.5, 0.73):
    assert abs(pair_value(x_inf, y_inf, math.inf, lam) - 1.0) < 1e-15

rng = random.Random(20211016)
for p in (1.0, 1.2, 1.5, 2.0, 3.0, 4.0, 8.0):
    for dim in (2, 3, 5):
        for lam in (0.2, 0.37, 0.5, 0.73):
            bound = formula(p, lam)
            for _ in range(200):
                x = unit([rng.uniform(-1.0, 1.0) for _ in range(dim)], p)
                y = unit([rng.uniform(-1.0, 1.0) for _ in range(dim)], p)
                assert pair_value(x, y, p, lam) <= bound + 2e-12

print("VERIFY_OK")
