#!/usr/bin/env python3
"""Exact verification of a twelve-vertex Euclidean clique filtration.

Run from the directory containing CERTIFICATES.json. Only Python standard-library
integer arithmetic and finite set operations are required.
"""
import json
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product
from pathlib import Path

cert = json.loads(Path(__file__).with_name('CERTIFICATES.json').read_text(encoding='utf-8'))
V = sorted({tuple(p[i] * s[i] for i in range(3))
            for p in set(permutations((3, 1, 1)))
            for s in product((-1, 1), repeat=3) if s[0] * s[1] * s[2] == 1})
assert len(V) == 12 and [list(v) for v in V] == cert['vertices']
P = {v: i for i, v in enumerate(V)}
D = {(i, j): sum((a-b)**2 for a, b in zip(V[i], V[j]))
     for i, j in combinations(range(12), 2)}
assert Counter(D.values()) == {8: 18, 24: 24, 32: 12, 40: 12}


def faces(q):
    return {frozenset(i for i in range(12) if mask & (1 << i))
            for mask in range(1, 1 << 12)
            if all(D[min(i,j),max(i,j)] <= q
                   for i,j in combinations((i for i in range(12) if mask & (1 << i)),2))}


K8, K24, K32, K40 = (faces(q) for q in (8,24,32,40))
assert tuple(map(len, (K8, K24, K32, K40))) == (34, 114, 342, 4095)
assert len(K40) == (1 << 12) - 1
# At the intermediate Euclidean shell, the missing-edge graph is three C4's.
missing={i:set() for i in range(12)}
for (i,j),d in D.items():
    if d==40: missing[i].add(j);missing[j].add(i)
assert all(len(missing[i])==2 for i in missing)
components=[];unseen=set(missing)
while unseen:
    root=min(unseen);cc={root};queue=deque([root]);unseen.remove(root)
    while queue:
        for u in missing[queue.popleft()]:
            if u in unseen: unseen.remove(u);cc.add(u);queue.append(u)
    components.append(cc)
assert len(components)==3 and all(len(c)==4 for c in components)


def vsub(a, b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


# Exhaustively enumerate the supporting planes of the convex hull.
facets = set()
for i,j,k in combinations(range(12),3):
    normal = cross(vsub(V[j],V[i]),vsub(V[k],V[i]))
    if normal == (0,0,0): continue
    signs = [dot(normal,vsub(w,V[i])) for w in V]
    if min(signs) < 0 < max(signs):continue
    facets.add(frozenset(h for h,s in enumerate(signs) if s==0))
assert Counter(map(len,facets)) == {3:4, 6:4}
hexagons=[tuple(h) for h in cert['boundary_hexagons']]
tri_facets=[tuple(t) for t in cert['boundary_facets_triangular']]
assert facets == {frozenset(f) for f in hexagons+tri_facets}
for h in hexagons:
    assert len(set(h)) == 6
    assert all(D[tuple(sorted((h[i],h[(i+1)%6])))] == 8 for i in range(6))

expected_tris = {frozenset(t) for t in tri_facets}
for h in hexagons:
    for t in (h[:3],h[2:5],(h[4],h[5],h[0]),(h[0],h[2],h[4])):
        assert all(D[tuple(sorted(e))] <= 24 for e in combinations(t,2))
        expected_tris.add(frozenset(t))
assert {frozenset(t) for t in cert['boundary_triangles']} == expected_tris
B = {frozenset(q) for t in expected_tris
     for k in (1,2,3) for q in combinations(sorted(t),k)}
assert Counter(map(len,B)) == {1:12,2:30,3:20}
assert B <= K24 <= K32
# Each vertex link is a single cycle; chi(B)=2, so B triangulates S^2.
for v in range(12):
    edge_link=[t-{v} for t in expected_tris if v in t]
    verts=set().union(*edge_link)
    adj={u:set() for u in verts}
    for e in edge_link:
        u,w=tuple(e);adj[u].add(w);adj[w].add(u)
    assert all(len(n)==2 for n in adj.values())
    visited={min(verts)};queue=deque(visited)
    while queue:
        for w in adj[queue.popleft()]:
            if w not in visited:visited.add(w);queue.append(w)
    assert visited==verts


def replay(initial,pairs,target=None):
    live=set(initial)
    target=set() if target is None else target
    for a,b in pairs:
        a,b=frozenset(a),frozenset(b)
        assert a < b and len(b)==len(a)+1
        assert a in live and b in live and a not in target and b not in target
        assert {f for f in live if a < f} == {b}, (sorted(a), sorted(b))
        live.remove(a);live.remove(b)
    return live


p8=cert['collapse_r8']
R8=replay(K8,p8)
assert len(p8)==4 and Counter(map(len,R8))=={1:12,2:14}
adj={i:set() for i in range(12)}
for e in (x for x in R8 if len(x)==2):
    a,b=tuple(e);adj[a].add(b);adj[b].add(a)
visited={0};queue=deque([0])
while queue:
    for w in adj[queue.popleft()]:
        if w not in visited:visited.add(w);queue.append(w)
assert len(visited)==12  # Connected graph: first Betti number 14-12+1=3.

p24=cert['collapse_r24_to_R']
R = replay(K24,p24,B)
assert len(p24)==12
extra_edges={f for f in R-B if len(f)==2}
extra_tris={f for f in R-B if len(f)==3}
assert len(extra_edges)==12 and len(extra_tris)==16 and not (R-B)-extra_edges-extra_tris
omitted={frozenset(t) for t in cert['omitted_triangles']}
assert len(omitted)==4 and omitted <= extra_tris
core=R-omitted
assert len(cert['collapse_core_to_boundary'])==12
assert replay(core,cert['collapse_core_to_boundary'],B)==B
# Thus the core collapses to a simply connected 2-sphere; the four omitted
# triangles attach along null-homotopic loops and add four 2-sphere summands.
assert len(cert['collapse_r32_to_boundary'])==140
assert replay(K32,cert['collapse_r32_to_boundary'],B)==B
# This proves that the *included* convex-boundary sphere generates H_2(K32;Z).


def inversion_sign(a):
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))


