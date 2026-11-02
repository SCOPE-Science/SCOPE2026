#!/usr/bin/env python3
"""Finite checks for paired forcing-orthoframe enumerations (standard Python)."""
from itertools import combinations
from math import comb


def partitions(n):
    def recur(s):
        if not s:
            yield ()
            return
        x, rest = s[0], s[1:]
        for p in recur(rest):
            yield ((x,),) + p
            for i in range(len(p)):
                q = list(p)
                q[i] = (x,) + q[i]
                yield tuple(q)
    yield from recur(tuple(range(n)))


def graph_components(n, mask):
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i, (u, v) in enumerate(combinations(range(n), 2)):
        if (mask >> i) & 1:
            parent[root(u)] = root(v)
    return len({root(i) for i in range(n)})


def is_equivalence(n, masks):
    for i in range(n):
        if not (masks[i] >> i) & 1:
            return False
        for j in range(n):
            if ((masks[i] >> j) & 1) != ((masks[j] >> i) & 1):
                return False
    for i in range(n):
        for j in range(n):
            if (masks[i] >> j) & 1 and masks[j] & ~masks[i]:
                return False
    return True


def direct_counts(n):
    # Evaluate the defining forcing implication, without the component formula.
    nmask = (1 << n) - 1
    a = b = 0
    for graph in range(1 << comb(n, 2)):
        neigh = [1 << j for j in range(n)]
        for e, (i, j) in enumerate(combinations(range(n), 2)):
            if graph >> e & 1:
                neigh[i] |= 1 << j
                neigh[j] |= 1 << i
        for bits in range(1 << (n * n)):
            rows = tuple((bits >> (i * n)) & nmask for i in range(n))
            if not all(
                (rows[i] & ~rows[j]) == 0
                for i in range(n)
                for j in range(n)
                if neigh[i] >> j & 1
            ):
                continue
            a += 1
            b += is_equivalence(n, rows)
    return a, b


def exact_formula(n):
    # Independently enumerate every undirected compatibility graph.
    rank = [0] * n
    for graph in range(1 << comb(n, 2)):
        r = n - graph_components(n, graph)
        rank[r] += 1
    a = sum(cnt * (1 << (n * (n - r))) for r, cnt in enumerate(rank))
    # Independently enumerate every equivalence partition.
    b = sum(1 << sum(comb(len(block), 2) for block in p)
            for p in partitions(n))
    return a, b, rank


def main():
    expected_a = [2, 20, 736, 95584, 46101248, 87161615360]
    expected_b = [1, 3, 15, 121, 1665, 43883]
    for n in range(1, 7):
        a, b, rank = exact_formula(n)
        assert a == expected_a[n-1] and b == expected_b[n-1], (n, a, b)
        if n >= 3:
            assert rank[2] == 4 * comb(n, 3) + 3 * comb(n, 4)
        if n <= 3:
            assert direct_counts(n) == (a, b), (n, a, b)
    print('ALL_CHECKS_OK (direct forcing n<=3, graph/partition census n<=6)')

if __name__ == '__main__':
    main()
