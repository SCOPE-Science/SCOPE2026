"""Independent exact enumeration for recovery times of theta-graph cycle matroids.

Run with Python 3.9+; uses only the Python standard library.  The direct
method tests graph connectivity for every subset not containing the target
edge; it does not use the path-completion formula under test.
"""
from fractions import Fraction
from math import comb


def make_graph(lengths):
    next_vertex = 2
    edges, paths = [], []
    for length in lengths:
        tail, indices = 0, []
        for offset in range(length):
            head = 1 if offset == length - 1 else next_vertex
            if offset != length - 1:
                next_vertex += 1
            indices.append(len(edges))
            edges.append((tail, head))
            tail = head
        paths.append(indices)
    return next_vertex, edges, paths


def endpoint_connected(num_vertices, edges, subset, src, dst):
    adjacency = [[] for _ in range(num_vertices)]
    for i, (u, v) in enumerate(edges):
        if subset & (1 << i):
            adjacency[u].append(v)
            adjacency[v].append(u)
    visited, stack = {src}, [src]
    while stack:
        for v in adjacency[stack.pop()]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return dst in visited


def enumerate_expectations(lengths):
    num_vertices, edges, paths = make_graph(lengths)
    n = len(edges)
    result = []
    for target, (src, dst) in enumerate(edges):
        others = [e for e in range(n) if e != target]
        counts = [0] * n
        for small_mask in range(1 << (n - 1)):
            full_mask = 0
            for i, edge_index in enumerate(others):
                if small_mask & (1 << i):
                    full_mask |= 1 << edge_index
            if endpoint_connected(num_vertices, edges, full_mask, src, dst):
                counts[small_mask.bit_count()] += 1
        result.append(Fraction(n) - sum(
            (Fraction(counts[s], comb(n-1, s)) for s in range(1, n)),
            Fraction(0),
        ))
    return result, paths


def predicted_expectations(lengths):
    n = sum(lengths)
    result = []
    for index, length in enumerate(lengths):
        terms = [Fraction(1)]
        for other, exponent in enumerate(lengths):
            if other == index:
                continue
            enlarged = terms + [Fraction(0)] * exponent
            for k, coeff in enumerate(terms):
                enlarged[k + exponent] -= coeff
            terms = enlarged
        integral = sum((c / (length + k) for k, c in enumerate(terms)),
                       Fraction(0))
        result.append(n * (1 - Fraction(1, length) + integral))
    return result


def verify():
    cases = [
        (2, 2, 2), (2, 3, 2), (2, 3, 4), (3, 3, 3),
        (2, 2, 2, 2), (2, 2, 3, 2), (2, 2, 2, 2, 2),
        (3, 3, 4), (2, 2, 2, 3),
    ]
    tested_subsets = 0
    for lengths in cases:
        direct, paths = enumerate_expectations(lengths)
        expected = predicted_expectations(lengths)
        assert direct == [expected[i] for i, path in enumerate(paths)
                          for _ in path], lengths
        assert sum(direct) == sum(lengths) * (sum(lengths) - len(lengths) + 1)
        for i in range(len(lengths)):
            for j in range(len(lengths)):
                assert (expected[i] < expected[j]) == (lengths[i] < lengths[j])
        tested_subsets += sum(lengths) * (1 << (sum(lengths) - 1))
    print("VERIFY_OK", "families=", len(cases),
          "targeted_subset_tests=", tested_subsets,
          "exact_fraction_comparisons=", "passed")


if __name__ == "__main__":
    verify()
