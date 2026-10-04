#!/usr/bin/env python3
from pathlib import Path
from itertools import product
from collections import Counter
import json

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
P = 3

def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]=(out[i+j]+x*y)%P
    return out

f={k:[int(x) for x in v] for k,v in cert["factors_low_to_high"].items()}
assert pmul(pmul(f["f1"],f["f2"]),f["f3"]) == [1]+[0]*10+[1]
assert pmul(pmul(f["f4"],f["f5"]),f["f6"]) == [1]+[0]*9+[1]

g0=pmul(f["f2"],f["f3"])
g1=pmul(f["f5"],f["f6"])
assert g0 == cert["generator_components_low_to_high"]["f2f3"]
assert g1 == cert["generator_components_low_to_high"]["f5f6"]

def reduce_consta(poly,m,lam=2):
    a=poly[:]
    while len(a)>m:
        c=a.pop()
        if c:
            deg=len(a)
            target=deg-m
            a[target]=(a[target]+lam*c)%P
    a += [0]*(m-len(a))
    return a

def constashift(v,lam=2):
    return [(lam*v[-1])%P]+v[:-1]

v0=reduce_consta(g0,11)
v1=reduce_consta(g1,10)
rows=[]
a,b=v0,v1
for _ in range(3):
    rows.append(a+b)
    a=constashift(a)
    b=constashift(b)
assert rows == cert["generator_matrix"]

def rankmod(A):
    A=[r[:] for r in A]; m=len(A); n=len(A[0]); rr=0
    for c in range(n):
        q=next((i for i in range(rr,m) if A[i][c]%P),None)
        if q is None: continue
        A[rr],A[q]=A[q],A[rr]
        iv=pow(A[rr][c],-1,P)
        A[rr]=[(iv*x)%P for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]:
                z=A[i][c]
                A[i]=[(A[i][j]-z*A[rr][j])%P for j in range(n)]
        rr+=1
        if rr==m: break
    return rr
assert rankmod(rows)==3

h=cert["explicit_weight_five_multiplier_low_to_high"]
first=reduce_consta(pmul(h,g0),11)
second=reduce_consta(pmul(h,g1),10)
word=first+second
assert word == cert["explicit_weight_five_word"]
assert sum(x!=0 for x in word)==5
assert first == [0]*11

dist=Counter()
for a in product(range(3),repeat=3):
    w=[sum(a[i]*rows[i][j] for i in range(3))%P for j in range(21)]
    dist[sum(x!=0 for x in w)]+=1
expected={int(k):v for k,v in cert["weight_distribution"].items()}
assert dict(sorted(dist.items()))==expected
assert min(w for w in dist if w)>0
assert min(w for w in dist if w)!=6
assert min(w for w in dist if w)==5

def norm(v):
    for x in v:
        if x:
            iv=pow(x,-1,P)
            return tuple((iv*y)%P for y in v)
    return None
cols=[tuple(rows[i][j] for i in range(3)) for j in range(21)]
norms=[norm(v) for v in cols]
assert all(v is not None for v in norms)
mult=Counter(norms)
assert sorted(mult.values(),reverse=True)==[11,5,5]
ghw=[5,21-max(mult.values()),21]
assert ghw==cert["generalized_hamming_weights"]

print("VERIFY_OK")
