#!/usr/bin/env python3
"""Exact finite verification of the icosahedral neighborhood homology character.
Uses only Python's standard library; graph and complex are regenerated from edges.
"""
from itertools import combinations
from collections import Counter, defaultdict

EDGES = [
(0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),
(2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),(4,5),
(4,6),(4,10),(4,11),(5,6),(5,11),(7,8),(7,9),(7,10),
(7,11),(8,9),(9,10),(10,11)]
N = 12
edge_set = {tuple(sorted(e)) for e in EDGES}
assert len(edge_set) == 30
neighborhoods = [set() for _ in range(N)]
for u,v in edge_set:
    neighborhoods[u].add(v); neighborhoods[v].add(u)
assert all(len(n) == 5 for n in neighborhoods)
F = {tuple()}
for n in neighborhoods:
    for k in range(1,6):
        F.update(combinations(sorted(n),k))
faces = {k: sorted(f for f in F if len(f) == k + 1) for k in range(-1,5)}
assert [len(faces[k]) for k in range(-1,5)] == [1,12,60,120,60,12]

# All graph automorphisms, generated from images of the positively oriented flag 0,1,5.
# The image must be one of the 120 ordered triangles. The adjacency-based search
# independently checks existence and uniqueness of the extension of each image.
source = (0,1,5)
triangles = [t for t in combinations(range(N),3)
             if all(tuple(sorted(e)) in edge_set for e in combinations(t,2))]
assert len(triangles) == 20

def extend(partial):
    if len(partial) == N:
        return [[partial[i] for i in range(N)]]
    unmapped = [v for v in range(N) if v not in partial]
    u = max(unmapped, key=lambda x: (sum((min(x,v),max(x,v)) in edge_set for v in partial), -x))
    options = [w for w in range(N) if w not in partial.values() and
               all(((min(u,v),max(u,v)) in edge_set) ==
                   ((min(w,partial[v]),max(w,partial[v])) in edge_set)
                   for v in partial)]
    result = []
    for w in options:
        result += extend({**partial,u:w})
    return result

automorphisms = []
for t in triangles:
    for image in __import__('itertools').permutations(t):
        ex = extend(dict(zip(source,image)))
        assert len(ex) == 1, (image,len(ex))
        automorphisms += [tuple(ex[0])]
assert len(set(automorphisms)) == 120

def sign(perm):
    return -1 if sum(perm[i] > perm[j] for i in range(len(perm))
                     for j in range(i+1,len(perm))) % 2 else 1

# Coherent triangulated-sphere orientation is transported by graph automorphisms.
orients = {triangles[0]:1}

def incidence(tri, e):
    pos = next(i for i in range(3) if tri[i] not in e)
    rem = tuple(tri[i] for i in range(3) if i != pos)
    return (-1 if pos % 2 else 1) * (1 if rem == e else -1)
while len(orients) < len(triangles):
    changed = False
    for t in list(orients):
        for s in triangles:
            e = tuple(sorted(set(t)&set(s)))
            if len(e) != 2 or s in orients:continue
            orients[s] = -orients[t]*incidence(t,e)//incidence(s,e)
            changed = True
    assert changed

# Verify the transported triangle orientations form a coherent icosahedral cycle.
for t in triangles:
    for u in triangles:
        if t >= u:continue
        e = tuple(sorted(set(t)&set(u)))
        if len(e)==2:
            assert orients[t]*incidence(t,e) == -orients[u]*incidence(u,e)

def orientation(g):
    t=triangles[0]
    mapped=tuple(g[i] for i in t)
    return orients[t]*orients[tuple(sorted(mapped))]*sign(mapped)

def order(g):
    p=tuple(range(N))
    for k in range(1,121):
        p=tuple(g[i] for i in p)
        if p==tuple(range(N)):return k
    raise AssertionError('order')

def face_trace(g,k):
    ans=0
    for f in faces[k]:
        image=tuple(g[i] for i in f)
        if tuple(sorted(image)) == f:ans += sign(image)
    return ans

def mod2_rank(columns):
    pivot={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p not in pivot:
                pivot[p]=x;break
            x^=pivot[p]
    return len(pivot)

def boundary_rank(k):
    index={f:i for i,f in enumerate(faces[k-1])}
    columns=[]
    for f in faces[k]:
        bit=0
        for j in range(k+1):bit |= 1 << index[f[:j]+f[j+1:]]
        columns.append(bit)
    return mod2_rank(columns)
ranks=[boundary_rank(k) for k in range(1,5)]
assert ranks == [11,49,48,12], ranks
# These are also rational ranks: they attain the upper bounds from chain exactness.
# d1 <= 11, d2 <= 60-11, d3 <= 60-12, d4 <= 12.
expected={
    (1,1,12):(1,23),
    (1,2,0):(15,3),
    (1,3,0):(20,-1),
    (1,5,2):(24,3),
    (-1,2,0):(1,-1),
    (-1,2,4):(15,-5),
    (-1,6,0):(20,-1),
    (-1,10,0):(24,-1),
}
observed=defaultdict(list)
for g in automorphisms:
    g_orientation = orientation(g)
    for t in triangles:
        mapped = tuple(g[i] for i in t)
        assert g_orientation == orients[t]*orients[tuple(sorted(mapped))]*sign(mapped)
    key=(g_orientation,order(g),sum(g[i]==i for i in range(N)))
    signed=[face_trace(g,k) for k in range(5)]
    character=-1 + sum((-1 if k%2 else 1)*signed[k] for k in range(5))
    observed[key].append(character)
assert {key:(len(vals),vals[0]) for key,vals in observed.items()} == expected
assert all(len(set(vals))==1 for vals in observed.values())
assert sum(sum(v) for v in observed.values())==0
assert sum(sum(v) for k,v in observed.items() if k[0]==1)==120
assert sum(sum(x*x for x in v) for v in observed.values())==120*11
print('VERIFY_OK: faces=(12,60,120,60,12), F2 ranks=', ranks)
print('VERIFY_OK: 120 automorphisms and 8 order/orientation types')
for key in sorted(expected):print(key,expected[key])
print('VERIFY_OK: A5-invariant dimension 2, full-icosahedral invariant dimension 0')
