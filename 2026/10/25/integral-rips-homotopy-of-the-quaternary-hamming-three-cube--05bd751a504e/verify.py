#!/usr/bin/env python3
"""Exact finite discrete-Morse certificate for the quaternary three-cube.

Pure Python 3 standard library. All outputs are derived from the graph,
not from a stored matching or precalculated faces.
"""
from collections import Counter, deque
from array import array
from itertools import product, combinations
import hashlib

Q=4
POINTS=list(product(range(Q), repeat=3))
N=len(POINTS)
ALL=(1<<N)-1
NEIGHBORS=[sum(1<<j for j,other in enumerate(POINTS)
               if j!=i and sum(a!=b for a,b in zip(point,other))<=2)
           for i,point in enumerate(POINTS)]

def maximal_cliques():
    out=[]
    def visit(R,P,X):
        if not (P|X):
            out.append(R)
            return
        union=P|X
        best=-1
        while union:
            t=union&-union
            v=t.bit_length()-1
            union-=t
            z=(P&NEIGHBORS[v]).bit_count()
            if z>best:
                best=z; pivot=v
        candidates=P&~NEIGHBORS[pivot]
        while candidates:
            b=candidates&-candidates
            candidates-=b
            v=b.bit_length()-1
            visit(R|b,P&NEIGHBORS[v],X&NEIGHBORS[v])
            P-=b;X|=b
    visit(0,ALL,0)
    return out

FACETS=maximal_cliques()
EXPECTED=Counter({4:432,10:64,16:12})
assert Counter(f.bit_count() for f in FACETS)==EXPECTED
assert len(set(FACETS))==508

# Independently characterize facets: coordinate planes, distance-one balls,
# and parity tetrahedra using two-element subsets of each coordinate.
explicit=[]
for dim in range(3):
    for a in range(Q):
        explicit.append(sum(1<<j for j,x in enumerate(POINTS) if x[dim]==a))
for c in POINTS:
    explicit.append(sum(1<<j for j,x in enumerate(POINTS)
                        if sum(a!=b for a,b in zip(x,c))<=1))
for pairs in product(list(combinations(range(Q),2)),repeat=3):
    for parity in range(2):
        explicit.append(sum(1<<POINTS.index(tuple(pairs[i][(t>>i)&1]
                                               for i in range(3)))
                            for t in range(8) if t.bit_count()%2==parity))
assert set(FACETS)==set(explicit)
print('FACETS_OK',len(FACETS),dict(EXPECTED),flush=True)

# Enumerate every face by taking all subsets of every maximal clique.
faces=set()
for F in FACETS:
    subset=F
    while subset:
        faces.add(subset)
        subset=(subset-1)&F
faces.add(0)
assert len(faces)==830101
fvec=Counter(f.bit_count()-1 for f in faces)
assert sum(((-1)**d)*n for d,n in fvec.items() if d>=0)==1-405
assert fvec[3]==29136
print('FACES_OK',len(faces),sorted(fvec.items()),flush=True)

# Exhaustive lexicographic pivot matching on augmented face poset:
# at each coordinate-vertex v pair all *currently unused* F and F+v.
# Removing the empty-to-singleton pair yields an ordinary Morse matching
# with exactly one critical vertex and the high-dimensional critical faces.
remaining=faces.copy()
up={}
down={}
for v in range(N):
    bit=1<<v
    lower_faces=[f for f in remaining if not f&bit and (f|bit) in remaining]
    for lower in lower_faces:
        upper=lower|bit
        assert lower in remaining and upper in remaining
        remaining.remove(lower);remaining.remove(upper)
        up[lower]=upper
        down[upper]=lower
assert len(up)==414848
assert up[0]==1
assert Counter(x.bit_count()-1 for x in remaining)==Counter({3:405})
assert 0 not in remaining
print('MATCHING_OK',len(up),len(remaining),flush=True)

# Direct complete acyclicity test. Give each face an integer ID. Every cover
# U>U\{v} is oriented downward except matched covers, reversed upward.
# Kahn topological sorting visits ALL face nodes; no acyclicity assumption.
listing=list(faces)
index={s:i for i,s in enumerate(listing)}
assert len(index)==830101
indegree=array('i',[0])*len(listing)
matched_upper=array('i',[-1])*len(listing)
matched_lower=array('i',[-1])*len(listing)
for lower,upper in up.items():
    li=index[lower];ui=index[upper]
    matched_upper[li]=ui
    matched_lower[ui]=li
for ui,s in enumerate(listing):
    paired_lower=matched_lower[ui]
    b=s
    while b:
        low=s^(b&-b);b&=b-1
        li=index[low]
        if li==paired_lower:
            indegree[ui]+=1
        else:
            indegree[li]+=1
q=deque(i for i,d in enumerate(indegree) if d==0)
seen=0;edges=0
while q:
    ui=q.popleft();seen+=1
    lower_id=matched_lower[ui]
    s=listing[ui]
    b=s
    while b:
        li=index[s^(b&-b)];b&=b-1
        if li==lower_id: continue
        indegree[li]-=1
        edges+=1
        if indegree[li]==0: q.append(li)
    upper_id=matched_upper[ui]
    if upper_id>=0:
        indegree[upper_id]-=1
        edges+=1
        if indegree[upper_id]==0: q.append(upper_id)
assert seen==len(listing), ('gradient_cycle',seen,len(listing))
assert not any(indegree)
assert len(up)==414848
print('ACYCLIC_OK',seen,edges,flush=True)
print('VERIFY_OK',flush=True)
