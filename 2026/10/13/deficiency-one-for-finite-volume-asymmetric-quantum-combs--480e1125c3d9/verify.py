#!/usr/bin/env python3
from fractions import Fraction as F

class QI:
    __slots__ = ('r','i')
    def __init__(self,r=0,i=0): self.r,self.i=F(r),F(i)
    def __add__(self,o): o=q(o); return QI(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return QI(-self.r,-self.i)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return QI(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def inv(self):
        d=self.r*self.r+self.i*self.i
        return QI(self.r/d,-self.i/d)
    def __truediv__(self,o): return self*q(o).inv()
    def __rtruediv__(self,o): return q(o)/self
    def __eq__(self,o): o=q(o); return self.r==o.r and self.i==o.i
    def abs2(self): return self.r*self.r+self.i*self.i

def q(x): return x if isinstance(x,QI) else QI(x,0)

I=QI(0,1)

def check(z):
    # Exact rational sample: asymmetric teeth and summable geometric edge lengths.
    N=12
    ell=[None]+[F(1,2**(k+2)) for k in range(1,N+1)]
    ap=[None]+[F(1,3*2**k) for k in range(1,N+1)]
    am=[None]+[F(1,5*3**k) for k in range(1,N+1)]
    mc=[None]*(N+1)
    for k in range(1,N+1):
        left=F(0) if k==1 else ell[k-1]
        mc[k]=left+ell[k]+ap[k]+am[k]
    f=[None]*(N+2); p=[None]*(N+1)
    f[1]=QI(1)
    qk=[None]*(N+1)
    for k in range(1,N+1):
        qk[k]=q(mc[k]) + ap[k]/(q(1)-z*ap[k]*ap[k]) + am[k]/(q(1)-z*am[k]*am[k])
    p[1]=z*qk[1]*f[1]
    f[2]=f[1]-ell[1]*p[1]
    for k in range(2,N+1):
        p[k]=p[k-1]+z*qk[k]*f[k]
        f[k+1]=f[k]-ell[k]*p[k]

    leaf_checks=0; spine_checks=0
    for k in range(1,N+1):
        for a in (ap[k],am[k]):
            u=f[k]/(q(1)-z*a*a)
            resid=(u-f[k])/(a*a)-z*u
            assert resid==QI(0)
            leaf_checks += 1
        left=QI(0) if k==1 else (f[k]-f[k-1])/ell[k-1]
        right=(f[k]-f[k+1])/ell[k]
        up=f[k]/(q(1)-z*ap[k]*ap[k])
        dn=f[k]/(q(1)-z*am[k]*am[k])
        tooth=(f[k]-up)/ap[k]+(f[k]-dn)/am[k]
        resid=left+right+tooth-z*mc[k]*f[k]
        assert resid==QI(0)
        spine_checks += 1
    # The exact recurrence is nontrivial and its finite state remains finite.
    assert f[1]!=QI(0)
    mx=max(float(v.abs2()) for v in f[1:N+2])
    return leaf_checks,spine_checks,mx

tot_leaf=tot_spine=0; worst=0.0
for z in (I,-I):
    a,b,c=check(z); tot_leaf+=a; tot_spine+=b; worst=max(worst,c)
print(f"VERIFY_OK exact_leaf={tot_leaf} exact_spine={tot_spine} max_state_abs2={worst:.6g}")
