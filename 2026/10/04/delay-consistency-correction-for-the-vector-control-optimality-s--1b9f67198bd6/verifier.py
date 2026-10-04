#!/usr/bin/env python3
from fractions import Fraction

VARS = ('eps','u','rho','b','e','x','dx','y','dy')
IDX = {v:i for i,v in enumerate(VARS)}
ZERO = (0,)*len(VARS)

class P:
    def __init__(self, terms=None):
        self.t = {m:Fraction(c) for m,c in (terms or {}).items() if c}
    @staticmethod
    def c(q): return P({ZERO: Fraction(q)})
    @staticmethod
    def v(name):
        m=list(ZERO); m[IDX[name]]=1
        return P({tuple(m):Fraction(1)})
    def __add__(self,o):
        if not isinstance(o,P): o=P.c(o)
        d=dict(self.t)
        for m,c in o.t.items():
            d[m]=d.get(m,Fraction(0))+c
            if not d[m]: d.pop(m)
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({m:-c for m,c in self.t.items()})
    def __sub__(self,o): return self+(-o)
    def __rsub__(self,o): return P.c(o)-self
    def __mul__(self,o):
        if not isinstance(o,P): o=P.c(o)
        d={}
        for m,c in self.t.items():
            for n,k in o.t.items():
                z=tuple(a+b for a,b in zip(m,n))
                d[z]=d.get(z,Fraction(0))+c*k
        return P(d)
    __rmul__=__mul__
    def coeff_eps(self,k):
        d={}
        for m,c in self.t.items():
            if m[IDX['eps']]==k:
                z=list(m); z[IDX['eps']]=0
                d[tuple(z)]=d.get(tuple(z),Fraction(0))+c
        return P(d)
    def __eq__(self,o):
        if not isinstance(o,P): o=P.c(o)
        return self.t==o.t

one=P.c(1)
eps,u,rho,b,e,x,dx,y,dy=[P.v(v) for v in VARS]
perturbed=(one-u-eps*rho)*b*e*(x+eps*dx)*(y+eps*dy)
actual=perturbed.coeff_eps(1)
expected=b*e*((one-u)*(dx*y+x*dy)-rho*x*y)
assert actual==expected
# The coefficient must retain the survival factor e and both state variations.
assert any(m[IDX['e']]==1 and m[IDX['dx']]==1 for m in actual.t)
assert any(m[IDX['e']]==1 and m[IDX['dy']]==1 for m in actual.t)
assert any(m[IDX['e']]==1 and m[IDX['rho']]==1 for m in actual.t)
print('VERIFY_OK')
