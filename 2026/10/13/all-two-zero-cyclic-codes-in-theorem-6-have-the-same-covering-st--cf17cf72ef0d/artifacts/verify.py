#!/usr/bin/env python3
import itertools, collections, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))

def nonsquare(q):
    sq={x*x%q for x in range(1,q)}
    return next(d for d in range(2,q) if d not in sq)

class FQ2:
    def __init__(self,q):
        self.q=q; self.d=nonsquare(q); self.one=(1,0); self.zero=(0,0)
        self.gamma=self._primitive()
    def add(self,x,y): return ((x[0]+y[0])%self.q,(x[1]+y[1])%self.q)
    def mul(self,x,y):
        a,b=x; c,d=y; q=self.q
        return ((a*c+b*d*self.d)%q,(a*d+b*c)%q)
    def pow(self,x,n):
        r=self.one; y=x
        while n:
            if n&1:r=self.mul(r,y)
            y=self.mul(y,y); n//=2
        return r
    def trace(self,x): return (2*x[0])%self.q
    def _primitive(self):
        n=self.q*self.q-1; z=n; fac=[]; p=2
        while p*p<=z:
            if z%p==0:
                fac.append(p)
                while z%p==0:z//=p
            p+=1
        if z>1:fac.append(z)
        for a in range(self.q):
            for b in range(self.q):
                x=(a,b)
                if x==(0,0):continue
                if all(self.pow(x,n//p)!=self.one for p in fac):return x
        raise AssertionError

def rank_mod(rows,q):
    M=[list(r) for r in rows]
    rr=0
    if not M:return 0
    for c in range(len(M[0])):
        p=next((i for i in range(rr,len(M)) if M[i][c]%q),None)
        if p is None:continue
        M[rr],M[p]=M[p],M[rr]
        inv=pow(M[rr][c]%q,-1,q)
        M[rr]=[(inv*x)%q for x in M[rr]]
        for i in range(len(M)):
            if i!=rr and M[i][c]%q:
                f=M[i][c]%q
                M[i]=[(M[i][j]-f*M[rr][j])%q for j in range(len(M[0]))]
        rr+=1
        if rr==len(M[0]):break
    return rr

def generator(q,e1,e2):
    F=FQ2(q); n=q*q-1; gp=[F.one]
    for _ in range(1,n):gp.append(F.mul(gp[-1],F.gamma))
    G=[]
    for i in range(n):
        xa=gp[((q-1)*e1*i)%n]; xb=gp[(e2*i)%n]
        # trace-pairing coordinates in message basis (a0,a1,b0,b1)
        G.append(((2*xa[0])%q,(2*F.d*xa[1])%q,(2*xb[0])%q,(2*F.d*xb[1])%q))
    assert rank_mod(G,q)==4
    return G

def projective_messages(q):
    for first in range(4):
        for tail in itertools.product(range(q),repeat=3-first):
            yield (0,)*first+(1,)+tail

def profile(q,e1,e2):
    G=generator(q,e1,e2); n=len(G)
    wd=collections.Counter(); minimal=collections.Counter()
    proj=0
    for u in projective_messages(q):
        zero=[]
        for g in G:
            if sum(u[j]*g[j] for j in range(4))%q==0: zero.append(g)
        w=n-len(zero); wd[w]+=1; proj+=1
        if rank_mod(zero,q)==3:minimal[w]+=1
    assert proj==(q**4-1)//(q-1)
    return wd,minimal

def expected_projective_wd(q):
    counts={
      (q-1)**2: ((q*q-1)*(2*q-1)//2)//(q-1),
      q*(q-1)-1: ((q*q-1)**2//2)//(q-1),
      q*(q-1): (q*q-1)//(q-1),
      q*(q-1)+1: (((q*q-1)*(q-1)**2)//2)//(q-1),
      q*q-1: ((q*q-1)//2)//(q-1),
    }
    return counts

for qs,pairs in CERT['tested_pairs'].items():
    q=int(qs)
    for e1,e2 in pairs:
        wd,mins=profile(q,e1,e2)
        assert dict(sorted(wd.items()))==dict(sorted(expected_projective_wd(q).items()))
        if q==3:
            assert set(mins)=={4,5}
        else:
            assert set(mins)=={(q-1)**2,q*(q-1)-1,q*(q-1)+1}
            predicted=((q*q-1)*(2*q*q-1)//2)//(q-1)
            assert sum(mins.values())==predicted

print('VERIFY_OK')
