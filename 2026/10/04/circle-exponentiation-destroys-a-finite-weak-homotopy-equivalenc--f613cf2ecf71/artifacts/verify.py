#!/usr/bin/env python3
from itertools import product, combinations
from collections import defaultdict, deque
import json, os

# Four-point minimal circle C: two minima 0,1 and two maxima 2,3.
C_N = 4
C_COVERS = [(0,2),(0,3),(1,2),(1,3)]

# Nine-point space R from Cianci--Ottina Figure 1.
# Point order: c1,c2,c3,b1,b2,b3,a1,a2,a3 = 0,...,8.
R_N = 9
R_COVERS = [
    (0,3),(1,3),
    (0,4),(1,4),(2,4),
    (1,5),(2,5),
    (3,6),(3,7),
    (4,6),(4,8),
    (5,7),(5,8),
]

def closure(n, covers):
    le = [[False]*n for _ in range(n)]
    for i in range(n): le[i][i] = True
    for a,b in covers: le[a][b] = True
    for k in range(n):
        for i in range(n):
            if le[i][k]:
                for j in range(n):
                    if le[k][j]: le[i][j] = True
    return le

C_LE = closure(C_N, C_COVERS)
R_LE = closure(R_N, R_COVERS)
C_STRICT = [(i,j) for i in range(C_N) for j in range(C_N) if i != j and C_LE[i][j]]

# Exhaust all functions C -> R and keep precisely the monotone ones.
MAPS = []
for f in product(range(R_N), repeat=C_N):
    if all(R_LE[f[i]][f[j]] for i,j in C_STRICT):
        MAPS.append(f)
assert len(MAPS) == 461

# Pointwise order on the function space.
def map_le(f,g):
    return all(R_LE[a][b] for a,b in zip(f,g))

N = len(MAPS)
LE = [[False]*N for _ in range(N)]
for i,f in enumerate(MAPS):
    for j,g in enumerate(MAPS):
        LE[i][j] = map_le(f,g)

# Stong beat deletions; always take lexicographically first currently beat map,
# preferring an up-beat witness if both checks could be made.
active = set(range(N))
beat_log = []

def strict_upper(x, active):
    return [y for y in active if y != x and LE[x][y]]
def strict_lower(x, active):
    return [y for y in active if y != x and LE[y][x]]

def minimum_of(S):
    for m in S:
        if all(LE[m][z] for z in S):
            return m
    return None

def maximum_of(S):
    for m in S:
        if all(LE[z][m] for z in S):
            return m
    return None

while True:
    found = None
    for x in sorted(active):
        U = strict_upper(x, active)
        if U:
            w = minimum_of(U)
            if w is not None:
                found = (x, 'up', w)
                break
        L = strict_lower(x, active)
        if L:
            w = maximum_of(L)
            if w is not None:
                found = (x, 'down', w)
                break
    if found is None:
        break
    x, kind, w = found
    # Replay the defining beat condition immediately before deletion.
    if kind == 'up':
        U = strict_upper(x, active)
        assert U and all(LE[w][z] for z in U)
    else:
        L = strict_lower(x, active)
        assert L and all(LE[z][w] for z in L)
    beat_log.append((x,kind,w))
    active.remove(x)

assert len(beat_log) == 426
assert sum(k == 'up' for _,k,_ in beat_log) == 179
assert sum(k == 'down' for _,k,_ in beat_log) == 247
assert len(active) == 35

# Verify final set has no beat points.
for x in active:
    U = strict_upper(x, active)
    L = strict_lower(x, active)
    assert not (U and minimum_of(U) is not None)
    assert not (L and maximum_of(L) is not None)

CORE = sorted(active)
core_pos = {x:i for i,x in enumerate(CORE)}

# Enumerate all nonempty chains in the 35-point core as simplices.
# A finite chain is exactly a subset whose elements are pairwise comparable.
simplices = set()
for x in CORE:
    simplices.add((x,))
