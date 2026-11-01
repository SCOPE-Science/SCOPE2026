#!/usr/bin/env python3
"""Exact-rational consistency checks for the homothetic-frustum John certificates.

No third-party dependencies.  The universal result is proved analytically in RESULT.md;
this program checks independent finite rational substitutions and the simplex
contact-frame Gram identities without floating-point calculations.
"""
from fractions import Fraction as F


def check(n, lam):
    assert n >= 2 and F(0) <= lam <= F(1)
    m = n - 1
    cutoff = F(m, n + 1)
    if lam <= cutoff:
        z = a = F(1, (n + 1)) / (1 - lam)
        b2 = cutoff
    else:
        z = a = F(1, 2)
        b2 = lam
    assert z - a == 0
    assert z + a <= 1
    d = 1 - (1 - lam) * z
    assert d > 0
    assert d * d == ((1 - lam) * a) ** 2 + b2
    q = (1 - lam) * a / d
    assert F(0) <= q <= F(1, n)
    W = F(m) / (1 - q * q)
    plus = (1 - W * (q*q + q)) / 2
    minus = (1 - W * (q*q - q)) / 2
    assert plus >= 0 and minus > 0
    assert plus - minus + W*q == 0
    assert plus + minus + W*q*q == 1
    assert (1 - q*q) * W == m
    if lam <= cutoff:
        assert plus == 0 and minus == F(n, n+1)
    if lam >= cutoff:
        assert plus == (F(1) - n*q) / (2 * (1-q))
        assert minus == (F(1) + n*q) / (2 * (1+q))
    # A regular simplex of m+1 unit vectors in dimension m has this Gram
    # matrix and positive John coefficients c_i=m/(m+1).
    t = m + 1
    G = [[F(1) if i == j else -F(1, m)
          for j in range(t)] for i in range(t)]
    weight = F(m, t)
    for j in range(t):
        assert sum((weight * G[i][j] for i in range(t)), F(0)) == 0
        for k in range(t):
            assert sum((weight * G[j][i] * G[i][k]
                        for i in range(t)), F(0)) == G[j][k]
    # In arbitrary dimension, these same frame identities yield the complete
    # normalized frustum contact certificate.
    return True


def main():
    samples = [F(0), F(1, 20), F(1, 10), F(1, 4), F(1, 3),
               F(2, 5), F(1, 2), F(3, 5), F(3, 4),
               F(4, 5), F(9, 10), F(19, 20), F(1)]
    checks = 0
    for n in range(2, 15):
        cutoff = F(n - 1, n + 1)
        for lam in sorted(set(samples + [cutoff, (cutoff + 1)/2, cutoff/2])):
            assert check(n, lam)
            checks += 1
    print(f'PASS: {checks} dimension/parameter pairs, exact Fraction arithmetic;')
    print('both transition regimes and the degenerate top-base endpoint included.')


if __name__ == '__main__':
    main()
