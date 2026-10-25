#!/usr/bin/env python3
"""Recompute the dodecahedral perfect-matching complex and its integral Morse invariants.

Python 3 standard library only; deterministic integer arithmetic.
"""
from collections import Counter, deque
from functools import lru_cache

N = 10
VERTICES = 20
EDGES = sorted({tuple(sorted(e)) for i in range(N) for e in
                ((i, (i+1)%N), (i, N+i), (N+i, N+(i+2)%N))})
assert len(EDGES) == 30 and len(set(EDGES)) == 30
neighbors = [[] for _ in range(VERTICES)]
for j,(u,v) in enumerate(EDGES):
    neighbors[u].append((v,j)); neighbors[v].append((u,j))
assert all(len(a)==3 for a in neighbors)

@lru_cache(None)
def perfect_matchings(unused):
    if unused == 0:
        return ((),)
    v = (unused & -unused).bit_length()-1
    out=[]
    for w,e in neighbors[v]:
        if (unused>>w)&1:
            out.extend((e,)+t for t in perfect_matchings(unused^(1<<v)^(1<<w)))
    return tuple(out)

pm = perfect_matchings((1<<VERTICES)-1)
assert len(pm)==36 and all(len(t)==10 for t in pm)
facets=[]
for p in pm:
    f=sum(1<<j for j in p)
    assert f.bit_count()==10
    facets.append(f)
assert len(set(facets))==36

faces=set()
for f in facets:
    # All nonempty subsets of each facet, explicitly, not just a sample.
    s=f
    while s:
        faces.add(s)
        s=(s-1)&f
assert len(faces)==30503
fvector=Counter(f.bit_count() for f in faces)
assert [fvector[k] for k in range(1,11)] == [30,375,2180,5790,8352,7440,4320,1620,360,36]

# Sequential matching: at stage j, toggle j on every still-available lower face
# whose upper partner is still available. A stage is an acyclic matching and all
# remaining faces form a union of components when oriented by the stage label.
remaining=set(faces)
pairs=[]
for j in range(len(EDGES)):
    for face in sorted(remaining):
        if (face>>j)&1: continue
        up=face|(1<<j)
        if up in remaining:
            pairs.append((face,up))
            remaining.remove(face); remaining.remove(up)
assert len(pairs)==15231 and len(remaining)==41
assert Counter(x.bit_count()-1 for x in remaining)==Counter({0:1,2:10,3:30})
low_high=dict(pairs)
high_low={b:a for a,b in pairs}
assert len(low_high)==len(high_low)==len(pairs)
assert len(set(low_high).intersection(high_low))==0

# Independently inspect the entire modified Hasse digraph; matched arrows go
# upwards, all other cover arrows go downwards.
indegree={f:0 for f in faces}
outdegree={f:0 for f in faces}
for f in faces:
    s=f
    while s:
        b=s&-s
        g=f^b
        s-=b
        if g==0:continue
        if low_high.get(g)==f:
            a,z=g,f
        else:
            a,z=f,g
        indegree[z]+=1
        outdegree[a]+=1
arrows=sum(outdegree.values())
assert arrows==sum(indegree.values())
# Kahn without holding a redundant adjacency list: generate neighbors by
# traversing only potential dimension +1 and -1 Hasse covers.
queue=deque(f for f,n in indegree.items() if n==0)
seen=0
while queue:
    f=queue.popleft(); seen+=1
    s=f
    while s:
        b=s&-s; g=f^b; s-=b
        if g and low_high.get(g)!=f:
            indegree[g]-=1
            if indegree[g]==0:queue.append(g)
    for j in range(len(EDGES)):
        if not ((f>>j)&1):
            up=f|(1<<j)
            if low_high.get(f)==up:
                indegree[up]-=1
                if indegree[up]==0:queue.append(up)
assert seen==len(faces),('cycle',seen,len(faces))

# Reduce critical three-cell boundaries to critical two-cells through the
# elementary integral chain cancellations induced by the acyclic matching.
crit2=sorted(f for f in remaining if f.bit_count()==3)
crit3=sorted(f for f in remaining if f.bit_count()==4)
which={f:i for i,f in enumerate(crit2)}
def boundary(f):
    pos=0
    for j in range(len(EDGES)):
        if f>>j&1:
            yield ((-1 if pos%2 else 1),f^(1<<j))
            pos+=1

@lru_cache(None)
def reduce2(f):
    if f in which:
        return {which[f]:1}
    if f in high_low:
        return {}
    up=low_high[f]
    coefficient=next(a for a,g in boundary(up) if g==f)
    values={}
    for a,g in boundary(up):
        if g==f:continue
        for i,z in reduce2(g).items():
            values[i]=values.get(i,0)-coefficient*a*z
    return {i:v for i,v in values.items() if v}

B=[[0]*len(crit3) for _ in crit2]
for col,f in enumerate(crit3):
    for a,g in boundary(f):
        for row,n in reduce2(g).items():B[row][col]+=a*n
assert len(B)==10 and all(len(r)==30 for r in B)
assert max(abs(x) for row in B for x in row) == 1

def rank_mod2(mat):
    piv={}
    for row in mat:
        bits=sum((x%2)<<i for i,x in enumerate(row))
        while bits:
            k=bits.bit_length()-1
            if k not in piv:
                piv[k]=bits;break
            bits^=piv[k]
    return len(piv)
assert rank_mod2(B)==9

def det_bareiss(mat):
    a=[list(row) for row in mat]
    n=len(a)
    if n==0:return 1
    assert all(len(row)==n for row in a)
    sign=1;prev=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None:return 0
        if p!=k:a[k],a[p]=a[p],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

cols10=[0,2,4,5,6,7,8,10,11,26]
rows9=[0,1,3,4,5,6,7,8,9]
cols9=[0,4,5,6,7,8,10,11,26]
minor10=det_bareiss([[B[i][j] for j in cols10] for i in range(10)])
minor9=det_bareiss([[B[i][j] for j in cols9] for i in rows9])
assert minor10==2 and minor9==-1
# rank over Q = 10 from the nonzero full minor. Rank mod 2 = 9 forces
# all full-order minors even. A 9-minor is +/-1. Thus Smith factors =
# 1 (nine times), 2 (once), with no higher factors.
# A one-vertex, zero-one-cell, two/three-cell Morse CW model is simply
# connected; GL(Z) changes of cellular bases are realized by homotopy
# equivalences of the wedge-of-2-spheres skeleton, so the attaching matrix
# isolates a degree-two map and twenty trivial 3-cell attachments.

print('VERIFY_OK')
print('VERTICES=20 EDGES=30 PERFECT_MATCHINGS=36')
print('FVECTOR_BY_SIZE='+','.join(str(fvector[k]) for k in range(1,11)))
print(f'FACES={len(faces)} HASSE_ARROWS={arrows} ACYCLIC_VERTICES={seen}')
print(f'MATCHING_PAIRS={len(pairs)} CRITICAL_0_2_3=(1,10,30)')
print('MORSE_BOUNDARY_SHAPE=10x30 MOD2_RANK=9 FULL_MINOR_10=2 UNIT_MINOR_9=-1')
print('SMITH=1,1,1,1,1,1,1,1,1,2')
print('HOMOTOPY=M(Z/2,2) WEDGE 20*S^3')
