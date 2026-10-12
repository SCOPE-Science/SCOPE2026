#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))

def cols(m):
    # source row order: constant coordinate first, then binary point coordinates
    return [tuple([1]+[(x>>j)&1 for j in range(m)]) for x in range(1<<m)]

def vxor(vs,k):
    out=[0]*k
    for v in vs:
        out=[a^b for a,b in zip(out,v)]
    return tuple(out)

def minimal_recovery_sets(m,target):
    C=cols(m); k=m+1; e=tuple(1 if j==target else 0 for j in range(k))
    good=[]
    for mask in range(1,1<<len(C)):
        S=tuple(i for i in range(len(C)) if (mask>>i)&1)
        if vxor([C[i] for i in S],k)==e:
            good.append(frozenset(S))
    gs=set(good)
    return sorted([S for S in gs if not any(T < S for T in gs)], key=lambda z:(len(z),sorted(z)))

m=3
C=cols(m)
assert C==[
 (1,0,0,0),(1,1,0,0),(1,0,1,0),(1,1,1,0),
 (1,0,0,1),(1,1,0,1),(1,0,1,1),(1,1,1,1)
]
R=[minimal_recovery_sets(m,i) for i in range(4)]
assert [len(x) for x in R]==[8,12,12,12]
assert sorted(map(len,R[0]))==[1]+[3]*7
for i in range(1,4):
    assert sorted(map(len,R[i]))==[2]*4+[4]*8

# Weighted server dual certificate: special zero-point column has weight 3, all others 1.
w=[3]+[1]*7
for S in R[0]:
    assert sum(w[j] for j in S)>=3
for i in range(1,4):
    for S in R[i]:
        assert sum(w[j] for j in S)>=2
assert sum(w)==10

# Exact rational allocations for all nonzero corrected-polytope vertices.
def check_alloc(alloc,target):
    load=[Fraction(0) for _ in range(8)]
    rate=[Fraction(0) for _ in range(4)]
    for i,S,a in alloc:
        S=frozenset(S); a=Fraction(a)
        assert S in R[i]
        rate[i]+=a
        for j in S: load[j]+=a
    assert tuple(rate)==tuple(map(Fraction,target)), (rate,target)
    assert max(load)<=1,load

# distinguished axis 10/3: singleton weight 1, all seven triples weight 1/3
alloc=[(0,{0},1)] + [(0,S,Fraction(1,3)) for S in R[0] if len(S)==3]
check_alloc(alloc,(Fraction(10,3),0,0,0))

# Other axes 4: the four pair recovery sets are disjoint partitions.
for i in range(1,4):
    pairs=[S for S in R[i] if len(S)==2]
    assert len(pairs)==4 and len(set().union(*pairs))==8
    assert sum(len(S) for S in pairs)==8
    check_alloc([(i,S,1) for S in pairs], tuple(4 if j==i else 0 for j in range(4)))

# Mixed vertices: explicit disjoint allocations.
check_alloc([(0,{0},1),(0,{1,6,7},1),(1,{2,3},1),(1,{4,5},1)],(2,2,0,0))
check_alloc([(0,{0},1),(0,{2,5,7},1),(2,{1,3},1),(2,{4,6},1)],(2,0,2,0))
check_alloc([(0,{0},1),(0,{3,4,7},1),(3,{1,5},1),(3,{2,6},1)],(2,0,0,2))

# All listed vertices satisfy the two corrected facets, and the claimed 2026-only point does not.
verts=[(0,0,0,0),(Fraction(10,3),0,0,0),(0,4,0,0),(0,0,4,0),(0,0,0,4),(2,2,0,0),(2,0,2,0),(2,0,0,2)]
for v in verts:
    assert sum(v)<=4
    assert 3*v[0]+2*sum(v[1:])<=10
bad=(Fraction(10,3),Fraction(2,3),0,0)
assert sum(bad)==4
assert bad[0]<=Fraction(10,3) and bad[1]<=4
assert 3*bad[0]+2*sum(bad[1:])>10

# General symbolic/rational checks over representative dimensions and column normal form.
for m in range(3,9):
    C=cols(m)
    assert len(C)==1<<m and len(set(C))==1<<m
    assert all(v[0]==1 for v in C)
    assert C[0]==tuple([1]+[0]*m)
    a=Fraction((1<<m)+2,3)
    b=Fraction(1<<(m-1),1)-a
    assert b>0
    lam=[a,b]+[Fraction(0)]*(m-1)
    # Every coordinate cap and every subset-sum cap printed in the new source is obeyed.
    assert lam[0]<=a
    assert all(x<=1<<(m-1) for x in lam[1:])
    assert sum(lam)==1<<(m-1)
    # Missing weighted facet is violated.
    assert 3*lam[0]+2*sum(lam[1:]) > (1<<m)+2
    # The weighted server certificate has total capacity 2^m+2.
    assert 3+((1<<m)-1)==(1<<m)+2

print('VERIFY_OK')
print('m3_minimal_recovery_counts', [len(x) for x in R])
print('m3_excluded_vector', '10/3,2/3,0,0')
