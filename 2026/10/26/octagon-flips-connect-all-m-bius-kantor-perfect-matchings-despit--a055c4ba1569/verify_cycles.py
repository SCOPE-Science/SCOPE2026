#!/usr/bin/env python3
"""Independent recursive-matching and explicit simple-cycle flip verification.

Python 3 standard library only. Run with the adjacent certificate.json file.
"""
import collections
import hashlib
import json
from pathlib import Path
import sys

adj = [set() for _ in range(16)]
for i in range(8):
    for a, b in ((i, (i - 1) % 8), (i, 8 + i), (8 + i, 8 + ((i - 3) % 8))):
        adj[a].add(b)
        adj[b].add(a)
for vertex in range(16):
    assert len(adj[vertex]) == 3
edges = sorted({(a, b) if a < b else (b, a)
                for a in range(16) for b in adj[a]})
assert len(edges) == 24
edge_numbers = {e: i for i, e in enumerate(edges)}


def edge_id(a, b):
    return edge_numbers[(min(a, b), max(a, b))]


# Recursive exact-cover enumeration: choose the first vertex not yet matched.
matchings = set()

def extend(remaining, chosen):
    if not remaining:
        matchings.add(tuple(sorted(chosen)))
        return
    u = min(remaining)
    for v in adj[u].intersection(remaining):
        extend(remaining.difference((u, v)), chosen + (edge_id(u, v),))

extend(set(range(16)), ())
matchings = sorted(matchings)
assert len(matchings) == 33
matching_number = {frozenset(m): i for i, m in enumerate(matchings)}


# DFS enumerates every simple cycle of the stated length; sorted edge-ID
# frozensets canonicalize rotations and the two traversal directions.
def simple_cycles(length):
    found = set()
    for start in range(16):
        def walk(path):
            if len(path) == length:
                if start in adj[path[-1]]:
                    e = frozenset(edge_id(path[i], path[(i + 1) % length])
                                  for i in range(length))
                    found.add(e)
                return
            for v in adj[path[-1]]:
                if v > start and v not in path:
                    walk(path + (v,))
        walk((start,))
    return sorted(found, key=lambda c: tuple(sorted(c)))

cycles6 = simple_cycles(6)
cycles8 = simple_cycles(8)
assert len(cycles6) == 24 and len(cycles8) == 30


def switches(cycles):
    pairs = set()
    for i, matching in enumerate(matchings):
        m = frozenset(matching)
        for cycle in cycles:
            occupied = m.intersection(cycle)
            if len(occupied) != len(cycle) // 2:
                continue
            successor = m.symmetric_difference(cycle)
            assert successor in matching_number
            j = matching_number[successor]
            assert i != j
            pairs.add((min(i, j), max(i, j)))
    return sorted(map(list, pairs))

hex_pairs = switches(cycles6)
oct_pairs = switches(cycles8)
assert len(hex_pairs) == 96 and len(oct_pairs) == 36
result = {'graph': 'GP(8,3)', 'vertices': 16, 'edges': [list(e) for e in edges],
          'matchings': [list(m) for m in matchings],
          'hex_pairs': hex_pairs, 'oct_pairs': oct_pairs}
cert = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
assert result == cert
serialized = json.dumps(result, sort_keys=True, ensure_ascii=False,
                        separators=(',', ':')).encode()


def adjacency(pairs):
    out = [set() for _ in matchings]
    for a,b in pairs:
        out[a].add(b)
        out[b].add(a)
    return out


def bfs(adjacencies, source):
    dist = {source: 0}
    frontier = collections.deque([source])
    while frontier:
        u = frontier.popleft()
        for v in adjacencies[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                frontier.append(v)
    return dist

hex_adj = adjacency(hex_pairs)
oct_adj = adjacency(oct_pairs)
all_adj = adjacency(hex_pairs + oct_pairs)
assert collections.Counter(map(len,hex_adj)) == {0:3,6:24,8:6}
assert collections.Counter(map(len,oct_adj)) == {1:24,2:6,12:3}
assert len(bfs(oct_adj, 0)) == 33
assert max(max(bfs(oct_adj, i).values()) for i in range(33)) == 4
assert max(max(bfs(all_adj, i).values()) for i in range(33)) == 3

hubs = [i for i in range(33) if len(oct_adj[i]) == 12]
assert len(hubs) == 3
assert {i for i in range(33) if not hex_adj[i]} == set(hubs)
assert all(sum(len(oct_adj[v]) == 1 for v in oct_adj[h]) == 8 for h in hubs)
assert all(sum(len(oct_adj[v]) == 2 for v in oct_adj[h]) == 4 for h in hubs)
assert collections.Counter(tuple(sorted(oct_adj[i])) for i in range(33) if len(oct_adj[i]) == 2) == {
    (min(hubs[0], hubs[1]),max(hubs[0], hubs[1])): 2,
    (min(hubs[0], hubs[2]),max(hubs[0], hubs[2])): 2,
    (min(hubs[1], hubs[2]),max(hubs[1], hubs[2])): 2}
assert all(len(bfs(oct_adj,i))==33 for i in range(33))
assert collections.Counter(max(bfs(oct_adj,i).values()) for i in range(33)) == {3:3,4:30}
assert all(len(bfs(all_adj,i))==33 and max(bfs(all_adj,i).values())==3 for i in range(33))
print('method=recursive_exact_cover_and_simple_cycle_dfs perfect_matchings=33')
print('simple_cycles_length6=24 simple_cycles_length8=30')
print('flip_edges_length6=96 flip_edges_length8=36')
print('length6_degrees=0:3,6:24,8:6 length8_degrees=1:24,2:6,12:3')
print('length8_structure=3_hubs_8_leaves_each_2_subdivided_parallel_edges_per_pair')
print('length8_radius=3 length8_diameter=4 both_length_radius=3 both_length_diameter=3')
print('certificate_sha256=' + hashlib.sha256(serialized).hexdigest())
