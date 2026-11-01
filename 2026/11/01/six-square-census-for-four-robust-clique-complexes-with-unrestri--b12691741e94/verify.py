#!/usr/bin/env python3
"""Exact finite certificate for four-robust clique complexes of square sequences.

Requires NetworkX 3.x for graph representation and exact isomorphism tests.
The simplicial and discrete-Morse checks use integer bit masks and integers.
"""
import collections
import csv
import io
import itertools
import pathlib
import sys
import warnings

import networkx as nx

warnings.filterwarnings('ignore', category=UserWarning, module='networkx')
MAX_SQUARES = 6
EXPECTED_LEVEL_COUNTS = (1, 2, 7, 29, 179, 1410)
EXPECTED_VERTEX_COUNTS = (
    {4: 1},
    {5: 1, 6: 1},
    {6: 2, 7: 2, 8: 3},
    {7: 3, 8: 8, 9: 10, 10: 8},
    {8: 9, 9: 26, 10: 59, 11: 53, 12: 32},
    {9: 26, 10: 129, 11: 315, 12: 452, 13: 347, 14: 141},
)
EXPECTED_CRITICAL_TYPES = (
    {(0,): 1},
    {(0,): 2},
    {(0,): 4, (0, 5): 3},
    {(0,): 7, (0, 5): 22},
    {(0,): 10, (0, 5): 169},
    {(0,): 14, (0, 5): 1396},
)
EXPECTED_FACE_TOTALS = (15, 94, 1032, 10617, 136973, 1968168)


def children(g):
    """All legal edge and two-edge-path gluings of a new 4-cycle."""
    a = g.number_of_nodes()
    for u, w in list(g.edges()):
        h = g.copy()
        h.add_edges_from(((u, a), (a, a+1), (a+1, w)))
        yield h
    for center in list(g.nodes()):
        for u, w in itertools.combinations(list(g.neighbors(center)), 2):
            h = g.copy()
            h.add_edges_from(((u, a), (w, a)))
            yield h


def add_isomorphism_class(g, buckets):
    # The WL hash is used only as an isomorphism-invariant prescreen.
    # Exact GraphMatcher isomorphism is checked within every hash bucket.
    key = nx.weisfeiler_lehman_graph_hash(g)
    if all(not nx.is_isomorphic(g, old) for old in buckets[key]):
        buckets[key].append(g)
        return True
    return False


def enumerate_faces(g):
    n = g.number_of_nodes()
    assert set(g.nodes()) == set(range(n))
    assert nx.is_bipartite(g)
    neighbors = [0] * n
    for u, v in g.edges():
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u
    # A subset of seven vertices in a bipartite graph necessarily
    # contains four vertices from one independent bipartition class.
    forbidden = []
    for four in itertools.combinations(range(n), 4):
        if all(not (neighbors[x] & (1 << y)) for x, y in itertools.combinations(four, 2)):
            forbidden.append(sum(1 << x for x in four))
    faces = []
    f_vector = [0] * 6
    for size in range(1, min(n, 6) + 1):
        for subset in itertools.combinations(range(n), size):
            mask = sum(1 << x for x in subset)
            if size < 4 or all((mask & z) != z for z in forbidden):
                faces.append(mask)
                f_vector[size - 1] += 1
    return faces, f_vector


