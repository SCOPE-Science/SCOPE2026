#!/usr/bin/env python3
from pathlib import Path
from itertools import product
from collections import Counter
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))
MOD=0b1011

def add(a,b): return a^b

def mul(a,b):
    r=0
    while b:
        if b&1: r^=a
        b>>=1
        a<<=1
        if a&8: a^=MOD
    return r&7

def inv(a):
    assert a!=0
    r=1
    for _ in range(6): r=mul(r,a)
    return r

def rank(A):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]) if A else 0; rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if A[i][c]),None)
        if p is None: continue
        A[rr],A[p]=A[p],A[rr]
        s=inv(A[rr][c])
        A[rr]=[mul(s,x) for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]:
                a=A[i][c]
                A[i]=[add(A[i][j],mul(a,A[rr][j])) for j in range(n)]
        rr+=1
        if rr==m: break
    return rr

def gram(H):
    k=len(H); n=len(H[0]); out=[]
    for i in range(k):
        row=[]
        for j in range(k):
            s=0
            for t in range(n): s=add(s,mul(H[i][t],H[j][t]))
            row.append(s)
        out.append(row)
    return out

powers=[1]
for _ in range(1,7): powers.append(mul(powers[-1],2))
assert powers==[1,2,4,3,6,7,5]
G=[
    [1,0,0,1,powers[5],powers[5]],
    [0,1,0,powers[1],powers[4],powers[6]],
    [0,0,1,powers[4],powers[1],powers[5]],
]
assert G==cert['generator_matrix_integer_encoding']
assert rank(G)==3
assert 3-rank(gram(G))==cert['baseline_hull_dimension']==1

wd=Counter()
for a in product(range(8),repeat=3):
    w=[]
    for j in range(6):
        s=0
        for i in range(3): s=add(s,mul(a[i],G[i][j]))
        w.append(s)
    wd[sum(x!=0 for x in w)]+=1
expected_wd={int(k):v for k,v in cert['baseline_weight_distribution'].items()}
assert dict(sorted(wd.items()))==expected_wd

profile=Counter()
witness={}
for tail in product(range(1,8),repeat=5):
    scale=(1,)+tail
    H=[[mul(G[i][j],scale[j]) for j in range(6)] for i in range(3)]
    h=3-rank(gram(H))
    profile[h]+=1
    witness.setdefault(h,scale)
expected={int(k):v for k,v in cert['hull_dimension_profile'].items()}
for h in range(4):
    assert profile[h]==expected[h]
assert sum(profile.values())==cert['normalized_scalings_examined']==16807
assert sorted(h for h,c in profile.items() if c)==cert['attainable_hull_dimensions']==[0,1,2]
assert max(h for h,c in profile.items() if c)==cert['maximal_hull_dimension']==2

for hstr,scale in cert['witness_scalings_integer_encoding'].items():
    h=int(hstr)
    H=[[mul(G[i][j],scale[j]) for j in range(6)] for i in range(3)]
    assert 3-rank(gram(H))==h

print('VERIFY_OK')
