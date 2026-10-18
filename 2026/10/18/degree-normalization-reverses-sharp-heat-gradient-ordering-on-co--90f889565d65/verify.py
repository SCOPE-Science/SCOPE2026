#!/usr/bin/env python3
"""Finite-dimensional numerical checks for bipartite graph heat-gradient identities.

Runs with Python 3 standard library only. Infinite-family assertions are established
analytically in the accompanying note; these tests check finite instances.
"""
import math


def formula(a, b, theta, t):
    alpha = b ** (1.0 - theta)
    beta = a ** (1.0 - theta)
    x = math.exp(-alpha * t)
    y = math.exp(-beta * t)
    z = math.exp(-(alpha + beta) * t)
    return 2 * ((1 - 1 / a) * x + (1 - 1 / b) * y +
                (1 / a + 1 / b - 1) * z)


def independent_uniformization(a, b, theta, t):
    """Difference of two heat rows from Poissonized embedded Markov-chain steps.

    No spectral decomposition or closed-form heat-kernel coefficients are used.
    """
    n = a + b
    rates = [b ** (1 - theta)] * a + [a ** (1 - theta)] * b
    q = max(rates)
    trans = []
    for i in range(n):
        row = [0.0] * n
        row[i] = 1.0 - rates[i] / q
        if i < a:
            for j in range(a, n):
                row[j] = rates[i] / (q * b)
        else:
            for j in range(a):
                row[j] = rates[i] / (q * a)
        assert abs(sum(row) - 1) < 1e-13
        trans.append(row)
    v = [0.0] * n
    v[0], v[a] = 1.0, -1.0
    prob = math.exp(-q * t)
    accum = [prob * z for z in v]
    cutoff = max(80, math.ceil(q * t + 20 * math.sqrt(q * t + 1) + 20))
    for k in range(1, cutoff + 1):
        v = [sum(v[i] * trans[i][j] for i in range(n)) for j in range(n)]
        prob *= q * t / k
        for j in range(n):
            accum[j] += prob * v[j]
    return sum(abs(z) for z in accum)


def test():
    count = 0
    for n in range(3, 15):
        for a in range(1, n // 2 + 1):
            b = n - a
            for theta in (0.0, 0.2, 0.5, 0.8, 1.0):
                for t in (0.025, 0.12, 0.7, 1.4):
                    observed = independent_uniformization(a, b, theta, t)
                    predicted = formula(a, b, theta, t)
                    assert abs(observed - predicted) < 2e-11, (n, a, theta, t, observed, predicted)
                    count += 1
    for n in range(4, 36):
        for t in (0.005, 0.08, 0.5, 1.0):
            for theta, increasing in ((0.0, False), (1.0, True)):
                vals = [formula(a, n - a, theta, t) for a in range(1, n // 2 + 1)]
                for x, y in zip(vals, vals[1:]):
                    assert (x < y) if increasing else (x > y), (n, t, theta, x, y)
                    count += 1
    for n in range(4, 19):
        for a in range(1, n // 2):
            b = n - a
            for c in range(a + 1, n // 2 + 1):
                d = n - c
                for theta in (0.2, 0.5, 0.8):
                    # First derivative at the origin is strictly more negative for
                    # the more imbalanced split.
                    slope_a = -(a ** (-theta) + b ** (-theta))
                    slope_c = -(c ** (-theta) + d ** (-theta))
                    assert slope_a < slope_c
                    # Dominant long-time eigenvalue is strictly smaller in the
                    # more imbalanced split.
                    assert a ** (1 - theta) < c ** (1 - theta)
                    count += 2
    for n in range(4, 24):
        for a in range(1, n // 2 + 1):
            b = n - a
            for theta in (0, 0.35, 0.7, 1):
                # Near t=0, the predicted derivative is -2(a^-theta+b^-theta).
                t = 1e-5
                diff = (formula(a, b, theta, t) - 2) / t
                goal = -2 * (a ** (-theta) + b ** (-theta))
                assert abs(diff - goal) < 0.006, (n, a, theta, diff, goal)
                count += 1
    print(f"PASS {count} independent finite numerical/analytic-identity assertions")


if __name__ == '__main__':
    test()
