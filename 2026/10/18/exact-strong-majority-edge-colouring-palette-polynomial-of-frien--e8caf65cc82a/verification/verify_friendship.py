#!/usr/bin/env python3
"""Independent exhaustive edge-neighbourhood checks for the friendship-graph formulas."""
from itertools import product
from math import comb


def proposed_count(n, q):
    both = comb(q, 2) * 2**n
    one = q * (2 * (q - 1))**n - q * (q - 1) * 2**n
    zero = (q * (q - 1))**n - q * (2 * (q - 1))**n + both
    return zero * q**n + one * (q - 1)**n + both * (q - 2)**n


def original_graph_edges(n):
    # Hub vertex 0; two peripheral vertices in each triangle.
    return ([(0, 2 * i + 1) for i in range(n)]
            + [(0, 2 * i + 2) for i in range(n)]
            + [(2 * i + 1, 2 * i + 2) for i in range(n)])


def run_exact(n, q):
    edges = original_graph_edges(n)
    nbrs = [tuple(j for j, edge2 in enumerate(edges)
                  if j != i and (set(edge) & set(edge2)))
            for i, edge in enumerate(edges)]
    valid_by_graph = valid_by_structure = 0
    for coloring in product(range(q), repeat=len(edges)):
        by_graph = all(2 * sum(coloring[j] == alpha for j in nearby) <= len(nearby)
                       for nearby in nbrs for alpha in range(q))
        counts = [sum(coloring[i] == alpha for i in range(2*n)) for alpha in range(q)]
        by_structure = (all(coloring[i] != coloring[n+i] for i in range(n))
                        and all(counts[coloring[2*n+i]] < n for i in range(n)))
        if by_graph != by_structure:
            raise AssertionError((n, q, coloring, by_graph, by_structure))
        valid_by_graph += by_graph
        valid_by_structure += by_structure
    assert valid_by_graph == valid_by_structure == proposed_count(n, q)
    return q ** (3*n), valid_by_graph


def main():
    tested = 0
    for q, ns in [(2, [1, 2, 3]), (3, [1, 2, 3, 4]), (4, [1, 2, 3]), (5, [1, 2])]:
        for n in ns:
            assignments, successes = run_exact(n, q)
            tested += assignments
            print(f'q={q} n={n} tested={assignments} valid={successes} expected={proposed_count(n,q)}')
    assert proposed_count(1, 3) == 6
    assert proposed_count(2, 3) == 108
    assert proposed_count(3, 3) == 2472
    assert proposed_count(4, 3) == 57456
    print(f'PASS: {tested} labelled colour assignments examined; all two independent predicates and counts agree')

if __name__ == '__main__':
    main()
