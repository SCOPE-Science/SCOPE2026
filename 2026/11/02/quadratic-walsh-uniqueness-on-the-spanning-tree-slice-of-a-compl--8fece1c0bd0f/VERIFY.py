#!/usr/bin/env python3
"""Exact finite checks of low-degree edge-character restrictions on uniform labelled trees.

The infinite-rank theorem has an independent analytic inductive proof; this
script performs finite exact consistency checks only.
"""
from itertools import combinations, product
from math import comb

P = 1000003


def edges_of_prufer(code, n):
    deg = [1] * n
    for v in code:
        deg[v] += 1
    ans = []
    for v in code:
        u = next(i for i in range(n) if deg[i] == 1)
        ans.append(tuple(sorted((u, v))))
        deg[u] -= 1
        deg[v] -= 1
    last = [i for i in range(n) if deg[i] == 1]
    ans.append(tuple(last))
    return frozenset(ans)


def modular_rank(rows, width, p=P):
    pivots = {}
    for nonzero in rows:
        v = [0] * width
        for i in nonzero:
            v[i] = 1
        while True:
            idx = next((i for i, x in enumerate(v) if x), None)
            if idx is None:
                break
            if idx in pivots:
                pivot = pivots[idx]
                multiplier = v[idx]
                for j in range(idx, width):
                    v[j] = (v[j] - multiplier * pivot[j]) % p
            else:
                inv = pow(v[idx], -1, p)
                for j in range(idx, width):
                    v[j] = v[j] * inv % p
                pivots[idx] = v
                break
    return len(pivots)


def test(n):
    E = list(combinations(range(n), 2))
    edge_index = {e: i for i, e in enumerate(E)}
    pairs = list(combinations(range(len(E)), 2))
    pair_index = {pair: i for i, pair in enumerate(pairs)}
    seen = 0

    def rows():
        nonlocal seen
        for seq in product(range(n), repeat=n-2):
            forest = edges_of_prufer(seq, n)
            assert len(forest) == n-1
            assert len({tuple(sorted(edge)) for edge in forest}) == n-1
            J = sorted(edge_index[e] for e in forest)
            seen += 1
            yield [pair_index[pair] for pair in combinations(J, 2)]

    rank = modular_rank(rows(), len(pairs))
    assert seen == n ** (n-2), (n, seen)
    assert rank == comb(comb(n, 2), 2), (n, rank)
    print('n=%d trees=%d pair-columns=%d exact-prime-field-rank=%d' %
          (n, seen, len(pairs), rank))


if __name__ == '__main__':
    for n in range(3, 7):
        test(n)
    print('PASS: all four exact finite consistency checks; theorem requires the separate induction.')
