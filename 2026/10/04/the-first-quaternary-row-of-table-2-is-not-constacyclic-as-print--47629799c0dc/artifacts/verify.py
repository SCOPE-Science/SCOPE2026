#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
from itertools import product
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def add(a,b): return a^b
def mul(a,b):
    a0,a1=a&1,(a>>1)&1
    b0,b1=b&1,(b>>1)&1
    c0=(a0*b0)^(a1*b1)
    c1=(a0*b1)^(a1*b0)^(a1*b1)
    return c0|(c1<<1)
def power(a,e):
    r=1
    while e:
        if e&1:r=mul(r,a)
        a=mul(a,a);e>>=1
    return r

assert mul(2,2)==3 and mul(2,3)==1

def trim(p):
    p=p[:]
    while p and p[-1]==0:p.pop()
    return p
def divmod4(a,b):
    a=trim(a);b=trim(b)
    q=[0]*max(1,len(a)-len(b)+1)
    inv=power(b[-1],2)
    while a and len(a)>=len(b):
        d=len(a)-len(b);c=mul(a[-1],inv);q[d]=c
        for j,x in enumerate(b):a[d+j]^=mul(c,x)
        a=trim(a)
    return trim(q),trim(a)

g=[1,2,1,1,1]
modulus=[2]+[0]*9+[1]
_,r=divmod4(modulus,g)
_,rr=divmod4(modulus,list(reversed(g)))
assert r==[1,3,0,2]
assert rr==[2,2,3,3]

rows=[]
for s in range(6):
    v=[0]*10
    for j,x in enumerate(g):v[s+j]=x
    rows.append(v)

def rank4(A):
    A=[r[:] for r in A];r=0
    for c in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        inv=power(A[r][c],2)
        A[r]=[mul(inv,x) for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[A[i][j]^mul(f,A[r][j]) for j in range(len(A[0]))]
        r+=1
    return r

assert rank4(rows)==6

def word(a):
    v=[0]*10
    for i,c in enumerate(a):
        for j,x in enumerate(rows[i]):v[j]^=mul(c,x)
    return v

dist=Counter()
for a in product(range(4),repeat=6):
    v=word(a);dist[sum(x!=0 for x in v)]+=1
assert sum(dist.values())==4096
assert min(k for k in dist if k>0)==3
assert dist==Counter({0:1,3:12,4:57,5:246,6:645,7:960,8:1158,9:798,10:219})

gram=[]
for u in rows:
    row=[]
    for v in rows:
        z=0
        for a,b in zip(u,v):z^=mul(a,power(b,2))
        row.append(z)
    gram.append(row)
assert rank4(gram)==6
assert 6-rank4(gram)==0

expected={int(k):v for k,v in cert["ordinary_shift_span"]["weight_distribution"].items()}
assert dict(dist)==expected
assert cert["ordinary_shift_span"]["parameters"]==[10,6,3]
assert cert["ordinary_shift_span"]["hermitian_hull_dimension"]==0
print("VERIFY_OK")
