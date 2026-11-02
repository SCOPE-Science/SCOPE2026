"""Finite independent checks for lower-approximation knowledge tomography.

Run: python3 checker.py. Uses only the Python standard library.
"""
from itertools import combinations


def partitions(n):
    result = []
    def grow(i, blocks):
        if i == n:
            result.append(tuple(sum(1 << j for j in block) for block in blocks))
            return
        for block in blocks:
            block.append(i)
            grow(i + 1, blocks)
            block.pop()
        blocks.append([i])
        grow(i + 1, blocks)
        blocks.pop()
    grow(0, [])
    return result


def lower(blocks, query):
    value = 0
    for block in blocks:
        if block & query == block:
            value |= block
    return value


def signatures_distinguish(parts, queries):
    return len({tuple(lower(p, x) for x in queries) for p in parts}) == len(parts)


# Discrete orders: independently enumerate all partitions, every subset query,
# all nonadaptive collections of fewer than n-1 queries for n<=5.
for n in range(1, 7):
    ps = partitions(n)
    prefix = [(1 << j) - 1 for j in range(1, n)]
    assert signatures_distinguish(ps, prefix), (n, 'prefix failure')
    assert len(ps) == (1, 1, 2, 5, 15, 52, 203)[n]
    if n <= 5:
        xs = list(range(1 << n))
        for k in range(n - 1):
            for qs in combinations(xs, k):
                assert not signatures_distinguish(ps, qs), (n, k, qs)


# Explicit finite posets. Build order-components, then every component-block
# partition; test both triangle confluence and recovery under persistent upsets.
orders = [
    [(0, 1), (1, 2), (0, 2)],          # one chain
    [(0, 1), (2, 3)],                  # two disjoint chains
    [(0, 2), (1, 2), (3, 4)],          # one vee and one chain
    [(0, 1), (1, 2), (0, 2), (3, 4), (5, 6)],
    [],                               # singleton
]
sizes = [3, 4, 5, 7, 1]
for n, strict_order in zip(sizes, orders):
    le = {(i, i) for i in range(n)} | set(strict_order)
    # Undirected comparability closure.
    parent = list(range(n))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, j in le:
        a, b = find(i), find(j)
        parent[b] = a
    roots = sorted({find(i) for i in range(n)})
    comps = [sum(1 << i for i in range(n) if find(i) == root) for root in roots]
    c = len(comps)
    all_upsets = [x for x in range(1 << n) if all(not (x & (1 << a)) or (x & (1 << b)) for a, b in le)]
    seq = [sum(comps[:j]) for j in range(1, c)]
    assert all(x in all_upsets for x in seq)
    observed = set()
    for p in partitions(c):
        blocks = tuple(sum(comps[i] for i in range(c) if mask & (1 << i)) for mask in p)
        relations = {(i, j) for i in range(n) for j in range(n)
                     if any(b & (1 << i) and b & (1 << j) for b in blocks)}
        assert all((w, u) in relations for w, v in le for vv, u in relations if v == vv)
        signature = tuple(lower(blocks, x) for x in seq)
        assert signature not in observed
        observed.add(signature)
    assert len(observed) == len(partitions(c))

print('ALL_CHECKS_OK')
