"""Exact finite checks for projected matching laws of interconnection trees.

No external packages. Run: python verify.py
All checks are finite corroboration, not a proof for all part profiles.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial
import heapq


def falling(a, r):
    p = 1
    for j in range(r):
        p *= a - j
    return p


def all_quotient_trees(k):
    # Standard Prufer decoding, independent of forest-factorization proof.
    for word in product(range(k), repeat=k - 2):
        deg = [1] * k
        for i in word:
            deg[i] += 1
        leaves = [i for i in range(k) if deg[i] == 1]
        heapq.heapify(leaves)
        E = []
        for i in word:
            j = heapq.heappop(leaves)
            E.append(tuple(sorted((i, j))))
            deg[j] -= 1
            deg[i] -= 1
            if deg[i] == 1:
                heapq.heappush(leaves, i)
        E.append(tuple(sorted((heapq.heappop(leaves), heapq.heappop(leaves)))))
        yield frozenset(E), tuple(1 + word.count(i) for i in range(k))


def matchings_of_edges(k):
    edges = list(combinations(range(k), 2))
    for r in range(1, k // 2 + 1):
        for F in combinations(edges, r):
            if len({v for edge in F for v in edge}) == 2 * r:
                yield frozenset(F)


def test_prufer():
    comparisons = 0
    for k in (3, 4, 5):
        trees = tuple(all_quotient_trees(k))
        assert len(trees) == k ** (k - 2)
        edge_tests = tuple(matchings_of_edges(k))
        for ns in product((1, 2, 3), repeat=k):
            M = sum(ns) - k
            if M < k - 2:
                continue
            weighted = []
            for E, degrees in trees:
                ways = 1
                for n, d in zip(ns, degrees):
                    ways *= falling(n, d)
                if ways:
                    weighted.append((E, ways))
            total = sum(w for _, w in weighted)
            assert total == factorial(k - 2) * comb(M, k - 2) * __import__('math').prod(ns)
            for F in edge_tests:
                actual = Fraction(sum(w for E, w in weighted if F <= E), total)
                numerator = __import__('math').prod(ns[i] + ns[j] - 2 for i, j in F)
                expected = Fraction(numerator, falling(M, len(F)))
                assert actual == expected, (ns, F, actual, expected)
                comparisons += 1
    return comparisons


def physical_count(ns, F):
    k = len(ns)
    part_of = [i for i, size in enumerate(ns) for _ in range(size)]
    physical_edges = [
        (u, v)
        for u in range(len(part_of))
        for v in range(u + 1, len(part_of))
        if part_of[u] != part_of[v]
    ]
    total = hits = 0
    for edge_set in combinations(physical_edges, k - 1):
        vertices = [v for edge in edge_set for v in edge]
        if len(set(vertices)) != 2 * (k - 1):
            continue
        parents = list(range(k))
        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x
        qedges = set()
        cycle = False
        for u, v in edge_set:
            i, j = part_of[u], part_of[v]
            a, b = find(i), find(j)
            if a == b:
                cycle = True
                break
            parents[a] = b
            qedges.add(tuple(sorted((i, j))))
        if cycle:
            continue
        total += 1
        if F <= qedges:
            hits += 1
    return total, hits


def test_physical():
    cases = (
        ((2, 2, 1, 1), ((0, 2), (1, 3))),
        ((2, 2, 2, 2), ((0, 1), (2, 3))),
        ((3, 1, 1, 1), ((0, 1), (2, 3))),
        ((2, 2, 1), ((0, 1),)),
        ((1, 1, 2), ((0, 1),)),
        ((2, 2, 2, 1, 1), ((0, 1), (2, 3))),
    )
    for ns, edges in cases:
        F = frozenset(edges)
        M = sum(ns) - len(ns)
        total, hits = physical_count(ns, F)
        assert total == factorial(len(ns)-2) * comb(M, len(ns)-2) * __import__('math').prod(ns)
        assert Fraction(hits, total) == Fraction(
            __import__('math').prod(ns[i] + ns[j] - 2 for i, j in edges),
            falling(M, len(edges)),
        )
    return len(cases)


if __name__ == '__main__':
    n1 = test_prufer()
    n2 = test_physical()
    print(f"PASS: {n1} exact quotient-tree matching events across all part profiles with k=3,4,5 and sizes 1..3")
    print(f"PASS: {n2} independent physical-edge subset enumerations")
