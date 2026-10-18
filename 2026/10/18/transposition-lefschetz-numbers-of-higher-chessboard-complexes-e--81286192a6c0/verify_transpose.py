#!/usr/bin/env python3
"""Independent finite checks for the transpose Lefschetz identity.

All enumeration is exhaustive on the stated finite sets. The general identity
is proved combinatorially in RESULT.md, not inferred from these tests.
"""
import itertools
import math


def signed_fixed_chain_trace(n, cap):
    """Build the reduced oriented simplicial chain trace from actual faces."""
    result = 0
    for mask in range(1 << (n * n)):
        rows = [0] * n
        cols = [0] * n
        selected = []
        admissible = True
        for p in range(n * n):
            if not (mask >> p) & 1:
                continue
            i, j = divmod(p, n)
            rows[i] += 1
            cols[j] += 1
            if rows[i] > cap or cols[j] > cap:
                admissible = False
                break
            selected.append(p)
        if not admissible:
            continue
        mapped = [n * (p % n) + p // n for p in selected]
        if sorted(mapped) != selected:  # A non-fixed simplex cannot enter trace.
            continue
        inversions = sum(x > y for i, x in enumerate(mapped) for y in mapped[i + 1:])
        result += (-1 if len(selected) % 2 == 0 else 1) * (-1 if inversions % 2 else 1)
    return result


def labeled_regular_graph_count(n, degree):
    """Enumerate every labeled undirected simple graph, independently."""
    edges = list(itertools.combinations(range(n), 2))
    total = 0
    for mask in range(1 << len(edges)):
        degrees = [0] * n
        for e, (u, v) in enumerate(edges):
            if mask & (1 << e):
                degrees[u] += 1
                degrees[v] += 1
        if all(x == degree for x in degrees):
            total += 1
    return total


def predicted_trace(n, degree, regular_count):
    return 0 if n * degree % 2 else (-1 if (n * degree // 2) % 2 == 0 else 1) * regular_count


def two_factors_by_cycle_decomposition(limit):
    """Count unordered disjoint cycles of length >=3 by the block of vertex 0."""
    a = [0] * (limit + 1)
    a[0] = 1
    for n in range(1, limit + 1):
        a[n] = sum(math.comb(n - 1, k - 1) * math.factorial(k - 1) // 2 * a[n - k]
                   for k in range(3, n + 1))
    return a


def main():
    print('Full reduced oriented chain trace versus regular-graph prediction:')
    for n in range(2, 5):
        for degree in range(1, n):
            observed = signed_fixed_chain_trace(n, degree)
            graphs = labeled_regular_graph_count(n, degree)
            predicted = predicted_trace(n, degree, graphs)
            assert observed == predicted, (n, degree, observed, predicted)
            print(f'n={n} cap={degree} regular_graphs={graphs} observed={observed} predicted={predicted}')
    print('Independent labeled-graph enumeration versus cycle-component recurrence:')
    seq = two_factors_by_cycle_decomposition(8)
    assert seq[3:9] == [1, 3, 12, 70, 465, 3507]
    for n in (3, 4, 5, 6):
        count = labeled_regular_graph_count(n, 2)
        assert count == seq[n], (n, count, seq[n])
        print(f'n={n} 2-regular_graphs={count} component_recurrence={seq[n]}')
    print(f'two_factor_counts_n3_to_n8={seq[3:9]}')
    print('All finite checks passed.')


if __name__ == '__main__':
    main()
