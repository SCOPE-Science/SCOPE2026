#!/usr/bin/env python3
"""Independent combinatorial check by edge-subset search and explicit alternating cycles.

Uses only the Python standard library. Does not import the other verifier.
"""
import collections
import hashlib
import itertools
import json

# Static adjacency table for a two-pentagon icosahedral graph, vertices 0,...,11.
NEIGHBORS = (
    (1, 2, 3, 4, 5),
    (0, 2, 5, 6, 7),
    (0, 1, 3, 7, 8),
    (0, 2, 4, 8, 9),
    (0, 3, 5, 9, 10),
    (0, 1, 4, 6, 10),
    (1, 5, 7, 10, 11),
    (1, 2, 6, 8, 11),
    (2, 3, 7, 9, 11),
    (3, 4, 8, 10, 11),
    (4, 5, 6, 9, 11),
    (6, 7, 8, 9, 10),
)


def all_cycles(length):
    cycles = set()
    def visit(path):
        if len(path) == length:
            if path[-1] in NEIGHBORS[path[0]] and path[1] < path[-1]:
                cycles.add(tuple(path))
            return
        for nxt in NEIGHBORS[path[-1]]:
            if nxt > path[0] and nxt not in path:
                visit(path + [nxt])
    for smallest in range(12):
        for neighbor in NEIGHBORS[smallest]:
            if neighbor > smallest:
                visit([smallest, neighbor])
    return sorted(cycles)


def digest(lines):
    return hashlib.sha256(('\n'.join(lines) + '\n').encode('ascii')).hexdigest()


def main():
    assert all(len(set(ns)) == 5 for ns in NEIGHBORS)
    assert all(u in NEIGHBORS[v] for u, ns in enumerate(NEIGHBORS) for v in ns)
    edges = sorted((u, v) for u, ns in enumerate(NEIGHBORS) for v in ns if u < v)
    assert len(edges) == 30
    edgeid = {edge: j for j, edge in enumerate(edges)}
    bitedges = [(1 << u) | (1 << v) for u, v in edges]
    # Intentionally scans all choose(30,6)=593775 six-edge subsets rather than recursive pairings.
    matchings = []
    for picks in itertools.combinations(range(len(edges)), 6):
        occupied = 0
        for p in picks:
            uv = bitedges[p]
            if occupied & uv:
                break
            occupied |= uv
        else:
            if occupied == (1 << 12) - 1:
                matchings.append(tuple(edges[p] for p in picks))
    matchings.sort()
    assert len(matchings) == 125
    masks = []
    for matching in matchings:
        masks.append(sum(1 << edgeid[e] for e in matching))
    bymask = {bits: k for k, bits in enumerate(masks)}
    assert len(bymask) == 125
    lists = {4: [set() for _ in masks], 6: [set() for _ in masks]}
    for length in (4, 6):
        for cyc in all_cycles(length):
            path_edges = [tuple(sorted((cyc[i], cyc[(i + 1) % length]))) for i in range(length)]
            a = sum(1 << edgeid[e] for e in path_edges[::2])
            b = sum(1 << edgeid[e] for e in path_edges[1::2])
            toggle = a | b
            for source, bits in enumerate(masks):
                if bits & toggle not in (a, b):
                    continue
                target = bymask.get(bits ^ toggle)
                assert target is not None, 'alternating flip must give perfect matching'
                if source != target:
                    lists[length][source].add(target)
                    lists[length][target].add(source)
    def distances(graph, source):
        cur = {source: 0}
        frontier = [source]
        while frontier:
            subsequent = []
            for u in frontier:
                for v in graph[u]:
                    if v not in cur:
                        cur[v] = cur[u] + 1
                        subsequent.append(v)
            frontier = subsequent
        return cur
    def components(graph):
        unvisited = set(range(len(graph)))
        found = []
        while unvisited:
            block = set(distances(graph, min(unvisited)))
            found.append(block)
            unvisited -= block
        return sorted(found, key=lambda p: (-len(p), min(p)))
    blocks4 = components(lists[4])
    blocks6 = components(lists[6])
    ecc4 = {i: max(distances(lists[4], i).values()) for i in blocks4[0]}
    ecc6 = {i: max(distances(lists[6], i).values()) for i in range(len(masks))}
    frozen = [i for i, nbrs in enumerate(lists[4]) if not nbrs]
    center = [i for i, ecc in ecc6.items() if ecc == min(ecc6.values())]
    flips = {length: sorted((i, j) for i, ns in enumerate(lists[length]) for j in ns if i < j) for length in (4, 6)}
    def m_line(i, m):
        return '%03d %s' % (i, ' '.join('%02d-%02d' % e for e in m))
    lines_m = [m_line(i, m) for i, m in enumerate(matchings)]
    out = {
        'graph_vertices': 12, 'graph_edges': 30, 'perfect_matchings': len(masks),
        'four_flip_edges': len(flips[4]), 'four_component_sizes': [len(p) for p in blocks4],
        'four_giant_radius': min(ecc4.values()), 'four_giant_diameter': max(ecc4.values()),
        'six_flip_edges': len(flips[6]), 'six_component_sizes': [len(p) for p in blocks6],
        'six_radius': min(ecc6.values()), 'six_diameter': max(ecc6.values()),
        'four_frozen_indices': frozen, 'six_center_indices': center,
        'six_eccentricity_histogram': dict(sorted(collections.Counter(ecc6.values()).items())),
        'sha256_matchings_tsv': digest(lines_m),
        'sha256_four_flips_tsv': digest(['%03d %03d' % p for p in flips[4]]),
        'sha256_six_flips_tsv': digest(['%03d %03d' % p for p in flips[6]]),
    }
    assert out['four_component_sizes'] == [120, 1, 1, 1, 1, 1]
    assert out['six_component_sizes'] == [125]
    assert out['four_flip_edges'] == 300 and out['six_flip_edges'] == 580
    assert out['four_giant_radius'] == 5 and out['four_giant_diameter'] == 6
    assert out['six_radius'] == 3 and out['six_diameter'] == 4
    assert len(frozen) == 5 and frozen == center
    print(json.dumps(out, sort_keys=True, separators=(',', ':')))
    print('ICOSAHEDRON_CYCLES_PASS')


if __name__ == '__main__':
    main()
