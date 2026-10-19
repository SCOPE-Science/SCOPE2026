"""Recompute edge-metric bases and their exchange graph for the Tutte eight-cage.
Uses only Python's standard library. Vertex order: 15 duads, then 15 synthemes.
"""
from collections import Counter, deque
from itertools import combinations
duads = list(combinations(range(6), 2))

def perfect_matchings(vertices):
    if not vertices:
        yield ()
    else:
        a = vertices[0]
        for b in vertices[1:]:
            rest = tuple(x for x in vertices if x not in (a, b))
            for tail in perfect_matchings(rest):
                yield tuple(sorted(((a, b),) + tail))

synthemes = sorted(set(perfect_matchings(tuple(range(6)))))
edges = [(i, 15 + j) for i, p in enumerate(duads)
         for j, m in enumerate(synthemes) if p in m]
assert len(duads) == len(synthemes) == 15 and len(edges) == 45
adj = [[] for _ in range(30)]
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)
assert all(len(a) == 3 for a in adj)

# Build the vertex-to-vertex distance table without graph packages.
distance = []
for root in range(30):
    d = [-1] * 30
    d[root] = 0
    q = deque([root])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                q.append(v)
    assert -1 not in d
    distance.append(d)

# One integer bit mask per landmark records precisely the edge pairs it resolves.
pairs = list(combinations(range(45), 2))
resolves = []
for v in range(30):
    dd = [min(distance[v][u], distance[v][w]) for u, w in edges]
    mask = 0
    for k, (a, b) in enumerate(pairs):
        if dd[a] != dd[b]:
            mask |= 1 << k
    resolves.append(mask)
full = (1 << len(pairs)) - 1
bases = []
for k in range(1, 6):
    solutions = []
    for comb in combinations(range(30), k):
        cover = 0
        for v in comb:
            cover |= resolves[v]
        if cover == full:
            solutions.append(comb)
    print(f"size_{k}_bases {len(solutions)}", flush=True)
    if k == 5:
        bases = solutions
assert len(bases) == 4560
basis_to_id = {s: i for i, s in enumerate(bases)}

# The exchange relation is a direct symmetric-difference-two test.
exchange = [[] for _ in bases]
for i, s in enumerate(bases):
    S = set(s)
    for old in s:
        base = S - {old}
        for new in range(30):
            if new not in S:
                other = tuple(sorted(base | {new}))
                j = basis_to_id.get(other)
                if j is not None:
                    exchange[i].append(j)
    exchange[i].sort()
    assert len(exchange[i]) == len(set(exchange[i]))
assert all(i in exchange[j] for i, nbrs in enumerate(exchange) for j in nbrs)
edge_pairs = [(i, j) for i, nbrs in enumerate(exchange) for j in nbrs if i < j]
print('vertex_compositions', dict(sorted(Counter(sum(v < 15 for v in b) for b in bases).items())),flush=True)
print('exchange_edges', len(edge_pairs),flush=True)
print('degrees',dict(sorted(Counter(map(len,exchange)).items())),flush=True)

# All-source BFS proves connectedness, eccentricity and diameter-pair census.
n = len(bases)
ecc = Counter()
far_pairs = []
for source in range(n):
    d = [-1] * n
    d[source] = 0
    queue = [source]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in exchange[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                queue.append(v)
    assert len(queue) == n
    ecc[max(d)] += 1
    for j in range(source + 1, n):
        if d[j] == 7:
            far_pairs.append((source, j))
print('components 1')
print('radius',min(ecc))
print('diameter',max(ecc))
print('eccentricities',dict(sorted(ecc.items())))
print('distance_7_unordered_pairs',len(far_pairs))

# Generate exact finite witnesses using a stable lexicographic basis order.
with open('basis_states.txt', 'w', encoding='ascii', newline='\n') as out:
    for s in bases:
        out.write(','.join(map(str,s)) + '\n')
with open('exchange_edges.txt', 'w', encoding='ascii', newline='\n') as out:
    for i,j in edge_pairs:
        out.write(f'{i},{j}\n')
with open('distance_7_pairs.txt', 'w', encoding='ascii', newline='\n') as out:
    for i,j in far_pairs:
        out.write(f'{i},{j}\n')
