#!/usr/bin/env python3
"""Exhaustive bipartite-permutation verification of Möbius--Kantor matching flips.

Python 3 standard library only. Run with the adjacent certificate.json file.
"""
import collections
import hashlib
import itertools
import json
from pathlib import Path
import sys

N = 8
V = tuple(range(2 * N))
EDGES = sorted({tuple(sorted((i, (i + 1) % N))) for i in range(N)} |
               {tuple(sorted((N + i, N + (i + 3) % N))) for i in range(N)} |
               {(i, N + i) for i in range(N)})
EDGE_ID = {e: a for a, e in enumerate(EDGES)}
L = tuple(x for x in V if (x < 8 and x % 2 == 0) or (x >= 8 and x % 2 == 1))
R = tuple(x for x in V if x not in L)
assert len(EDGES) == 24 and len(L) == len(R) == 8


def is_single_cycle(edge_ids):
    adjacency = collections.defaultdict(set)
    for edge_id in edge_ids:
        a, b = EDGES[edge_id]
        adjacency[a].add(b)
        adjacency[b].add(a)
    if any(len(z) != 2 for z in adjacency.values()):
        return False
    seen = {next(iter(adjacency))}
    frontier = list(seen)
    while frontier:
        node = frontier.pop()
        for other in adjacency[node]:
            if other not in seen:
                seen.add(other)
                frontier.append(other)
    return len(seen) == len(adjacency)


def distances(neighbors, source):
    d = {source: 0}
    queue = collections.deque([source])
    while queue:
        a = queue.popleft()
        for b in neighbors[a]:
            if b not in d:
                d[b] = d[a] + 1
                queue.append(b)
    return d


def component_sizes(neighbors):
    unseen = set(range(len(neighbors)))
    sizes = []
    while unseen:
        s = next(iter(unseen))
        comp = set(distances(neighbors, s))
        sizes.append(len(comp))
        unseen.difference_update(comp)
    return sorted(sizes)


def graph_for(pairs, count):
    neighbors = [set() for _ in range(count)]
    for a, b in pairs:
        neighbors[a].add(b)
        neighbors[b].add(a)
    return neighbors


def main(path, create=False):
    matchings = set()
    for image in itertools.permutations(R):
        chosen = []
        for a, b in zip(L, image):
            e = tuple(sorted((a, b)))
            if e not in EDGE_ID:
                break
            chosen.append(EDGE_ID[e])
        else:
            matchings.add(tuple(sorted(chosen)))
    matchings = sorted(matchings)
    assert len(matchings) == 33
    hex_pairs, oct_pairs = [], []
    for i, j in itertools.combinations(range(len(matchings)), 2):
        difference = set(matchings[i]) ^ set(matchings[j])
        if len(difference) in (6, 8) and is_single_cycle(difference):
            (hex_pairs if len(difference) == 6 else oct_pairs).append([i, j])
    assert len(hex_pairs) == 96 and len(oct_pairs) == 36
    expected = {
        'graph': 'GP(8,3)', 'vertices': 16, 'edges': [list(z) for z in EDGES],
        'matchings': [list(z) for z in matchings],
        'hex_pairs': hex_pairs, 'oct_pairs': oct_pairs
    }
    raw = json.dumps(expected, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    digest = hashlib.sha256(raw).hexdigest()
    if create:
        Path(path).write_text(json.dumps(expected, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    else:
        assert json.loads(Path(path).read_text(encoding='utf-8')) == expected
    hex_neigh = graph_for(hex_pairs, 33)
    oct_neigh = graph_for(oct_pairs, 33)
    all_neigh = graph_for(hex_pairs + oct_pairs, 33)
    assert component_sizes(hex_neigh) == [1, 1, 1, 30]
    assert component_sizes(oct_neigh) == [33]
    assert component_sizes(all_neigh) == [33]
    assert collections.Counter(map(len, hex_neigh)) == {0: 3, 6: 24, 8: 6}
    assert collections.Counter(map(len, oct_neigh)) == {1: 24, 2: 6, 12: 3}
    assert collections.Counter(map(len, all_neigh)) == {7: 24, 10: 6, 12: 3}
    frozen = [i for i, adj in enumerate(hex_neigh) if not adj]
    hubs = [i for i, adj in enumerate(oct_neigh) if len(adj) == 12]
    assert sorted(frozen) == sorted(hubs)
    spoke_ids = {EDGE_ID[(i, i+8)] for i in range(N)}
    assert collections.Counter(len(set(m) & spoke_ids) for m in matchings) == {0:4,2:16,4:12,8:1}
    assert collections.Counter(len(set(matchings[i]) & spoke_ids) for i in frozen) == {0:2,8:1}
    assert all(len(oct_neigh[i]) == 12 or len(oct_neigh[j]) == 12 for i, j in oct_pairs)
    assert all(collections.Counter(len(oct_neigh[k]) for k in oct_neigh[h]) == {1:8,2:4}
               for h in hubs)
    bridge_pairs = collections.Counter(tuple(sorted(oct_neigh[i])) for i in range(33)
                                       if len(oct_neigh[i]) == 2)
    assert bridge_pairs == {tuple(sorted(pair)):2 for pair in itertools.combinations(hubs,2)}
    oct_ecc = [max(distances(oct_neigh, i).values()) for i in range(33)]
    all_ecc = [max(distances(all_neigh, i).values()) for i in range(33)]
    assert collections.Counter(oct_ecc) == {3:3,4:30}
    assert set(all_ecc) == {3}
    assert set(frozen) == set(i for i, e in enumerate(oct_ecc) if e == 3)
    mobile = [i for i in range(33) if i not in frozen]
    ecc_hex = {i: max(distances(hex_neigh, i).values()) for i in mobile}
    assert set(ecc_hex.values()) <= {3, 4} and min(ecc_hex.values()) == 3 and max(ecc_hex.values()) == 4
    print('method=bipartite_permutations all_permutations=40320 perfect_matchings=33')
    print('spokes_histogram=0:4,2:16,4:12,8:1')
    print('hexagon_edges=96 hexagon_components=1,1,1,30 hexagon_degrees=0:3,6:24,8:6')
    print('octagon_edges=36 octagon_components=33 octagon_degrees=1:24,2:6,12:3')
    print('octagon_structure=3_hubs_8_leaves_each_2_subdivided_parallel_edges_per_pair')
    print('octagon_radius=3 octagon_diameter=4 combined_edges=132 combined_radius=3 combined_diameter=3')
    print('combined_degrees=7:24,10:6,12:3 mobile_hexagon_radius=3 mobile_hexagon_diameter=4')
    print('certificate_sha256=' + digest)

if __name__ == '__main__':
    assert len(sys.argv) in (2, 3)
    main(sys.argv[1], create=len(sys.argv) == 3 and sys.argv[2] == '--create')
