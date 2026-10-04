#!/usr/bin/env python3
from pathlib import Path
from itertools import product
from collections import Counter
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))

# GF(9)=GF(3)[u]/(u^2+1), u^2=2. Elements are tuples (a,b)=a+b*u.
E=[(a,b) for a in range(3) for b in range(3)]
Z=(0,0); O=(1,0); M1=(2,0)
def add(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def mul(x,y):
    a,b=x; c,d=y
    return ((a*c+2*b*d)%3,(a*d+b*c)%3)
def smul(a,v): return tuple(mul(a,x) for x in v)
def vadd(v,w): return tuple(add(x,y) for x,y in zip(v,w))

def mm(A,B):
    return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
minus_I=[[M1,Z],[Z,M1]]

sis=[]
for a,b,c in product(E,repeat=3):
    A=[[a,b],[b,c]]
    if mm(A,A)==minus_I:
        sis.append(A)
assert len(sis)==10

def unpack(A): return [[[x[0],x[1]] for x in row] for row in A]
assert sorted(map(str,map(unpack,sis)))==sorted(map(str,cert['matrices']))

def code_data(A):
    rows=[(O,Z,A[0][0],A[0][1]),(Z,O,A[1][0],A[1][1])]
    # GG^T=0.
    for i in range(2):
        for j in range(2):
            s=Z
            for x,y in zip(rows[i],rows[j]): s=add(s,mul(x,y))
            assert s==Z
    dist=Counter()
    for a,b in product(E,repeat=2):
        w=vadd(smul(a,rows[0]),smul(b,rows[1]))
        dist[sum(x!=Z for x in w)]+=1
    d=min(k for k in dist if k)
    return d,dist

distance_counts=Counter()
for A in sis:
    d,_=code_data(A)
    distance_counts[d]+=1
assert distance_counts==Counter({2:6,3:4})
assert {str(k):v for k,v in sorted(distance_counts.items())}==cert['distance_distribution']

A=[[(1,0),(1,0)],[(1,0),(2,0)]]
assert A in sis
d,wd=code_data(A)
assert d==3
assert dict(sorted(wd.items()))=={0:1,3:32,4:48}
assert {str(k):v for k,v in sorted(wd.items())}==cert['explicit_mds_weight_distribution']

# Structural split: four diagonal, two pure off-diagonal, four prime-subfield MDS cases.
diag=[A for A in sis if A[0][1]==Z]
pure_off=[A for A in sis if A[0][0]==Z and A[0][1]!=Z]
mds=[A for A in sis if code_data(A)[0]==3]
assert len(diag)==4 and len(pure_off)==2 and len(mds)==4
assert all(all(x[1]==0 for row in A for x in row) for A in mds)

print('VERIFY_OK')
