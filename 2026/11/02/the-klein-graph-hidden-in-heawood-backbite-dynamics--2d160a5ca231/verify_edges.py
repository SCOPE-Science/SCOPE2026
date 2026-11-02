"""Independent edge-complement and rotation certificate, no external modules.

Construct PG(2,2) via nonzero binary vectors and dot-product incidence;
enumerate ALL eight-edge complements among the 21 incidences, rather than
using the vertex-order path DFS of the other checker.
Run: python3 verify_edges.py.
"""
from collections import Counter, deque
from itertools import combinations

N = 14
incidence = [set() for _ in range(N)]
for x in range(1, 8):
    for y in range(1, 8):
        if ((x & y).bit_count() & 1) == 0:
            u, v = x - 1, 7 + y - 1
            incidence[u].add(v)
            incidence[v].add(u)
assert all(len(x) == 3 for x in incidence)
edges = sorted((u, v) for u in range(N) for v in incidence[u] if u < v)
assert len(edges) == 21
edgeid = {e: i for i, e in enumerate(edges)}
def eid(u, v):
    return edgeid[(min(u, v), max(u, v))]
ALL = (1 << 21) - 1

# Each Hamiltonian path complement consists of eight edges. The degree
# condition reduces 203490 possible subsets to candidates that are then
# checked for connectedness without using an ordered Hamiltonian path.
configs = set()
profile_hits = 0
for omitted in combinations(range(21), 8):
    missing_degrees = [0] * N
    missing_mask = 0
    for j in omitted:
        missing_mask |= 1 << j
        u, v = edges[j]
        missing_degrees[u] += 1
        missing_degrees[v] += 1
    if Counter(missing_degrees) != {1: 12, 2: 2}:
        continue
    profile_hits += 1
    path_edges = ALL ^ missing_mask
    path_neigh = [set() for _ in range(N)]
    for i, (u, v) in enumerate(edges):
        if path_edges & (1 << i):
            path_neigh[u].add(v)
            path_neigh[v].add(u)
    endpoints = [v for v in range(N) if len(path_neigh[v]) == 1]
    assert len(endpoints) == 2
    visited = {endpoints[0]}
    stack = [endpoints[0]]
    while stack:
        u = stack.pop()
        for v in path_neigh[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    if len(visited) == 14:
        configs.add(path_edges)
assert len(configs) == 504, (len(configs), profile_hits)
configs = sorted(configs)
index = {m: i for i, m in enumerate(configs)}

# Moves are constructed directly as edge exchanges. For each unused
# endpoint-to-interior edge, delete the last edge on the old path segment
# from that endpoint to the new neighbor.
R = [set() for _ in configs]
for i, mask in enumerate(configs):
    nbrs = [set() for _ in range(N)]
    for j, (u, v) in enumerate(edges):
        if mask & (1 << j):
            nbrs[u].add(v)
            nbrs[v].add(u)
    endpoints = [u for u in range(N) if len(nbrs[u]) == 1]
    assert len(endpoints) == 2
    for u in endpoints:
        other = endpoints[0] if endpoints[1] == u else endpoints[1]
        for v in incidence[u] - nbrs[u] - {other}:
            prev, cur = -1, u
            while cur != v:
                nxt = next(x for x in nbrs[cur] if x != prev)
                prev, cur = cur, nxt
            assert prev >= 0
            z = (mask | (1 << eid(u, v))) ^ (1 << eid(prev, v))
            assert z in index
            R[i].add(index[z])
assert all(i in R[j] for i, row in enumerate(R) for j in row)
assert Counter(map(len, R)) == {2: 336, 4: 168}
assert sum(map(len, R)) // 2 == 672
assert all(not (R[i] & {j for j in range(len(R)) if len(R[j]) == len(R[i])})
           for i in range(len(R)))

# Independently recover the quotiented 56-vertex cubic graph.
core = {i for i in range(len(R)) if len(R[i]) == 4}
sub = {i for i in range(len(R)) if len(R[i]) == 2}
mult = Counter(tuple(sorted(R[i])) for i in sub)
assert Counter(mult.values()) == {1: 168, 2: 84}
plain = {i: set() for i in core}
for (i, j), m in mult.items():
    if m == 1:
        plain[i].add(j); plain[j].add(i)
assert all(len(plain[i]) == 2 for i in core)
tr = set()
for i in core:
    for j in plain[i]:
        for k in plain[i] & plain[j]:
            tr.add(tuple(sorted((i, j, k))))
assert len(tr) == 56
tr = sorted(tr)
which = {i: j for j, triple in enumerate(tr) for i in triple}
assert len(which) == 168
K = [set() for _ in range(56)]
for (i, j), m in mult.items():
    if m == 2:
        a, b = which[i], which[j]
        assert a != b
        K[a].add(b); K[b].add(a)
assert all(len(x) == 3 for x in K)
assert sum(map(len, K)) // 2 == 84

# Both exact girth and all-root distance profiles without a graph library.
def all_roots(G):
    girth = 10**9
    profile = Counter()
    for root in range(len(G)):
        dist = {root: 0}; pred = {root: -1}
        todo = deque([root]); this_girth = 10**9
        while todo:
            u = todo.popleft()
            for v in G[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    pred[v] = u
                    todo.append(v)
                elif pred[u] != v:
                    this_girth = min(this_girth, dist[u] + dist[v] + 1)
        assert len(dist) == len(G)
        girth = min(girth, this_girth)
        profile[tuple(Counter(dist.values())[j] for j in range(max(dist.values()) + 1))] += 1
    return girth, profile
R_girth, R_profiles = all_roots(R)
assert sum(R_profiles.values()) == 504
ecc_count = Counter()
for profile, count in R_profiles.items():
    ecc_count[len(profile) - 1] += count
assert ecc_count == {24: 168, 25: 336}, ecc_count
assert all_roots(K) == (7, {(1, 3, 6, 12, 15, 18, 1): 56})
print('EDGE_COMPLEMENTS_203490_EXHAUSTIVE_504_HAMILTON_PATHS_PASS')
print('INDEPENDENT_BACKBITE_EDGES_672_DEGREE2_336_DEGREE4_168_PASS')
print('QUOTIENT_56_CUBIC_GIRTH7_DIAMETER6_PASS')
