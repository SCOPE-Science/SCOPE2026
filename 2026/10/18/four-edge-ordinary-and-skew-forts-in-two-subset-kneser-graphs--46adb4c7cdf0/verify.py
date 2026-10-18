#!/usr/bin/env python3
"""Exact independent checks of minimum ordinary and skew forts in K(n,2).

Uses only the Python standard library.  The input graphs and forcing processes
are constructed from their definitions rather than from the classification.
"""
from collections import Counter
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def graph(n):
    edges = list(combinations(range(n), 2))
    adj = [0] * len(edges)
    for i, a in enumerate(edges):
        for j, b in enumerate(edges):
            if i != j and not set(a).intersection(b):
                adj[i] |= 1 << j
    return edges, adj


def stalled(white, adj, skew):
    full = (1 << len(adj)) - 1
    for i, nbr in enumerate(adj):
        if skew or not (white & (1 << i)):
            if (nbr & white).bit_count() == 1:
                return False
    return 0 < white <= full


def closure_white(white, adj, skew):
    """Complement of deterministic coloring closure, independent of any formula."""
    while True:
        moves = 0
        for i, nbr in enumerate(adj):
            if skew or not (white & (1 << i)):
                w = nbr & white
                if w and not (w & (w - 1)):
                    moves |= w
        if not moves:
            return white
        white &= ~moves


def type_of(edges, subset, n):
    deg = [0] * n
    for j in subset:
        a, b = edges[j]
        deg[a] += 1
        deg[b] += 1
    if 4 in deg:
        return 'star4'
    if all(x <= 1 for x in deg):
        return 'matching4'
    if sorted([x for x in deg if x], reverse=True) == [2] * 4:
        return 'cycle4'
    if sorted([x for x in deg if x], reverse=True) == [3, 1, 1, 1, 1, 1]:
        return 'claw3_plus_edge'
    return 'other'


def predicted(n):
    skew_count = n * choose(n - 1, 4) + 105 * choose(n, 8)
    ordinary_count = skew_count + 3 * choose(n, 4) + (60 if n == 6 else 0)
    return ordinary_count, skew_count


def run():
    examined = 0
    dynamic_states = 0
    for n in range(5, 11):
        edges, adj = graph(n)
        m = len(edges)
        counts = Counter()
        observed_types = Counter()
        for k in range(1, 5):
            for subset in combinations(range(m), k):
                examined += 1
                white = sum(1 << i for i in subset)
                f = stalled(white, adj, False)
                s = stalled(white, adj, True)
                assert not s or f
                if k < 4:
                    assert not f and not s, (n, k, subset)
                else:
                    t = type_of(edges, subset, n)
                    if f:
                        counts['ordinary'] += 1
                        observed_types[t] += 1
                    if s:
                        counts['skew'] += 1
                        assert t in ('star4', 'matching4'), (n, t, subset)
                    if t == 'star4' or t == 'matching4':
                        assert f and s
                    elif t == 'cycle4' or (t == 'claw3_plus_edge' and n == 6):
                        assert f and not s
                    else:
                        assert not f and not s, (n, t, subset)
                if n <= 8:
                    # Starting from the complement of a small white set, run the
                    # two distinct coloring algorithms to a fixed point.
                    dynamic_states += 1
                    assert bool(closure_white(white, adj, False)) == f
                    assert bool(closure_white(white, adj, True)) == s
        ordinary, skew_count = predicted(n)
        assert counts == Counter({'ordinary': ordinary, 'skew': skew_count}), (n, counts)
        expected = Counter({'star4': n * choose(n - 1, 4),
                            'cycle4': 3 * choose(n, 4)})
        if n >= 8:
            expected['matching4'] = 105 * choose(n, 8)
        if n == 6:
            expected['claw3_plus_edge'] = 60
        assert observed_types == expected, (n, observed_types, expected)
        print('n=%d ordinary=%d skew=%d types=%s' % (
            n, ordinary, skew_count, dict(sorted(observed_types.items()))))
    print('VERIFICATION_OK n=5..10 examined=%d dynamic_states=%d' %
          (examined, dynamic_states))


if __name__ == '__main__':
    run()
