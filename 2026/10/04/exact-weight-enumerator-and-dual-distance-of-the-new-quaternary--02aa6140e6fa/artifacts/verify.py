#!/usr/bin/env python3
from pathlib import Path
from itertools import product, combinations
from collections import Counter
from math import comb
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
G=cert["generator_matrix"]

ADD=[[a^b for b in range(4)] for a in range(4)]
MUL=[[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
INV=[None,1,3,2]
CONJ=[0,1,3,2]
def add(a,b): return ADD[a][b]
def mul(a,b): return MUL[a][b]

def rank4(rows,ncols=None):
    if not rows:return 0
    if ncols is None:ncols=len(rows[0])
    A=[list(r) for r in rows]
    rr=0
    for c in range(ncols):
        p=next((i for i in range(rr,len(A)) if A[i][c]),None)
        if p is None:continue
        A[rr],A[p]=A[p],A[rr]
        s=INV[A[rr][c]]
        A[rr]=[mul(s,x) for x in A[rr]]
        for i in range(rr+1,len(A)):
            if A[i][c]:
                a=A[i][c]
                A[i]=[add(A[i][j],mul(a,A[rr][j])) for j in range(ncols)]
        rr+=1
        if rr==len(A):break
    return rr

assert len(G)==10 and all(len(r)==22 for r in G)
assert rank4(G,22)==10

Gram=[]
for i in range(10):
    row=[]
    for j in range(10):
        s=0
        for a,b in zip(G[i],G[j]):
            s=add(s,mul(a,CONJ[b]))
        row.append(s)
    Gram.append(row)
assert rank4(Gram,10)==10

dist=Counter()
for coeff in product(range(4),repeat=10):
    v=[0]*22
    for a,row in zip(coeff,G):
        if a:
            v=[add(x,mul(a,y)) for x,y in zip(v,row)]
    dist[sum(x!=0 for x in v)]+=1
expected={int(k):v for k,v in cert["weight_distribution"].items()}
assert dict(sorted(dist.items()))==expected
assert sum(dist.values())==4**10
assert min(k for k in dist if k)>0
assert min(k for k in dist if k)==9

cols=[tuple(G[i][j] for i in range(10)) for j in range(22)]
assert all(any(c) for c in cols)

for I in combinations(range(22),6):
    assert rank4([cols[j] for j in I],10)==6

dep7=[]
for I in combinations(range(22),7):
    r=rank4([cols[j] for j in I],10)
    if r<7:
        assert r==6
        dep7.append(I)
assert len(dep7)==cert["dependent_seven_subsets"]
assert tuple(cert["dependent_seven_subset_witness"]) in dep7
assert cert["dual_minimum_distance"]==7
assert cert["orthogonal_array_strength"]==6
assert cert["dual_weight_seven_words"]==3*len(dep7)

# Independent MacWilliams check of the dual weight-seven coefficient.
n=22;q=4;j=7
s=0
for i,Ai in dist.items():
    K=0
    lo=max(0,j-(n-i)); hi=min(j,i)
    for h in range(lo,hi+1):
        K += ((-1)**h)*(q-1)**(j-h)*comb(i,h)*comb(n-i,j-h)
    s += Ai*K
assert s%(4**10)==0
A7=s//(4**10)
assert A7==264==cert["dual_weight_seven_words"]

print("VERIFY_OK")
