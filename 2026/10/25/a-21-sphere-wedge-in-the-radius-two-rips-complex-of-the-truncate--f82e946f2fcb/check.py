#!/usr/bin/env python3
"""Exact finite verification for the 60-vertex truncated-icosahedral graph at graph distance two.
No dependencies beyond Python's standard library. Run: python3 check.py
"""
from itertools import combinations
from collections import Counter,defaultdict,deque

# Abstract icosahedron: two pentagonal rings and their north/south poles.
U=tuple(range(5)); L=tuple(range(5,10)); N=10; S=11
edge=set()
def e(u,v): edge.add(tuple(sorted((u,v))))
for i in range(5):
    e(N,U[i]);e(S,L[i]); e(U[i],U[(i+1)%5]);e(L[i],L[(i+1)%5]);
    e(U[i],L[i]);e(U[i],L[(i-1)%5]);
assert len(edge)==30
adj={i:set() for i in range(12)}
for a,b in edge: adj[a].add(b);adj[b].add(a)
assert all(len(adj[i])==5 for i in adj)
triangles={frozenset(t) for t in combinations(range(12),3) if all(tuple(sorted(p)) in edge for p in combinations(t,2))}
assert len(triangles)==20
assert all(sum({a,b}<=t for t in triangles)==2 for a,b in edge)

arcs=tuple(sorted((a,b) for a,b in edge for a,b in ((a,b),(b,a))))
assert len(arcs)==60
idx={a:i for i,a in enumerate(arcs)}
G={i:set() for i in range(60)}
def conn(x,y): a=idx[x];b=idx[y];G[a].add(b);G[b].add(a)
for a,b in edge: conn((a,b),(b,a))
for face in triangles:
    for a in face:
        b,c=sorted(face-{a});conn((a,b),(a,c))
assert sum(len(x) for x in G.values())==180 and set(map(len,G.values()))=={3}
# Exact all-pairs unweighted shortest paths.
dist={}
for i in range(60):
    d={i:0};Q=deque([i])
    while Q:
        v=Q.popleft()
        for w in G[v]:
            if w not in d: d[w]=d[v]+1;Q.append(w)
    assert len(d)==60
    dist[i]=d
# Every shortcut edge is homotopic to an original length-two edge.
assert all(sum(v in G[u] and w in G[u] for u in G)==1
           for v,w in combinations(range(60),2) if dist[v][w]==2)
assert all(not (G[a]&G[b]) for a,b in ((a,b) for a in G for b in G[a] if a < b)) # triangle-free
assert all(len(G[a]&G[b])<=1 for a,b in combinations(range(60),2)) # four-cycle-free

# The 12 five-gonal and 20 six-gonal faces of the truncation.
pentagons=[]
for u in range(12):
    p={idx[(u,v)] for v in adj[u]}
    assert len(p)==5
    assert all(len(G[v]&p)==2 for v in p)
    # Every two corners of this pentagon have graph distance at most two.
    assert all(dist[x][y]<=2 for x,y in combinations(sorted(p),2))
    pentagons.append(p)
hexagons=[]
for face in sorted(triangles,key=lambda s:tuple(sorted(s))):
    a,b,c=sorted(face)
    h=[idx[z] for z in ((a,b),(b,a),(b,c),(c,b),(c,a),(a,c))]
    assert len(set(h))==6
    assert all(h[(i+1)%6] in G[h[i]] for i in range(6))
    # The fan of four triangles gives an explicit filling of the hexagon.
    assert all(all(dist[x][y]<=2 for x,y in combinations(t,2))
        for t in [(h[0],h[1],h[2]),(h[2],h[3],h[4]),
                  (h[4],h[5],h[0]),(h[0],h[2],h[4])])
    hexagons.append(h)
assert len(pentagons)==12 and len(hexagons)==20
# Their boundaries use each original edge twice, identifying the planar embedding.
edgeuses=Counter()
for cyc in hexagons:
    for a,b in zip(cyc,cyc[1:]+cyc[:1]): edgeuses[tuple(sorted((a,b)))]+=1
# The pentagonal boundary is the induced 5-cycle, computed without a starting orientation.
for p in pentagons:
    for a,b in combinations(sorted(p),2):
        if b in G[a]: edgeuses[(a,b)]+=1
assert len(edgeuses)==90 and set(edgeuses.values())=={2}

# Enumerate every simplex from the distance-two graph, in strictly increasing vertex order.
near={i:{j for j in range(60) if j!=i and dist[i][j]<=2} for i in range(60)}
faces=set()
def walk(prefix,candidates):
    for i,x in enumerate(candidates):
        t=prefix+(x,);faces.add(t)
        walk(t,[y for y in candidates[i+1:] if y in near[x]])
walk((),list(range(60)))
count=Counter(len(s)-1 for s in faces)
assert count=={0:60,1:270,2:340,3:120,4:12},count
assert sum((-1)**k*v for k,v in count.items())==22

# Every high-dimensional simplex disappears by a verified *elementary* collapse.
# A free codimension-one face belongs to exactly one currently remaining coface.
cofaces=defaultdict(set)
for t in faces:
    if len(t)>1:
        for k in range(len(t)): cofaces[t[:k]+t[k+1:]].add(t)
collapses=[]
while any(len(t)>=4 for t in faces):
    free=[]
    for s,cs in cofaces.items():
        if len(s)<3 or s not in faces or len(cs)!=1: continue
        t=next(iter(cs))
        if t in faces and len(t)==len(s)+1: free.append((s,t))
    assert free,'No remaining free face: collapse does not exist'
    s,t=min(free,key=lambda st:(-len(st[1]),st[0]))
    for z in (s,t):
        assert z in faces
        faces.remove(z)
        for k in range(len(z)):
            cofaces[z[:k]+z[k+1:]].discard(z)
    collapses.append((s,t))
assert len(collapses)==120,len(collapses)
assert Counter(len(t)-1 for t in faces)=={0:60,1:270,2:232}
assert all(t[:i]+t[i+1:] in faces for t in faces if len(t)>1 for i in range(len(t)))
# This 2-complex is simply connected by the face-filling argument in RESULT.md;
# its Euler characteristic is 22. Whitehead and Hurewicz imply 21 two-spheres.
print('PASS: icosahedron 12 vertices, 30 edges, 20 triangular faces')
print('PASS: truncated graph 60 vertices, 90 edges, 12 pentagons, 20 hexagons')
print('PASS: facial fillings at graph scale two; every shortcut edge has unique midpoint')
print('PASS: Rips simplex counts (60,270,340,120,12), Euler characteristic 22')
print('PASS: 120 elementary collapses eliminate all dimensions greater than 2')
print('RESULT: VR_le_2(truncated_icosahedral_graph) homotopy wedge of 21 two-spheres')
