#!/usr/bin/env python3
import json,itertools,collections,sys
from pathlib import Path
from collections import deque

HERE=Path(__file__).resolve().parent
cert=json.loads((HERE/'morse_certificate.json').read_text())
V=[tuple(x) for x in cert['vertices']]
assert V==sorted(itertools.permutations(range(4),2))

# The truncated tetrahedral graph: each original K4 vertex becomes a triangle
# of outgoing arcs, and each original edge gives the bridge between opposite arcs.
adj={v:set() for v in V}
for a,b in itertools.combinations(V,2):
    if a[0]==b[0] or a==(b[1],b[0]):
        adj[a].add(b); adj[b].add(a)
assert sum(map(len,adj.values()))//2==18
assert all(len(adj[v])==3 for v in V)

D={}
for s in V:
    ds={s:0}; q=deque([s])
    while q:
        u=q.popleft()
        for w in sorted(adj[u]):
            if w not in ds:
                ds[w]=ds[u]+1; q.append(w)
    assert len(ds)==12
    D[s]=ds
assert max(max(ds.values()) for ds in D.values())==3

def vr_faces(r):
    out=[]
    for mask in range(1,1<<12):
        s=tuple(i for i in range(12) if (mask>>i)&1)
        if all(D[V[i]][V[j]]<=r for i,j in itertools.combinations(s,2)):
            out.append(s)
    return set(out)

F1=vr_faces(1)
F2=vr_faces(2)
fv1=collections.Counter(len(s)-1 for s in F1)
fv2=collections.Counter(len(s)-1 for s in F2)
assert fv1==collections.Counter({1:18,0:12,2:4})
assert fv2==collections.Counter({2:48,1:42,0:12,3:12})

# r=1: collapse one free edge from each of the four filled tail-triangles.
active=set(F1)
for tail in range(4):
    ids=[i for i,v in enumerate(V) if v[0]==tail]
    tri=tuple(sorted(ids))
    edge=tuple(sorted(ids[:2]))
    assert tri in active and edge in active
    co=[t for t in active if len(t)==3 and set(edge)<set(t)]
    assert co==[tri]
    active.remove(edge); active.remove(tri)
# Remaining complex is a connected graph with V=12,E=14, hence wedge of 3 circles.
verts=[s for s in active if len(s)==1]
edges=[s for s in active if len(s)==2]
assert len(verts)==12 and len(edges)==14
A={i:set() for i in range(12)}
for a,b in edges: A[a].add(b);A[b].add(a)
seen={0};q=deque([0])
while q:
    u=q.popleft()
    for w in A[u]:
        if w not in seen: seen.add(w);q.append(w)
assert len(seen)==12
assert len(edges)-len(verts)+1==3

# r=2: replay a discrete-Morse elimination order. A matched lower face must have
# exactly one active immediate coface, which certifies a free pair at that stage.
active=set(F2); matches=[]; critical=[]
for step in cert['steps']:
    if step[0]=='match':
        lo=tuple(step[1]); hi=tuple(step[2])
        assert lo in active and hi in active and len(hi)==len(lo)+1 and set(lo)<set(hi)
        co=[]
        for t in active:
            if len(t)==len(lo)+1 and set(lo)<set(t): co.append(t)
        assert co==[hi], (lo,co,hi)
        active.remove(lo);active.remove(hi);matches.append((lo,hi))
    else:
        c=tuple(step[1]); assert c in active
        active.remove(c); critical.append(c)
assert not active
assert collections.Counter(len(c)-1 for c in critical)==collections.Counter({2:5,0:1})
assert len(matches)==54

# Direct acyclicity check on Forman orientation of the full Hasse diagram.
matchset={(lo,hi) for lo,hi in matches}
digraph={s:set() for s in F2}
for hi in F2:
    if len(hi)<=1: continue
    for k in range(len(hi)):
        lo=hi[:k]+hi[k+1:]
        if (lo,hi) in matchset: digraph[lo].add(hi)
        else: digraph[hi].add(lo)
indeg={s:0 for s in F2}
for u in digraph:
    for w in digraph[u]: indeg[w]+=1
q=deque([s for s,d in indeg.items() if d==0]);n=0
while q:
    u=q.popleft();n+=1
    for w in digraph[u]:
        indeg[w]-=1
        if indeg[w]==0:q.append(w)
assert n==len(F2)

print('graph: V=12 E=18 diameter=3')
print('r=1 f-vector:', [fv1[i] for i in range(3)], 'collapse -> connected graph beta1=3')
print('r=2 f-vector:', [fv2[i] for i in range(4)], 'Morse critical counts: c0=1,c1=0,c2=5,c3=0')
print('r>=3: full 11-simplex')
print('VERIFY_OK')
