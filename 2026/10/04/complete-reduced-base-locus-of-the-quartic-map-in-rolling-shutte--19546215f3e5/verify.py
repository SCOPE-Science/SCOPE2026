#!/usr/bin/env python3
# Exact standard-library verifier for the displayed quartic map in Example 21.
from collections import defaultdict

class P:
    def __init__(self, n, terms=None):
        self.n=n
        self.t={m:int(c) for m,c in (terms or {}).items() if c}
    @staticmethod
    def one(n): return P(n,{(0,)*n:1})
    @staticmethod
    def var(n,i):
        e=[0]*n; e[i]=1
        return P(n,{tuple(e):1})
    def __add__(self,o):
        if isinstance(o,int): o=P(self.n,{(0,)*self.n:o})
        d=defaultdict(int,self.t)
        for m,c in o.t.items(): d[m]+=c
        return P(self.n,d)
    __radd__=__add__
    def __neg__(self): return P(self.n,{m:-c for m,c in self.t.items()})
    def __sub__(self,o): return self+(-o)
    def __rsub__(self,o): return o+(-self)
    def __mul__(self,o):
        if isinstance(o,int): return P(self.n,{m:c*o for m,c in self.t.items()})
        d=defaultdict(int)
        for a,ca in self.t.items():
            for b,cb in o.t.items(): d[tuple(x+y for x,y in zip(a,b))]+=ca*cb
        return P(self.n,d)
    __rmul__=__mul__
    def __pow__(self,k):
        r=P.one(self.n); b=self
        while k:
            if k&1: r=r*b
            b=b*b; k//=2
        return r
    def __eq__(self,o):
        if isinstance(o,int): o=P(self.n,{(0,)*self.n:o})
        return self.t==o.t
    def sub(self, imgs):
        n2=imgs[0].n
        out=P(n2)
        for mon,c in self.t.items():
            z=P(n2,{(0,)*n2:c})
            for i,e in enumerate(mon): z=z*(imgs[i]**e)
            out=out+z
        return out
    def min_weight(self, inds):
        return min(sum(m[i] for i in inds) for m,c in self.t.items() if c)

# Ring Z[x1,x2,x3,x0]
x1,x2,x3,x0=[P.var(4,i) for i in range(4)]
d=x0-x3
q=2*x1*x2+x3**2-x0**2
F0=-2*x1**2*x2*x3-x1*x3**3+2*x1**2*x2*x0+x1*x3**2*x0+x1*x3*x0**2-x1*x0**3
F1=-2*x1**3*x3-2*x1*x3**3+x2*x3**3+3*x1*x3**2*x0-3*x2*x3**2*x0+3*x2*x3*x0**2-x1*x0**3-x2*x0**3
F2=2*x1*x2*x3**2+x3**4-4*x1*x2*x3*x0-2*x3**3*x0+2*x1*x2*x0**2+2*x3*x0**3-x0**4
assert F0 == x1*d*q
assert F2 == d**2*q
assert F1.sub([x1,x2,x0,x0]) == -2*x0*x1**3

# Segre chart variables Z[s,t,u,v]
s,t,u,v=[P.var(4,i) for i in range(4)]
psi=[2*s*u,2*t*v,t*u-2*s*v,t*u+2*s*v]
h=2*s*u*v-t*u**2-4*t*v**2
assert q.sub(psi) == 0
assert F1.sub(psi) == 16*s**3*(u**2+2*v**2)*h
q1=x1*x3-x2*x3+x2*x0
q2=2*x2**2+x3**2+x3*x0
q3=2*x1*x2+x3**2-x0**2
assert q1.sub(psi) == -2*s*h
assert q2.sub(psi) == -2*t*h
assert q3.sub(psi) == 0

# Ring Z[x1,x2,d,x0], with x3=x0-d.
a,b,dd,z=[P.var(4,i) for i in range(4)]
imgs=[a,b,z-dd,z]
F0k,F1k,F2k=[f.sub(imgs) for f in (F0,F1,F2)]
expected=2*dd**3*a-dd**3*b-3*dd**2*z*a+2*dd*a**3-2*z*a**3
assert F1k == expected
weights=[f.min_weight((0,2)) for f in (F0k,F1k,F2k)]
assert min(weights)==3 and all(w>=3 for w in weights)
print('VERIFY_OK')
