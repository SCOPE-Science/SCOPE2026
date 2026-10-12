#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def peval(c,x,p):
    v=0
    for a in reversed(c): v=(v*x+a)%p
    return v

def cubic(p):
    for a0 in range(1,p):
        for a1 in range(p):
            for a2 in range(p):
                c=(a0,a1,a2,1)
                if all(peval(c,x,p) for x in range(p)): return (a0,a1,a2)
    raise RuntimeError

class Fp3:
    def __init__(self,p): self.p=p; self.a0,self.a1,self.a2=cubic(p)
    def add(self,x,y): return tuple((x[i]+y[i])%self.p for i in range(3))
    def mul(self,x,y):
        p=self.p; t=[0]*5
        for i,a in enumerate(x):
            for j,b in enumerate(y): t[i+j]=(t[i+j]+a*b)%p
        for d in (4,3):
            z=t[d]%p
            if z:
                t[d]=0
                t[d-3]=(t[d-3]-z*self.a0)%p
                t[d-2]=(t[d-2]-z*self.a1)%p
                t[d-1]=(t[d-1]-z*self.a2)%p
        return tuple(t[:3])
    def power(self,x,n):
        r=(1,0,0)
        while n:
            if n&1: r=self.mul(r,x)
            x=self.mul(x,x); n//=2
        return r
    def tr(self,x):
        z=self.add(self.add(x,self.power(x,self.p)),self.power(x,self.p*self.p))
        assert z[1:]==(0,0)
        return z[0]%self.p
    def elems(self): return list(itertools.product(range(self.p),repeat=3))

def rank_mod(M,p):
    A=[r[:] for r in M]
    if not A: return 0
    m=len(A); n=len(A[0]); rr=0
    for c in range(n):
        q=next((i for i in range(rr,m) if A[i][c]%p),None)
        if q is None: continue
        A[rr],A[q]=A[q],A[rr]
        iv=pow(A[rr][c]%p,-1,p)
        A[rr]=[(iv*x)%p for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]%p:
                f=A[i][c]%p
                A[i]=[(A[i][j]-f*A[rr][j])%p for j in range(n)]
        rr+=1
        if rr==m: break
    return rr

def gram(rows,p):
    return [[sum(a*b for a,b in zip(x,y))%p for y in rows] for x in rows]

def check(p):
    F=Fp3(p); E=F.elems()
    S=[]
    for x in E:
        xx=F.mul(x,x)
        for y in E:
            if F.tr(F.add(xx,F.mul(y,y)))==0: S.append((x,y))
    assert len(S)==p**5-p**3+p**2
    B=[(1,0,0),(0,1,0),(0,0,1)]
    rows=[[1]*len(S)]
    rows += [[F.tr(F.mul(b,x)) for x,y in S] for b in B]
    rows += [[F.tr(F.mul(c,y)) for x,y in S] for c in B]
    assert rank_mod(rows,p)==7
    assert all(v==0 for row in gram(rows,p) for v in row)
    first=[0]+[F.tr(b) for b in B]+[0,0,0]
    unp=[[first[i]]+rows[i] for i in range(7)]
    UG=gram(unp,p)
    assert UG==[[first[i]*first[j]%p for j in range(7)] for i in range(7)]
    assert rank_mod(UG,p)==1
    if p==3:
        ctr=collections.Counter()
        for msg in itertools.product(range(3),repeat=7):
            w=0
            for j in range(len(S)):
                v=sum(msg[i]*rows[i][j] for i in range(7))%3
                w += v!=0
            ctr[w]+=1
        assert dict(sorted(ctr.items()))=={int(k):v for k,v in CERT["ternary_source_enumerator"].items()}

for p in CERT["verification_primes"]: check(p)
print("VERIFY_OK")
