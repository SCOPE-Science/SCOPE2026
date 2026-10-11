#!/usr/bin/env python3
"""Finite numerical stress checks for the scalar-coordinate defect norm.

The analytic proof, not these finite tests, establishes universal convexity.
Requires only the Python standard library.
"""
import math
import random


def cp(p):
    return (p - 1) * 2 ** (2 / p) / p


def curvature_bound(p, r):
    z = r ** p
    return (p - 1) * (1 + z) ** (2 / p) * r ** (p - 2) / (1 + (p - 1) * z)


def defect(p, lam2, a, y, ynorm="max"):
    if ynorm == "max":
        b = max(abs(v) for v in y)
    else:
        b = sum(abs(v) ** 2 for v in y) ** 0.5
    if p == math.inf:
        base = max(abs(a), b)
    else:
        base = (abs(a) ** p + b ** p) ** (1 / p)
    return math.sqrt(max(0.0, base * base - lam2 * abs(a) ** 2))


def test():
    rng = random.Random(20240721)
    checks = 0
    for p in (1.05, 1.1, 1.25, 1.5, 1.75, 1.95):
        c = cp(p)
        assert 0 < c < 1
        assert abs(curvature_bound(p, 1) - c) < 4e-15
        for r in (1e-5, 0.0001, .01, .5, .99, 1, 1.01, 2, 10, 1e4):
            assert curvature_bound(p, r) >= c - 2e-12
            checks += 1
        b12 = (2 - p) * 2 ** (2 / p - 2)
        b22 = p * 2 ** (2 / p - 2)
        h = b12 / b22
        # Hessian's Schur complement at (1,1), as used in the proof.
        for eps in (0.001, 0.0001):
            lam2 = min(.9999, c + 0.025)
            middle = defect(p, lam2, 1, (1,)) ** 2
            plus = defect(p, lam2, 1 + eps, (1 - h * eps,)) ** 2
            minus = defect(p, lam2, 1 - eps, (1 + h * eps,)) ** 2
            assert middle > (plus + minus) / 2 + 1e-10 * eps * eps
            checks += 1
        for ynorm in ("max", "ell2"):
            for lam2 in (0.0, c * .5, c):
                for _ in range(550):
                    def rnd():
                        return complex(rng.uniform(-2, 2), rng.uniform(-2, 2))
                    a, b = rnd(), rnd()
                    y, z = [rnd() for _ in range(3)], [rnd() for _ in range(3)]
                    lhs = defect(p, lam2, a + b, [u + v for u, v in zip(y, z)], ynorm)
                    rhs = defect(p, lam2, a, y, ynorm) + defect(p, lam2, b, z, ynorm)
                    assert lhs <= rhs + 3e-12, (p, lam2, lhs, rhs)
                    checks += 1
    for p in (2.7, 3.0, 4.0, 8.0, math.inf):
        lam2 = .1
        for h in (1e-3, 1e-4, 1e-5):
            # For sufficiently small h, symmetric points violate convexity.
            upper = defect(p, lam2, h, (1,))
            mid = defect(p, lam2, 0, (1,))
            assert upper < mid, (p, h, upper)
            checks += 1
    for lam2 in (.0001, .4, .9):
        lhs = defect(1, lam2, 1, (1,))
        rhs = defect(1, lam2, 1, (0,)) + defect(1, lam2, 0, (1,))
        assert lhs > rhs
        checks += 1
    print("PASS", checks, "numeric, complex-triangle, curvature, and failure-witness tests")


if __name__ == "__main__":
    test()
