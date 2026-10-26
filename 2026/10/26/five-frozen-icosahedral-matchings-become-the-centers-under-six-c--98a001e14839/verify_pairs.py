#!/usr/bin/env python3
"""Exhaustive perfect-matching and symmetric-difference verification on a labeled icosahedron.

Standard-library only. Run with --cert-dir DIR to regenerate optional text certificates.
"""
import collections
import hashlib
import json
import os
import sys
from collections import deque


def edges_of_graph():
    edges = set()
    def put(a, b):
        assert a != b
        edges.add(tuple(sorted((a, b))))
    for i in range(5):
        u, u1 = 1 + i, 1 + ((i + 1) % 5)
        v, v1 = 6 + i, 6 + ((i + 1) % 5)
        for a, b in ((0, u), (11, v), (u, u1), (v, v1), (u, v), (u, v1)):
            put(a, b)
    return sorted(edges)


def all_matchings(edges):
    neighbors = {u: set() for u in range(12)}
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    def rec(free):
        if not free:
            yield ()
            return
        u = min(free)
        for v in sorted(neighbors[u] & free):
            for suffix in rec(free - {u, v}):
                yield tuple(sorted(((u, v) if u < v else (v, u),) + suffix))
    return sorted(set(rec(frozenset(range(12)))))


def is_cycle(delta, length):
    if len(delta) != length:
        return False
    adj = collections.defaultdict(set)
    for u, v in delta:
        adj[u].add(v)
        adj[v].add(u)
    if len(adj) != length or any(len(ns) != 2 for ns in adj.values()):
        return False
    start = min(adj)
    seen = {start}
    stack = [start]
    while stack:
        x = stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen) == length


def distances(graph, start):
    result = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in result:
                result[v] = result[u] + 1
                q.append(v)
    return result


def analyze_graph(graph):
    unseen = set(range(len(graph)))
    parts = []
    while unseen:
        start = min(unseen)
        part = set(distances(graph, start))
        parts.append(part)
        unseen -= part
    parts.sort(key=lambda part: (-len(part), min(part)))
    component_sizes = [len(part) for part in parts]
    main = parts[0]
    ecc = {u: max(distances(graph, u).values()) for u in main}
    return component_sizes, min(ecc.values()), max(ecc.values()), ecc


def digest(lines):
    return hashlib.sha256(('\n'.join(lines) + '\n').encode('ascii')).hexdigest()


def main():
    edges = edges_of_graph()
    assert len(edges) == 30
    deg = collections.Counter(x for e in edges for x in e)
    assert len(deg) == 12 and set(deg.values()) == {5}
    matchings = all_matchings(edges)
    assert len(matchings) == 125
    adj = {4: [set() for _ in matchings], 6: [set() for _ in matchings]}
    pairs = {4: [], 6: []}
    for i, m in enumerate(matchings):
        a = set(m)
        for j in range(i + 1, len(matchings)):
            delta = a.symmetric_difference(matchings[j])
            for length in (4, 6):
                if is_cycle(delta, length):
                    adj[length][i].add(j)
                    adj[length][j].add(i)
                    pairs[length].append((i, j))
    c4, r4, d4, ecc4 = analyze_graph(adj[4])
    c6, r6, d6, ecc6 = analyze_graph(adj[6])
    frozen = {i for i in range(125) if not adj[4][i]}
    center = {i for i in range(125) if ecc6[i] == r6}
    assert sorted(c4) == [1, 1, 1, 1, 1, 120]
    assert c6 == [125]
    assert len(frozen) == 5 and frozen == center
    assert len(pairs[4]) == 300 and len(pairs[6]) == 580
    assert (r4, d4, r6, d6) == (5, 6, 3, 4)
    def m_line(i, m):
        return '%03d %s' % (i, ' '.join('%02d-%02d' % e for e in m))
    lines_m = [m_line(i, m) for i, m in enumerate(matchings)]
    lines_4 = ['%03d %03d' % p for p in pairs[4]]
    lines_6 = ['%03d %03d' % p for p in pairs[6]]
    out = {
        'graph_vertices': 12, 'graph_edges': 30, 'perfect_matchings': 125,
        'four_flip_edges': len(pairs[4]), 'four_component_sizes': c4,
        'four_giant_radius': r4, 'four_giant_diameter': d4,
        'six_flip_edges': len(pairs[6]), 'six_component_sizes': c6,
        'six_radius': r6, 'six_diameter': d6,
        'four_frozen_indices': sorted(frozen),
        'six_center_indices': sorted(center),
        'six_eccentricity_histogram': dict(sorted(collections.Counter(ecc6.values()).items())),
        'sha256_matchings_tsv': digest(lines_m),
        'sha256_four_flips_tsv': digest(lines_4),
        'sha256_six_flips_tsv': digest(lines_6),
    }
    if len(sys.argv) == 3 and sys.argv[1] == '--cert-dir':
        os.makedirs(sys.argv[2], exist_ok=True)
        for name, lines in [('matchings.tsv', lines_m), ('flip4.tsv', lines_4), ('flip6.tsv', lines_6)]:
            with open(os.path.join(sys.argv[2], name), 'w', encoding='ascii', newline='\n') as handle:
                handle.write('\n'.join(lines) + '\n')
    else:
        assert len(sys.argv) == 1, 'Usage: python3 verify_pairs.py [--cert-dir DIR]'
    print(json.dumps(out, sort_keys=True, separators=(',', ':')))
    print('ICOSAHEDRON_PAIRS_PASS')


if __name__ == '__main__':
    main()
