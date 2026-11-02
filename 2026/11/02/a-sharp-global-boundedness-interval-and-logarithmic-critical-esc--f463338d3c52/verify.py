#!/usr/bin/env python3
"""Reproducibility checks for a coupled Gaussian interval-to-plane map.

Standard-library numeric checks are finite consistency tests. The all-orbit
classification and asymptotic statements require the separate proof.
"""
import math


def f(a, x):
    return a * x * (1 - x * x) * math.exp(-x * x)


def bound(a):
    ts = ((5 - math.sqrt(17)) / 4, (5 + math.sqrt(17)) / 4)
    return a * max(math.sqrt(t) * abs(1 - t) * math.exp(-t) for t in ts)


def step(a, b, s, d):
    x, y = s + d, s - d
    fx, fy = f(a, x), f(a, y)
    return (fx + fy) / 2, (fx - fy) / 2 - 2 * b * d


def test_exact_coordinate_compatibility():
    count = 0
    for a in (0.2, 1.0, 3.4, 10.0):
        for b in (-0.6, -0.5, -0.25, 0.0, 0.49, 0.5, 0.6):
            for s, d in ((0.3, 0.8), (0.0, 2.2), (-0.5, -1.5)):
                s2, d2 = step(a, b, s, d)
                x, y = s + d, s - d
                x2 = f(a, x) + b * (y - x)
                y2 = f(a, y) + b * (x - y)
                assert math.isclose(s2 + d2, x2, rel_tol=2e-13, abs_tol=2e-13)
                assert math.isclose(s2 - d2, y2, rel_tol=2e-13, abs_tol=2e-13)
                count += 1
    return count


def test_interior_absorption():
    count = 0
    for a in (0.2, 1, 3.4, 10):
        M = bound(a)
        for b in (-0.49, -0.3, 0.0, 0.3, 0.49):
            q = 2 * abs(b)
            R = M / (1 - q) + 1
            for s, d in ((0, 8), (2, -12), (-20, 6)):
                for _ in range(1500):
                    s, d = step(a, b, s, d)
                assert abs(s) <= M * (1 + 1e-13)
                assert abs(d) < R * (1 + 1e-12)
                count += 1
    return count


def test_closed_negative_endpoint():
    count = 0
    for a in (0.2, 1, 3.4, 10):
        M = bound(a)
        R = M + 1
        for s, d in ((M / 2, 2 * M + 0.9), (M / 2, -2 * M - 0.8), (-M / 2, 0.4)):
            assert abs(s) < M and abs(d) < 2 * M + 1
            for _ in range(1000):
                s, d = step(a, -0.5, s, d)
                assert abs(s) <= M * (1 + 1e-12)
                assert abs(d) <= 2 * M + 1 + 1e-12
                count += 1
    return count


def test_escape():
    count = 0
    for a in (0.2, 1, 3.4, 10):
        M = bound(a)
        for b in (-0.7, -0.6, 0.6, 0.7):
            q = 2 * abs(b)
            d = M / (q - 1) + 2
            s = 0.25
            for _ in range(30):
                s2, d2 = step(a, b, s, d)
                assert abs(d2) > abs(d) + 1e-12
                s, d = s2, d2
                count += 1
    return count


def test_positive_endpoint_asymptotic():
    # The slow escape is numerically expensive; the finite tests do not prove
    # the logarithmic law, which follows from the auxiliary H increment proof.
    results = []
    for a in (0.5, 1.0, 3.4):
        M = bound(a)
        s, d = 0.05, M + 1.3
        ratios = []
        for n in range(1, 200001):
            sn, dn = step(a, 0.5, s, d)
            assert abs(dn) >= abs(d)
            s, d = sn, dn
            if n in (10000, 200000):
                r = d * d
                H = math.exp(r) / (2 * a * r * r)
                ratios.append(H / n)
        # A drift toward the asymptotic one verifies the implementation only.
        assert len(ratios) == 2 and 0.5 < ratios[0] < ratios[1] < 1.05
        assert abs(s) < 1e-15
        results.append((a, ratios))
    return results


if __name__ == '__main__':
    print('Coordinate comparison cases:', test_exact_coordinate_compatibility())
    print('Interior bounded-orbit cases:', test_interior_absorption())
    print('Closed endpoint invariant-state steps:', test_closed_negative_endpoint())
    print('Outside escape inequalities checked:', test_escape())
    print('Critical ratio H(r_n)/n at 10k and 200k:', test_positive_endpoint_asymptotic())
    print('All finite reproducibility checks passed; analytic proof is separate.')
