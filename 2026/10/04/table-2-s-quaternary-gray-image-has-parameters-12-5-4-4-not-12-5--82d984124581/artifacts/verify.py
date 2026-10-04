#!/usr/bin/env python3
from pathlib import Path
from itertools import product, combinations
from collections import Counter
import json

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# GF(4) = GF(2)[w]/(w^2+w+1), 0,1,w,w^2 encoded 0,1,2,3.
MUL = [[0]*4 for _ in range(4)]
for x in range(4):
    for y in range(4):
        a0,a1=x&1,(x>>1)&1
        b0,b1=y&1,(y>>1)&1
        c0=(a0*b0) ^ (a1*b1)
        c1=(a0*b1) ^ (a1*b0) ^ (a1*b1)
        MUL[x][y]=c0|(c1<<1)

def mul(a,b): return MUL[a][b]
def add(a,b): return a ^ b
def theta(a): return mul(a,a)
def inv(a):
    for b in range(1,4):
        if mul(a,b)==1: return b
    raise ZeroDivisionError

w=2
def delta(a):
    return mul(w, add(theta(a), a))  # subtraction equals addition in characteristic two

def T(v, alpha=1):
    n=len(v)
    out=[0]*n
    out[0]=add(mul(alpha,theta(v[-1])), delta(v[0]))
    for i in range(1,n):
        out[i]=add(theta(v[i-1]), delta(v[i]))
    return out

g1=[2,2,2,2]
g2=[1,1,0,0]
g3=[1,1,1,1]
component_bases = [
    [g1],
    [g2, T(g2), T(T(g2))],
    [g3]
]
assert component_bases[1] == [[1,1,0,0],[0,1,1,0],[0,0,1,1]]

M=cert["gray_matrix"]
def gray(component_rows):
    out=[]
    for j in range(4):
        a=[component_rows[r][j] for r in range(3)]
        out.extend([
            add(add(mul(a[0],M[0][c]),mul(a[1],M[1][c])),mul(a[2],M[2][c]))
            for c in range(3)
        ])
    return out

G=[]
for comp,basis in enumerate(component_bases):
    for v in basis:
        rows=[[0]*4 for _ in range(3)]
        rows[comp]=v
        G.append(gray(rows))
assert G == cert["gray_generator_matrix"]

# Explicit word: component multipliers (0, 1+x^2, 1).
c2=[add(g2[i],T(T(g2))[i]) for i in range(4)]
assert c2==g3
explicit = gray([[0]*4,c2,g3])
assert explicit == cert["explicit_gray_word"]
assert sum(x!=0 for x in explicit)==4

def rref(rows,ncols=None):
    A=[list(r) for r in rows if any(r)]
    if not A:return tuple()
    if ncols is None:ncols=len(A[0])
    rr=0
    for c in range(ncols):
        p=next((i for i in range(rr,len(A)) if A[i][c]),None)
        if p is None:continue
        A[rr],A[p]=A[p],A[rr]
        s=inv(A[rr][c])
        A[rr]=[mul(s,x) for x in A[rr]]
        for i in range(len(A)):
            if i!=rr and A[i][c]:
                a=A[i][c]
                A[i]=[add(A[i][j],mul(a,A[rr][j])) for j in range(ncols)]
        rr+=1
        if rr==len(A):break
    return tuple(tuple(r) for r in A[:rr])

assert len(rref(G,12))==5

dist=Counter()
for coeff in product(range(4),repeat=5):
    v=[0]*12
    for a,row in zip(coeff,G):
        if a:
            v=[add(x,mul(a,y)) for x,y in zip(v,row)]
    dist[sum(x!=0 for x in v)]+=1
expected={int(k):v for k,v in cert["weight_distribution"].items()}
assert dict(sorted(dist.items()))==expected
assert min(t for t in dist if t)>0
assert min(t for t in dist if t)==4

cols=[tuple(G[i][j] for i in range(5)) for j in range(12)]
def in_span(v,basis):
    return len(rref(list(basis)+[v],5))==len(basis)

maxima=[0]
counts=[1]
for t in range(1,5):
    spans=set()
    for comb in combinations(range(12),t):
        key=rref([cols[j] for j in comb],5)
        if len(key)==t:
            spans.add(key)
    counts.append(len(spans))
    maxima.append(max(sum(in_span(v,key) for v in cols) for key in spans))

assert counts==cert["distinct_column_generated_subspaces_by_dimension"]
assert maxima==cert["column_intersection_maxima_by_subspace_dimension"]
ghw=[12-maxima[5-r] for r in range(1,6)]
assert ghw==cert["generalized_hamming_weights"]

print("VERIFY_OK")
