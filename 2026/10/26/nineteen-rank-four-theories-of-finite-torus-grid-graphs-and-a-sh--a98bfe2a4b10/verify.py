#!/usr/bin/env python3
"""Exact four-quantifier-rank census for unlabelled Cartesian torus-grid graphs.

Uses only Python's standard library.  The two recurrences deliberately use
independent graph encodings and atomic diagrams.  No probabilistic tests occur.
"""
import json
from collections import defaultdict
from itertools import combinations_with_replacement
from pathlib import Path


def graph_matrix(m, n):
    """A[i][j] = 1 iff the corresponding vertices are adjacent."""
    size = m * n
    out = []
    for u in range(size):
        a, b = divmod(u, n)
        row = bytearray(size)
        for v in range(size):
            c, d = divmod(v, n)
            row[v] = int((b == d and (a-c) % m in (1, m-1)) or
                         (a == c and (b-d) % n in (1, n-1)))
        out.append(row)
    return out


def signature_a(m, n):
    """Four-round sentence type via rooted 2-,3-,4-point diagrams.

    The graph is vertex transitive, so the first vertex is fixed to index 0.
    A triple with one remaining move has a 6-bit atomic prefix and a 64-bit
    subset of fourth-vertex adjacency/equality extension patterns.
    """
    adj = graph_matrix(m, n)
    size = len(adj)
    root = adj[0]
    pair_types = set()
    for b in range(size):
        eb = adj[b]
        third_types = set()
        for c in range(size):
            ec = adj[c]
            triple_atom = ((b == 0) | ((c == 0) << 1) |
                           ((b == c) << 2) | (root[b] << 3) |
                           (root[c] << 4) | (eb[c] << 5))
            extension_mask = 0
            for d in range(size):
                x = ((d == 0) | ((d == b) << 1) | ((d == c) << 2) |
                     (root[d] << 3) | (eb[d] << 4) | (ec[d] << 5))
                extension_mask |= 1 << x
            third_types.add((triple_atom, extension_mask))
        pair_types.add(((b == 0), root[b], frozenset(third_types)))
    return frozenset(pair_types)


def graph_edges(m, n):
    """Independent edge-set construction using cyclic step generators."""
    edge = set()
    for i in range(m):
        for j in range(n):
            u = (i, j)
            for v in (((i + 1) % m, j), (i, (j + 1) % n)):
                edge.add(frozenset((u, v)))
    return edge


def signature_b(m, n):
    """Direct ordered quadruple atomic diagrams; independent from A."""
    nodes = [(i, j) for i in range(m) for j in range(n)]
    edges = graph_edges(m, n)
    root = (0, 0)
    pairs = set()
    for b in nodes:
        thirds = set()
        for c in nodes:
            quadruples = set()
            for d in nodes:
                four = (root, b, c, d)
                atom = 0
                bit = 0
                for i in range(4):
                    for j in range(i + 1, 4):
                        if four[i] == four[j]:
                            atom |= 1 << bit
                        bit += 1
                        if four[i] != four[j] and frozenset((four[i], four[j])) in edges:
                            atom |= 1 << bit
                        bit += 1
                quadruples.add(atom)
            thirds.add(frozenset(quadruples))
        pairs.add(frozenset(thirds))
    return frozenset(pairs)


def predicted_class(m, n):
    a, b = sorted((m, n))
    if a == 3:
        return ('3', str(min(b, 8)))
    if a == 4:
        return ('4', str(min(b, 8)))
    if a == 5:
        return ('5', str(min(b, 7)))
    if a == 6:
        return ('6', str(min(b, 8)))
    if a == 7:
        return ('7', 'all')
    return ('8+', 'all')


def partition_for(method):
    groups = defaultdict(list)
    for m, n in combinations_with_replacement(range(3, 12), 2):
        groups[method(m, n)].append((m, n))
    return sorted((tuple(members) for members in groups.values()),
                  key=lambda g: (min(m*n for m, n in g), g))


def main():
    p_a = partition_for(signature_a)
    p_b = partition_for(signature_b)
    assert p_a == p_b, 'Two independent atomic-diagram recurrences disagree'
    assert len(p_a) == 19

    expected = defaultdict(list)
    for m, n in combinations_with_replacement(range(3, 12), 2):
        expected[predicted_class(m, n)].append((m, n))
    expected_groups = sorted((tuple(v) for v in expected.values()),
                             key=lambda g: (min(m*n for m, n in g), g))
    assert p_a == expected_groups

    report = json.loads(Path(__file__).with_name('classification.json').read_text('utf-8'))
    assert len(report['classes']) == 19
    table = [tuple(tuple(pair) for pair in row['canonical_pairs']) for row in report['classes']]
    assert table == p_a
    assert sum(len(t) for t in p_a) == 45
    minima = [min(m*n for m, n in group) for group in p_a]
    assert max(minima) == 64
    assert [g for g in p_a if (8,8) in g] == [p_a[-1]]
    assert set(p_a[-1]) == {(m,n) for m,n in combinations_with_replacement(range(8,12),2)}

    # Supplemental cases beyond the finite logical cut-off (not a substitute
    # for the infinite reduction from the cycle theorem).
    for m,n in ((3,12),(5,16),(7,14),(8,12),(12,12),(16,17)):
        assert signature_a(m,n) == signature_a(min(m,11),min(n,11))
    print('FINITE_CENSUS_OK canonical_pairs=45 classes=19 implementations=2')
    print('CUTOFF_TABLE_OK 3:8 4:8 5:7 6:8 7:7 8+:8+')
    print('SHARP_BOUND_OK largest_least_representative=64 graph=C8_square_C8')
    print('SUPPLEMENTAL_OK instances=6')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
