#!/usr/bin/env python3
"""Exact rational checks for the boundary-mode identities in RESULT.md."""
from fractions import Fraction
from math import factorial

def p(j, s):
    # Common exp(-s) factor cancels in all normalized identities.
    return s ** j / factorial(j)

def kappa(m, N, s):
    crossing = sum(
        (p(j, s) * p(j + m, s) / sum(p(r, s) for r in range(j + 1, j + m + 1)))
        for j in range(max(0, N - m), N)
    )
    return p(N - 1, s) - crossing

def main():
    cases = 0
    for N in range(1, 32):
        for s in [Fraction(1, 8), Fraction(1, 2), Fraction(1), Fraction(5, 2), Fraction(4), Fraction(11)]:
            telescoping = sum(p(j, s) * (Fraction(j, 1) / s - 1) for j in range(N))
            assert telescoping == -p(N - 1, s)
            assert kappa(1, N, s) == 0
            expected = p(N - 1, s) * (N + 2 * s + 1) / ((N + s) * (N + s + 1))
            assert kappa(2, N, s) == expected
            assert expected > 0
            for m in (3, 4, 8, 12):
                assert Fraction(0) <= kappa(m, N, s) <= p(N - 1, s)
            cases += 1
    print(f"CHECK_OK: {cases} exact rational parameter pairs")

if __name__ == '__main__':
    main()
