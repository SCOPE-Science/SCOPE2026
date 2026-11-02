#!/usr/bin/env python3
"""Exact rational checks for the weighted-pentagon retraction theorem.

No nonstandard dependencies; finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as Q
from itertools import permutations, product


def metric(t):
    d = [[Q(0) if i == j else Q(1000) for j in range(5)] for i in range(5)]
    for i in range(5):
        a, b = i, (i + 1) % 5
        w = t if i == 4 else Q(1)
        d[a][b] = d[b][a] = w
    for k in range(5):
        for i in range(5):
            for j in range(5):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def lipschitz(d, mapping):
    return max(d[mapping[i]][mapping[j]] / d[i][j]
               for i in range(5) for j in range(i + 1, 5))


def proposed_maps(t):
    if t <= 1:
        return ((0, 0, 0, 0, 0), (0, 1, 0, 1, 0),
                (0, 1, 2, 1, 0), (0, 1, 2, 3, 0), (0, 1, 2, 3, 4))
    return ((0, 0, 0, 0, 0), (0, 1, 0, 1, 0),
            (0, 1, 2, 1, 2), (0, 1, 2, 3, 2), (0, 1, 2, 3, 4))


def formula(t):
    return 1 + t if t <= 1 else (Q(2) / t if t <= 2 else Q(1))


# Each triple is omitted vertex, target, fixed witness.
WITNESSES = ((1, 0, 2), (1, 2, 0), (1, 3, 0), (1, 4, 2),
             (2, 0, 3), (2, 1, 3), (2, 3, 1), (2, 4, 1),
             (3, 0, 2), (3, 1, 4), (3, 2, 4), (3, 4, 2),
             (4, 0, 3), (4, 1, 3), (4, 2, 0), (4, 3, 0))


def exact_optimum(t):
    """Enumerate all compatible retractions, with no prespecified ordering."""
    d = metric(t)
    bound = Q(1000)
    for order_suffix in permutations((1, 2, 3, 4)):
        order = (0,) + order_suffix

        def rec(level, old_map, sofar):
            nonlocal bound
            if level == 0:
                bound = min(bound, sofar)
                return
            # Current level fixes its first level+1 vertices.
            retained = order[:level + 1]
            omitted = order[level + 1:]
            for values in product(retained, repeat=len(omitted)):
                mp = {v: v for v in retained}
                mp.update(zip(omitted, values))
                nxt = tuple(mp[v] for v in range(5))
                if any(nxt[old_map[v]] != nxt[v] for v in range(5)):
                    continue
                lip = max(sofar, lipschitz(d, nxt))
                if lip > bound:
                    continue
                rec(level - 1, nxt, lip)

        rec(3, tuple(range(5)), Q(1))
    return bound


def main():
    test_values = (Q(1, 10), Q(1, 2), Q(3, 4), Q(1), Q(5, 4),
                   Q(3, 2), Q(2), Q(5, 2), Q(4), Q(5))
    for t in test_values:
        d = metric(t)
        maps = proposed_maps(t)
        assert max(lipschitz(d, m) for m in maps) == formula(t)
        for i, r in enumerate(maps):
            assert all(r[k] == k for k in range(i + 1))
            for j, s in enumerate(maps):
                assert all(r[s[k]] == maps[min(i, j)][k] for k in range(5))
        if t <= 2:
            for omitted, target, fixed in WITNESSES:
                assert d[target][fixed] / d[omitted][fixed] >= formula(t)
    for t in (Q(1, 2), Q(1), Q(3, 2), Q(2), Q(3)):
        assert exact_optimum(t) == formula(t)
    print('PENTAGON_RATIONAL_CHECK_OK')


if __name__ == '__main__':
    main()
