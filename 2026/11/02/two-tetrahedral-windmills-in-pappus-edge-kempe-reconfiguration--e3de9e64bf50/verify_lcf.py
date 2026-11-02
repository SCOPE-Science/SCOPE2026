#!/usr/bin/env python3
"""Exact finite edge-Kempe enumeration for the Pappus graph (stdlib only)."""
import itertools
import collections
import json
import sys
from pathlib import Path

OFFSETS = (5, 7, -7, 7, -7, -5) * 3
N = 18
AUT = (0, 1, 8, 7, 6, 5, 4, 3, 2, 13, 14, 15, 16, 9, 10, 11, 12, 17)


def graph():
    edges = {tuple(sorted((i, (i + 1) % N))) for i in range(N)}
    edges.update(tuple(sorted((i, (i + OFFSETS[i]) % N))) for i in range(N))
    edges = sorted(edges)
    assert len(edges) == 27 and len(set(edges)) == 27
    adj = [[] for _ in range(N)]
    for i, (u, v) in enumerate(edges):
        adj[u].append(i)
        adj[v].append(i)
    assert all(len(a) == 3 for a in adj)
    return edges, adj


def states_by_edge_recursion(edges, inc):
    result = []
    free = [7] * N
    current = [0] * len(edges)
    def dfs(i):
        if i == len(edges):
            result.append(''.join(str(a) for a in current))
            return
        u, v = edges[i]
        for c in range(3):
            bit = 1 << c
            if free[u] & bit and free[v] & bit:
                free[u] ^= bit
                free[v] ^= bit
                current[i] = c
                dfs(i + 1)
                free[u] ^= bit
                free[v] ^= bit
    dfs(0)
    assert len(result) == 120 and len(set(result)) == 120
    return sorted(result)


def switch_neighbors(s, edges, inc):
    result = set()
    cycle_structures = []
    for a, b in itertools.combinations(range(3), 2):
        todo = {i for i, c in enumerate(s) if int(c) in (a, b)}
        part_sizes = []
        while todo:
            root = min(todo)
            stack = [root]
            block = {root}
            todo.remove(root)
            while stack:
                e = stack.pop()
                for v in edges[e]:
                    for f in inc[v]:
                        if f in todo:
                            todo.remove(f)
                            block.add(f)
                            stack.append(f)
            part_sizes.append(len(block))
            new = list(s)
            for f in block:
                new[f] = str(b if int(s[f]) == a else a)
            result.add(''.join(new))
        cycle_structures.append(tuple(sorted(part_sizes)))
    assert len(result) == sum(map(len, cycle_structures))
    return result, tuple(sorted(cycle_structures))


def classify(states, adj):
    todo = set(range(len(states)))
    comps = []
    while todo:
        root = min(todo)
        reachable = {root}
        todo.remove(root)
        queue = collections.deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in reachable:
                    reachable.add(v)
                    todo.remove(v)
                    queue.append(v)
        comps.append(sorted(reachable))
    comps.sort(key=lambda C:C[0])
    assert len(comps) == 2 and all(len(C) == 60 for C in comps)
    reports = []
    for C in comps:
        deg = collections.Counter(len(adj[i]) for i in C)
        spheres = collections.defaultdict(collections.Counter)
        pairs = collections.Counter()
        parity = {}
        for root in C:
            dist = {root: 0}
            q = collections.deque([root])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in dist:
                        dist[v] = dist[u] + 1
                        q.append(v)
            assert len(dist) == 60
            ds = tuple(collections.Counter(dist.values()).get(j, 0) for j in range(5))
            spheres[len(adj[root])][ds] += 1
            assert max(dist.values()) == 4
            for v, d in dist.items():
                if v > root:
                    pairs[d] += 1
            if root not in parity:
                parity = {u: d % 2 for u, d in dist.items()}
                assert all(parity[u] != parity[v] for u in C for v in adj[u])
        report = {
            'vertices': 60,
            'edges': sum(len(adj[x]) for x in C) // 2,
            'degrees': dict(sorted(deg.items())),
            'radius': 4,
            'diameter': 4,
            'bipartite': True,
            'spheres_by_degree': {str(k): {','.join(map(str, profile)): v for profile, v in x.items()} for k, x in spheres.items()},
            'unordered_distance_pairs': dict(sorted(pairs.items())),
        }
        reports.append(report)
    assert reports[0] == reports[1]
    expected = {
        'vertices': 60,
        'edges': 162,
        'degrees': {5: 54, 9: 6},
        'radius': 4,
        'diameter': 4,
        'bipartite': True,
        'spheres_by_degree': {'5': {'1,5,17,25,12': 54}, '9': {'1,9,27,21,2': 6}},
        'unordered_distance_pairs': {1: 162, 2: 540, 3: 738, 4: 330},
    }
    assert reports[0] == expected
    return comps, reports


