#!/usr/bin/env python3
"""Independent executable checks of a two-round majority bound on leaf coronas."""
from itertools import combinations

def next_state(bits, vertices, edges):
    neighbors = [set() for _ in range(vertices)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    result = 0
    for v, nbs in enumerate(neighbors):
        votes = sum((bits >> u) & 1 for u in nbs)
        old = (bits >> v) & 1
        new = int(votes * 2 > len(nbs)) if 2 * votes != len(nbs) else old
        result |= new << v
    return result

def corona(base_vertices, base_edges):
    return base_edges + [(j, j + base_vertices) for j in range(base_vertices)]

def entry_time(state, vertices, edges):
    trajectory = [state]
    for _ in range(5):
        trajectory.append(next_state(trajectory[-1], vertices, edges))
    for t in range(4):
        if trajectory[t + 2] == trajectory[t]:
            return t
    return -1

for n in range(2, 9):
    for kind, base_edges in (
        ('path', [(i, i + 1) for i in range(n - 1)]),
        ('cycle', [(i, (i + 1) % n) for i in range(n)] if n >= 3 else []),
    ):
        if kind == 'cycle' and n == 2:
            continue
        edges = corona(n, base_edges)
        counts = [0, 0, 0]
        for z in range(1 << (2 * n)):
            t = entry_time(z, 2 * n, edges)
            assert 0 <= t <= 2, (n, kind, z, t)
            counts[t] += 1
        print(f'{kind} {n}: states={sum(counts)} entry_0_1_2={counts}')

star = [(0, 1), (0, 2), (0, 3)]
z = 33
edges = corona(4, star)
trajectory = [z]
for _ in range(5):
    trajectory.append(next_state(trajectory[-1], 8, edges))
assert trajectory[:5] == [33, 18, 32, 0, 0]
print('degree-3 star witness:', trajectory[:5])

for m in range(1, 13):
    n = 2 * m + 1
    edges = [(i, (i + 1) % n) for i in range(n)]
    z = sum((i % 2) << i for i in range(n))
    trajectory = [z]
    for _ in range(m + 2):
        trajectory.append(next_state(trajectory[-1], n, edges))
    assert trajectory[m] == 0
    assert all(trajectory[k] != trajectory[k + 2] for k in range(m))
print('unwhiskered odd-cycle witnesses: m=1..12, entry time exactly m')
print('VERIFY_OK')
