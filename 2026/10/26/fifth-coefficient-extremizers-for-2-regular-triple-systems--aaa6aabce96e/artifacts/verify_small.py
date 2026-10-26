#!/usr/bin/env python3
"""Exact small-case checks for independent 5-sets in 2-regular triple systems."""
from itertools import combinations
from math import comb


def cubic_multigraphs(order):
    pairs = list(combinations(range(order), 2))
    degrees = [0] * order
    multiplicities = [0] * len(pairs)
    output = []

    def visit(i):
        if i == len(pairs):
            if all(degree == 3 for degree in degrees):
                output.append(tuple(multiplicities))
            return
        u, v = pairs[i]
        for multiplicity in range(3):
            if degrees[u] + multiplicity > 3 or degrees[v] + multiplicity > 3:
                continue
            degrees[u] += multiplicity
            degrees[v] += multiplicity
            multiplicities[i] = multiplicity
            visit(i + 1)
            degrees[u] -= multiplicity
            degrees[v] -= multiplicity
            multiplicities[i] = 0

    visit(0)
    return pairs, output


def hypergraph_from_dual(order, pairs, multiplicities):
    dual_edges = []
    for pair, multiplicity in zip(pairs, multiplicities):
        dual_edges.extend([pair] * multiplicity)
    incident = [[] for _ in range(order)]
    for edge_id, (u, v) in enumerate(dual_edges):
        incident[u].append(edge_id)
        incident[v].append(edge_id)
    hyperedges = tuple(frozenset(edge_ids) for edge_ids in incident)
    assert all(len(edge) == 3 for edge in hyperedges)
    assert len(set(hyperedges)) == order
    return hyperedges, len(dual_edges)


def independent_five_count(hyperedges, n):
    total = 0
    for subset in combinations(range(n), 5):
        chosen = set(subset)
        if all(not edge.issubset(chosen) for edge in hyperedges):
            total += 1
    return total


def double_pair_count(hyperedges):
    return sum(
        len(hyperedges[i] & hyperedges[j]) == 2
        for i in range(len(hyperedges))
        for j in range(i + 1, len(hyperedges))
    )


def triple_union_five_count(hyperedges):
    return sum(
        len(hyperedges[i] | hyperedges[j] | hyperedges[k]) == 5
        for i, j, k in combinations(range(len(hyperedges)), 3)
    )


def alternating_cycle_hypergraph(k):
    """Dual cycle C_(2k) with alternating edge multiplicities 2 and 1."""
    order = 2 * k
    dual_edges = []
    for j in range(k):
        dual_edges.extend([(2 * j, 2 * j + 1), (2 * j, 2 * j + 1)])
    for j in range(k):
        dual_edges.append((2 * j + 1, (2 * (j + 1)) % order))
    incident = [[] for _ in range(order)]
    for edge_id, (u, v) in enumerate(dual_edges):
        incident[u].append(edge_id)
        incident[v].append(edge_id)
    hyperedges = tuple(frozenset(edge_ids) for edge_ids in incident)
    assert all(len(edge) == 3 for edge in hyperedges)
    assert len(set(hyperedges)) == order
    return hyperedges, len(dual_edges)


def theorem_bound(n):
    return comb(n, 5) - n * (n - 3) * (n - 5) // 3


def main():
    pairs, duals = cubic_multigraphs(6)
    assert len(duals) == 640
    maximum = -1
    equality_cases = 0
    for multiplicities in duals:
        hyperedges, n = hypergraph_from_dual(6, pairs, multiplicities)
        assert n == 9
        m = len(hyperedges)
        assert 3 * m == 2 * n
        actual = independent_five_count(hyperedges, n)
        p2 = double_pair_count(hyperedges)
        t = triple_union_five_count(hyperedges)
        identity = comb(n, 5) - m * comb(n - 3, 2) + n + (n - 6) * p2 - t
        bound = theorem_bound(n)
        assert actual == identity
        assert actual <= bound
        assert (actual == bound) == (p2 == n // 3 and t == 0)
        maximum = max(maximum, actual)
        equality_cases += actual == bound
    assert maximum == 54
    assert equality_cases == 120

    construction_counts = {}
    for k in (3, 4, 5):
        hyperedges, n = alternating_cycle_hypergraph(k)
        actual = independent_five_count(hyperedges, n)
        assert actual == theorem_bound(n)
        assert double_pair_count(hyperedges) == n // 3
        assert triple_union_five_count(hyperedges) == 0
        construction_counts[n] = actual

    print({
        "dual_multigraphs_checked_order_6": len(duals),
        "order_9_maximum_independent_5_sets": maximum,
        "order_9_equality_duals": equality_cases,
        "alternating_cycle_examples": construction_counts,
        "status": "PASS",
    })


if __name__ == "__main__":
    main()
