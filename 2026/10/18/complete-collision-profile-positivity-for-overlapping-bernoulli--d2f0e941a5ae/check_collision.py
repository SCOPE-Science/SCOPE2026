#!/usr/bin/env python3
"""Exact rational checks for the collision-bias polynomial of weighted Bernoulli sums.

Run with Python 3.10 or later. No third-party dependencies.
The checks illustrate the identities; the proof applies to every finite weight vector.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement


def polynomial_coefficients(weights):
    # Fourier constant terms of product (cos^2(w theta/2)+u sin^2(w theta/2)).
    # Multiplying by 4 per factor keeps all calculations integral.
    state = {(0, 0): 1}
    for w in weights:
        fresh = defaultdict(int)
        for (exponent, degree), value in state.items():
            for shift, scalar in ((0, 2), (w, 1), (-w, 1)):
                fresh[exponent + shift, degree] += value * scalar
            for shift, scalar in ((0, 2), (w, -1), (-w, -1)):
                fresh[exponent + shift, degree + 1] += value * scalar
        state = dict(fresh)
    n = len(weights)
    return [Fraction(state.get((0, k), 0), 4 ** n) for k in range(n + 1)]


def direct_collision(weights, p):
    law = {0: Fraction(1)}
    for w in weights:
        fresh = defaultdict(Fraction)
        for s, mass in law.items():
            fresh[s] += mass * (1 - p)
            fresh[s + w] += mass * p
        law = dict(fresh)
    return sum((v * v for v in law.values()), Fraction(0))


def main():
    tests = 0
    sample_ps = [Fraction(0), Fraction(1, 7), Fraction(2, 5),
                 Fraction(1, 2), Fraction(3, 4), Fraction(1)]
    for n in range(1, 7):
        for weights in combinations_with_replacement(range(1, 6), n):
            gamma = polynomial_coefficients(weights)
            assert all(c > 0 for c in gamma)
            assert sum(gamma) == 1
            tests += 2
            for p in sample_ps:
                u = (1 - 2 * p) ** 2
                profile = sum((gamma[k] * u ** k for k in range(n + 1)), Fraction(0))
                assert profile == direct_collision(weights, p)
                lower = gamma[0] + gamma[1] * u
                upper = gamma[0] + (1 - gamma[0]) * u
                assert lower <= profile <= upper
                if n >= 2 and 0 < u < 1:
                    assert lower < profile < upper
                tests += 3
            assert gamma[0] == direct_collision(weights, Fraction(1, 2))
            tests += 1
    print(f"PASS: {tests} exact assertions across all positive weight multisets "
          "of length 1 through 6 with weights at most 5")


if __name__ == "__main__":
    main()
