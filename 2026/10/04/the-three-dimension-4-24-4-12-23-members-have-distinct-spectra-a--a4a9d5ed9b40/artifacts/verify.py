#!/usr/bin/env python3
from pathlib import Path
from itertools import product, combinations
from collections import Counter
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
P=23
D=5

def add(a,b): return ((a[0]+b[0])%P,(a[1]+b[1])%P)
def mul(a,b): return ((a[0]*b[0]+D*a[1]*b[1])%P,(a[0]*b[1]+a[1]*b[0])%P)
ONE=(1,0)
def fpow(a,n):
    r=ONE
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a); n//=2
    return r
def order(a):
    r=ONE
    for k in range(1,P*P):
        r=mul(r,a)
        if r==ONE:return k
    raise AssertionError("no order")

beta=tuple(cert["beta"])
assert order(beta)==24
assert fpow(beta,23)==fpow(beta,23)  # field Frobenius representative
def mi(i):
    a=fpow(beta,i); b=fpow(beta,24-i)
    tr=add(a,b)
    assert tr[1]==0 and mul(a,b)==ONE
    return [1,(-tr[0])%P,1]
for i in range(1,12):
    assert mi(i)==cert["minimal_polynomials_low_to_high"][str(i)]

def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]=(out[i+j]+x*y)%P
    return out

def pdivmod(a,b):
    a=a[:]
    while len(a)>1 and a[-1]==0:a.pop()
    q=[0]*max(1,len(a)-len(b)+1)
    inv=pow(b[-1],-1,P)
    while len(a)>=len(b) and any(a):
        t=a[-1]*inv%P
        d=len(a)-len(b); q[d]=t
        for i,v in enumerate(b): a[d+i]=(a[d+i]-t*v)%P
        while len(a)>1 and a[-1]==0:a.pop()
    return q,a

def gen(I):
    g=[1]
    for i in sorted(set(I)|set(range(4,12))):
        g=pmul(g,mi(i))
    return g

def Gmat(g):
    G=[]
    for s in range(4):
        row=[0]*24
        for j,v in enumerate(g): row[s+j]=v
        G.append(row)
    return G

def rank(A):
    A=[list(r) for r in A]
    if not A:return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]%P),None)
        if q is None:continue
        A[r],A[q]=A[q],A[r]
        inv=pow(A[r][c],-1,P)
        A[r]=[x*inv%P for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%P:
                t=A[i][c]%P
                A[i]=[(A[i][j]-t*A[r][j])%P for j in range(n)]
        r+=1
        if r==m:break
    return r

def norm(v):
    for x in v:
        if x%P:
            inv=pow(x,-1,P)
            return tuple(y*inv%P for y in v)
    return None

def rref_basis(vs):
    A=[list(v) for v in vs]
    m=len(A); n=4; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]),None)
        if q is None:continue
        A[r],A[q]=A[q],A[r]
        inv=pow(A[r][c],-1,P)
        A[r]=[x*inv%P for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                t=A[i][c]
                A[i]=[(A[i][j]-t*A[r][j])%P for j in range(n)]
        r+=1
        if r==m:break
    return tuple(tuple(A[i]) for i in range(r))

def in_span(v,B):
    return rank(list(B)+[v])==len(B)

def weight_distribution(G):
    # 529 pair-combinations for first two and last two rows, then 529^2 sums.
    pair01=[]
    pair23=[]
    for a,b in product(range(P),repeat=2):
        pair01.append(tuple((a*G[0][j]+b*G[1][j])%P for j in range(24)))
        pair23.append(tuple((a*G[2][j]+b*G[3][j])%P for j in range(24)))
    ctr=Counter()
    for u in pair01:
        for v in pair23:
            ctr[sum(((u[j]+v[j])%P)!=0 for j in range(24))]+=1
    return dict(sorted(ctr.items()))

xn=[0]*25; xn[0]=P-1; xn[24]=1
for key,I in [("1,2",{1,2}),("1,3",{1,3}),("2,3",{2,3})]:
    c=cert["cases"][key]
    g=gen(I)
    assert g==c["generator_low_to_high"]
    _,rem=pdivmod(xn,g)
    assert rem==[0]
    G=Gmat(g)
    assert rank(G)==4

    got=weight_distribution(G)
    expected={int(k):v for k,v in c["weight_distribution"].items()}
    assert got==expected
    assert sum(got.values())==P**4
    assert min(w for w in got if w)>0 and min(w for w in got if w)==12

    cols=[tuple(G[i][j] for i in range(4)) for j in range(24)]
    assert all(any(c0) for c0 in cols)
    pc=Counter(norm(c0) for c0 in cols)
    assert len(pc)==c["projective_point_count"]
    assert set(pc.values())=={c["projective_point_multiplicity"]}
    pts=list(pc)
    lines=set()
    for a,b in combinations(pts,2):
        B=rref_basis([a,b])
        if len(B)==2: lines.add(B)
    maxline=max(sum(mult for q,mult in pc.items() if in_span(q,B)) for B in lines)
    assert maxline==c["max_line_column_count"]
    maxpoint=max(pc.values())
    ghw=[12,24-maxline,24-maxpoint,24]
    assert ghw==c["generalized_hamming_weights"]

print("VERIFY_OK")
