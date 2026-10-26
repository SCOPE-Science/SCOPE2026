#!/usr/bin/env python3
"""Exhaustive small-word verification for the adjacent-swap radius-two theorem."""
from fractions import Fraction
from itertools import product
from math import comb


def local_formula(word):
    n = len(word)
    assert n >= 2
    boundaries = sum(a != b for a, b in zip(word, word[1:]))
    consecutive = all_distinct = one_boundary = 0
    for a, b, c in zip(word, word[1:], word[2:]):
        consecutive += (a != b and b != c)
        all_distinct += (a != b and b != c and a != c)
        one_boundary += (a == b) != (b == c)
    return (1 + boundaries + comb(boundaries, 2) - consecutive
            + 2 * all_distinct + one_boundary)


def direct_ball(word):
    def neighbors(w):
        for i in range(len(w) - 1):
            if w[i] != w[i + 1]:
                v = list(w)
                v[i], v[i + 1] = v[i + 1], v[i]
                yield tuple(v)

    seen = {tuple(word)}
    frontier = seen
    for _ in range(2):
        frontier = {v for w in frontier for v in neighbors(w)} - seen
        seen |= frontier
    return len(seen)


def predicted_mean(n, q):
    p = Fraction(q - 1, q)
    return 1 + (n - 1) * p + Fraction((n - 2) * (n + 1), 2) * p * p


def check():
    words_tested = 0
    for q, last_n in [(2, 12), (3, 9), (4, 7), (5, 6), (6, 5)]:
        for n in range(2, last_n + 1):
            total = 0
            maximum = 0
            maxima = 0
            for word in product(range(q), repeat=n):
                by_formula = local_formula(word)
                by_brute = direct_ball(word)
                assert by_formula == by_brute, (q, n, word, by_formula, by_brute)
                total += by_formula
                words_tested += 1
                if by_formula > maximum:
                    maximum, maxima = by_formula, 1
                elif by_formula == maximum:
                    maxima += 1
            assert Fraction(total, q**n) == predicted_mean(n, q), (q, n)
            if q >= 3:
                assert maximum == comb(n + 1, 2) - 1
                assert maxima == q * (q - 1) * (q - 2)**(n - 2)
            if q == 2 and n == 4:
                assert maximum == 6
    print('ADJACENT_SWAP_RADIUS2_PASS', 'words=', words_tested,
          'q_ranges=2:2..12,3:2..9,4:2..7,5:2..6,6:2..5',
          'formula=direct_BFS', 'means=exact', 'q>=3_maxima=verified')


if __name__ == '__main__':
    check()
