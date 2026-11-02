#!/usr/bin/env python3
"""Exact-rational finite checks for the mixed Gaussian circle-mean bound.

The analytical proof, rather than these finite tests, covers all entire
functions, all radii, and all Gaussian parameters.
"""
from fractions import Fraction
from math import factorial
from random import Random


def moment(k):
    return Fraction(factorial(k), 2 ** (k + 1))


def evaluate(p, s):
    return sum(coef * (s ** k) for k, coef in p.items())


def energy(p):
    return sum(u * v * moment(i + j)
               for i, u in p.items() for j, v in p.items())


def certificate(n, s):
    assert n <= s < n + 1
    c = Fraction(2 * n + 1, 2)
    if s <= c:
        return {n: Fraction(1)}
    return {n: c * (n + 1 - s), n + 1: s - c}


def formula(n, s):
    base = (2 * s) ** (2 * n) / factorial(2 * n)
    c = Fraction(2 * n + 1, 2)
    return base * (1 if s <= c else 1 + 2 * (s - c) ** 2 / c)


def check():
    rng = Random(260926821)
    counted = 0
    for n in range(8):
        for eighths in range(1, 8):
            s = Fraction(n * 8 + eighths, 8)
            Q = certificate(n, s)
            value = evaluate(Q, s) ** 2 / (2 * energy(Q))
            assert value == formula(n, s), (n, s, Q)
            # The exact certificate must be tight at every supported degree.
            for k in Q:
                assert sum(v * moment(k + j) for j, v in Q.items()) * evaluate(Q, s) == energy(Q) * s ** k
            for _ in range(10):
                P = {k: Fraction(rng.randrange(0, 8), rng.randrange(1, 7))
                     for k in range(12)}
                if not any(P.values()):
                    P[0] = Fraction(1)
                assert evaluate(P, s) ** 2 <= value * 2 * energy(P)
                counted += 1
    for n in range(8):
        for s in (Fraction(n), Fraction(2 * n + 1, 2)):
            Q = certificate(n, s)
            assert evaluate(Q, s) ** 2 == formula(n, s) * 2 * energy(Q)
    assert formula(0, Fraction(0)) == 1
    print(f"PASS: {counted} exact-rational positive-coefficient inequalities; "
          "56 formula, 80 supporting-moment, 16 boundary and one origin exact checks")


if __name__ == '__main__':
    check()
