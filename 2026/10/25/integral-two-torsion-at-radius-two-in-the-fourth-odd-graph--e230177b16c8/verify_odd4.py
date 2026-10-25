#!/usr/bin/env python3
"""Exact integral first homology of the radius-two Rips complex of O_4."""
from itertools import combinations
from collections import Counter,defaultdict
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

triples=list(combinations(range(7),3));sets=list(map(set,triples));N=len(triples)
# Original Kneser graph: disjoint triples. In KG(7,3), distances:
# 1 when intersection 0; 2 when intersection 2; 3 when intersection 1.
adj={i:set() for i in range(N)}
orig=[]
for i,j in combinations(range(N),2):
    d=len(sets[i]&sets[j])
    if d==0: orig.append((i,j))
    if d in (0,2):adj[i].add(j);adj[j].add(i)
assert len(orig)==70
# Independently verify the shortest-path definition and the girth-six boundary.
from collections import deque
origadj={i:set() for i in range(N)}
for a,b in orig: origadj[a].add(b);origadj[b].add(a)
assert all(len(origadj[i])==4 for i in range(N))
girth=100
for start in range(N):
    dist={start:0}; parent_bfs={start:-1}; queue=deque([start])
    while queue:
        v=queue.popleft()
        for w in origadj[v]:
            if w not in dist:
                dist[w]=dist[v]+1;parent_bfs[w]=v;queue.append(w)
            elif parent_bfs[v]!=w:
                girth=min(girth,dist[v]+dist[w]+1)
    assert len(dist)==N and max(dist.values())==3
    for j in range(N): assert (j in adj[start])==(0<dist[j]<=2)
assert girth==6
# Deterministic Bron-Kerbosch maximal-clique enumeration.
def bker(R,P,X):
    if not P and not X:
        yield tuple(sorted(R));return
    pivot=max(P|X,key=lambda v:len(P&adj[v])) if P|X else None
    for v in sorted(P-(adj[pivot] if pivot is not None else set())):
        yield from bker(R|{v},P&adj[v],X&adj[v]);P.remove(v);X.add(v)
facets=list(bker(set(),set(range(N)),set()))
assert len(facets)==56 and all(len(f)==5 for f in facets)
faces=set()
for f in facets:
    for k in range(1,6):faces.update(combinations(f,k))
assert Counter(map(len,faces))=={1:35,2:280,3:560,4:280,5:56}
cofaces=defaultdict(set)
for f in faces:
    if len(f)>1:
        for i in range(len(f)):
            cofaces[f[:i]+f[i+1:]].add(f)
active=set(faces);pairs=[]
for top in [5,4]:
    while True:
        available=[]
        for s in active:
            if len(s)!=top-1:continue
            cs=[f for f in cofaces[s] if f in active]
            if len(cs)==1 and len(cs[0])==top:
                available.append((s,cs[0]))
        if not available:break
        a,b=min(available)
        assert a in active and b in active
        active.remove(a);active.remove(b);pairs.append((a,b))
assert len(pairs)==280 and Counter(map(len,active))=={1:35,2:280,3:336}
# A collapsed two-complex has the same integral homology.
edges=sorted(s for s in active if len(s)==2)
triangles=sorted(s for s in active if len(s)==3)
# Kruskal spanning tree (the graph is connected).
parent=list(range(N))
def root(i):
    while parent[i]!=i:
        i=parent[i]
    return i
T=set()
for a,b in edges:
    u,v=root(a),root(b)
    if u!=v:
        parent[u]=v;T.add((a,b))
assert len(T)==34
chords=[e for e in edges if e not in T]
ci={e:i for i,e in enumerate(chords)}
B=[[0]*len(triangles) for _ in chords]
for j,t in enumerate(triangles):
    for i in range(3):
        e=t[:i]+t[i+1:]
        if e in ci:B[ci[e]][j]=(-1)**i
# The cycles of a connected graph are identified with the free abelian
# group on non-tree edges. The relation lattice is the column lattice B.
H=hermite_normal_form(Matrix(B))
assert H.shape==(246,246)
diag=[int(H[i,i]) for i in range(246)]
assert Counter(diag)=={1:245,2:1}
# Independent characteristic-two rank check on the same signed cellular boundary.
def gf2_rank(matrix):
    pivots={}
    for row in matrix:
        word=sum((int(x)&1)<<j for j,x in enumerate(row))
        while word:
            lead=word.bit_length()-1
            if lead not in pivots:
                pivots[lead]=word;break
            word^=pivots[lead]
    return len(pivots)
assert gf2_rank(B)==245
# Over Q, the exact HNF certificate has rank 246. The mod-2 deficit
# independently witnesses a nonzero element of order two in H1.
# HNF is a Z-basis of the image lattice, so the quotient is Z/2.
# No third or fourth homology remains after verified elementary collapses.
# Euler characteristic of collapsed complex is 35-280+336=91.
# Connectedness, H1=Z/2 and absence of higher homology imply H2=Z^90.
print('ORIGINAL_KNESER_VERTICES_AND_EDGES',N,len(orig))
print('GIRTH_AND_DIAMETER',girth,3)
print('SQUARED_GRAPH_EDGES',len(edges))
print('MAXIMAL_FACETS',len(facets))
print('ORIGINAL_FACE_VECTOR',35,280,560,280,56)
print('ELEMENTARY_COLLAPSE_PAIRS',len(pairs))
print('COLLAPSED_FACE_VECTOR',35,280,336)
print('GRAPH_CYCLE_RANK',len(chords))
print('TRIANGLE_RELATIONS',len(triangles))
print('HNF_DIAGONAL_INVARIANTS',Counter(diag))
print('MOD2_BOUNDARY_RANK',gf2_rank(B))
print('INTEGRAL_H1_Z2_H2_Z90')
print('SCALE_1_H1_RANK',len(orig)-N+1)
print('VERIFY_OK_ODD_GRAPH_O4_RIPS2_TORSION')
