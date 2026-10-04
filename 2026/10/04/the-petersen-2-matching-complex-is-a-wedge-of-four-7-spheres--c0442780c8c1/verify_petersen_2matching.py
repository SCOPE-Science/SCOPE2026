#!/usr/bin/env python3
from collections import Counter, deque

EDGES=[(0,1),(1,2),(2,3),(3,4),(0,4),(0,5),(1,6),(2,7),(3,8),(4,9),(5,7),(6,8),(7,9),(5,8),(6,9)]
EXPECTED_F=[15,105,445,1245,2358,2985,2400,1095,215,6]
EXPECTED_CRIT=[1,15058,22964,26442,27316]

inc=[[] for _ in range(10)]
for j,(u,v) in enumerate(EDGES):
    inc[u].append(j); inc[v].append(j)

def is_face(mask):
    return all(sum((mask>>j)&1 for j in inc[v])<=2 for v in range(10))

faces=[m for m in range(1,1<<len(EDGES)) if is_face(m)]
face_set=set(faces)
f=Counter(m.bit_count()-1 for m in faces)
assert [f[d] for d in range(10)]==EXPECTED_F
assert len(faces)==10869

active=set(faces); pairs=[]
for eidx in range(len(EDGES)):
    bit=1<<eidx
    lows=sorted(m for m in active if not (m&bit) and (m|bit) in active)
    for lo in lows:
        hi=lo|bit
        if lo in active and hi in active:
            assert hi in face_set and lo in face_set
            assert hi.bit_count()==lo.bit_count()+1
            pairs.append((lo,hi))
            active.remove(lo); active.remove(hi)

critical=sorted(active)
assert len(pairs)==5432
assert critical==EXPECTED_CRIT
assert Counter(m.bit_count()-1 for m in critical)==Counter({7:4,0:1})

pairset=set(pairs)
adj={m:[] for m in faces}
indeg={m:0 for m in faces}
cover_count=0
for hi in faces:
    if hi.bit_count()<2: continue
    for j in range(len(EDGES)):
        if (hi>>j)&1:
            lo=hi^(1<<j)
            if lo==0: continue
            assert lo in face_set
            cover_count+=1
            if (lo,hi) in pairset: a,b=lo,hi
            else: a,b=hi,lo
            adj[a].append(b); indeg[b]+=1
assert cover_count==63780

q=deque(m for m,d in indeg.items() if d==0)
seen=0
while q:
    u=q.popleft(); seen+=1
    for v in adj[u]:
        indeg[v]-=1
        if indeg[v]==0: q.append(v)
assert seen==len(faces)

by_dim={d:[] for d in range(10)}
for m in faces: by_dim[m.bit_count()-1].append(m)

def gf2_rank(cols):
    basis={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in basis: x^=basis[p]
            else:
                basis[p]=x; break
    return len(basis)

ranks={}
for d in range(1,10):
    ridx={m:i for i,m in enumerate(by_dim[d-1])}
    cols=[]
    for m in by_dim[d]:
        c=0
        for j in range(len(EDGES)):
            if (m>>j)&1: c^=1<<ridx[m^(1<<j)]
        cols.append(c)
    ranks[d]=gf2_rank(cols)

betti={}
for d in range(10):
    b=len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)
    if d==0: b-=1
    if b: betti[d]=b
assert betti=={7:4}
assert sum(((-1)**d)*EXPECTED_F[d] for d in range(10))==-3
print("VERIFY_OK faces=10869 hasse=63780 pairs=5432 critical={0:1,7:4} betti={7:4}")
