#!/usr/bin/env python3
"""Exhaustive exact finite verification of peak-time epidemic susceptibility on rooted trees.

Run: python3 verify.py
Requires only Python's standard library. Arithmetic is integral/rational throughout.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import product
from math import comb
from heapq import heapify, heappop, heappush
from pathlib import Path
import sys


def labeled_trees(n):
    """Generate every vertex-labeled tree exactly once, via the Prufer correspondence."""
    if n == 1:
        yield ()
        return
    for code in product(range(n), repeat=n - 2):
        degree = [1] * n
        for vertex in code:
            degree[vertex] += 1
        leaves = [v for v in range(n) if degree[v] == 1]
        heapify(leaves)
        edges = []
        for vertex in code:
            leaf = heappop(leaves)
            edges.append((leaf, vertex))
            degree[leaf] -= 1
            degree[vertex] -= 1
            if degree[vertex] == 1:
                heappush(leaves, vertex)
        u, v = leaves
        edges.append((u, v))
        yield tuple(sorted(tuple(sorted(edge)) for edge in edges))


def adjacency(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def rooted_code(adj, root, parent=-1):
    """Canonical recursive code, invariant exactly under root-preserving isomorphism."""
    return '(' + ''.join(sorted(rooted_code(adj, v, root)
                              for v in adj[root] if v != parent)) + ')'


def peak_total(n, root, edges, mask):
    """Cumulative number infected at the FIRST maximum of synchronous incidence."""
    present = [[] for _ in range(n)]
    for j, (u, v) in enumerate(edges):
        if mask & (1 << j):
            present[u].append(v)
            present[v].append(u)
    dist = [-1] * n
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in present[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                queue.append(v)
    counts = [0] * (max(dist) + 1)
    for d in dist:
        if d >= 0:
            counts[d] += 1
    first_peak = counts.index(max(counts))
    return sum(counts[:first_peak + 1])


def exact_profile(n, root, edges):
    m = n - 1
    totals = [0] * (m + 1)
    for mask in range(1 << m):
        totals[mask.bit_count()] += peak_total(n, root, edges, mask)
    means = [Fraction(totals[k], comb(m, k)) for k in range(m + 1)]
    bernstein_differences = tuple(means[k + 1] - means[k] for k in range(m))
    # Expected total = sum_k totals[k] p^k (1-p)^(m-k).
    polynomial = tuple(sum((-1) ** (j - k) * totals[k] * comb(m - k, j - k)
                           for k in range(j + 1)) for j in range(m + 1))
    return tuple(totals), bernstein_differences, polynomial


def verify():
    expected_types = {1: 1, 2: 1, 3: 2, 4: 4, 5: 9, 6: 20, 7: 48}
    all_classes = {}
    for n in range(1, 8):
        classes = {}
        labeled_count = 0
        for edges in labeled_trees(n):
            labeled_count += 1
            adj = adjacency(n, edges)
            for root in range(n):
                key = rooted_code(adj, root)
                if key not in classes:
                    classes[key] = (root, edges)
        assert labeled_count == (1 if n == 1 else n ** (n - 2))
        assert len(classes) == expected_types[n], (n, len(classes))
        classified = {}
        for code, (root, edges) in classes.items():
            profile = exact_profile(n, root, edges)
            classified[code] = profile
        all_classes[n] = classified
        if n <= 6:
            assert all(all(d >= 0 for d in profile[1]) for profile in classified.values())
        print('vertices', n, 'root-isomorphism types', len(classes),
              'nonmonotone near full transmission',
              sum(profile[1][-1] < 0 for profile in classified.values()) if n >= 2 else 0)
    exceptional = {
        '((((()())))())': (1, 0, 2, 0, 0, 5, -5),
        '((()()())()())': (1, 0, 6, 6, -23, 25, -11),
    }
    # Each tuple above is the coefficient list of E[C] in ascending powers of p.
    anomalies = {}
    for code, (totals, differences, coefficients) in all_classes[7].items():
        if any(d < 0 for d in differences):
            anomalies[code] = coefficients
            assert differences[-1] < 0
            assert all(d >= 0 for d in differences[:-1])
        else:
            assert all(d >= 0 for d in differences)
    assert anomalies == exceptional, anomalies
    assert len(anomalies) == 2
    # For f(p)=0, set p=t/(1+t); these coefficient lists have exactly
    # one sign change, so each f has exactly one positive root (Descartes).
    def transform_to_positive_line(coeff):
        return tuple(sum(coeff[k] * comb(4-k, j-k) for k in range(j+1))
                     for j in range(5))
    assert transform_to_positive_line((-4, 0, 0, -25, 30)) == (-4, -16, -24, -41, 1)
    assert transform_to_positive_line((-12, -18, 92, -125, 66)) == (-12, -66, -34, -43, 3)
    # Verify exact endpoint sensitivities and initial sign of change.
    for code, coeff in anomalies.items():
        near_one_slope = sum(k * coeff[k] for k in range(1, 7))
        assert near_one_slope == (-1 if code == '((((()())))())' else -3)
        assert coeff[2] > 0 and coeff[1] == 0
    # A separate complete profile table can be regenerated and independently checked.
    def rational_string(q):
        return str(q.numerator) + '/' + str(q.denominator)
    lines = ['n\trooted_code\tconditional_totals_by_open_edges\tbernstein_differences\tpolynomial_coefficients']
    for size in range(1, 8):
        for code in sorted(all_classes[size]):
            totals, ds, poly = all_classes[size][code]
            lines.append(str(size) + '\t' + code + '\t' +
                         ','.join(map(str, totals)) + '\t' +
                         ','.join(map(rational_string, ds)) + '\t' +
                         ','.join(map(str, poly)))
    certified_bytes = ('\n'.join(lines) + '\n').encode('utf-8')
    certificate = Path(__file__).with_name('rooted_tree_certificate.tsv')
    if len(sys.argv) == 2 and sys.argv[1] == '--regenerate-certificate':
        certificate.write_bytes(certified_bytes)
    assert certificate.read_bytes() == certified_bytes
    print('EXACT_CERTIFICATE_OK', 'rooted_types_checked', sum(expected_types.values()),
          'seven_vertex_exception_types', len(anomalies))

if __name__ == '__main__':
    verify()
