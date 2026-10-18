#!/usr/bin/env python3
"""Exact modular linear-algebra checks for multipartite matching-difference spans.
The all-orders theorem is proved separately; these computations are finite corroboration.
"""
from collections import Counter
from itertools import combinations
from math import comb

PRIME = 1000003


def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    if cap is None:
        cap = n
    for a in range(min(n, cap), 0, -1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def matchings(edges, k):
    """All size-k sets of pairwise disjoint edges, each exactly once."""
    if k == 0:
        yield ()
        return
    for seq in combinations(edges, k):
        vs = [u for e in seq for u in e]
        if len(set(vs)) == 2 * k:
            yield seq


def polynomial(matching):
    coeff = {(): 1}
    for u, v in matching:
        update = {}
        for term, x in coeff.items():
            for vertex, sign in ((u, 1), (v, -1)):
                newterm = tuple(sorted(term + (vertex,)))
                update[newterm] = update.get(newterm, 0) + sign * x
        coeff = update
    return {t: x for t, x in coeff.items() if x}


def modular_rank(rows, keys):
    pivots = {}
    for row in rows:
        vec = {j: row.get(t, 0) % PRIME for j, t in enumerate(keys) if row.get(t, 0) % PRIME}
        while vec:
            p = min(vec)
            if p not in pivots:
                inv = pow(vec[p], PRIME - 2, PRIME)
                pivots[p] = {i: (x * inv) % PRIME for i, x in vec.items() if x}
                break
            mul = vec[p]
            for i, x in pivots[p].items():
                z = (vec.get(i, 0) - mul * x) % PRIME
                if z:
                    vec[i] = z
                else:
                    vec.pop(i, None)
    return len(pivots)


def count_max_matching(profile):
    n = sum(profile)
    part = {}
    j = 0
    for i, size in enumerate(profile):
        for _ in range(size):
            part[j] = i
            j += 1
    edges = tuple((u, v) for u in range(n) for v in range(u + 1, n) if part[u] != part[v])
    return edges


def main():
    cases = 0
    degrees = 0
    nonfull = 0
    max_rank = 0
    for n in range(2, 9):
        for profile in partitions(n):
            if len(profile) < 2:
                continue
            edges = count_max_matching(profile)
            nu = min(n // 2, n - max(profile))
            for k in range(0, n // 2 + 1):
                matches = list(matchings(edges, k))
                if k > nu:
                    assert not matches, ('maximum matching violation', profile, k)
                    nonfull += 1
                    continue
                assert matches, ('missing k-matching', profile, k)
                keys = list(combinations(range(n), k))
                rank = modular_rank((polynomial(m) for m in matches), keys)
                target = comb(n, k) - (comb(n, k - 1) if k else 0)
                assert rank == target, ('rank discrepancy', profile, k, rank, target)
                degrees += 1
                max_rank = max(max_rank, rank)
            cases += 1
    print('VERIFIED_MULTIPARTITE_CASES', cases)
    print('VERIFIED_DEGREES', degrees)
    print('VERIFIED_ZERO_DEGREES', nonfull)
    print('MAX_RECORDED_SPECHT_RANK', max_rank)
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
