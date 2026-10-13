#!/usr/bin/env python3
"""Exact finite algebra and numerical stress tests for heterogeneous Ising stars.
The unbounded claims require the separate analytic proof.
"""
from fractions import Fraction
from itertools import product
import cmath
import math
import random

F = Fraction


def times(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    return c


def coeffs(q):
    a, b = [F(1)], [F(1)]
    for v in q:
        a = times(a, [F(1), v])
        b = times(b, [v, F(1)])
    return [u + (b[i - 1] if i >= 1 else F(0))
            for i, u in enumerate(a + [F(0)])]


def spin_sum(q):
    n = len(q) + 1
    ans = [F(0)] * (n + 1)
    for bits in product((0, 1), repeat=n):
        w = F(1)
        for k, v in enumerate(q):
            if bits[0] != bits[k + 1]:
                w *= v
        ans[sum(bits)] += w
    return ans


def poly_eval(c, z):
    y = 0j
    for a in reversed(c):
        y = y * z + float(a)
    return y


def inner_root(q):
    a = [float(F(1) / v) for v in q]
    left, right = 0.0, min(a)

    def balance(x):
        return math.prod((v - x) / (1 - v * x) for v in a) - x

    for _ in range(100):
        mid = (left + right) / 2
        if balance(mid) > 0:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def phase(a, t):
    if t == math.pi or t == -math.pi:
        return t
    return math.atan2((1 - a * a) * math.sin(t),
                      2 * a + (1 + a * a) * math.cos(t))


def phase_derivative(a, t):
    return (1 - a * a) / (1 + a * a + 2 * a * math.cos(t))


def circular_roots(q):
    m = len(q)
    a = [float(F(1) / v) for v in q]

    def delta(t):
        return sum(phase(v, t) for v in a) - t

    out = []
    for k in range((m - 1) // 2):
        level = (2 * k + 1) * math.pi
        lo, hi = 0.0, math.pi
        for _ in range(90):
            mid = (lo + hi) / 2
            if delta(mid) < level:
                lo = mid
            else:
                hi = mid
        t = (lo + hi) / 2
        assert sum(phase_derivative(v, t) for v in a) > 1
        out.extend((cmath.exp(1j * t), cmath.exp(-1j * t)))
    if m % 2 == 0:
        out.append(-1 + 0j)
    return out


algebra_checks = 0
root_checks = 0
bound_checks = 0
arc_checks = 0
cases = [
    [F(2), F(3), F(5)],
    [F(5, 4), F(7, 3), F(9, 5), F(11, 2)],
    [F(13, 10)] * 5,
    [F(11, 10)] * 6,
    [F(2)] * 12,
    [F(3, 2)],
]
rng = random.Random(821820)
for m in range(1, 13):
    for _ in range(8):
        cases.append([F(rng.randint(5, 23), 4) for _ in range(m)])

for q in cases:
    m = len(q)
    c = coeffs(q)
    assert c[0] == 1 and c[-1] == 1 and c == c[::-1]
    algebra_checks += 1
    if m <= 6:
        assert spin_sum(q) == c
        algebra_checks += 1
    a = [float(F(1) / v) for v in q]
    x = inner_root(q)
    P = math.prod(a)
    assert 0 < x < min(a) and x < P < 1
    assert abs(math.prod((v - x) / (1 - v * x) for v in a) - x) < 1e-13
    astar = max(a)
    err = 1 - x / P
    limit = m * astar ** (m - 1) / (1 - astar ** (m + 1))
    assert -1e-12 <= err <= limit + 1e-10
    bound_checks += 1
    roots = circular_roots(q)
    assert len(roots) == m - 1
    roots.extend([-x, -1 / x])
    assert len(roots) == m + 1
    for z in roots:
        denom = sum(abs(float(v)) * max(1, abs(z)) ** i
                    for i, v in enumerate(c))
        assert abs(poly_eval(c, z)) / denom < 5e-11
        root_checks += 1

    co = (1 - astar) / (1 + astar)
    if m * co > 1:
        angular = sorted(((cmath.phase(z) + math.pi) % (2 * math.pi)
                          - math.pi) for z in roots[:-2])
        for _ in range(10):
            alpha, beta = sorted((rng.uniform(-math.pi, math.pi),
                                  rng.uniform(-math.pi, math.pi)))
            n_arc = sum(alpha <= t < beta for t in angular)
            avg_mass = sum(phase(v, beta) - phase(v, alpha)
                           for v in a) / (2 * math.pi * m)
            assert abs(n_arc / (m + 1) - avg_mass) < 3 / (m + 1) + 1e-10
            arc_checks += 1

assert coeffs([F(2), F(3), F(5)]) == [1, 40, 62, 40, 1]
print('VERIFY_OK algebra=' + str(algebra_checks) +
      ' root_residual=' + str(root_checks) +
      ' outlier_bounds=' + str(bound_checks) +
      ' arc_discrepancy=' + str(arc_checks))
