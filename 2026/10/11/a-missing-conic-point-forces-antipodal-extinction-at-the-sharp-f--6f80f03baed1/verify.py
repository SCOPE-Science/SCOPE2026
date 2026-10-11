#!/usr/bin/env python3
"""Exact finite-field fourth-moment checks for punctured anisotropic conics.
Public, reproducible arithmetic checks; finite sampling is not an infinite proof.
"""
from collections import defaultdict
import random

class F:
    def __init__(self,p,nu=None):
        self.p=p; self.nu=nu; self.q=p if nu is None else p*p
    def xy(self,z):
        return (z,0) if self.nu is None else (z%self.p,z//self.p)
    def enc(self,x,y):
        return x%self.p if self.nu is None else (x%self.p)+self.p*(y%self.p)
    def add(self,a,b):
        x,y=self.xy(a);u,v=self.xy(b);return self.enc(x+u,y+v)
    def neg(self,a):
        x,y=self.xy(a);return self.enc(-x,-y)
    def mul(self,a,b):
        x,y=self.xy(a);u,v=self.xy(b);return self.enc(x*u+(self.nu or 0)*y*v,x*v+y*u)
    def sq(self,a):return self.mul(a,a)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def nonsquare(self):
        squares={self.sq(i) for i in range(self.q)}
        return next(i for i in range(1,self.q) if i not in squares)

def cadd(a,b):return (a[0]+b[0],a[1]+b[1])
def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def abs2(a):return a[0]*a[0]+a[1]*a[1]

def moment(C,f,F):
    coeff=defaultdict(lambda:(0,0))
    for (x,y),a in zip(C,f):
        for (u,v),b in zip(C,f):
            k=(F.add(x,u),F.add(y,v))
            coeff[k]=cadd(coeff[k],cmul(a,b))
    return sum(abs2(v) for v in coeff.values())

def check(p,nu=None,trials=100):
    fld=F(p,nu)
    delta=fld.nonsquare()
    C=[(x,y) for x in range(fld.q) for y in range(fld.q) if fld.sub(fld.sq(x),fld.mul(delta,fld.sq(y)))==1]
    assert len(C)==fld.q+1, (p,nu,delta,len(C))
    # Delete (1,0), retain its opposite; all other points split into pairs.
    w=(1,0);op=(fld.neg(1),0)
    A=[z for z in C if z!=w]
    assert len(A)==fld.q and op in A
    pairs=[]; unseen=set(A)-{op}
    while unseen:
        x=next(iter(unseen)); y=(fld.neg(x[0]),fld.neg(x[1]))
        assert y in unseen and x!=y
        unseen.remove(x);unseen.remove(y);pairs.append((x,y))
    k=len(pairs);assert k==(fld.q-1)//2
    # Ordered 2-sums: unique unordered representation away from 0.
    seen={}
    for i,x in enumerate(C):
        for j in range(i,len(C)):
            y=C[j]; s=(fld.add(x[0],y[0]),fld.add(x[1],y[1]))
            if s!=(0,0):
                assert s not in seen,(fld.q,s,seen.get(s), (i,j))
                seen[s]=(i,j)
    # For q>=5 the unique optimizer avoids the unmatched antipodal point.
    if fld.q>=5:
        f={z:(0,0) for z in A}
        for j,(x,y) in enumerate(pairs):
            phase=((1,0),(0,1),(-1,0),(0,-1))[j%4]
            f[x]=phase; f[y]=(phase[0],-phase[1])
        values=[f[z] for z in A]
        S=sum(abs2(z) for z in values)
        E=moment(A,values,fld)
        assert S==fld.q-1 and E==3*(fld.q-1)*(fld.q-2),(fld.q,S,E)
    else:
        values=[(1,0)]*fld.q
        S=fld.q;E=moment(A,values,fld)
        assert E==15 and S==3,(fld.q,S,E)
    # Independent exact-arithmetic random search, no floating point.
    rng=random.Random(38117+fld.q)
    for i in range(trials):
        values=[(rng.randint(-2,2),rng.randint(-2,2)) for _ in A]
        S=sum(abs2(z) for z in values)
        E=moment(A,values,fld)
        assert (fld.q-1)*E<=3*(fld.q-2)*S*S if fld.q>=5 else 3*E<=5*S*S,(fld.q,i,S,E)
    return (fld.q,delta,len(C),len(A),k,trials)

if __name__=='__main__':
    cases=[(3,None),(5,None),(7,None),(11,None),(13,None),(3,2),(5,2)]
    for p,nu in cases:
        print('PASS q,delta,conic_size,punctured_size,pairs,trials:',check(p,nu))
