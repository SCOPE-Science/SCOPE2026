#!/usr/bin/env python3
from itertools import combinations, permutations, product
from collections import Counter, deque

FACETS = [
    (0,1,2),(0,1,4),(0,2,3),(0,3,5),(0,4,5),
    (1,2,5),(1,3,4),(1,3,5),(2,3,4),(2,4,5),
]
V = tuple(range(6))
FSET = {tuple(sorted(f)) for f in FACETS}
EDGES = sorted({tuple(sorted(e)) for f in FACETS for e in combinations(f,2)})
assert len(EDGES) == 15
INC = {e: [] for e in EDGES}
for i,f in enumerate(FACETS):
    for e in combinations(f,2):
        INC[tuple(sorted(e))].append(i)
assert all(len(INC[e]) == 2 for e in EDGES)


def connected(n, edges):
    if n == 0:
        return True
    adj = [[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b); adj[b].append(a)
    seen = {0}
    q = [0]
    while q:
        u = q.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w); q.append(w)
    return len(seen) == n


def prufer_tree(seq, n=6):
    deg = [1]*n
    for x in seq:
        deg[x] += 1
    seq = list(seq)
    out = []
    for x in seq:
        leaf = min(i for i,d in enumerate(deg) if d == 1)
        out.append(tuple(sorted((leaf,x))))
        deg[leaf] -= 1
        deg[x] -= 1
    leaves = [i for i,d in enumerate(deg) if d == 1]
    assert len(leaves) == 2
    out.append(tuple(sorted(leaves)))
    return frozenset(out)


def dual_edges(primal_edges):
    return [tuple(INC[e]) for e in primal_edges]


def unique_cycle_length(n, edges):
    # For a connected graph with n vertices and n edges, peel leaves.
    assert len(edges) == n
    adj = [set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    deg = [len(x) for x in adj]
    q = deque(i for i,d in enumerate(deg) if d == 1)
    alive = [True]*n
    while q:
        u = q.popleft()
        if not alive[u]:
            continue
        alive[u] = False
        for w in list(adj[u]):
            if alive[w]:
                adj[w].discard(u)
                deg[w] -= 1
                if deg[w] == 1:
                    q.append(w)
    return sum(alive)

# All 6^(6-2)=1296 spanning trees of K6, generated without relying on Cayley's count.
trees = {prufer_tree(seq) for seq in product(V, repeat=4)}
assert len(trees) == 1296
cycle_hist = Counter()
leftover_hist = Counter()
tree_cotree_pairs = 0
for T in trees:
    assert len(T) == 5 and connected(6, T)
    allowed = [e for e in EDGES if e not in T]
    D = dual_edges(allowed)
    assert len(D) == 10 and connected(10, D)
    ell = unique_cycle_length(10, D)
    cycle_hist[ell] += 1

    # Every dual spanning tree is obtained by deleting one allowed edge.
    local = 0
    for e in allowed:
        remain = [x for x in allowed if x != e]
        if connected(10, dual_edges(remain)):
            local += 1
            leftover_hist[e] += 1
    assert local == ell
    tree_cotree_pairs += local

assert cycle_hist == Counter({5:726, 6:540, 9:30})
assert tree_cotree_pairs == 7140
assert set(leftover_hist.values()) == {476}
assert len(leftover_hist) == 15

# Independent symmetry check: the simplicial automorphism group has 60 elements
# and acts transitively on the 15 edges.
autos = []
for p in permutations(V):
    image = {tuple(sorted(p[v] for v in f)) for f in FACETS}
    if image == FSET:
        autos.append(p)
assert len(autos) == 60
edge_orbit = {tuple(sorted((p[0],p[1]))) for p in autos}
assert len(edge_orbit) == 15

# Mod-2 Betti vector from Euler characteristic and closed connected surface data.
# Connectivity follows from K6 as the 1-skeleton; each edge has exactly two incident triangles.
chi = 6 - 15 + 10
assert chi == 1
# Closed connected 2-manifold over F2 has b0=b2=1, hence b1=b0+b2-chi=1.
betti = (1, 1, 1)

root_choices = 6 * 10
perfect_fields = tree_cotree_pairs * root_choices
per_critical_edge = 476 * root_choices
assert perfect_fields == 428400
assert per_critical_edge == 28560

print(
    'VERIFY_OK '
    'facets=10 edges=15 trees=1296 '
    'cycle_hist=5:726,6:540,9:30 '
    'tree_cotree=7140 perfect_fields=428400 '
    'critical_edge_each=28560 aut=60 betti=1,1,1'
)
