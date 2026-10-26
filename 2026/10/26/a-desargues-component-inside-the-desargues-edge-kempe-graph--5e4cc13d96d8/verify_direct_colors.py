"""Independent edge-by-edge 3-coloring and edge-Kempe switch census for GP(10,3).

No perfect-matching decomposition is used. Run with certificate.json present.
"""
import hashlib
import json
from collections import Counter, deque
from itertools import combinations
from pathlib import Path


def edges_of_graph():
    result = set()
    for i in range(10):
        result.update((tuple(sorted(e)) for e in (
            (i, (i+1)%10), (i, 10+i), (10+i, 10+(i+3)%10))))
    return sorted(result)


def enumerate_colorings(edges):
    at_vertex = [[] for _ in range(20)]
    for eid, (u, v) in enumerate(edges):
        at_vertex[u].append(eid)
        at_vertex[v].append(eid)
    normalized_edges = sorted(at_vertex[0])
    locked = {e: color for color, e in enumerate(normalized_edges)}
    assignment = [-1] * 30
    used = [set() for _ in range(20)]
    solutions = []

    def dfs(left):
        if not left:
            assert all({assignment[e] for e in at_vertex[u]} == {0, 1, 2}
                       for u in range(20))
            solutions.append(tuple(assignment))
            return
        # Most constrained uncolored edge is explored first; no matching data needed.
        choices = []
        for eid in left:
            a, b = edges[eid]
            opts = ({0, 1, 2} - used[a]) - used[b]
            if eid in locked:
                opts &= {locked[eid]}
            choices.append((len(opts), eid, tuple(sorted(opts))))
        _, eid, opts = min(choices)
        a, b = edges[eid]
        next_left = left - {eid}
        for color in opts:
            assignment[eid] = color
            used[a].add(color)
            used[b].add(color)
            dfs(next_left)
            used[a].remove(color)
            used[b].remove(color)
            assignment[eid] = -1

    dfs(set(range(30)))
    assert len(solutions) == 32
    canonical = []
    for assignment in solutions:
        masks = []
        for color in range(3):
            masks.append(sum(1 << j for j, c in enumerate(assignment) if c == color))
        canonical.append(tuple(sorted(masks)))
    assert len(set(canonical)) == 32
    return {key: perm for key, perm in zip(canonical, solutions)}


def switch_targets(assignment, edges):
    incident = [[] for _ in range(20)]
    for eid, (a, b) in enumerate(edges):
        incident[a].append(eid)
        incident[b].append(eid)
    results = set()
    patterns = []
    for x, y in combinations(range(3), 2):
        allowed = {eid for eid, c in enumerate(assignment) if c in (x, y)}
        assert len(allowed) == 20
        cycles = []
        while allowed:
            seed = min(allowed)
            q = deque([seed])
            found = {seed}
            while q:
                e = q.popleft()
                for u in edges[e]:
                    for f in incident[u]:
                        if f in allowed and f not in found:
                            found.add(f)
                            q.append(f)
            cycles.append(found)
            allowed -= found
        patterns.append(tuple(sorted(len(c) for c in cycles)))
        for cycle in cycles:
            swapped = list(assignment)
            for e in cycle:
                swapped[e] = y if assignment[e] == x else x
            masks = tuple(sorted(sum(1 << i for i, c in enumerate(swapped) if c == color)
                                 for color in range(3)))
            results.add(masks)
    return results, tuple(sorted(patterns))


def main():
    cert = json.loads(Path('certificate.json').read_text(encoding='utf8'))
    edges = edges_of_graph()
    assert cert['base_edges'] == [list(x) for x in edges]
    assignments = enumerate_colorings(edges)
    sorted_colors = sorted(assignments)
    assert cert['colorings'] == [list(x) for x in sorted_colors]
    indices = {x: i for i, x in enumerate(sorted_colors)}
    links = set()
    profiles = Counter()
    for key, assignment in assignments.items():
        targets, profile = switch_targets(assignment, edges)
        profiles[profile] += 1
        for target in targets:
            assert target in indices
            a, b = indices[key], indices[target]
            if a != b:
                links.add(tuple(sorted((a, b))))
    assert [list(e) for e in sorted(links)] == cert['kempe_edges']
    assert profiles == Counter({((10, 10), (10, 10), (10, 10)): 20,
                                ((10, 10), (20,), (20,)): 12})
    graph = [set() for _ in range(32)]
    for a, b in links:
        graph[a].add(b)
        graph[b].add(a)
    assert Counter(map(len, graph)) == {3: 20, 1: 12}
    assert [len(x) for x in cert['components']] == [20] + [2] * 6
    for comp in cert['components']:
        for v in comp:
            assert graph[v] <= set(comp)
    iso = {int(k): val for k, val in cert['desargues_isomorphism'].items()}
    assert set(iso) == set(cert['components'][0])
    assert set(iso.values()) == set(range(20))
    images = {tuple(sorted((iso[a], iso[b]))) for a, b in links if a in iso}
    assert images == set(edges)
    # Independently verify the largest component's full distance distribution.
    spectra = set()
    for root in cert['components'][0]:
        dist = {root: 0}
        q = deque([root])
        while q:
            v = q.popleft()
            for w in graph[v]:
                if w not in dist:
                    dist[w] = dist[v]+1
                    q.append(w)
        assert len(dist) == 20
        spectra.add(tuple(Counter(dist.values()).get(j, 0) for j in range(6)))
    assert spectra == {(1, 3, 6, 6, 3, 1)}
    print(json.dumps({
        'graph': 'GP(10,3)', 'independent_coloring_backtracks': 32,
        'kempe_edges': len(links),
        'color_pair_cycle_profiles': {'three_10_10': 20, 'one_10_10': 12},
        'twenty_vertex_component_distance_profile': [1, 3, 6, 6, 3, 1],
        'isomorphic_twenty_vertex_component': True,
        'certificate_sha256': hashlib.sha256(Path('certificate.json').read_bytes()).hexdigest()
    }, sort_keys=True))


if __name__ == '__main__':
    main()
