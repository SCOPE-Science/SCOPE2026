#!/usr/bin/env python3
"""Exhaustive finite check of the circular binary mesosome theorem.

Checks all binary words of lengths 1 through 15. Mathematical all-length
proof is given separately; finite checks do not replace that proof.
"""
from itertools import product


def avoids_circular_mesosome(w):
    n = len(w)
    twice = w + w
    for i in range(n):
        for k in range(2, n // 2 + 1):
            left = twice[i:i + k]
            right = twice[i + k:i + 2 * k]
            if left != right and right in (left + left)[1:-1]:
                return False
    return True


def allowed_by_run_theorem(w):
    n = len(w)
    transitions = sum(w[i] != w[(i + 1) % n] for i in range(n))
    if transitions == 0:
        return True
    if transitions == n:
        return n % 2 == 0
    if transitions != 2:
        return False
    a = w.count('0')
    b = n - a
    return min(a, b) == 1 or (a % 2 == 1 and b % 2 == 1)


def canonical_rotation(w):
    return min(w[k:] + w[:k] for k in range(len(w)))


def expected_counts(n):
    if n == 1:
        return (2, 2)
    if n == 2:
        return (3, 4)
    if n % 2:
        return (4, 2 + 2*n)
    return (n//2 + 3, n*n//2 + 4)


def run():
    total = 0
    for n in range(1, 16):
        words = [''.join(bits) for bits in product('01', repeat=n)]
        valid = set()
        for w in words:
            brute = avoids_circular_mesosome(w)
            formula = allowed_by_run_theorem(w)
            assert brute == formula, (n, w, brute, formula)
            if brute:
                valid.add(w)
        necklaces = {canonical_rotation(w) for w in valid}
        expected_necklaces, expected_words = expected_counts(n)
        assert len(necklaces) == expected_necklaces, (n, len(necklaces), expected_necklaces)
        assert len(valid) == expected_words, (n, len(valid), expected_words)
        print(f"n={n} words={len(valid)} necklaces={len(necklaces)}")
        total += len(words)
    print(f'CIRCULAR_MESOSOME_PASS tested_words={total} n_range=1..15')


if __name__ == '__main__':
    run()