def discrete_morse_certificate(faces, vertex_count):
    unpaired = set(faces)
    mate = {}
    for vertex in range(vertex_count):
        bit = 1 << vertex
        for lower in faces:
            higher = lower | bit
            if lower in unpaired and not (lower & bit) and higher in unpaired:
                unpaired.remove(lower)
                unpaired.remove(higher)
                mate[lower] = higher
    remaining = collections.Counter(x.bit_count()-1 for x in unpaired)
    # Check the FULL directed Hasse graph, without dropping any incidence.
    in_degree = {x: 0 for x in faces}
    outgoing = collections.defaultdict(list)
    incidence_count = 0
    for higher in faces:
        bits = higher
        while bits:
            bit = bits & -bits
            bits ^= bit
            lower = higher ^ bit
            if not lower:  # Empty simplex is not a Morse cell here.
                continue
            if mate.get(lower) == higher:
                start, end = higher, lower
            else:
                start, end = lower, higher
            outgoing[start].append(end)
            in_degree[end] += 1
            incidence_count += 1
    todo = collections.deque(x for x in faces if in_degree[x] == 0)
    visited = 0
    while todo:
        x = todo.popleft()
        visited += 1
        for y in outgoing[x]:
            in_degree[y] -= 1
            if in_degree[y] == 0:
                todo.append(y)
    assert visited == len(faces), (visited, len(faces), 'cyclic matching')
    assert sum(remaining.values()) + 2*len(mate) == len(faces)
    assert remaining[0] == 1 and set(remaining) <= {0, 5}, remaining
    return remaining[5], len(mate), incidence_count, tuple(sorted(remaining))


def analyze(g, level):
    faces, fv = enumerate_faces(g)
    b, p, incidence_count, crit_type = discrete_morse_certificate(faces, len(g))
    assert -1 + sum((-1)**i * count for i, count in enumerate(fv)) == -b
    assert len(g.edges()) in range(2*level+2, 3*level+2)
    code = nx.to_graph6_bytes(g, header=False).decode('ascii').strip()
    decoded = nx.from_graph6_bytes(code.encode('ascii'))
    assert nx.is_isomorphic(decoded, g)
    return dict(level=level, vertices=len(g), edges=len(g.edges()), graph6=code,
                beta5=b, nonempty_faces=len(faces), matching_pairs=p,
                hasse_incidences=incidence_count, critical_types=crit_type)


def perform():
    g_list = [nx.cycle_graph(4)]
    records = []
    for level in range(1, MAX_SQUARES + 1):
        assert len(g_list) == EXPECTED_LEVEL_COUNTS[level-1]
        assert dict(collections.Counter(len(g) for g in g_list)) == EXPECTED_VERTEX_COUNTS[level-1]
        hist = collections.Counter()
        faces_this_level = 0
        for g in g_list:
            r = analyze(g, level)
            hist[r['critical_types']] += 1
            faces_this_level += r['nonempty_faces']
            del r['critical_types']
            records.append(r)
        assert dict(hist) == EXPECTED_CRITICAL_TYPES[level-1], (level, hist)
        assert faces_this_level == EXPECTED_FACE_TOTALS[level-1]
        print(f'LEVEL_OK {level} graphs={len(g_list)} faces={faces_this_level} '
              f'critical_types={dict(hist)}', flush=True)
        if level < MAX_SQUARES:
            buckets = collections.defaultdict(list)
            for g in g_list:
                for h in children(g):
                    add_isomorphism_class(h, buckets)
            g_list = [g for bucket in buckets.values() for g in bucket]
    return records


def csv_bytes(records):
    fields = ['level','vertices','edges','graph6','beta5','nonempty_faces','matching_pairs','hasse_incidences']
    out = io.StringIO(newline='')
    w = csv.DictWriter(out, fieldnames=fields, lineterminator='\n')
    w.writeheader()
    w.writerows(records)
    return out.getvalue().encode('utf8')


if __name__ == '__main__':
    rows = perform()
    data = csv_bytes(rows)
    filename = pathlib.Path(__file__).with_name('census.csv')
    if '--write-table' in sys.argv:
        filename.write_bytes(data)
        print(f'CENSUS_TABLE_WRITTEN rows={len(rows)} bytes={len(data)}')
    else:
        assert filename.is_file() and filename.read_bytes() == data, 'census table mismatch'
        print(f'ALL_VERIFY_OK classes={len(rows)} table_bytes={len(data)} '
              f'positive_beta={sum(x["beta5"]>0 for x in rows)} '
              f'contractible={sum(x["beta5"]==0 for x in rows)}')
