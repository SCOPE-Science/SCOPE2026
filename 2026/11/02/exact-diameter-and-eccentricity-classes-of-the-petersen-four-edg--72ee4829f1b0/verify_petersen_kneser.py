#!/usr/bin/env python3
"""Exhaustive edge-Kempe graph of the Petersen graph, in KG(5,2) coordinates.

Python 3.9+ standard library. Invoking with --certificate writes the finite
orbit-and-distance witness to the specified JSON path. No external data needed.
"""
import collections
import itertools
import json
import sys


def graph():
    vertices = list(itertools.combinations(range(5), 2))
    E = [(i, j) for i in range(10) for j in range(i + 1, 10)
         if not (set(vertices[i]) & set(vertices[j]))]
    assert len(E) == 15
    adj = [set() for _ in E]
    for i, (u, v) in enumerate(E):
        for j, (x, y) in enumerate(E):
            if i != j and (u in (x, y) or v in (x, y)):
                adj[i].add(j)
    return vertices, E, adj


def enumerate_colorings(adj):
    colors = [-1] * 15
    answer = []

    def visit(left):
        if not left:
            answer.append(tuple(colors))
            return
        best = None
        possibilities = None
        for i in range(15):
            if colors[i] != -1:
                continue
            used = {colors[j] for j in adj[i] if colors[j] >= 0}
            available = [c for c in range(4) if c not in used]
            if not available:
                return
            if possibilities is None or len(available) < len(possibilities):
                best, possibilities = i, available
                if len(available) == 1:
                    break
        for c in possibilities:
            colors[best] = c
            visit(left - 1)
        colors[best] = -1

    visit(15)
    assert len(answer) == len(set(answer)) == 49920
    return answer


def make_reconfiguration(states, adj):
    index = {s: k for k, s in enumerate(states)}
    neighbors = []
    for s in states:
        nbr = set()
        for a in range(4):
            for b in range(a + 1, 4):
                visited = set()
                for i in range(15):
                    if s[i] not in (a, b) or i in visited:
                        continue
                    # Components in the line graph restricted to two colors.
                    component = [i]
                    visited.add(i)
                    for j in component:
                        for h in adj[j]:
                            if h not in visited and s[h] in (a, b):
                                visited.add(h)
                                component.append(h)
                    t = list(s)
                    for j in component:
                        t[j] = a + b - t[j]
                    nbr.add(index[tuple(t)])
        nbr.discard(index[s])
        neighbors.append(nbr)
    assert all(i in neighbors[j] for i, n in enumerate(neighbors) for j in n)
    assert sum(map(len, neighbors)) // 2 == 377280
    return neighbors


def generators(vertices, edges, states):
    vertex_index = {v: i for i, v in enumerate(vertices)}
    edge_index = {e: k for k, e in enumerate(edges)}
    maps = []
    for a in range(4):
        def swap(x):
            return a + 1 if x == a else a if x == a + 1 else x
        vm = [vertex_index[tuple(sorted(map(swap, v)))] for v in vertices]
        maps.append([edge_index[tuple(sorted((vm[u], vm[v])))] for u, v in edges])
    return maps


def symmetry_orbits(vertices, edges, states):
    index = {s: i for i, s in enumerate(states)}
    edge_maps = generators(vertices, edges, states)
    seen = set()
    orbits = []
    for i in range(len(states)):
        if i in seen:
            continue
        orbit = [i]
        seen.add(i)
        for r in orbit:
            s = states[r]
            for pm in edge_maps:
                t = [0] * 15
                for k, target in enumerate(pm):
                    t[target] = s[k]
                j = index[tuple(t)]
                if j not in seen:
                    seen.add(j)
                    orbit.append(j)
            for a in range(3):
                t = tuple(a + 1 if c == a else a if c == a + 1 else c for c in s)
                j = index[t]
                if j not in seen:
                    seen.add(j)
                    orbit.append(j)
        orbits.append(orbit)
    assert len(seen) == 49920
    return orbits


def distance_spheres(start, adj):
    dist = [-1] * len(adj)
    dist[start] = 0
    queue = collections.deque([start])
    counts = []
    while queue:
        i = queue.popleft()
        d = dist[i]
        if d == len(counts):
            counts.append(0)
        counts[d] += 1
        for j in adj[i]:
            if dist[j] < 0:
                dist[j] = d + 1
                queue.append(j)
    assert sum(counts) == len(adj)
    return counts, dist


def main():
    vertices, edges, line_neighbors = graph()
    states = enumerate_colorings(line_neighbors)
    adj = make_reconfiguration(states, line_neighbors)
    orbits = symmetry_orbits(vertices, edges, states)
    records = []
    for orbit in orbits:
        r = orbit[0]
        counts, dist = distance_spheres(r, adj)
        far = [states[i] for i, d in enumerate(dist) if d == 8]
        record = {
            'representative': ''.join(str(x) for x in states[r]),
            'orbit_size': len(orbit),
            'degree': len(adj[r]),
            'eccentricity': len(counts) - 1,
            'distance_spheres': counts,
            'distance_eight_targets': [''.join(str(x) for x in s) for s in far]
        }
        records.append(record)
    degrees = collections.Counter()
    eccentricities = collections.Counter()
    eight_pairs = 0
    for x in records:
        degrees[x['degree']] += x['orbit_size']
        eccentricities[x['eccentricity']] += x['orbit_size']
        eight_pairs += x['orbit_size'] * len(x['distance_eight_targets'])
    assert len(records) == 21
    assert dict(degrees) == {15: 44160, 16: 5760}
    assert dict(eccentricities) == {7: 45600, 8: 4320}
    assert eight_pairs == 5760
    assert all(sum(x['distance_spheres']) == 49920 for x in records)
    summary = {
        'base_graph': 'Petersen graph KG(5,2)', 'edges': edges,
        'colors': [0, 1, 2, 3], 'number_colorings': len(states),
        'exchange_edges': sum(map(len, adj)) // 2,
        'symmetry_orbits': len(records),
        'automorphism_times_palette_group_order': 120 * 24,
        'degree_distribution': dict(degrees),
        'eccentricity_distribution': dict(eccentricities),
        'radius': 7, 'diameter': 8,
        'unordered_pairs_at_diameter': eight_pairs // 2,
        'orbit_records': records,
    }
    if len(sys.argv) > 1:
        assert len(sys.argv) == 3 and sys.argv[1] == '--certificate'
        with open(sys.argv[2], 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, sort_keys=True)
            f.write('\n')
    print('KG_VERIFIER_PASS states=49920 edges=377280 orbits=21 '
          'radius=7 diameter=8 distance8_pairs=2880')


if __name__ == '__main__':
    main()
