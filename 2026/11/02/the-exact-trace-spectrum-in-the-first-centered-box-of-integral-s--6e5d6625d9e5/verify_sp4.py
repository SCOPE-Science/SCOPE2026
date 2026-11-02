#!/usr/bin/env python3
"""Exact first-box trace enumerator for integral 4 by 4 symplectic matrices.

Requires Python 3 standard library only. Both checks traverse complete finite
spaces using algebraically equivalent, differently arranged symplectic tests.
"""
from collections import Counter
from itertools import product

EXPECTED = {-4: 561, -3: 1000, -2: 1900, -1: 2840, 0: 4710,
            1: 2840, 2: 1900, 3: 1000, 4: 561}
PAIR_PROFILE = {8: 512, 9: 128, 12: 416, 14: 128,
                18: 96, 21: 128, 27: 32}


def bracket(x, y):
    return (x[0]*y[2] + x[1]*y[3]
            - x[2]*y[0] - x[3]*y[1])


def column_algorithm():
    vectors = list(product((-1, 0, 1), repeat=4))
    brackets = [[bracket(v, w) for w in vectors] for v in vectors]
    nonzero = [i for i, v in enumerate(vectors) if any(v)]
    trace = Counter()
    base_completion = Counter()
    for i in nonzero:
        for j in nonzero:
            if brackets[i][j] != 0:
                continue
            first = [k for k in range(81)
                     if brackets[i][k] == 1 and brackets[j][k] == 0]
            second = [k for k in range(81)
                      if brackets[i][k] == 0 and brackets[j][k] == 1]
            if not first or not second:
                continue
            completions = 0
            for k in first:
                for ell in second:
                    if brackets[k][ell] == 0:
                        completions += 1
                        trace[(vectors[i][0] + vectors[j][1]
                               + vectors[k][2] + vectors[ell][3])] += 1
            if completions:
                base_completion[completions] += 1
    return dict(trace), dict(base_completion)


def block_algorithm():
    """Independent enumeration using 2x2 block equations.

    If M=[[A,B],[C,D]], the necessary and sufficient conditions are
    (A^T C) symmetric, (B^T D) symmetric, A^T D-C^T B=I.
    Every 2x2 block has 81 possibilities; all four blocks are traversed.
    """
    blocks = list(product((-1, 0, 1), repeat=4))

    def transpose_times(x, y):
        return (x[0]*y[0]+x[2]*y[2], x[0]*y[1]+x[2]*y[3],
                x[1]*y[0]+x[3]*y[2], x[1]*y[1]+x[3]*y[3])

    products = [[transpose_times(x, y) for y in blocks] for x in blocks]
    trace = Counter()
    for ai, a in enumerate(blocks):
        for ci, c in enumerate(blocks):
            ac = products[ai][ci]
            if ac[1] != ac[2]:
                continue
            for bi, b in enumerate(blocks):
                cb = products[ci][bi]
                required_ad = (cb[0]+1, cb[1], cb[2], cb[3]+1)
                for di, d in enumerate(blocks):
                    bd = products[bi][di]
                    if bd[1] != bd[2]:
                        continue
                    if products[ai][di] == required_ad:
                        trace[a[0]+a[3]+d[0]+d[3]] += 1
    return dict(trace)


def main():
    by_columns, completion_profile = column_algorithm()
    by_blocks = block_algorithm()
    assert by_columns == EXPECTED, ('column calculation', by_columns)
    assert by_blocks == EXPECTED, ('block calculation', by_blocks)
    assert completion_profile == PAIR_PROFILE, completion_profile
    assert sum(by_columns.values()) == 17312
    assert sum(n * multiplicity for n, multiplicity
               in completion_profile.items()) == 17312
    assert sum(completion_profile.values()) == 1440
    assert all(by_columns[t] == by_columns[-t] for t in EXPECTED)
    print('VERIFY_OK: distinct algorithms agree; 17312 matrices')
    print('trace distribution:', sorted(by_columns.items()))
    print('first-column-pair completion profile:', sorted(completion_profile.items()))


if __name__ == '__main__':
    main()
