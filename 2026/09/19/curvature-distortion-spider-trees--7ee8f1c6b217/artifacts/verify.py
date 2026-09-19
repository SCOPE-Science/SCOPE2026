#!/usr/bin/env python3
"""Verify the spider curvature-distortion formulas numerically.

Uses only the Python standard library.  The computation solves the scalar
equation by bisection, reconstructs the canonical weights, and checks the
nonlinear fixed-point equations directly.
"""

import itertools
import math
import random


def rho_of(s, length):
    lo, hi = 1.0, s
    for _ in range(60):
        mid = (lo + hi) / 2.0
        if (mid ** (length - 1)) * (mid + 1.0) < s:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def solve_spider(lengths):
    d = len(lengths)
    if max(lengths) == 1:
        return float(d), [[1.0] for _ in lengths], 1.0

    def scalar_sum(s):
        ans = 0.0
        for length in lengths:
            if length == 1:
                ans += 1.0 / s
            else:
                r = rho_of(s, length)
                ans += 1.0 / (1.0 + r)
        return ans

    lo = float(d)
    hi = max(2.0 * d, d + 1.0)
    while scalar_sum(hi) > 1.0:
        hi *= 2.0

    for _ in range(70):
        mid = (lo + hi) / 2.0
        if scalar_sum(mid) > 1.0:
            lo = mid
        else:
            hi = mid

    s = (lo + hi) / 2.0
    weights = []
    for length in lengths:
        if length == 1:
            weights.append([1.0])
        else:
            r = rho_of(s, length)
            weights.append(
                [r ** (length - j) for j in range(1, length + 1)]
            )

    distortion = max(max(row) for row in weights)
    return s, weights, distortion


def fixed_point_residual(lengths, weights):
    s = sum(row[0] for row in weights)
    err = 0.0
    for i, length in enumerate(lengths):
        for j in range(length):
            left = (s - weights[i][0]) if j == 0 else weights[i][j - 1]
            right = 0.0 if j == length - 1 else weights[i][j + 1]
            target = max(1.0, math.sqrt(left * right))
            err = max(err, abs(target - weights[i][j]))
    return err


def main():
    random.seed(20260919)
    samples = []
    for _ in range(600):
        d = random.randint(3, 7)
        samples.append(tuple(random.randint(1, 6) for _ in range(d)))

    for d in range(3, 8):
        for length in range(1, 7):
            samples.append((length,) * d)
            samples.append(tuple([length] + [1] * (d - 1)))

    max_residual = 0.0
    for lengths in samples:
        _, weights, distortion = solve_spider(lengths)
        max_residual = max(
            max_residual, fixed_point_residual(lengths, weights)
        )

        d = len(lengths)
        L = max(lengths)

        if len(set(lengths)) == 1:
            expected = 1.0 if L == 1 else (d - 1) ** (L - 1)
            assert abs(distortion - expected) < 1e-8 * max(1.0, expected)

        if L >= 2:
            lower = (d - 1) ** ((L - 1) / L)
            upper = (d - 1) ** (L - 1)
            assert lower - 1e-8 <= distortion <= upper + 1e-8

    print("cases_checked", len(samples))
    print("max_fixed_point_residual", f"{max_residual:.3e}")
    print("closed_form_and_bounds", "passed")


if __name__ == "__main__":
    main()