def lefschetz(g,K):
    value=-1  # reduced C_{-1} term
    for f in K:
        s=sorted(f);image=[g[x] for x in s]
        if set(image)==set(s):value+=(-1)**(len(s)-1)*inversion_sign(image)
    return value


def cycle_type(permutation):
    seen=set();parts=[]
    for x in range(len(permutation)):
        if x in seen:continue
        y=x;count=0
        while y not in seen:
            seen.add(y);y=permutation[y];count+=1
        parts.append(count)
    return tuple(sorted(parts,reverse=True))


corners=sorted((x,y,z) for x,y,z in product((-1,1),repeat=3) if x*y*z==1)
corner_index={v:i for i,v in enumerate(corners)}
expected={
    (1,1,1,1):(1,5,1),
    (2,1,1):(6,1,-1),
    (2,2):(3,1,1),
    (3,1):(8,2,1),
    (4,):(6,-1,-1)
}
chars=defaultdict(list)
for p in permutations(range(3)):
    for sign in product((-1,1),repeat=3):
        if sign[0]*sign[1]*sign[2]!=1:continue
        moved=lambda x:tuple(x[p[i]]*sign[i] for i in range(3))
        g=tuple(P[moved(v)] for v in V)
        c=tuple(corner_index[moved(v)] for v in corners)
        ty=cycle_type(c)
        det=inversion_sign(p)
        assert det == (-1)**(sum(t-1 for t in ty))
        a,b=lefschetz(g,K24),lefschetz(g,K32)
        chars[ty].append((a,b))
        assert b==det
assert {k:(len(v),v[0][0],v[0][1]) for k,v in chars.items()}==expected
assert all(len(set(v))==1 for v in chars.values())
# S_4 character identities: chi_24 = chi_trivial + chi_standard + chi_sign;
# chi_32=chi_sign, so the kernel is the four-point permutation module over Q.
for ty,(n,a,b) in expected.items():
    fixed=sum(t==1 for t in ty)
    sign=(-1)**(4-len(ty))
    assert b==sign and a==fixed+sign
print('VERIFY_OK: 12 vertices; pair-distance multiplicities (18,24,12,12)')
print('COLLAPSES_OK: r8=4, r24=12, relative_core=12, r32_to_boundary=140')
print('GEOMETRIC_SPHERE_OK: 12 vertices, 30 edges, 20 triangles')
print('S4_CHARACTERS_OK: 24 transformations, five conjugacy classes')
print('INTEGRAL_PERSISTENCE_OK: H2 rank 5 -> rank 1 surjectively -> 0')
