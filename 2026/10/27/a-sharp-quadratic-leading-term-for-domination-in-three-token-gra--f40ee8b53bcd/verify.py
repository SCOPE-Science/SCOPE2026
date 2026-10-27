#!/usr/bin/env python3
"""Independent finite checks of the three-token complete-bipartite construction.

This checks explicit witnesses only. The infinite lower bound uses Mantel's
triangle-free-graph theorem, with a self-contained proof in RESULT.md.
No external packages are required.
"""
from itertools import combinations
from math import comb
import json


def candidates(n):
    """Return the proposed dominating family as sets of base vertex labels."""
    assert n >= 4
    B = list(range(2, n + 2))
    s = n // 2
    X, Y = B[:s], B[s:]
    W = set(B[:3])
    selected = set()
    for part in (X, Y):
        selected.update(frozenset((0, b, c)) for b, c in combinations(part, 2))
    selected.add(frozenset(W))
    selected.update(frozenset((0, 1, b)) for b in B if b not in W)
    assert len(selected) == comb(n, 2) - (n * n // 4) + n - 2
    return selected


def adjacent(p, q):
    """Adjacency of two token positions, without reusing layer arguments."""
    left = p - q
    right = q - p
    return (len(left) == len(right) == 1 and
            (next(iter(left)) < 2) != (next(iter(right)) < 2))


def validate(n):
    S = candidates(n)
    counts = {0: 0, 1: 0, 2: 0}
    for tri in combinations(range(n + 2), 3):
        q = frozenset(tri)
        k = sum(v < 2 for v in q)
        counts[k] += 1
        if q not in S and not any(adjacent(q, d) for d in S):
            raise AssertionError('undominated token position: ' + str((n, tri)))
    return {'n': n,
            'lower_bound': comb(n, 2) - n*n//4,
            'witness_size': len(S),
            'total_token_vertices': sum(counts.values()),
            'layer_sizes': [counts[i] for i in range(3)]}


def check_mantel_small():
    """Exhaustively confirm Mantel bound on graphs of up to six vertices."""
    checked = {}
    for n in range(2, 7):
        edges = list(combinations(range(n), 2))
        triangles = list(combinations(range(n), 3))
        mx = 0
        for mask in range(1 << len(edges)):
            E = {edge for i, edge in enumerate(edges) if (mask >> i) & 1}
            if any(all(tuple(sorted(edge)) in E for edge in combinations(t, 2))
                   for t in triangles):
                continue
            mx = max(mx, len(E))
        assert mx == n*n//4
        checked[n] = mx
    return checked


if __name__ == '__main__':
    records = [validate(n) for n in range(4, 19)]
    print(json.dumps({'construction_validated_n': [4, 18],
                      'records': records,
                      'mantel_exhaustive_small': check_mantel_small()},
                     indent=2, sort_keys=True))
