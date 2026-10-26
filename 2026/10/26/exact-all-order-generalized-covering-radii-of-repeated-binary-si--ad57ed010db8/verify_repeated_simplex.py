#!/usr/bin/env python3
"""Independent finite checks for the generalized covering radii of repeated binary simplex codes.

Requires Python 3 standard library only.  A histogram triple represents every target matrix
up to coordinate permutation inside each of its three equal column blocks.
"""
from itertools import product
from math import ceil
from random import Random


def compositions(total, size):
    if size == 1:
        yield (total,)
    else:
        for n in range(total + 1):
            for rest in compositions(total - n, size - 1):
                yield (n,) + rest


def matches(a, b, c, q):
    return max(a[u] + b[v] + c[u ^ v] for u in range(q) for v in range(q))


def extremal_histograms(m, q):
    s, r = divmod(m, q)
    hist = [[s] * q for _ in range(3)]
    if r <= q // 2:
        subgroup = [v for v in range(q) if v & (q // 2) == 0]
        coset = [v for v in range(q) if v & (q // 2) != 0]
        for v in subgroup[:r]:
            hist[0][v] += 1
            hist[1][v] += 1
        for v in coset[:r]:
            hist[2][v] += 1
    else:
        for v in range(r):
            for h in hist:
                h[v] += 1
    return hist


def predicted_max_matches(m, q):
    return ceil(m / q) + ceil(2 * m / q)


def verify():
    total_hist_triples = 0
    for t, upper_m in ((1, 7), (2, 4), (3, 2), (4, 1)):
        q = 1 << t
        for m in range(1, upper_m + 1):
            possibilities = list(compositions(m, q))
            smallest = 3*m + 1
            for a in possibilities:
                for b in possibilities:
                    for c in possibilities:
                        smallest = min(smallest, matches(a, b, c, q))
            count = len(possibilities)**3
            total_hist_triples += count
            expected = predicted_max_matches(m, q)
            assert smallest == expected, (t, m, smallest, expected)
            extremizer = extremal_histograms(m, q)
            assert all(sum(a) == m for a in extremizer)
            assert matches(*extremizer, q) == expected
            print(f'EXHAUSTIVE_HISTOGRAMS t={t} m={m} count={count} radius={3*m-smallest}')

    # Independent direct target-matrix enumeration, WITHOUT histogram enumeration.
    total_matrices = 0
    for t, m in ((1, 1), (2, 1), (1, 2), (2, 2), (3, 1), (4, 1)):
        q = 1 << t
        worst = -1
        for target in product(range(q), repeat=3*m):
            nearest = 3*m
            for u in range(q):
                for v in range(q):
                    model = (u,)*m + (v,)*m + (u^v,)*m
                    nearest = min(nearest, sum(x != y for x, y in zip(target, model)))
            worst = max(worst, nearest)
            total_matrices += 1
        assert worst == 3*m-predicted_max_matches(m,q), (t,m,worst)
        print(f'EXHAUSTIVE_MATRICES t={t} m={m} number={q**(3*m)} radius={worst}')

    rng = Random(341771)
    random_cases = 0
    for t in range(1,9):
        q = 1 << t
        for m in (1, 2, 3, 4, 5, 7, 8, 9, 15, 17, 31, 64):
            assert matches(*extremal_histograms(m,q),q) == predicted_max_matches(m,q)
            for _ in range(10):
                hists = [[0] * q for _ in range(3)]
                for h in hists:
                    for __ in range(m):
                        h[rng.randrange(q)] += 1
                assert matches(*hists,q) >= predicted_max_matches(m,q)
                random_cases += 1
    print(f'REPEATED_SIMPLEX_VERIFY_OK histograms={total_hist_triples} matrices={total_matrices} randomized={random_cases}')


if __name__ == '__main__':
    verify()
