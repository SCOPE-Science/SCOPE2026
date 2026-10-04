#!/usr/bin/env python3
from itertools import product
from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# F4 = F2[w]/(w^2+w+1). Encode a+b*w as a+2*b.
def add(a,b): return a ^ b
def mul(a,b):
    a0=a&1; a1=(a>>1)&1
    b0=b&1; b1=(b>>1)&1
    return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1)<<1)

def inv(a):
    if a == 0: raise ZeroDivisionError
    for b in (1,2,3):
        if mul(a,b)==1: return b
    raise AssertionError("no inverse")

def rref(rows):
    if not rows: return [], []
    A=[r[:] for r in rows]
    m=len(A); n=len(A[0]); piv=[]; rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if A[i][c]), None)
        if p is None: continue
        A[rr],A[p]=A[p],A[rr]
        q=inv(A[rr][c])
        A[rr]=[mul(q,x) for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]:
                q=A[i][c]
                A[i]=[add(A[i][j],mul(q,A[rr][j])) for j in range(n)]
        piv.append(c); rr+=1
        if rr==m: break
    return A[:rr], piv

def rank(rows):
    if not rows: return 0
    return len(rref(rows)[1])

def nullspace(rows):
    R,piv=rref(rows)
    n=len(rows[0])
    free=[j for j in range(n) if j not in piv]
    out=[]
    for f in free:
        v=[0]*n; v[f]=1
        for i,p in enumerate(piv):
            v[p]=R[i][f]  # subtraction equals addition in characteristic 2
        out.append(v)
    return out

def polyvec(p,m):
    assert len(p)<=m
    return p+[0]*(m-len(p))

def shift(v,j):
    j%=len(v)
    return v[-j:]+v[:-j] if j else v[:]

def qc_basis(p11,p12,p22,m):
    a=polyvec(p11,m); b=polyvec(p12,m); c=polyvec(p22,m)
    rows=[]
    for j in range(m):
        rows.append(shift(a,j)+shift(b,j))
        rows.append([0]*m+shift(c,j))
    return rref(rows)[0]

def word(B, coeff):
    n=len(B[0]); out=[0]*n
    for i,c in enumerate(coeff):
        if c:
            out=[add(out[j],mul(c,B[i][j])) for j in range(n)]
    return out

def weight_distribution(B):
    C=Counter()
    for a in product(range(4), repeat=len(B)):
        v=word(B,a)
        C[sum(x!=0 for x in v)] += 1
    return C

def ghw(B):
    k=len(B); n=len(B[0])
    ans=[n+1]*k
    for mask in range(1<<n):
        s=mask.bit_count()
        outside=[j for j in range(n) if ((mask>>j)&1)==0]
        rr=rank([[row[j] for j in outside] for row in B]) if outside else 0
        dim=k-rr
        for r in range(1,dim+1):
            if s<ans[r-1]:
                ans[r-1]=s
    return ans

row=cert["table_row"]; m=row["m"]
cg=row["C_generators_ascending"]; dg=row["D_generators_ascending"]
C=qc_basis(cg["g11"],cg["g12"],cg["g22"],m)
D=qc_basis(dg["f11"],dg["f12"],dg["f22"],m)
Dp=nullspace(D)
exp=cert["expected"]

assert len(C)==exp["dim_C"]==9
assert len(D)==exp["dim_D"]==5
assert len(Dp)==exp["dim_Dperp"]==9
assert rank(C+D)==exp["rank_C_plus_D"]==14

# Direct orthogonality check for D and Dperp.
for u in D:
    for v in Dp:
        z=0
        for a,b in zip(u,v):
            z=add(z,mul(a,b))
        assert z==0

wc=weight_distribution(C)
wd=weight_distribution(Dp)
ec=Counter({int(k):v for k,v in exp["weight_distribution_C"].items()})
ed=Counter({int(k):v for k,v in exp["weight_distribution_Dperp"].items()})
# certificate includes explicit zero at weight 5 for Dperp; Counter equality ignores absent zero
ed += Counter()
assert wc==ec
assert wd==Counter({k:v for k,v in ed.items() if v})
assert sum(wc.values())==4**9
assert sum(wd.values())==4**9
assert min(k for k in wc if k)>0 and min(k for k in wd if k)>0
assert min(k for k in wc if k>0)==4
assert min(k for k in wd if k>0)==4

assert ghw(C)==exp["ghw_C"]
assert ghw(Dp)==exp["ghw_Dperp"]
assert wc != wd
assert exp["ghw_C"] != exp["ghw_Dperp"]

print("VERIFY_OK")
