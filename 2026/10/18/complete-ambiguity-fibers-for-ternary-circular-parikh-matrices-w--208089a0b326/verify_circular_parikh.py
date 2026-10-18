#!/usr/bin/env python3
"""Independent exhaustive check of a restricted circular Parikh-matrix classification.

Only standard-library Python is required. The oracle computes subsequence counts
in every cyclic rotation, without using the positional formulas in the proof.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def full_matrix_signature(word):
    n = len(word)
    totals = [0, 0, 0]
    for k in range(n):
        v = word[k:] + word[:k]
        ca = cb = cab = cbc = cabc = 0
        for symbol in v:
            if symbol == 'a':
                ca += 1
            elif symbol == 'b':
                cab += ca
                cb += 1
            elif symbol == 'c':
                cabc += cab
                cbc += cb
            else:
                raise ValueError('Unknown symbol')
        totals[0] += cab
        totals[1] += cbc
        totals[2] += cabc
    return tuple(word.count(s) for s in 'abc') + tuple(totals)


def predicted_signature(c, t, u):
    n = c + 3
    s = t + u
    y = (t * (t - 1) + u * (u - 1)) // 2 - (u - t)
    return (2, 1, c, s, n * c - n * (n - 1) // 2 + s, y)


def check(max_c=35):
    tested = 0
    for c in range(max_c + 1):
        m, n = c + 2, c + 3
        observed = defaultdict(list)
        for t, u in combinations(range(1, m + 1), 2):
            w = ['c'] * n
            w[0], w[t], w[u] = 'b', 'a', 'a'
            key = full_matrix_signature(''.join(w))
            expected = predicted_signature(c, t, u)
            assert key == expected, ('matrix mismatch', c, t, u, key, expected)
            observed[key].append((t, u))
            tested += 1

        expected_doubletons = {
            frozenset(((t, t + 1), (t - 1, t + 2)))
            for t in range(2, c + 1)
        }
        doubletons = set()
        for fiber in observed.values():
            assert len(fiber) <= 2, ('oversized fiber', c, fiber)
            if len(fiber) == 2:
                doubletons.add(frozenset(fiber))
        assert doubletons == expected_doubletons, ('fiber mismatch', c)
        assert len(observed) == comb(c + 2, 2) - max(c - 1, 0)
        assert sum(len(v) == 1 for v in observed.values()) == comb(c + 2, 2) - 2 * max(c - 1, 0)

    # The unique-middle-letter and one-outer-letter boundary is injective.
    for c in range(max_c + 1):
        n = c + 2
        signatures = set()
        for t in range(1, n):
            w = ['c'] * n
            w[0], w[t] = 'b', 'a'
            signatures.add(full_matrix_signature(''.join(w)))
        assert len(signatures) == c + 1, ('one-outer boundary mismatch', c)

    print('CIRCULAR_PARIKH_CLASSIFICATION_PASS',
          'two_a_c_range=0..%d' % max_c,
          'anchored_necklaces=%d' % tested,
          'one_a_boundary_c_range=0..%d' % max_c)


if __name__ == '__main__':
    check()