def test_swap_aut(states, adj, edges, comps):
    idx = {p: i for i, p in enumerate(states)}
    emap = {e: i for i, e in enumerate(edges)}
    image = [0] * len(edges)
    for i, (u, v) in enumerate(edges):
        image[i] = emap[tuple(sorted((AUT[u], AUT[v])))]
    assert sorted(image) == list(range(27))
    def mapped(s):
        q = [None] * 27
        for i, c in enumerate(s):
            q[image[i]] = c
        return idx[''.join(q)]
    phi = [mapped(s) for s in states]
    assert sorted(phi) == list(range(len(states)))
    assert all(set(phi[v] for v in adj[u]) == set(adj[phi[u]]) for u in range(len(states)))
    assert set(phi[u] for u in comps[0]) == set(comps[1])


def quotient_by_palette(states, adjacency):
    palette = tuple(itertools.permutations(range(3)))
    normalized = [min(''.join(str(t[int(c)]) for c in s) for t in palette) for s in states]
    labels = sorted(set(normalized))
    assert len(labels) == 20 and all(normalized.count(c)==6 for c in labels)
    ids = {c:i for i,c in enumerate(labels)}
    quotient = [set() for _ in labels]
    for i, neighbors in enumerate(adjacency):
        a = ids[normalized[i]]
        for j in neighbors:
            b = ids[normalized[j]]
            if a != b:
                quotient[a].add(b)
    assert all(u in quotient[v] for v in range(20) for u in quotient[v])
    unseen = set(range(20))
    components = []
    for root in range(20):
        if root not in unseen:
            continue
        comp = {root};q=[root];unseen.remove(root)
        for v in q:
            for w in quotient[v]:
                if w not in comp:
                    comp.add(w);q.append(w);unseen.remove(w)
        components.append(sorted(comp))
    assert len(components)==2 and all(len(c)==10 for c in components)
    for comp in components:
        high=[u for u in comp if len(quotient[u])==9]
        low=[u for u in comp if len(quotient[u])==3]
        assert len(high)==1 and len(low)==9
        assert set(low)==quotient[high[0]]
        lowset=set(low)
        remaining=set(low);triangles=[]
        while remaining:
            u=min(remaining);tri={u}|(quotient[u]&lowset)
            assert len(tri)==3 and all((tri-{v})==(quotient[v]&lowset) for v in tri)
            remaining-=tri
            triangles.append(sorted(tri))
        assert len(triangles)==3
    return labels, [sorted(q) for q in quotient], components

def main():
    edges, inc = graph()
    states = states_by_edge_recursion(edges, inc)
    idx = {s: i for i, s in enumerate(states)}
    adjacency = []
    profiles = collections.Counter()
    for s in states:
        neigh, kinds = switch_neighbors(s, edges, inc)
        assert neigh <= set(idx)
        adjacency.append(sorted(idx[q] for q in neigh))
        profiles[kinds] += 1
    assert all(i in adjacency[j] for i, neighbors in enumerate(adjacency) for j in neighbors)
    assert profiles == collections.Counter({((6, 6, 6), (18,), (18,)): 108, ((6, 6, 6),) * 3: 12})
    comps, reports = classify(states, adjacency)
    test_swap_aut(states, adjacency, edges, comps)
    quotient_labels, quotient_adjacency, quotient_comps = quotient_by_palette(states, adjacency)
    assert sum(map(len, adjacency)) // 2 == 324
    certificate = {
        'vertex_labels': '0..17',
        'graph_edges_sorted': edges,
        'named_colorings_in_sorted_edge_order': states,
        'kempe_adjacency_indices': adjacency,
        'component_indices': comps,
        'component_report': reports[0],
        'unlabelled_palette_orbit_representatives': quotient_labels,
        'unlabelled_quotient_adjacency': quotient_adjacency,
        'unlabelled_quotient_components': quotient_comps,
        'two_color_cycle_profiles': {str(key): n for key, n in sorted(profiles.items())},
        'exchanging_graph_automorphism': AUT,
    }
    if len(sys.argv) == 3 and sys.argv[1] == '--write':
        Path(sys.argv[2]).write_text(json.dumps(certificate, sort_keys=True, separators=(',', ':')) + '\n', encoding='utf-8')
    elif len(sys.argv) == 3 and sys.argv[1] == '--check':
        assert json.loads(json.dumps(certificate)) == json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
    print('LCF_EXHAUSTIVE_KEMPE_PASS states=120 edges=324 comps=2x60 radius=4 diameter=4 spheres=2 degree_types=5,9 quotient=2xK1_join_3K3')

if __name__ == '__main__':
    main()
