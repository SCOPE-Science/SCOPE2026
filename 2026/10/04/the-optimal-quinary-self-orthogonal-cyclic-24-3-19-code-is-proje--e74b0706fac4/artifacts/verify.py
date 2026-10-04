#!/usr/bin/env python3
from pathlib import Path
from itertools import product
from collections import Counter
import json

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

p = 5
def add(x,y): return ((x[0]+y[0])%5,(x[1]+y[1])%5)
def neg(x): return ((-x[0])%5,(-x[1])%5)
def mul(x,y):
    a,b=x; c,d=y
    return ((a*c+3*b*d)%5,(a*d+b*c)%5)
one=(1,0); zero=(0,0)
def fpow(x,n):
    r=one
    while n:
        if n&1: r=mul(r,x)
        x=mul(x,x); n//=2
    return r
def order(x):
    r=one
    for k in range(1,25):
        r=mul(r,x)
        if r==one:return k
    raise AssertionError

alpha=(1,1)
assert order(alpha)==24

def coset(w):
    out=[]; x=w%24
    while x not in out:
        out.append(x); x=(5*x)%24
    return out

D1=[0,4,8,12]
D2=[1,2,3,6,7]
R=set()
for w in D1+D2+[9,13,14]:
    R.update(coset(w))
R=sorted(R)
assert R==cert["defining_set"]

def pmul(A,B):
    out=[zero]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):
            out[i+j]=add(out[i+j],mul(a,b))
    return out

g=[one]
for r in R:
    root=fpow(alpha,r)
    g=pmul(g,[neg(root),one])
assert all(c[1]==0 for c in g)
g5=[c[0] for c in g]
assert g5==cert["generator_polynomial_low_to_high"]

def poly_divmod(a,b):
    a=a[:]
    while len(a)>1 and a[-1]==0:a.pop()
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        t=a[-1]*pow(b[-1],-1,5)%5
        d=len(a)-len(b); q[d]=t
        for i,bi in enumerate(b):
            a[d+i]=(a[d+i]-t*bi)%5
        while len(a)>1 and a[-1]==0:a.pop()
    return q,a

xn=[0]*25; xn[0]=4; xn[24]=1
_,rem=poly_divmod(xn,g5)
assert rem==[0]

G=[]
for s in range(3):
    row=[0]*24
    for j,b in enumerate(g5):
        row[s+j]=b
    G.append(row)

def rank5(A):
    A=[r[:] for r in A]; m=len(A); n=len(A[0]); rr=0
    for c in range(n):
        k=next((i for i in range(rr,m) if A[i][c]%5),None)
        if k is None:continue
        A[rr],A[k]=A[k],A[rr]
        inv=pow(A[rr][c],-1,5)
        A[rr]=[(inv*x)%5 for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]%5:
                a=A[i][c]%5
                A[i]=[(A[i][j]-a*A[rr][j])%5 for j in range(n)]
        rr+=1
        if rr==m:break
    return rr

assert rank5(G)==3
for i in range(3):
    for j in range(3):
        assert sum(G[i][t]*G[j][t] for t in range(24))%5==0

dist=Counter()
min_complements=set()
for a in product(range(5),repeat=3):
    w=[sum(a[i]*G[i][j] for i in range(3))%5 for j in range(24)]
    wt=sum(x!=0 for x in w)
    dist[wt]+=1
    if wt==19:
        min_complements.add(tuple(i for i,x in enumerate(w) if x==0))
expected={int(k):v for k,v in cert["weight_distribution"].items()}
assert dict(sorted(dist.items()))==expected

def norm(v):
    for x in v:
        if x%5:
            inv=pow(x,-1,5)
            return tuple((inv*y)%5 for y in v)
    return None

cols=[tuple(G[i][j] for i in range(3)) for j in range(24)]
assert all(any(v) for v in cols)
norms=[norm(v) for v in cols]
assert len(set(norms))==24
assert cert["projective_column_count"]==24
assert cert["maximum_projective_column_multiplicity"]==1
ghw=[19,23,24]
assert ghw==cert["generalized_hamming_weights"]

assert len(min_complements)==24
B=tuple(cert["minimum_support_complement_orbit_representative"])
orbit={tuple(sorted((x+t)%24 for x in B)) for t in range(24)}
assert len(orbit)==24
assert orbit==min_complements

print("VERIFY_OK")
