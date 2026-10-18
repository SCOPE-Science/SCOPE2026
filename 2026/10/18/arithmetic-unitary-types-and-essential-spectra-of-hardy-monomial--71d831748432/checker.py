#!/usr/bin/env python3
"""Finite reproducibility diagnostics for the monomial Hardy composition-product classification.

Finite checks illustrate the exact number-theoretic orbit relations; the
infinite-dimensional spectral conclusions require the proof in RESULT.md.
"""
from math import gcd

PAIRS = [(2, 2), (2, 4), (4, 2), (6, 10), (10, 6),
         (12, 15), (15, 12), (8, 27), (27, 8), (16, 36), (49, 18)]
CHECKS = 0


def test(condition, message):
    global CHECKS
    assert condition, message
    CHECKS += 1


def decomposition(n, a, b):
    j = h = 0
    if a > 1:
        while n % a == 0:
            j += 1
            n //= a
    if b > 1:
        while n % b == 0:
            h += 1
            n //= b
    return j, h, n


def image(n, a, b):
    return (a * (n // b)) if n % b == 0 else None


for m, k in PAIRS:
    d = gcd(m, k)
    a, b = m // d, k // d
    test(gcd(a, b) == 1, (m, k, 'coprime'))
    for n in range(1, 2001):
        j, h, c = decomposition(n, a, b)
        test(n == a**j * b**h * c, (m, k, n, 'factor'))
        test((a == 1 or c % a != 0) and (b == 1 or c % b != 0),
             (m, k, n, 'maximality'))
        successor = image(n, a, b)
        expected = a**(j + 1) * b**(h - 1) * c if h >= 1 else None
        if b == 1:
            expected = a**(j + 1) * c
        test(successor == expected, (m, k, n, 'orbit transition'))
        # Every image has at most one predecessor; partial permutations.
        if successor is not None:
            test(successor % a == 0, (m, k, n, 'range'))
            test((successor // a) * b == n, (m, k, n, 'unique inverse'))

    if a >= 2 and b >= 2:
        for length in range(1, 16):
            seeds = [c for c in range(1, 201) if c % a and c % b]
            test(len(seeds) >= 2, (m, k, length, 'infinite multiplicity witnesses'))
            for c in seeds[:8]:
                orbit = [a**j * b**(length - j - 1) * c
                         for j in range(length)]
                test(len(orbit) == len(set(orbit)), (m, k, length, c, 'disjoint orbit'))
                for pos in range(length - 1):
                    test(image(orbit[pos], a, b) == orbit[pos + 1],
                         (m, k, length, c, pos, 'truncated forward shift'))
                test(image(orbit[-1], a, b) is None,
                     (m, k, length, c, 'terminal zero'))

    if a >= 2 and b == 1:
        for c in range(1, 31):
            if c % a:
                for j in range(12):
                    test(image(c*a**j, a, b) == c*a**(j+1),
                         (m, k, c, j, 'forward shift'))
    if a == 1 and b >= 2:
        for c in range(1, 31):
            if c % b:
                for j in range(1, 13):
                    test(image(c*b**j, a, b) == c*b**(j-1),
                         (m, k, c, j, 'backward shift'))
print(f'PASS: {CHECKS} exact integer/arithmetic diagnostics across {len(PAIRS)} pairs')
