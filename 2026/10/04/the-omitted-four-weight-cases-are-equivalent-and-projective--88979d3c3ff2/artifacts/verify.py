#!/usr/bin/env python3
import collections, math
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def enum_formula(p,m):
    q=p**m; s=p**(m-1)
    w1=p**(2*m-2)*(p-1)
    w2=p**(m-1)*(p**m-p**(m-1)-1)
    w3=p**(m-1)*(p**m-p**(m-1)-2)
    w4=p**(m-1)*(p**m-1)
    A1=(q-1)*(s+1+q*(p-1)//2)
    A2=(q-1)*(p-1)*(2*s+1)
    A3=(q-1)*s*(p-1)*(p-2)//2
    A4=p-1
    return collections.Counter({0:1,w1:A1,w2:A2,w3:A3,w4:A4})

def dual_a3(p,m):
    s=p**(m-1)
    return s*(p-1)*(p-2)*(s-1)*(s+1)*(p**m-1)//6

for p in (3,5,7):
    for m in (2,3,4):
        E=enum_formula(p,m)
        assert sum(E.values())==p**(2*m+1)
        actual=min(w for w in E if w)
        assert actual==p**(m-1)*(p**m-p**(m-1)-2)
        printed=p**(m-2)*(p**(m+1)-2*p**m-p+2)
        assert actual-printed==p**(m-2)*(p**m-p-2)>0
        assert dual_a3(p,m)>0

class Fp2:
    def __init__(self,p,nu): self.p=p; self.nu=nu
    def add(self,x,y): return ((x[0]+y[0])%self.p,(x[1]+y[1])%self.p)
    def neg(self,x): return ((-x[0])%self.p,(-x[1])%self.p)
    def sub(self,x,y): return self.add(x,self.neg(y))
    def mul(self,x,y):
        a,b=x; c,d=y; p=self.p
        return ((a*c+self.nu*b*d)%p,(a*d+b*c)%p)
    def power(self,x,e):
        r=(1,0)
        while e:
            if e&1:r=self.mul(r,x)
            x=self.mul(x,x);e>>=1
        return r
    def trace(self,x):
        z=self.add(x,self.power(x,self.p))
        assert z[1]==0
        return z[0]
    def elems(self): return [(a,b) for a in range(self.p) for b in range(self.p)]

def direct(p,nu,beta,gamma):
    F=Fp2(p,nu); E=F.elems(); gp=(gamma+F.trace(beta))%p
    assert gp!=0
    coords=[]
    for X in E:
        if X==(0,0): continue
        for y in E:
            if F.trace(F.add(F.mul(X,y),X))==gp:
                x=F.sub(X,beta)
                lhs=F.add(F.add(F.mul(x,y),F.mul(beta,y)),x)
                assert F.trace(lhs)==gamma
                coords.append((X,x,y))
    assert len(coords)==p*(p*p-1)
    A=collections.Counter(); B=collections.Counter()
    for a in E:
        for b in E:
            tr_ab=F.trace(F.mul(a,beta))
            for c in range(p):
                cp=(c-tr_ab)%p
                wa=wb=0
                for X,x,y in coords:
                    va=(F.trace(F.add(F.mul(a,x),F.mul(b,y)))+c)%p
                    vb=(F.trace(F.add(F.mul(a,X),F.mul(b,y)))+cp)%p
                    assert va==vb
                    wa+=va!=0; wb+=vb!=0
                A[wa]+=1; B[wb]+=1
    assert A==B==enum_formula(p,2)
    return A

assert direct(3,2,(1,1),2)==enum_formula(3,2)
assert direct(5,2,(1,1),1)==enum_formula(5,2)

source_checks={
    "p3_m2":{str(k):v for k,v in enum_formula(3,2).items()},
    "p3_m3":{str(k):v for k,v in enum_formula(3,3).items()},
    "p3_m4":{str(k):v for k,v in enum_formula(3,4).items()},
}
assert source_checks==cert["source_table_III_checks"]

def kraw(q,n,j,i):
    return sum(((-1)**s)*(q-1)**(j-s)*math.comb(i,s)*math.comb(n-i,j-s)
               for s in range(max(0,j-(n-i)),min(j,i)+1))

for p,m in ((3,2),(3,3),(5,2),(7,2)):
    E=enum_formula(p,m); n=p**(m-1)*(p**m-1); size=p**(2*m+1)
    A=[E.get(i,0) for i in range(n+1)]
    dual=[sum(A[i]*kraw(p,n,j,i) for i in range(n+1))//size for j in range(4)]
    assert dual[0]==1 and dual[1]==0 and dual[2]==0
    assert dual[3]==dual_a3(p,m)

print("VERIFY_OK")
