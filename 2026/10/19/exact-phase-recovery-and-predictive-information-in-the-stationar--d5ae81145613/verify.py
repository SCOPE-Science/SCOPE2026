#!/usr/bin/env python3
"""Exact finite-word validation for the stationary random dimer shift.

Uses direct phase-conditioned enumeration, with no simulation and no external packages.
Finite verification corroborates, but does not replace, the unrestricted counting proof.
"""
from itertools import product
from fractions import Fraction
from math import log2


def phase_likelihood(word, phase):
    """Mass of a word given dimer starts at even/odd integer positions."""
    n = len(word)
    count = 0
    for start in range(-2, n + 1):
        if start % 2 != phase:
            continue
        covered = [j for j in (start, start + 1) if 0 <= j < n]
        if not covered:
            continue
        count += 1
        if len(covered) == 2 and word[start] == word[start + 1]:
            return Fraction(0)
    return Fraction(1, 2**count)


def predicted(n):
    m = n // 2
    if n % 2 == 0:
        return (3 * 2**m - 2,
                Fraction(1, 2**(m + 1)),
                Fraction(3, 2**(m + 1)),
                m + 1.5 - 3 * 2**(-m-1) * binary_entropy(Fraction(1,3)))
    return (2**(m + 2) - 2,
            Fraction(1, 2**(m + 1)),
            Fraction(1, 2**m),
            m + 2 - 2**(-m))


def binary_entropy(t):
    x = float(t)
    return -(x * log2(x) + (1 - x) * log2(1 - x)) if 0 < x < 1 else 0.0


def main():
    tested = 0
    for n in range(1, 13):
        probs = {}
        support = 0
        bayes = Fraction(0)
        alternating = Fraction(0)
        entropy = 0.0
        normalization = Fraction(0)
        for w in product((-1,1),repeat=n):
            a,b = phase_likelihood(w, 0), phase_likelihood(w, 1)
            p = (a+b)/2
            normalization += p
            bayes += min(a,b)/2
            if not p:
                continue
            support += 1
            entropy -= float(p) * log2(float(p))
            if all(w[j] != w[j+1] for j in range(n-1)):
                alternating += p
                assert a > 0 and b > 0
            else:
                assert (a > 0) != (b > 0)
            tested += 1
        pc,pr,pa,ph=predicted(n)
        assert normalization == 1, (n,normalization)
        assert (support,bayes,alternating) == (pc,pr,pa), (n,support,bayes,alternating)
        assert abs(entropy-ph) < 1e-11, (n,entropy,ph)
    print(f'VERIFY_OK: {tested} positive exact phase-conditioned cylinders; 12 exact support, Bayes-risk and alternating-mass identities; 12 Shannon entropy comparisons')

if __name__ == '__main__':
    main()
