"""Independent F_2^3 incidence and symmetry certificate for metric-basis exchanges."""
from itertools import combinations
from collections import Counter

P = tuple(range(1, 8))   # nonzero vectors in F_2^3
L = tuple(range(1, 8))   # nonzero line normals in F_2^3

def on_line(point, normal):
    return ((point & normal).bit_count() % 2) == 0

assert all(sum(on_line(p,l) for p in P) == 3 for l in L)
assert all(sum(on_line(p,l) for l in L) == 3 for p in P)
assert all(sum(on_line(p,l) and on_line(q,l) for l in L) == 1 for p,q in combinations(P,2))

def name(vertex):
    return P[vertex] if vertex < 7 else L[vertex-7]

def graph_distance(u, v):
    if u == v:
        return 0
    if (u < 7) == (v < 7):
        return 2
    p,l = (name(u),name(v)) if u < 7 else (name(v),name(u))
    return 1 if on_line(p,l) else 3

def is_basis(A):
    # Explicit distance signatures; no graph-search machinery is used here.
    return len(set(tuple(graph_distance(u,s) for s in A) for u in range(14))) == 14

assert not any(is_basis(c) for c in combinations(range(14),4))
actual = {frozenset(c) for c in combinations(range(14),5) if is_basis(c)}
assert len(actual) == 168

candidate = set()
for X in combinations(range(7),3):
    vec = [name(x) for x in X]
    if vec[0]^vec[1]^vec[2] == 0: # three collinear points
        continue
    normals = [7+j for j,l in enumerate(L) if sum(on_line(name(p),l) for p in X) == 1]
    assert len(normals) == 3
    for T in combinations(normals,2):
        candidate.add(frozenset(X+T))
for Y in combinations(range(7,14),3):
    vec = [name(y) for y in Y]
    if vec[0]^vec[1]^vec[2] == 0: # three concurrent lines
        continue
    pts = [i for i,p in enumerate(P) if sum(on_line(p,name(y)) for y in Y) == 1]
    assert len(pts) == 3
    for T in combinations(pts,2):
        candidate.add(frozenset(Y+T))
assert actual == candidate

# Algebraic automorphisms: 168 invertible linear maps plus point-line polarity.
def linear(columns,x):
    return (columns[0] if x&1 else 0) ^ (columns[1] if x&2 else 0) ^ (columns[2] if x&4 else 0)
matrices = [v for v in __import__('itertools').product(P,repeat=3)
            if len({linear(v,x) for x in P}) == 7]
assert len(matrices) == 168
maps = []
for cols in matrices:
    point_map = [linear(cols,p) for p in P]
    line_map = []
    for l in L:
        transformed = {linear(cols,p) for p in P if on_line(p,l)}
        options = [n for n in L if {p for p in P if on_line(p,n)} == transformed]
        assert len(options) == 1
        line_map.append(options[0])
    perm = tuple(P.index(v) for v in point_map) + tuple(7+L.index(v) for v in line_map)
    maps.append(perm)
assert len(set(maps)) == 168
polarity = tuple(i+7 if i<7 else i-7 for i in range(14))
full = maps + [tuple(polarity[x] for x in perm) for perm in maps]
assert len(set(full)) == 336
root = next(iter(actual))
images = {frozenset(perm[v] for v in root) for perm in full}
assert images == actual

# Independent exchange construction: collect all pairs with overlap four.
B = sorted(actual,key=lambda x:tuple(sorted(x)))
index = {s:i for i,s in enumerate(B)}
N = len(B)
E = [set() for i in range(N)]
for a,b in combinations(range(N),2):
    if len(B[a]&B[b]) == 4:
        E[a].add(b);E[b].add(a)
assert {len(e) for e in E} == {5}
assert sum(map(len,E))//2 == 420

# A single breadth-first search is complete because the full automorphism
# group acts transitively on the 168 bases.
def shell(src):
    dist={src:0}
    frontier={src}
    while frontier:
        more=set().union(*(E[v] for v in frontier)) - dist.keys()
        for w in more:dist[w]=dist[next(iter(E[w]&frontier))]+1
        frontier=more
    assert len(dist)==N
    return dist
root_i=index[root]
d=shell(root_i)
assert Counter(d.values())=={0:1,1:5,2:18,3:49,4:71,5:24}
# Full pair-distance census in a separate formulation, independent of symmetry.
c=Counter();detours=Counter()
for a in range(N):
    dist=shell(a)
    for b in range(a+1,N):
        c[dist[b]]+=1
        detours[dist[b]-(5-len(B[a]&B[b]))]+=1
assert c=={1:420,2:1512,3:4116,4:5964,5:2016}
assert detours=={0:9660,1:4368}

tri=[]
for a in range(N):
    for b in E[a]:
        if a>=b:continue
        for z in E[a]&E[b]:
            if b<z:tri.append(frozenset((a,b,z)))
assert len(tri)==56
assert Counter(v for t in tri for v in t)=={i:1 for i in range(168)}

print('GF2_FANO_SYMMETRY_PASS')
print('automorphisms=336 orbit=168 triangles=56 diameter=5')
print('distances=',sorted(c.items()),'detours=',sorted(detours.items()))
