#!/usr/bin/env python3
"""Exact finite checks of monomial Toeplitz inverse-power coefficients.

The general theorem depends on the separately supplied analytic proof.
"""
from fractions import Fraction


def weight_square(m: int, k: int) -> Fraction:
    if k >= 0:
        return Fraction(k + 1, k + m + 1)
    j = -k
    if j >= m:
        return Fraction(j - m + 1, j + 1)
    return Fraction((j + 1) * (m - j + 1), (m + 1) ** 2)


def target(m: int, N: int) -> Fraction:
    return Fraction((m * (N // 2) + 1) * (m * ((N + 1) // 2) + 1))


def endpoint(a: int, b: int, m: int, j: int) -> Fraction:
    return Fraction((m + 1) ** 2 * (a * m + j + 1) * (b * m + m - j + 1),
                    (j + 1) ** 2 * (m - j + 1) ** 2)


cases = 0
paths = 0
for m in range(1, 21):
    for N in range(1, 14):
        maximum = Fraction(0)
        max_positions = []
        # This includes all paths crossing zero, plus longer one-sided tails.
        for k in range(-m * (N + 2), m * (N + 2) + 1):
            forward_square = Fraction(1)
            for h in range(N):
                forward_square *= weight_square(m, k + h * m)
            inverse_square = 1 / forward_square
            paths += 1
            if inverse_square > maximum:
                maximum, max_positions = inverse_square, [k]
            elif inverse_square == maximum:
                max_positions.append(k)
        assert maximum == target(m, N), (m, N, maximum, target(m, N))
        expected_positions = sorted({-m * (N // 2), -m * ((N + 1) // 2)})
        assert max_positions == expected_positions, (m, N, max_positions)
        inverse_input_positions = sorted(k + N * m for k in max_positions)
        assert inverse_input_positions == sorted({m * (N // 2), m * ((N + 1) // 2)})
        for a in range(N):
            b = N - 1 - a
            ceiling = max(endpoint(a, b, m, 0), endpoint(a, b, m, m))
            for j in range(1, m):
                k = -a * m - j
                path = Fraction(1)
                for h in range(N):
                    path *= weight_square(m, k + h * m)
                assert 1 / path == endpoint(a, b, m, j)
                assert endpoint(a, b, m, j) < ceiling
        cases += 1
print('PASS: exact moment-derived weight products and full inverse-domain norming-index classification')
print('parameter_pairs=', cases, 'finite_paths=', paths)
print('The all-integer theorem uses the analytic convexity argument, not sampling.')
