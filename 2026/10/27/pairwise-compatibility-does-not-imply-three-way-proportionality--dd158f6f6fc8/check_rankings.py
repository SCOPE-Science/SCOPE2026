#!/usr/bin/env python3
"""Reproduce a finite ranking-compression compatibility obstruction.

Run: python3 check_rankings.py
Uses only the Python standard library; no downloads or inputs are needed.
"""
from itertools import permutations, combinations, combinations_with_replacement
from math import comb

CANDIDATES = (1, 2, 3, 4, 5)
INPUT = (
    (2, 5, 1, 4, 3),
    (5, 3, 1, 2, 4),
    (2, 4, 1, 5, 3),
    (2, 3, 1, 5, 4),
    (2, 5, 3, 4, 1),
    (3, 2, 4, 5, 1),
)
K = 3

# The three explicit pairwise-compatible outputs.
WITNESSES = {
    ('pos', 'pair'): (
        (2, 1, 4, 5, 3), (2, 3, 5, 4, 1), (5, 3, 1, 2, 4)),
    ('pos', 'psc'): (
        (1, 2, 3, 5, 4), (2, 3, 4, 5, 1), (2, 5, 1, 4, 3)),
    ('pair', 'psc'): (
        (2, 1, 4, 5, 3), (2, 5, 3, 1, 4), (3, 2, 5, 4, 1)),
}


def features(candidates):
    m = len(candidates)
    ans = []
    for c in candidates:
        for level in range(1, m + 1):
            ans.append(('pos', c, level))
    for a in candidates:
        for b in candidates:
            if a != b:
                ans.append(('pair', a, b))
    for size in range(1, m + 1):
        for subset in combinations(candidates, size):
            ans.append(('psc', subset))
    return ans


def indicator(order, f):
    kind = f[0]
    if kind == 'pos':
        return int(order.index(f[1]) < f[2])
    if kind == 'pair':
        return int(order.index(f[1]) < order.index(f[2]))
    if kind == 'psc':
        return int(set(order[:len(f[1])]) == set(f[1]))
    raise AssertionError('Unknown condition')


def check_output(inp, out, kinds):
    # Directly apply all integer t in the original quantified definitions.
    n, k = len(inp), len(out)
    for f in features(tuple(inp[0])):
        if f[0] not in kinds:
            continue
        number_in = sum(indicator(p, f) for p in inp)
        number_out = sum(indicator(p, f) for p in out)
        for t in range(1, k + 1):
            if number_in * k >= t * n and number_out < t:
                return False
    return True


def main():
    all_rankings = tuple(permutations(CANDIDATES))
    feats = features(CANDIDATES)
    by_type = {kind: tuple(i for i, f in enumerate(feats) if f[0] == kind)
               for kind in ('pos', 'pair', 'psc')}
    # A separate implementation: integer lower quotas computed from all inputs.
    incidence = tuple(tuple(indicator(p, f) for f in feats) for p in all_rankings)
    index = {p: i for i, p in enumerate(all_rankings)}
    q = tuple(sum(incidence[index[p]][j] for p in INPUT) * K // len(INPUT)
              for j in range(len(feats)))

    for kinds, rankings in WITNESSES.items():
        assert len(rankings) == K
        assert all(set(p) == set(CANDIDATES) for p in rankings)
        assert check_output(INPUT, rankings, set(kinds))
        for kind in kinds:
            assert all(sum(indicator(p, feats[j]) for p in rankings) >= q[j]
                       for j in by_type[kind])

    counts = {('pos', 'pair'): 0, ('pos', 'psc'): 0,
              ('pair', 'psc'): 0, ('pos', 'pair', 'psc'): 0}
    tested = 0
    for i, j, h in combinations_with_replacement(range(len(all_rankings)), K):
        row_i, row_j, row_h = incidence[i], incidence[j], incidence[h]
        status = {}
        for kind, ids in by_type.items():
            status[kind] = all(row_i[s] + row_j[s] + row_h[s] >= q[s]
                               for s in ids)
        for kinds in counts:
            if all(status[kind] for kind in kinds):
                counts[kinds] += 1
        tested += 1
    assert tested == comb(len(all_rankings) + K - 1, K) == 295240
    assert counts == {('pos', 'pair'): 5, ('pos', 'psc'): 44,
                      ('pair', 'psc'): 6, ('pos', 'pair', 'psc'): 0}, counts

    # Independent small logical-certificate prerequisites, with literal condition labels.
    necessary = (
        ('psc', (2, 5)), ('psc', (2, 3)), ('pos', 5, 4),
        ('pos', 1, 3), ('pos', 3, 3), ('pair', 2, 4),
        ('pair', 5, 3), ('pair', 3, 1), ('pair', 5, 1),
        ('pair', 4, 5), ('pair', 1, 5),
    )
    support = tuple(sum(indicator(p, f) for p in INPUT) for f in necessary)
    assert support == (2, 2, 6, 4, 4, 6, 4, 4, 4, 2, 2), support
    print('PASS: 120 distinct linear orders; 295240 multisets of three orders tested.')
    print('PASS: pairwise compatibility counts: 5, 44, 6; joint count: 0.')
    print('PASS: all displayed witnesses satisfy the directly quantified axioms.')
    print('PASS: every condition in the 11-condition contradiction has the claimed support.')

    # Replication and universally bottom-ranked additional alternatives.
    for copies in (1, 2, 3):
        for additional in (0, 1, 2):
            extra = tuple(range(6, 6 + additional))
            inp = tuple(p + extra for p in INPUT for _ in range(copies))
            for kinds, rankings in WITNESSES.items():
                assert check_output(inp, tuple(p + extra for p in rankings), set(kinds))
    print('PASS: finite extension checks for copies 1..3 and 0..2 extra alternatives.')


if __name__ == '__main__':
    main()
