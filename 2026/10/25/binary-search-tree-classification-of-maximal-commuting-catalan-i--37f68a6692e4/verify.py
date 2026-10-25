#!/usr/bin/env python3
"""Independent finite checks of maximal commuting idempotent families in Catalan monoids.
No external packages are required.
"""
from functools import lru_cache
from math import comb


def cmonoid_projections(n):
    """All idempotent decreasing order-preserving transformations as tuples."""
    ans = {}
    for a in range(1 << (n - 1)):
        fixed = (1,) + tuple(i for i in range(2, n + 1) if (a >> (i - 2)) & 1)
        tup = tuple(max(j for j in fixed if j <= i) for i in range(1, n + 1))
        ans[a] = tup
    return ans


def mul(f, g):
    return tuple(f[g[i] - 1] for i in range(len(f)))


def bron_kerbosch(R, P, X, adj, acc):
    if not P and not X:
        acc.add(frozenset(R))
        return
    pivot = max(P | X, key=lambda v: len(P & adj[v])) if P | X else None
    for v in tuple(sorted(P - (adj[pivot] if pivot is not None else set()))):
        bron_kerbosch(R | {v}, P & adj[v], X & adj[v], adj, acc)
        P.remove(v)
        X.add(v)


def maximal_cliques_literal(n):
    maps = cmonoid_projections(n)
    masks = set(maps)
    adj = {a: set() for a in masks}
    for a in maps:
        for b in maps:
            if a != b and mul(maps[a], maps[b]) == mul(maps[b], maps[a]):
                adj[a].add(b)
    acc = set()
    bron_kerbosch(set(), set(masks), set(), adj, acc)
    return acc


@lru_cache(None)
def bst_cliques(keys):
    if not keys:
        return (frozenset([0]),)
    out = []
    for i, root in enumerate(keys):
        left_keys, right_keys = keys[:i], keys[i+1:]
        for L in bst_cliques(left_keys):
            for R in bst_cliques(right_keys):
                root_bit = 1 << (root - 2)
                family = {0}
                family.update(root_bit | a | b for a in L for b in R)
                out.append(frozenset(family))
    return tuple(out)


def run():
    for n in range(2, 8):
        actual = maximal_cliques_literal(n)
        predicted = set(bst_cliques(tuple(range(2, n + 1))))
        expected_catalan = comb(2*(n-1), n-1)//n
        assert len(predicted) == expected_catalan, (n, len(predicted), expected_catalan)
        assert actual == predicted, (n, len(actual), len(predicted), list(actual ^ predicted)[:2])
        minimum = min(len(c) for c in actual)
        min_count = sum(len(c) == n for c in actual)
        assert minimum == n and min_count == 2**(n-2), (n, minimum, min_count)
        size_profile = {s: sum(len(c) == s for c in actual) for s in sorted(set(map(len, actual)))}
        print('n=%d maximal=%d min=%d min_count=%d profile=%s' % (n,len(actual),minimum,min_count,size_profile))
    for n in range(8, 10):
        pred = bst_cliques(tuple(range(2,n+1)))
        assert len(pred) == comb(2*(n-1), n-1)//n
        assert len(set(pred)) == len(pred)
        assert min(map(len,pred)) == n
        assert sum(len(c)==n for c in pred)==2**(n-2)
        print('n=%d recursive_BSTs=%d, all distinct, sharp minima' % (n, len(pred)))
    print('VERIFY_OK_CATALAN_MAXIMAL_IDEMPOTENT_CLIQUES')


if __name__ == '__main__':
    run()
