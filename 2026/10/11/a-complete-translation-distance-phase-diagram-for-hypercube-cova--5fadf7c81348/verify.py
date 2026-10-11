#!/usr/bin/env python3
"""Numerical diagnostics for a cube covariogram extremum theorem.

These tests are finite checks, not an infinite-dimensional proof.
Run with a standard Python 3 interpreter.
"""
import math
import random


def candidate(k, s):
    return (1 - s / math.sqrt(k)) ** k if s < math.sqrt(k) else 0.0


def normalized_overlap(x):
    out = 1.0
    for t in x:
        out *= max(0.0, 1.0 - abs(t))
    return out


def h(u):
    return math.log1p(-u) + u / (2 * (1 - u))


def bisect(fn, a, b, steps=90):
    fa, fb = fn(a), fn(b)
    assert fa * fb < 0, (a, b, fa, fb)
    for _ in range(steps):
        m = (a + b) / 2
        if fa * fn(m) > 0:
            a, fa = m, fn(m)
        else:
            b, fb = m, fn(m)
    return (a + b) / 2


rho = bisect(h, 0.6, 0.9)
assert abs(rho - 0.7153318629591615) < 1e-12
prev = 0.0
for k in range(1, 18):
    a = rho * math.sqrt(k)
    # If the right theoretical bracket exceeds sqrt(k), use a point just inside that boundary.
    b = min(rho * math.sqrt(k + 1), math.sqrt(k) * (1 - 1e-10))
    ck = bisect(lambda s: candidate(k, s) - candidate(k + 1, s), a, b)
    assert prev < ck
    assert rho * math.sqrt(k) < ck < rho * math.sqrt(k + 1)
    assert abs(candidate(k, ck) - candidate(k + 1, ck)) < 1e-13
    prev = ck
assert abs(2 * (math.sqrt(2) - 1) - bisect(lambda s: candidate(1,s)-candidate(2,s), rho, .99)) < 1e-12

rng = random.Random(514927)
cases = 0
for d in range(2, 10):
    for j in range(1, 48):
        s = (j / 48) * math.sqrt(d)
        values = [candidate(k, s) for k in range(1, d + 1)]
        opt = max(values)
        k = values.index(opt) + 1
        x = [s / math.sqrt(k)] * k + [0.0] * (d-k)
        assert abs(normalized_overlap(x) - opt) < 2e-14
        for _ in range(700):
            v = [rng.gauss(0, 1) for i in range(d)]
            norm = math.sqrt(sum(z*z for z in v))
            point = [s * z / norm for z in v]
            assert normalized_overlap(point) <= opt + 3e-13
            cases += 1
print('VERIFY_OK', 'tested_random_vectors', cases, 'rho', format(rho,'.15f'))
