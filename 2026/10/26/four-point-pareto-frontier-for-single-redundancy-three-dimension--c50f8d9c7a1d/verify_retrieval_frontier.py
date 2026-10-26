#!/usr/bin/env python3
"""Reproduce the four-coordinate, two-file retrieval frontier.

All calculations use exact rational arithmetic. This verifier independently
checks the coupon-drawing Markov recurrence and the subset-count formula.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import comb


def rank(vectors, p):
    mat = [list(v) for v in vectors]
    r = 0
    for c in range(3):
        pivot = next((i for i in range(r, len(mat)) if mat[i][c] % p), None)
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        inv = pow(mat[r][c], -1, p)
        mat[r] = [(x * inv) % p for x in mat[r]]
        for i in range(r + 1, len(mat)):
            t = mat[i][c]
            mat[i] = [(x - t * y) % p for x, y in zip(mat[i], mat[r])]
        r += 1
    return r


def projective_points(p):
    pts = set()
    for v in product(range(p), repeat=3):
        if v == (0, 0, 0):
            continue
        first = next(t for t in v if t)
        inv = pow(first, -1, p)
        pts.add(tuple((t * inv) % p for t in v))
    return sorted(pts)


def contained(target, vectors, p):
    return rank(vectors + list(target), p) == rank(vectors, p)


def subset_expectations(cols, p):
    a = [[0] * 5, [0] * 5]
    targets = [((1, 0, 0),), ((0, 1, 0), (0, 0, 1))]
    for mask in range(1, 16):
        v = [cols[j] for j in range(4) if (mask >> j) & 1]
        for i, target in enumerate(targets):
            a[i][len(v)] += int(contained(target, v, p))
    return tuple(Fraction(25, 3) - sum((Fraction(a[i][s], comb(3, s)) for s in range(1, 4)), Fraction(0)) for i in (0, 1))


def markov_expectations(cols, p):
    targets = [((1, 0, 0),), ((0, 1, 0), (0, 0, 1))]
    result = []
    for target in targets:
        time = [Fraction(0)] * 16
        for mask in range(15, -1, -1):
            vectors = [cols[i] for i in range(4) if (mask >> i) & 1]
            if contained(target, vectors, p):
                continue
            missing = [i for i in range(4) if not (mask >> i) & 1]
            time[mask] = (4 + sum((time[mask | (1 << i)] for i in missing), Fraction(0))) / len(missing)
        result.append(time[0])
    return tuple(result)


def frontier(points):
    minimum_e2 = None
    result = []
    for (e1, e2) in sorted(points):
        if minimum_e2 is None or e2 < minimum_e2:
            result.append((e1, e2))
            minimum_e2 = e2
    return result


def test_field(p):
    pts = projective_points(p)
    populations = defaultdict(int)
    nvalid = 0
    for idx in combinations_with_replacement(range(len(pts)), 4):
        cols = [pts[i] for i in idx]
        if rank(cols, p) != 3:
            continue
        nvalid += 1
        by_subset = subset_expectations(cols, p)
        by_markov = markov_expectations(cols, p)
        assert by_subset == by_markov, (p, cols, by_subset, by_markov)
        populations[by_subset] += 1
    expected_frontier = [(Fraction(2), Fraction(6)),
                         (Fraction(8, 3), Fraction(5)),
                         (Fraction(3), Fraction(4)),
                         (Fraction(4), Fraction(10, 3))]
    got = frontier(populations)
    assert got == expected_frontier, (p, got)
    print('FIELD', p, 'PROJECTIVE_POINTS', len(pts), 'FULL_RANK_MULTISETS', nvalid,
          'DISTINCT_EXPECTATION_PAIRS', len(populations), 'FRONTIER',
          [(str(a), str(b)) for a, b in got])


def test_witnesses():
    P = (1, 0, 0)
    U = (0, 1, 0)
    V = (0, 0, 1)
    w = [([P, P, U, V], (Fraction(2), Fraction(6))),
         ([P, U, (1, 1, 0), V], (Fraction(8, 3), Fraction(5))),
         ([P, U, V, (1, 1, 1)], (Fraction(3), Fraction(4))),
         ([P, U, V, (0, 1, 1)], (Fraction(4), Fraction(10, 3)))]
    for p in (2, 3, 5, 7):
        for cols, expected in w:
            assert rank(cols, p) == 3
            assert subset_expectations(cols, p) == markov_expectations(cols, p) == expected
    print('FOUR_WITNESSES_VERIFIED_IN_PRIME_FIELDS', (2, 3, 5, 7))


if __name__ == '__main__':
    test_witnesses()
    for p in (2, 3):
        test_field(p)
    print('VERIFY_OK')
