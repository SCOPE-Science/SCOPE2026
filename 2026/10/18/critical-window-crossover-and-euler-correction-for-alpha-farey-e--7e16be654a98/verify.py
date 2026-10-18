#!/usr/bin/env python3
"""Independent, standard-library numerical and exact identity checks for a Farey escape theorem.
These finite checks are not a proof of any limiting assertion.
"""
from fractions import Fraction
import math

EULER_GAMMA = 0.577215664901532860606512090082402431


def exact_harmonic_identities(n):
    a = [Fraction(1, k) - Fraction(1, k + 1) for k in range(1, n)]
    s = sum((k * ak for k, ak in enumerate(a, 1)), Fraction(0))
    h_minus_one = sum((Fraction(1, j) for j in range(2, n + 1)), Fraction(0))
    assert sum(a, Fraction(0)) == 1 - Fraction(1, n)
    assert s == h_minus_one


def escape_root(n, c):
    L = math.log(n)
    theta = 1.0 + c / L
    assert theta > 0
    a = [k ** (-theta) - (k + 1) ** (-theta) for k in range(1, n)]
    tail = n ** (-theta)
    S = sum(k * ak for k, ak in enumerate(a, 1))
    lo, hi = 0.0, tail / S
    # Monotonicity: sum a_k expm1(k*g) >= g*S; hence actual root <= tail / S.
    def F(g):
        return sum(ak * math.expm1(k * g) for k, ak in enumerate(a, 1))
    assert F(lo) < tail and F(hi) >= tail * (1.0 - 1e-11)
    for _ in range(58):
        middle = (lo + hi) / 2
        if F(middle) < tail:
            lo = middle
        else:
            hi = middle
    g = (lo + hi) / 2
    assert abs(F(g) - tail) <= 1e-10 * tail
    psi = -math.expm1(-c) / c if c else 1.0
    phi = math.exp(-c) / psi
    lead = n * L * g
    corrected = phi * (1.0 - (EULER_GAMMA - math.exp(-c)) / (L * psi))
    return lead, phi, corrected, n * g


def main():
    for n in range(2, 25):
        exact_harmonic_identities(n)
    for c in (-2.0, 0.0, 2.0):
        data = [escape_root(n, c) for n in (2000, 10000, 40000)]
        # Numerical evidence of leading transition, not a proof.
        assert abs(data[-1][0] - data[-1][2]) < 0.15
        assert data[-1][3] < 0.5
        print('c=', c, 'scaled roots', [round(v[0], 9) for v in data],
              'theory', round(data[-1][1], 9), 'Euler refinement', round(data[-1][2], 9))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
