#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
P=5
M=8

def pmul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            r[i+j]=(r[i+j]+x*y)%P
    while len(r)>1 and r[-1]==0:r.pop()
    return r

def xp(a): return [a%P,1]
def x2p(a): return [a%P,0,1]

def shift(poly,s):
    v=[0]*M
    for i,c in enumerate(poly):
        v[(i+s)%M]=(v[(i+s)%M]+c)%P
    return v

def rref(A):
    A=[[x%P for x in row] for row in A]
    rr=0;piv=[]
    for c in range(len(A[0])):
        p=next((i for i in range(rr,len(A)) if A[i][c]),None)
        if p is None:continue
        A[rr],A[p]=A[p],A[rr]
        inv=pow(A[rr][c],-1,P)
        A[rr]=[(inv*x)%P for x in A[rr]]
        for i in range(len(A)):
            if i!=rr and A[i][c]:
                f=A[i][c]
                A[i]=[(A[i][j]-f*A[rr][j])%P for j in range(len(A[0]))]
        piv.append(c);rr+=1
        if rr==len(A):break
    return A[:rr],piv

def qc_basis(a,b,c):
    rows=[]
    for s in range(M):rows.append(shift(a,s)+shift(b,s))
    for s in range(M):rows.append([0]*M+shift(c,s))
    return rref(rows)[0]

def nullspace(A):
    R,piv=rref(A)
    free=[j for j in range(len(A[0])) if j not in piv]
    out=[]
    for f in free:
        v=[0]*len(A[0]);v[f]=1
        for i,p in enumerate(piv):v[p]=(-R[i][f])%P
        out.append(v)
    return out

def in_span(v,B):
    R,piv=rref(B)
    w=v[:]
    for i,p in enumerate(piv):
        if w[p]:
            f=w[p]
            w=[(w[j]-f*R[i][j])%P for j in range(len(w))]
    return not any(w)

def stats(B):
    n=len(B[0]);k=len(B)
    hist=Counter(); comps=Counter()
    word=[0]*n
    def rec(i):
        if i==k:
            wt=sum(x!=0 for x in word)
            hist[wt]+=1
            comp=tuple(sum(x==a for x in word) for a in range(P))
            comps[comp]+=1
            return
        row=B[i]
        base=word[:]
        for a in range(P):
            if a==0:
                word[:] = base
            else:
                word[:] = [(base[j]+a*row[j])%P for j in range(n)]
            rec(i+1)
        word[:] = base
    rec(0)
    return hist,comps

g11=xp(2)
g12=pmul(xp(2),[1,0,1,1])
g22=[1]
for f in [xp(1),xp(2),xp(4),x2p(2),x2p(3)]:g22=pmul(g22,f)

f11=xp(3)
f12=pmul(xp(3),[1,0,1,4])
f22=[1]
for f in [xp(1),xp(3),xp(4),x2p(2),x2p(3)]:f22=pmul(f22,f)

C=qc_basis(g11,g12,g22)
D=qc_basis(f11,f12,f22)
DP=nullspace(D)

assert len(C)==8 and len(D)==8 and len(DP)==8
assert len(rref(C+D)[0])==16
assert all(sum(x*y for x,y in zip(d,h))%P==0 for d in D for h in DP)

HC,CC=stats(C)
HD,CD=stats(DP)
expected=Counter({int(k):v for k,v in cert["ordinary_weight_enumerator"].items()})
assert HC==expected and HD==expected
assert min(k for k in HC if k)>0 and min(k for k in HC if k>0)==7
assert min(k for k in HD if k>0)==7
assert HC[7]==704 and HD[7]==704

tc=tuple(cert["separating_composition"]["composition"])
assert CC[tc]==8 and CD[tc]==0
assert sum(1 for c,n in CC.items() if sum(c[1:])==7 and n)>0
assert sum(1 for c,n in CC.items() if sum(c[1:])==7 and n)==48
assert sum(1 for c,n in CD.items() if sum(c[1:])==7 and n)==20

w=cert["witness_C_block_order"]
assert tuple(sum(x==a for x in w) for a in range(P))==tc
assert in_span(w,C)

print("VERIFY_OK")
