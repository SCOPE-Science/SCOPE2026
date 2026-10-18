#!/usr/bin/env python3
"""Deterministic finite diagnostic for the mixed-sum tame-defect theorem.

This checks finite samples of the analytic comparison. It is not an
infinite-dimensional proof; the published argument is entirely analytic.
"""
import math
import random


def normq(f, v, q):
    if math.isinf(q):
        return max(f, v)
    return (f ** q + v ** q) ** (1 / q)


def profile(f, v, a, p, q):
    return normq(f, (v ** p + a ** p) ** (1 / p), q)


def check():
    rng = random.Random(314159)
    tests = 0
    for p in (1.25, 1.5, 2.0, 3.0, 8.0):
        for q in (1.0, 1.4, 2.0, 2.7, 10.0, math.inf):
            sharp = 2 ** abs(1 / p - (0 if math.isinf(q) else 1 / q))
            r = min(p, q)
            s = max(p, q)
            f1 = profile(1, 0, 1, p, q)
            f2 = profile(0, 1, 1, p, q)
            witness = max(f1 / f2, f2 / f1)
            assert abs(witness - sharp) < 1e-11, (p, q, witness, sharp)
            for _ in range(3500):
                fx, vx, fy, vy, a = [10 ** rng.uniform(-2.5, 2.5) for _ in range(5)]
                nx, ny = normq(fx, vx, q), normq(fy, vy, q)
                lhs = profile(fy, vy, a, p, q) / profile(fx, vx, a, p, q)
                rhs = sharp * max(1, ny / nx)
                assert lhs <= rhs * (1 + 2e-12), (p, q, lhs, rhs)
                M = profile(fx, vx, a, p, q)
                lo = max(nx, a) if math.isinf(s) else (nx ** s + a ** s) ** (1 / s)
                hi = (nx ** r + a ** r) ** (1 / r)
                assert lo <= M * (1 + 2e-12)
                assert M <= hi * (1 + 2e-12)
                tests += 1
    print('PASS: %d finite parameter tests; 30 exact-construction comparisons.' % tests)

if __name__ == '__main__':
    check()
