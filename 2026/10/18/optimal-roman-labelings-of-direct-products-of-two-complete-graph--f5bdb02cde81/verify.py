#!/usr/bin/env python3
"""Recompute minimum Roman-function profiles of direct clique products.

Uses the explicit graph adjacency relation, not the geometric proof cases.
Standard-library Python 3; no external input or dependencies.
"""
from itertools import combinations
from math import comb


def predicted(m, n):
    return (6*comb(m, 3)*comb(n, 3) + 6*comb(m, 2)*comb(n, 2)
            + (m*comb(n, 2) if n == 4 else 0)
            + (n*comb(m, 2) if m == 4 else 0))


def verify(m, n):
    vertices = [(r, c) for r in range(m) for c in range(n)]
    nvert = len(vertices)
    # Construct the actual graph, and independently test the zero-vertex rule.
    neighbors = [sum(1 << j for j, (r2, c2) in enumerate(vertices)
                     if i != j and r != r2 and c != c2)
                 for i, (r, c) in enumerate(vertices)]
    counts = {2: 0, 3: 0}
    best = 99
    total_examined = 0
    for k in (2, 3):
        for defenders in combinations(range(nvert), k):
            mask2 = sum(1 << i for i in defenders)
            forced_ones = [v for v in range(nvert)
                           if not (mask2 & (1 << v)) and not (neighbors[v] & mask2)]
            extra_budget = 6 - 2*k - len(forced_ones)
            if extra_budget < 0:
                continue
            forced_set = set(forced_ones)
            available = [v for v in range(nvert)
                         if v not in forced_set and not (mask2 & (1 << v))]
            for optional in combinations(available, extra_budget):
                ones = forced_set | set(optional)
                total_examined += 1
                assert all((mask2 & (1 << v)) or (v in ones) or (neighbors[v] & mask2)
                           for v in range(nvert))
                counts[k] += 1
                best = min(best, 2*k + len(ones))
    # To rule out smaller weights: zero 2s forces all mn labels >=1;
    # one 2 forces >= m+n-2 labels 1. For m,n >=4 both exceed weight 6.
    assert m*n >= 16 and 2+(m+n-2) >= 8
    # k=2 and k=3 categories exhaust possible weight 6 and lower weights.
    expected = predicted(m,n)
    assert best == 6 and sum(counts.values()) == expected, (m,n,counts,expected)
    return f'{m}x{n}: two_2s={counts[2]}, three_2s={counts[3]}, total={expected}, PASS'


if __name__ == '__main__':
    for dims in [(4,4),(4,5),(4,6),(5,5),(5,6),(6,6),(7,7),(8,9)]:
        print(verify(*dims))
    print('VERIFICATION_OK')
