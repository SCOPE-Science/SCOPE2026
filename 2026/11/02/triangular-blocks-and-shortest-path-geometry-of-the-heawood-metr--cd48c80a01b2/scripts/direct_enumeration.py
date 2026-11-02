"""Exact metric-basis exchange census for the Fano incidence graph.

No third-party packages are required. Run with Python 3.10 or newer.
"""
from collections import Counter, deque
from itertools import combinations

N = 14
lines = [{i % 7, (i + 1) % 7, (i + 3) % 7} for i in range(7)]
assert all(len(x) == 3 for x in lines)
assert all(sum(p in L for L in lines) == 3 for p in range(7))
assert all(sum({p,q}.issubset(L) for L in lines) == 1 for p,q in combinations(range(7), 2))
G = [set() for _ in range(N)]
for l, pts in enumerate(lines):
    for p in pts:
        G[p].add(7 + l)
        G[7 + l].add(p)
assert [len(nbr) for nbr in G] == [3] * N

def distances(source):
    out = [-1] * N
    out[source] = 0
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for w in G[v]:
            if out[w] < 0:
                out[w] = out[v] + 1
                queue.append(w)
    assert all(d >= 0 for d in out)
    return out

D = [distances(v) for v in range(N)]

def resolves(landmarks):
    return len({tuple(D[v][p] for p in landmarks) for v in range(N)}) == N

# All four-vertex subsets fail, so monotonicity excludes smaller candidates.
assert sum(resolves(a) for a in combinations(range(N), 4)) == 0
bases = {sum(1 << i for i in A) for A in combinations(range(N), 5) if resolves(A)}
assert len(bases) == 168

# A second, purely incidence-geometric specification of all bases.
formula = set()
for tri in combinations(range(7), 3):
    S = set(tri)
    if S in lines:
        continue
    tangents = [7 + j for j, L in enumerate(lines) if len(S & L) == 1]
    assert len(tangents) == 3
    for two in combinations(tangents, 2):
        formula.add(sum(1 << v for v in tri + two))
for tri in combinations(range(7), 3):
    # Duality: nonconcurrent triples of lines, with two dual tangents.
    T = set(tri)
    if any(all(p in lines[j] for j in tri) for p in range(7)):
        continue
    tangents = [p for p in range(7) if sum(p in lines[j] for j in T) == 1]
    assert len(tangents) == 3
    for two in combinations(tangents, 2):
        formula.add(sum(1 << v for v in two + tuple(7 + j for j in tri)))
assert formula == bases

B = sorted(bases)
lookup = {m:i for i,m in enumerate(B)}
adj = [[] for _ in B]
for i,m in enumerate(B):
    for a in range(N):
        if m & (1 << a):
            for b in range(N):
                if not m & (1 << b):
                    n = m ^ (1 << a) ^ (1 << b)
                    if n in lookup:
                        adj[i].append(lookup[n])
    adj[i] = sorted(set(adj[i]))
assert all(len(v) == 5 for v in adj)
assert all(i in adj[j] for i,ls in enumerate(adj) for j in ls)
assert sum(map(len, adj)) // 2 == 420

# Exact orbit-agnostic all-source BFS.
profiles = Counter()
excess = Counter()
pair_dist = Counter()
ecc = Counter()
for i,src in enumerate(B):
    d = [-1] * len(B)
    d[i] = 0
    todo = deque([i])
    while todo:
        v = todo.popleft()
        for w in adj[v]:
            if d[w] == -1:
                d[w] = d[v] + 1
                todo.append(w)
    assert -1 not in d
    profiles[tuple(Counter(d).get(j, 0) for j in range(6))] += 1
    ecc[max(d)] += 1
    for j in range(i + 1, len(B)):
        pair_dist[d[j]] += 1
        h = (src & ~B[j]).bit_count()
        excess[d[j] - h] += 1
assert profiles == {(1,5,18,49,71,24):168}
assert ecc == {5:168}
assert pair_dist == {1:420, 2:1512, 3:4116, 4:5964, 5:2016}
assert excess == {0:9660, 1:4368}

triangles = []
for i in range(len(B)):
    for j in adj[i]:
        if i < j:
            for k in sorted(set(adj[i]) & set(adj[j])):
                if j < k:
                    triangles.append((i,j,k))
assert len(triangles) == 56
assert Counter(v for abc in triangles for v in abc) == {v:1 for v in range(168)}

# Every external edge joins a 3-point/2-line basis to its dual type.
kind = [(m & 127).bit_count() for m in B]
assert Counter(kind) == {2:84,3:84}
for i, m in enumerate(B):
    assert sum(kind[v] == kind[i] for v in adj[i]) == 2
    assert sum(kind[v] != kind[i] for v in adj[i]) == 3
print('HEAWOOD_DIRECT_ALL_SOURCES_PASS')
print('bases=168 edges=420 triangles=56 diameter=5')
print('shells=(1,5,18,49,71,24) pair_distances=', sorted(pair_dist.items()))
print('excess=', sorted(excess.items()))
