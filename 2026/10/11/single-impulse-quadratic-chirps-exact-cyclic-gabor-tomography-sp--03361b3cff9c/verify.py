#!/usr/bin/env python3
"""Finite exact-index and independent discrete-sum checks of the stated formulas.

Uses only the Python standard library. The general theorem is proved symbolically
in RESULT.md; the finite tests here are corroboration, not an infinite proof.
"""
import cmath
import math


def e(n, k):
    return cmath.exp(2j * math.pi * (k % n) / n)


def predicted(n, a, t, u, v):
    if u == 0:
        return (n if v == 0 else 0) + t * (t + 2)
    k = (v - 2 * a * u) % n
    if k == 0:
        return (n + 2 * t) * e(n, a * u * u)
    return t * e(n, a * u * u) * (1 + e(n, u * k))


def direct(n, a, t, u, v):
    z = [e(n, a * j * j) + (t if j == 0 else 0) for j in range(n)]
    return sum(z[(j + u) % n] * z[j].conjugate() * e(n, -v * j)
               for j in range(n))


def phi(n):
    return sum(math.gcd(j, n) == 1 for j in range(1, n + 1))


def zeros_formula(n):
    if n % 2:
        return 0
    return sum(d * phi(n // d) for d in range(1, n // 2 + 1)
               if (n // 2) % d == 0)


def test():
    checked = 0
    for n in range(3, 29):
        for a in (0, 1, 2):
            for t in (0.5, 1.0, math.sqrt(n)):
                vals = []
                for u in range(n):
                    for v in range(n):
                        x = predicted(n, a, t, u, v)
                        y = direct(n, a, t, u, v)
                        assert abs(x - y) < 1e-8, (n, a, t, u, v, x, y)
                        vals.append(abs(x))
                        checked += 1
                numzeros = sum(z < 1e-8 for z in vals)
                assert numzeros == zeros_formula(n), (n, numzeros)
                positive = sorted(z for z in vals if z >= 1e-8)
                expected = 2 * t * math.sin(math.pi / (2 * n if n % 2 else n))
                assert abs(positive[0] - expected) < 1e-8, (n, positive[0])
                assert abs(positive[-1] - (n + 2 * t + t * t)) < 1e-8
    # Weyl conjugacy orthogonality independently gives sqrt(n) times
    # the ambiguity magnitudes as lifted-intensity singular values.
    # Check the modulus-normalized optimum and strict uniqueness algebraically.
    for n in range(3, 101):
        r = math.sqrt(n)
        def normalized(t):
            return 2 * t / (n + 2 * t + t * t)
        for scale in (0.02, 0.1, 0.5, 0.8, 1.2, 2, 10, 50):
            assert normalized(r) > normalized(r * scale)
        assert abs(normalized(r) - 1 / (r + 1)) < 1e-12
    print('VERIFY_OK discrete_sums=%d modulus_cases=3..28 nullity=PASS exact_optimum=PASS' % checked)


if __name__ == '__main__':
    test()
