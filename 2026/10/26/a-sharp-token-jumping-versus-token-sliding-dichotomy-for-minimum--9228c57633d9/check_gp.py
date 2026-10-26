"""Exact enumeration of ordinary zero forcing and its reconfiguration on GP(8,3).

Python 3 standard library only. Each loop has an explicit finite search domain.
"""
from collections import Counter, deque
from itertools import combinations
import json

N = 16
FULL = (1 << N) - 1
adj = [0] * N
for i in range(8):
    for a, b in ((i, (i + 1) % 8), (i, i + 8), (i + 8, ((i + 3) % 8) + 8)):
        adj[a] |= 1 << b
        adj[b] |= 1 << a
assert all(x.bit_count() == 3 for x in adj)
assert sum(x.bit_count() for x in adj) == 48


def closure(initial):
    b = initial
    while True:
        enlarged = b
        for v in range(N):
            if b & (1 << v):
                white = adj[v] & ~b
                if white and not (white & (white - 1)):
                    enlarged |= white
        if enlarged == b:
            return b
        b = enlarged

# Exhaust every candidate of size at most 6, not just a sampled family.
by_size = {}
minimum = []
for k in range(7):
    found = []
    for vertices in combinations(range(N), k):
        mask = sum(1 << v for v in vertices)
        if closure(mask) == FULL:
            found.append(mask)
    by_size[k] = len(found)
    if k == 6:
        minimum = found
assert by_size == {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1704}

index = {m: i for i, m in enumerate(minimum)}
assert len(index) == len(minimum)
jump = [set() for _ in minimum]
slide = [set() for _ in minimum]
for i, m in enumerate(minimum):
    for a in range(N):
        if not m & (1 << a):
            continue
        for b in range(N):
            if m & (1 << b):
                continue
            t = m ^ (1 << a) ^ (1 << b)
            j = index.get(t)
            if j is None:
                continue
            jump[i].add(j)
            if adj[a] & (1 << b):
                slide[i].add(j)
assert all(i not in jump[i] for i in range(len(minimum)))
assert all(i in jump[j] for j, row in enumerate(jump) for i in row)
assert all(i in slide[j] for j, row in enumerate(slide) for i in row)

j_edges = sum(len(row) for row in jump) // 2
s_edges = sum(len(row) for row in slide) // 2
assert j_edges == 16560 and s_edges == 0
assert Counter(map(len, jump)) == {16: 240, 17: 96, 18: 336, 19: 192,
                                  20: 288, 21: 192, 22: 240, 24: 120}


def distances(start):
    d = {start: 0}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for w in jump[v]:
            if w not in d:
                d[w] = d[v] + 1
                queue.append(w)
    return d

# Full BFS from all 1704 vertices: connectivity, radius, diameter.
ecc = Counter()
for i in range(len(minimum)):
    d = distances(i)
    assert len(d) == len(minimum)
    ecc[max(d.values())] += 1
assert ecc == {6: 1704}

start = index[sum(1 << i for i in (0, 1, 2, 3, 4, 5))]
end = index[sum(1 << i for i in (6, 7, 8, 9, 10, 13))]
assert distances(start)[end] == 6
example_path = [(0,1,2,3,4,5), (1,2,3,4,5,6), (2,3,4,5,6,7),
                (3,4,5,6,7,9), (4,5,6,7,8,9), (5,6,7,8,9,13),
                (6,7,8,9,10,13)]
assert all(index[sum(1 << x for x in s)] in range(len(minimum)) for s in example_path)
for a, b in zip(example_path, example_path[1:]):
    aa = index[sum(1 << x for x in a)]; bb = index[sum(1 << x for x in b)]
    assert bb in jump[aa]

output = {
    'graph': 'GP(8,3)', 'order': N, 'edges': 24,
    'zero_forcing_counts_through_6': {str(k): by_size[k] for k in range(7)},
    'minimum_sets': len(minimum), 'jump_edges': j_edges,
    'slide_edges': s_edges,
    'jump_degree_distribution': dict(sorted(Counter(map(len, jump)).items())),
    'jump_connected': True, 'jump_eccentricities': dict(sorted(ecc.items())),
    'jump_radius': min(ecc), 'jump_diameter': max(ecc),
    'slide_components': len(minimum), 'slide_isolated': len(minimum),
    'witness_distance': distances(start)[end],
    'witness_path': [list(s) for s in example_path]
}
print(json.dumps(output, sort_keys=True, indent=2))
