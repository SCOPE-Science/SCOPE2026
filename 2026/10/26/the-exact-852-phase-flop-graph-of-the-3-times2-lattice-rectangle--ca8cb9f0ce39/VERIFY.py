"""Exact integer verification for the 3-by-2 lattice-rectangle flip graph.

Run with Python 3: python3 VERIFY.py (CERTIFICATES.json in the same directory).
Only uses the Python standard library.  No numerical optimization is used.
"""
from collections import Counter, deque
from itertools import combinations
from math import gcd
from pathlib import Path
import json

P = [(x, y) for y in range(3) for x in range(4)]
V = len(P)
def ind(x,y): return 4*y+x
def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
def edge(a,b): return tuple(sorted((a,b)))
def crossing(e,f):
    if set(e)&set(f): return False
    a,b=(P[e[0]],P[e[1]])
    c,d=(P[f[0]],P[f[1]])
    return cross(a,b,c)*cross(a,b,d)<0 and cross(c,d,a)*cross(c,d,b)<0
boundary = set()
for x in range(3):
    boundary.update([edge(ind(x,0),ind(x+1,0)),edge(ind(x,2),ind(x+1,2))])
for y in range(2):
    boundary.update([edge(ind(0,y),ind(0,y+1)),edge(ind(3,y),ind(3,y+1))])
E = [e for e in combinations(range(V),2)
     if gcd(abs(P[e[0]][0]-P[e[1]][0]),abs(P[e[0]][1]-P[e[1]][1]))==1
     and e not in boundary]
C = [sum(1<<j for j,f in enumerate(E) if crossing(e,f)) for e in E]
assert len(boundary)==10
seed_edges=set()
for y in range(3):
    for x in range(3): seed_edges.add(edge(ind(x,y),ind(x+1,y)))
for x in range(4):
    for y in range(2): seed_edges.add(edge(ind(x,y),ind(x,y+1)))
for y in range(2):
    for x in range(3): seed_edges.add(edge(ind(x,y),ind(x+1,y+1)))
seed_edges-=boundary
assert len(seed_edges)==13
seed=sum(1<<E.index(e) for e in seed_edges)

adj={}
frontier=[seed]
seen={seed}
while frontier:
    new=[]
    for mask in frontier:
        nbr=set()
        for i in range(len(E)):
            if not(mask>>i)&1: continue
            candidates=C[i]&~mask
            while candidates:
                b=candidates&-candidates
                j=b.bit_length()-1
                candidates-=b
                nxt=(mask^(1<<i))|(1<<j)
                if not (nxt&C[j]):
                    nbr.add(nxt)
                    if nxt not in seen:
                        seen.add(nxt)
                        new.append(nxt)
        adj[mask]=nbr
    frontier=new
assert len(adj)==len(seen)==852
assert all(u in adj[v] for u,vs in adj.items() for v in vs)
assert all(t.bit_count()==13 for t in adj)
assert all(not ((t>>i)&1 and (t&C[i])) for t in adj for i in range(len(E)))
assert sum(map(len,adj.values()))==5252

triangles=[]
for tri in combinations(range(V),3):
    a,b,c=tri
    if abs(cross(P[a],P[b],P[c]))==1: triangles.append(tri)
tri_of={}
for mask in adj:
    es={E[k] for k in range(len(E)) if (mask>>k)&1}|boundary
    tris=frozenset(tr for tr in triangles if all(edge(a,b) in es for a,b in combinations(tr,2)))
    assert len(tris)==12
    tri_of[mask]=tris

def coefficients(tr,d):
    a,b,c=tr
    aa,bb,cc,dd=P[a],P[b],P[c],P[d]
    det=cross(aa,bb,cc)
    assert abs(det)==1
    nums=(cross(dd,bb,cc),cross(aa,dd,cc),cross(aa,bb,dd))
    return tuple(z//det for z in nums)

def clearance(h,tr,d):
    return h[d]-sum(k*h[v] for k,v in zip(coefficients(tr,d),tr))

bundle=json.loads((Path(__file__).resolve().parent/'CERTIFICATES.json').read_text(encoding='utf-8'))
node_certs={int(k):h for k,h in bundle['triangulations']}
assert set(node_certs)==set(adj)
for mask,h in node_certs.items():
    assert len(h)==V and all(type(x) is int for x in h)
    for tr in tri_of[mask]:
        for d in range(V):
            if d not in tr:
                assert clearance(h,tr,d)>=1,('node',mask,tr,d)
wall_certs={(int(a),int(b)):h for a,b,h in bundle['walls']}
true_walls={(a,b) for a,vs in adj.items() for b in vs if a<b}
assert set(wall_certs)==true_walls
for (a,b),h in wall_certs.items():
    assert len(h)==V and all(type(x) is int for x in h)
    common=tri_of[a]&tri_of[b]
    assert len(common)==10
    changed=tri_of[a]^tri_of[b]
    quad=set().union(*changed)
    assert len(quad)==4
    tr=next(iter(tri_of[a]-common))
    for cell in common:
        for d in range(V):
            if d not in cell:
                assert clearance(h,cell,d)>=1,('wall common',a,b,cell,d)
    for d in range(V):
        if d not in tr:
            assert (clearance(h,tr,d)==0 if d in quad else clearance(h,tr,d)>=1),('wall quad',a,b,d)

deg=Counter(map(len,adj.values()))
expected={2:2,3:48,4:108,5:176,6:180,7:132,8:128,9:34,10:30,11:12,13:2}
assert dict(deg)==expected
Ecc={}
radius=10
for root in adj:
    dist={root:0};q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v]=dist[u]+1;q.append(v)
    assert len(dist)==852
    Ecc[root]=max(dist.values())
assert min(Ecc.values())==radius
assert max(Ecc.values())==20
assert sum(n==20 for n in Ecc.values())==2
pair20=[]
for a in adj:
    q=deque([a]);dist={a:0}
    while q:
        u=q.popleft()
        for b in adj[u]:
            if b not in dist:
                dist[b]=dist[u]+1;q.append(b)
    pair20.extend((a,b) for b,d in dist.items() if d==20 and a<b)
assert len(pair20)==1
assert pair20[0]==(int('8c3c04117',16),int('71885e0820',16))
print('PASS: 852 triangulations; 2626 flip edges; 852 strict integer lifting certificates;')
print('2626 integer wall certificates; degree spectrum',sorted(deg.items()))
print('PASS: graph radius 10, diameter 20, unique diameter pair',tuple(map(hex,pair20[0])))
