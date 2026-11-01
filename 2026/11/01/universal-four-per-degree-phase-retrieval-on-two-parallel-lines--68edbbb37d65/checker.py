#!/usr/bin/env python3
"""Exact supplementary regression checks for two-line polynomial intensity interpolation.

Uses only the Python standard library. This tests finite identities, not the
universal rational-reflection uniqueness theorem proved in the accompanying text.
"""
from fractions import Fraction
from math import comb
from random import Random


def multiply(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gaussian_power(z, n):
    t = (1, 0)
    for _ in range(n):
        t = multiply(t, z)
    return t


def intensity_coefficients(a, h):
    """Exact real coefficients of |sum a[k] (x+i h)^k| squared."""
    d = len(a) - 1
    c = [(0, 0) for _ in range(d + 1)]
    for k, ak in enumerate(a):
        for j in range(k + 1):
            t = multiply(ak, gaussian_power((0, h), k - j))
            c[j] = (c[j][0] + comb(k, j) * t[0],
                    c[j][1] + comb(k, j) * t[1])
    out = [0 for _ in range(2 * d + 1)]
    for j, u in enumerate(c):
        for k, v in enumerate(c):
            out[j + k] += u[0] * v[0] + u[1] * v[1]
    return out


def evaluate(a, x):
    return sum(v * (x ** k) for k, v in enumerate(a))


def interpolation(data):
    """Lagrange interpolation over exact rational numbers."""
    n = len(data)
    out = [Fraction(0) for _ in range(n)]
    for i, (xi, yi) in enumerate(data):
        poly = [Fraction(1)]
        den = 1
        for j, (xj, _) in enumerate(data):
            if j == i:
                continue
            den *= xi - xj
            new = [Fraction(0)] * (len(poly) + 1)
            for t, v in enumerate(poly):
                new[t] -= xj * v
                new[t + 1] += v
            poly = new
        for t, v in enumerate(poly):
            out[t] += Fraction(yi, den) * v
    return out


def run():
    rng = Random(439175)
    trials = 0
    for d in range(1, 7):
        for t in range(65):
            a = [(rng.randint(-4, 4), rng.randint(-4, 4))
                 for _ in range(d + 1)]
            if t % 11 == 0:
                a[d] = (0, 0)  # degree strictly below the bound
            if t % 29 == 0:
                a = [(0, 0) for _ in a]  # zero polynomial
            h0 = rng.randint(-4, 2)
            h1 = h0 + rng.randint(1, 5)
            I0 = intensity_coefficients(a, h0)
            I1 = intensity_coefficients(a, h1)
            assert I0[-2:] == I1[-2:]
            x = sorted(rng.sample(range(-32, 34), 2 * d + 1))
            y = sorted(rng.sample(range(-32, 34), 2 * d - 1))
            a0 = interpolation([(v, evaluate(I0, v)) for v in x])
            assert a0 == I0
            top = [a0[2 * d - 1], a0[2 * d]]
            residual = interpolation([
                (v, evaluate(I1, v) - top[0] * v**(2*d-1) - top[1] * v**(2*d))
                for v in y
            ])
            recovered = residual + top
            assert recovered == I1
            assert all(evaluate(recovered, v) == evaluate(I1, v) for v in x + y)
            trials += 1
    print(f'PASS: {trials} exact two-line interpolation trials, 3 assertions per trial')


if __name__ == '__main__':
    run()
