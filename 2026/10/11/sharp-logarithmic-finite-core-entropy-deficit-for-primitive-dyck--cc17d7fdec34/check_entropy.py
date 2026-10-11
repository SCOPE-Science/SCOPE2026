#!/usr/bin/env python3
"""Standalone finite diagnostics for the positive-excursion finite-core entropy formula.

Uses only the Python standard library. This is not an infinite proof.
"""
import itertools
import math


def catalan(n):
    return math.comb(2 * n, n) // (n + 1)


def count_positive_excursions(n):
    count = 0
    for letters in itertools.product((1, -1), repeat=2 * n):
        height = 0
        admissible = True
        for j, sign in enumerate(letters, 1):
            height += sign
            if j < 2 * n and height <= 0:
                admissible = False
                break
        if admissible and height == 0:
            count += 1
    return count


def scaled_catalan_weights(N):
    weight = 0.25
    for n in range(1, N + 1):
        yield n, weight
        weight *= (2 * n - 1) / (2 * n + 2)


def finite_pressure_function(N, t):
    return sum(weight * math.exp(t * n / N)
               for n, weight in scaled_catalan_weights(N))


def root_t(N):
    lower, upper = 0.0, max(5., 2. * math.log(N + 2))
    assert finite_pressure_function(N, lower) <= 1.
    while finite_pressure_function(N, upper) < 1.:
        upper *= 2.
    for _ in range(75):
        midpoint = (lower + upper) / 2
        if finite_pressure_function(N, midpoint) < 1.:
            lower = midpoint
        else:
            upper = midpoint
    return (lower + upper) / 2


def main():
    diagnostics = 0
    for n in range(1, 8):
        observed = count_positive_excursions(n)
        expected = catalan(n - 1)
        assert observed == expected, (n, observed, expected)
        diagnostics += 1

    for N in (1, 2, 3, 4, 5, 10, 30, 100, 1000, 10000, 100000):
        t = root_t(N)
        entropy = math.log(2) - t / (2 * N)
        residual = abs(finite_pressure_function(N, t) - 1)
        assert residual < 5e-13, (N, residual)
        assert -1e-14 <= entropy < math.log(2)
        if N == 1:
            assert abs(entropy) < 1e-13
        if N >= 1000:
            approx = 0.5 * math.log(N) + math.log(math.log(N)) + 0.5 * math.log(math.pi)
            assert abs(t - approx) < 0.25, (N, t, approx)
        diagnostics += 1
        print(f'N={N:<6} entropy={entropy:.12f}  t={t:.9f}  pressure residual={residual:.2g}')
    print(f'PASS: {diagnostics} finite diagnostics (not a proof).')


if __name__ == '__main__':
    main()