# Build recursively in increasing index order; if every existing vertex <= new or vice versa,
# the subset is a chain. At 35 vertices and this sparse core, direct subset extension is small.
frontier = [(x,) for x in CORE]
while frontier:
    ch = frontier.pop()
    last_index = CORE.index(ch[-1])
    for y in CORE[last_index+1:]:
        if all(LE[z][y] or LE[y][z] for z in ch):
            new = tuple(sorted(ch + (y,)))
            if new not in simplices:
                simplices.add(new)
                frontier.append(new)

fvec = defaultdict(int)
for s in simplices:
    fvec[len(s)-1] += 1
assert [fvec[i] for i in range(max(fvec)+1)] == [35,94,80,24]

# Elementary simplicial collapses. At each step, choose lexicographically first pair
# (sigma,tau) where sigma is a codimension-one face of a unique maximal simplex tau.
def maximal_simplices(K):
    Klist = list(K)
    maximal = []
    sets = [(s,set(s)) for s in Klist]
    for s,S in sets:
        if not any(len(t)>len(s) and S.issubset(T) for t,T in sets):
            maximal.append(s)
    return maximal

K = set(simplices)
collapse_log = []
while True:
    maxs = maximal_simplices(K)
    candidates = []
    for tau in maxs:
        if len(tau) < 2:
            continue
        for i in range(len(tau)):
            sigma = tau[:i] + tau[i+1:]
            if sigma not in K:
                continue
            containing_max = [m for m in maxs if set(sigma).issubset(m)]
            if len(containing_max) == 1 and containing_max[0] == tau:
                candidates.append((sigma,tau))
    if not candidates:
        break
    sigma,tau = min(candidates)
    # Strong replay condition: sigma is a codim-one face and belongs to one maximal simplex.
    maxs = maximal_simplices(K)
    assert len(tau) == len(sigma)+1 and set(sigma).issubset(tau)
    assert [m for m in maxs if set(sigma).issubset(m)] == [tau]
    K.remove(sigma)
    K.remove(tau)
    collapse_log.append((sigma,tau))

assert len(collapse_log) == 90
assert all(len(s) <= 2 for s in K)
verts = sorted(s[0] for s in K if len(s)==1)
edges = sorted(s for s in K if len(s)==2)
assert len(verts) == 25
assert len(edges) == 28

# Connected residual graph and its rank.
adj = {v:set() for v in verts}
for a,b in edges:
    adj[a].add(b); adj[b].add(a)
seen = set()
q = deque([verts[0]])
while q:
    v=q.popleft()
    if v in seen: continue
    seen.add(v)
    q.extend(adj[v]-seen)
assert seen == set(verts)
rank = len(edges) - len(verts) + 1
assert rank == 4


# Cross-check the packaged certificate against the recomputed proof objects.
cert_path = os.path.join(os.path.dirname(__file__), 'certificate.json')
with open(cert_path, 'r', encoding='utf-8') as fh:
    cert = json.load(fh)
assert cert['map_count'] == len(MAPS)
assert cert['beat_deletions'] == [
    {'map_index':x,'kind':k,'witness_index':w} for x,k,w in beat_log
]
assert cert['core_indices'] == CORE
assert cert['core_maps'] == [list(MAPS[i]) for i in CORE]
assert cert['simplex_f_vector'] == [35,94,80,24]
assert cert['simplicial_collapses'] == [
    {'free_face':list(s),'maximal_simplex':list(t)} for s,t in collapse_log
]
assert cert['residual_graph_vertices'] == verts
assert cert['residual_graph_edges'] == [list(s) for s in edges]
assert cert['residual_graph_cycle_rank'] == rank

# The map R -> point is a weak equivalence because K(R) is contractible (source theorem).
# The calculation above proves K(Map(C,R)) has homotopy type wedge^4 S^1, so H1 has rank 4.
print('VERIFY_OK maps=461 deletions=426 up=179 down=247 core=35 simplices=35,94,80,24 collapses=90 graph=25,28 rank=4')
