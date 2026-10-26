#!/usr/bin/env python3
"""Independent finite checks of an exact binary abelian-square avoidance classification.

No external dependencies.  Results from finite tests are not used as an infinite proof.
"""
from itertools import product
from collections import Counter
from fractions import Fraction
import random


def is_valid_direct(word):
    """Test each even factor by its two explicit Parikh vectors."""
    n = len(word)
    for width in range(2, n + 1, 2):
        half = width // 2
        for left in range(n - width + 1):
            f = word[left:left + width]
            if sum(f[:half]) == sum(f[half:]) and 0 < sum(f) < width:
                return False
    return True


def is_valid_structural(word):
    runs = []
    for x in word:
        if runs and runs[-1][0] == x:
            runs[-1][1] += 1
        else:
            runs.append([x, 1])
    if len(runs) <= 2:
        return True
    if len(runs) == 3:
        return runs[1][1] % 2 == 1
    if len(runs) == 4:
        h, i, j, k = (z[1] for z in runs)
        return i % 2 == j % 2 == 1 and h < j and k < i
    return False


def by_weight(x, y):
    if min(x, y) == 0:
        return 1
    return (2 + (y - 1 if x % 2 else 0)
            + (x - 1 if y % 2 else 0)
            + 2 * (x // 4) * (y // 4))


def by_length(n):
    return sum(by_weight(x, n - x) for x in range(n + 1))


def by_gf(n):
    if n == 0:
        return 0
    one = 2
    two = 2 * max(n - 1, 0)
    three = 2 * sum(n - b - 1 for b in range(1, n - 1, 2))
    four = 2 * sum((x // 4) * ((n - x) // 4)
                   for x in range(1, n))
    return one + two + three + four


def main():
    # Complete brute-force coverage through all 65536 words at length 16.
    for n in range(1, 17):
        by_weight_direct = Counter()
        for w in product((0, 1), repeat=n):
            actual = is_valid_direct(w)
            assert actual == is_valid_structural(w), (n, w)
            if actual:
                by_weight_direct[sum(w)] += 1
        for x in range(n + 1):
            assert by_weight_direct[x] == by_weight(x, n - x), (n, x)
        assert sum(by_weight_direct.values()) == by_length(n) == by_gf(n), n

    # Separate randomized longer length comparison, independently scanned.
    rng = random.Random(2026)
    for n in (17, 19, 23, 37, 53, 81):
        for _ in range(100):
            w = tuple(rng.randrange(2) for _ in range(n))
            assert is_valid_structural(w) == is_valid_direct(w), (n, w)

    # Exact rational-GF coefficient checks and polynomial-growth bounds.
    for n in range(1, 501):
        assert by_length(n) == by_gf(n)
        assert abs(Fraction(by_length(n), n**3) - Fraction(1, 48)) < Fraction(5,n)

    print('VERIFY_OK')
    print('exhaustive lengths 1..16 and each Hamming weight; random longer words; exact GF coefficient checks 1..500')
    print('length counts n=1..20:', [by_length(n) for n in range(1, 21)])
    print('weight counts n=12:', [by_weight(x, 12-x) for x in range(13)])

if __name__ == '__main__':
    main()
