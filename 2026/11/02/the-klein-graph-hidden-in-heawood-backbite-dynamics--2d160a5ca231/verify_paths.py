"""Exhaustive ordered-path certificate for Heawood backbite/Klein reduction.

Run: python3 verify_paths.py. Pure Python standard library. The graph is defined
by the Fano difference set (0,1,3) modulo seven. The result is finite.
"""
from collections import Counter, deque, defaultdict
from itertools import permutations

N = 14
D = {0, 1, 3}
adj = [set() for _ in range(N)]
for p in range(7):
    for ell in range(7):
        if (p - ell) % 7 in D:
            adj[p].add(7 + ell)
            adj[7 + ell].add(p)
assert len({tuple(sorted(x)) for x in adj}) == 14
assert all(len(x) == 3 for x in adj)

paths = set()
def visit(path, mask):
    if len(path) == N:
        z = tuple(path)
        paths.add(min(z, z[::-1]))
        return
    for nxt in adj[path[-1]]:
        if not mask & (1 << nxt):
            visit(path + [nxt], mask | (1 << nxt))
for start in range(N):
    visit([start], 1 << start)
assert len(paths) == 504, len(paths)
paths = tuple(sorted(paths))
index = {p: i for i, p in enumerate(paths)}
R = [set() for _ in paths]
for i, p in enumerate(paths):
    for orient in (p, p[::-1]):
        # The other endpoint is expressly excluded: only interior vertices
        # may receive the added edge in a genuine backbite move.
        for j in range(2, N - 1):
            if orient[j] not in adj[orient[0]]:
                continue
            q = tuple(orient[:j][::-1]) + tuple(orient[j:])
            assert len(q) == N
            assert all(q[k + 1] in adj[q[k]] for k in range(N - 1))
            R[i].add(index[min(q, q[::-1])])
assert all(i not in R[i] for i in range(len(R)))
assert all(i in R[j] for i, nbrs in enumerate(R) for j in nbrs)
assert Counter(map(len, R)) == {2: 336, 4: 168}
assert sum(map(len, R)) // 2 == 672
assert Counter((paths[i][-1] in adj[paths[i][0]], len(R[i]))
               for i in range(len(R))) == {(True, 2): 336, (False, 4): 168}

# Exact all-root shortest paths; no random sampling.
ecc = Counter()
for root in range(len(R)):
    dist = {root: 0}
    q = deque([root])
    while q:
        u = q.popleft()
        for v in R[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    assert len(dist) == 504
    ecc[max(dist.values())] += 1
assert ecc == {24: 168, 25: 336}, ecc

core = {i for i, nbrs in enumerate(R) if len(nbrs) == 4}
subdiv = {i for i, nbrs in enumerate(R) if len(nbrs) == 2}
assert len(core) == 168 and len(subdiv) == 336
assert all(R[i] <= core for i in subdiv)
assert all(R[i] <= subdiv for i in core)
M = Counter(tuple(sorted(R[i])) for i in subdiv)
assert Counter(M.values()) == {1: 168, 2: 84}
assert len(M) == 252
S = {i: set() for i in core}
Double = {i: set() for i in core}
for (a, b), multiplicity in M.items():
    if multiplicity == 1:
        S[a].add(b); S[b].add(a)
    else:
        Double[a].add(b); Double[b].add(a)
assert all(len(S[i]) == 2 and len(Double[i]) == 1 for i in core)
triangles = set()
for a in core:
    for b in S[a]:
        for c in S[a] & S[b]:
            triangles.add(tuple(sorted((a, b, c))))
assert len(triangles) == 56
triangles = tuple(sorted(triangles))
assert all(sum(i in t for t in triangles) == 1 for i in core)
assert all(set(t) == S[t[0]] | {t[0]} for t in triangles)
which = {i: j for j, t in enumerate(triangles) for i in t}
K = [set() for _ in triangles]
for (a, b), multiplicity in M.items():
    if multiplicity == 2:
        u, v = which[a], which[b]
        assert u != v and v not in K[u]
        K[u].add(v); K[v].add(u)
assert len(K) == 56 and all(len(x) == 3 for x in K)
assert sum(map(len, K)) // 2 == 84

def exact_girth_and_distances(G):
    girth = 10**9
    shells = set()
    for root in range(len(G)):
        dist = {root: 0}; parent = {root: -1}; todo = deque([root])
        local_girth = 10**9
        while todo:
            u = todo.popleft()
            for v in G[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    parent[v] = u; todo.append(v)
                elif parent[u] != v:
                    local_girth = min(local_girth, dist[u] + dist[v] + 1)
        assert len(dist) == len(G)
        girth = min(girth, local_girth)
        c = Counter(dist.values())
        shells.add(tuple(c[k] for k in range(max(c) + 1)))
    return girth, shells
assert exact_girth_and_distances(K) == (7, {(1, 3, 6, 12, 15, 18, 1)})

# Enumerate the full 336-element Fano-incidence graph automorphism group.
linepoints = [{(j + d) % 7 for d in D} for j in range(7)]
lookup = {frozenset(L): j for j, L in enumerate(linepoints)}
collineations = []
for perm in permutations(range(7)):
    lineimg = []
    for j in range(7):
        image = frozenset(perm[x] for x in linepoints[j])
        if image not in lookup:
            break
        lineimg.append(lookup[image])
    if len(lineimg) == 7:
        collineations.append(tuple(perm) + tuple(7 + x for x in lineimg))
assert len(collineations) == 168
swap = tuple(7 + (-i) % 7 for i in range(7)) + tuple((-j) % 7 for j in range(7))
perms = collineations + [tuple(swap[x] for x in p) for p in collineations]
assert len(set(perms)) == 336
assert all(all(g[v] in adj[g[u]] for u in range(N) for v in adj[u]) for g in perms)
transformed = []
for g in perms:
    tmap = [index[min(tuple(g[x] for x in p), tuple(g[x] for x in p[::-1]))]
            for p in paths]
    assert len(set(tmap)) == 504
    transformed.append(tmap)
assert all(all(set(tr[j] for j in R[i]) == R[tr[i]]
               for i in range(len(R))) for tr in transformed)
# Three 168-element orbits of paths; one is the set of core states.
orbits = []
unseen = set(range(len(R)))
while unseen:
    first = min(unseen)
    orb = {tr[first] for tr in transformed}
    assert orb <= unseen
    orbits.append(orb)
    unseen -= orb
assert sorted(map(len, orbits)) == [168, 168, 168]

# The induced Klein candidate has a single orbit of oriented edges under
# actual Heawood graph symmetries. By the Foster census it is F056B.
Tmap = []
for tr in transformed:
    image = []
    for triangle in triangles:
        q = {which[tr[v]] for v in triangle}
        assert len(q) == 1
        image.append(q.pop())
    assert len(set(image)) == 56
    Tmap.append(image)
a, b = next((u, v) for u, nbrs in enumerate(K) for v in nbrs)
arcs = {(tr[a], tr[b]) for tr in Tmap}
assert len(arcs) == 168
assert arcs == {(u, v) for u in range(56) for v in K[u]}
print('PATH_DFS_504_BACKBITE_672_RADIUS24_DIAMETER25_PASS')
print('KLEIN_QUOTIENT_56_84_GIRTH7_DIAMETER6_ARC_TRANSITIVE_PASS')
print('THREE_PATH_SYMMETRY_ORBITS_OF_168_PASS')
