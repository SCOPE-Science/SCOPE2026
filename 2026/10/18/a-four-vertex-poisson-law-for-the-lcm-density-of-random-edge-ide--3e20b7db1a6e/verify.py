"""Exact finite-graph checks for the edge-ideal LCM-density theorem.

Run with Python 3: python verify.py
Uses no nonstandard packages.
"""
from itertools import combinations
from math import comb


def edges_on(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def distinct_lcm_count(n, graph_edges):
    """Count supports of unions of edge subsets, including the empty union."""
    masks = {0}
    for a, b in graph_edges:
        em = (1 << a) | (1 << b)
        masks |= {old | em for old in masks}
    return len(masks)


def has_private_endpoint(n, graph_edges):
    deg = [0] * n
    for a, b in graph_edges:
        deg[a] += 1
        deg[b] += 1
    return all(deg[a] == 1 or deg[b] == 1 for a, b in graph_edges)


def test_graphs_up_to_six():
    totals = {}
    for n in range(1, 7):
        choices = edges_on(n)
        good = 0
        for mask in range(1 << len(choices)):
            es = [choices[i] for i in range(len(choices)) if mask >> i & 1]
            lc = distinct_lcm_count(n, es)
            Boolean = lc == (1 << len(es))
            criterion = has_private_endpoint(n, es)
            assert Boolean == criterion, (n, mask, lc, criterion)
            good += Boolean
            if n <= 5:
                for i, edge in enumerate(choices):
                    if not(mask >> i & 1):
                        extended_count = distinct_lcm_count(n, es + [edge])
                        assert extended_count <= 2 * lc, (n, mask, edge)
        totals[n] = (1 << len(choices), good)
    return totals


def test_disjoint_four_paths():
    for k in range(1, 5):
        es = []
        for i in range(k):
            base = 4 * i
            es += [(base, base + 1), (base + 1, base + 2), (base + 2, base + 3)]
        assert distinct_lcm_count(4 * k, es) == 7 ** k
        assert 2 ** len(es) == 8 ** k


def test_path_counts():
    for n in range(4, 11):
        # Number of unoriented labeled four-vertex paths, with extra edges unrestricted.
        brute = sum(1 for v in __import__('itertools').permutations(range(n), 4) if v[0] < v[3])
        assert brute == 12 * comb(n, 4)


if __name__ == '__main__':
    totals = test_graphs_up_to_six()
    test_disjoint_four_paths()
    test_path_counts()
    print('EXHAUSTIVE_GRAPH_COUNTS', totals)
    print('VERIFY_OK: all simple graphs through 6 vertices, monotonicity through 5, four disjoint path products, labeled path counts')
