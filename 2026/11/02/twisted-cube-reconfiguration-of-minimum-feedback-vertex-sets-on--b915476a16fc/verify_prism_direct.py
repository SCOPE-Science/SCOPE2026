#!/usr/bin/env python3
"""Direct finite-graph checker for minimum feedback-vertex-set exchanges.
Independent of the coordinate transfer model. Python 3 standard library only.
Run: python3 verify_prism_direct.py
"""
from collections import Counter, deque
from itertools import combinations


def graph(n):
    adjacency = [0] * (2 * n)
    for i in range(n):
        for a, b in ((i, (i + 1) % n),
                     (n + i, n + (i + 1) % n),
                     (i, n + i)):
            adjacency[a] |= 1 << b
            adjacency[b] |= 1 << a
    return adjacency


def is_forest(retained, adjacency):
    """Reject a cycle by union-find on every remaining edge."""
    p = list(range(len(adjacency)))
    def root(i):
        while p[i] != i:
            i = p[i]
        return i
    for u in range(len(adjacency)):
        if not (retained >> u) & 1:
            continue
        nbr = adjacency[u] & retained & ~((1 << (u + 1)) - 1)
        while nbr:
            low = nbr & -nbr
            nbr ^= low
            v = low.bit_length() - 1
            a, b = root(u), root(v)
            if a == b:
                return False
            p[a] = b
    return True


def count_squares(neighbors):
    # Opposite pairs in four-cycles are two-element subsets of a neighborhood.
    pairs = Counter()
    for adj in neighbors:
        for u, v in combinations(sorted(adj), 2):
            pairs[u, v] += 1
    twice = sum(x * (x - 1) // 2 for x in pairs.values())
    assert twice % 2 == 0
    return twice // 2


def check(n):
    assert n >= 5 and n % 2 == 1
    k = (n - 1) // 2
    adj = graph(n)
    total_vertices = 2 * n
    full = (1 << total_vertices) - 1
    candidates = []
    for chosen in combinations(range(total_vertices), k + 1):
        mask = sum(1 << v for v in chosen)
        if is_forest(full ^ mask, adj):
            candidates.append(mask)
    index = {s: i for i, s in enumerate(candidates)}
    assert len(index) == len(candidates)
    assert len(candidates) == n * 2 ** k, (n, len(candidates))
    neigh = [set() for _ in candidates]
    for i, s in enumerate(candidates):
        for u in range(total_vertices):
            if not (s >> u) & 1:
                continue
            for v in range(total_vertices):
                if (s >> v) & 1:
                    continue
                j = index.get(s ^ (1 << u) ^ (1 << v))
                if j is not None:
                    neigh[i].add(j)
    assert all(len(x) == k + 1 for x in neigh)
    assert all(i in neigh[j] for j, xs in enumerate(neigh) for i in xs)
    reached = {0}
    queue = deque([0])
    while queue:
        for nxt in neigh[queue.popleft()]:
            if nxt not in reached:
                reached.add(nxt)
                queue.append(nxt)
    assert len(reached) == len(candidates)
    target = n * 2 ** (k - 2) * ((k - 1) * (k - 2) // 2 + 2 * (k - 2))
    got = count_squares(neigh)
    assert got == target, (n, got, target)
    # Check the exact odd-cycle-cover and opposite-layer structural condition.
    for s in candidates:
        occupied = [i for i in range(n) if (s >> i) & 1 or (s >> (i + n)) & 1]
        assert len(occupied) == k + 1
        adjacent_columns = [i for i in occupied if (i + 1) % n in occupied]
        assert len(adjacent_columns) == 1
        i = adjacent_columns[0]
        assert bool((s >> i) & 1) != bool((s >> ((i + 1) % n)) & 1)
    assert all((sum((s >> v) & 1 for v in range(n)) + sum((s >> (n + v)) & 1 for v in range(n))) == k + 1 for s in candidates)
    print(f'RAW_GRAPH_PASS n={n} optimal_sets={len(candidates)} edges={sum(map(len,neigh))//2} squares={got} degree={k+1}')


if __name__ == '__main__':
    for size in (5, 7, 9, 11, 13):
        check(size)
    print('PRISM_DIRECT_EXHAUSTIVE_PASS')
