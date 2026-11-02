#!/usr/bin/env python3
"""Exact rational interval checks of two adaPGM stepsize cycles and unstable return multipliers."""
from fractions import Fraction as F
from math import isqrt

PREC = 10**15
class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __repr__(self):return f'[{float(self.lo):.14g},{float(self.hi):.14g}]'
    def __add__(self,x):
        x=asI(x);return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,x):return self+-asI(x)
    def __rsub__(self,x):return asI(x)+-self
    def __mul__(self,x):
        x=asI(x);a=[u*v for u in (self.lo,self.hi) for v in (x.lo,x.hi)]
        return I(min(a),max(a))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=asI(x);assert x.lo*x.hi>0
        return self*I(1/x.hi,1/x.lo)
    def __rtruediv__(self,x):return asI(x)/self
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        if not k:return I(1)
        if k%2==0 and self.lo<0<self.hi:return I(0,max(abs(self.lo),abs(self.hi))**k)
        a=[self.lo**k,self.hi**k];return I(min(a),max(a))
    def sqrt(self):
        assert self.lo>=0
        def down(q):return F(isqrt((q.numerator*PREC**2)//q.denominator),PREC)
        return I(down(self.lo),down(self.hi)+F(1,PREC))
def asI(x):return x if isinstance(x,I) else I(x)
def lt(x,y):
    x=asI(x);y=asI(y);return x.hi<y.lo

def DG(u,v):
    q=v/u;s=(1+q).sqrt()
    return [[I(0),I(1)],[-q**2/(2*s),(2+3*q)/(2*s)]]
def DC(u,v,fv):return [[I(0),I(1)],[I(0),-fv/(2*v*(v-1))]]
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(2)),I(0)) for j in range(2)] for i in range(2)]
def trace(A):return A[0][0]+A[1][1]

# Strictly increasing ratio equations guarantee unique roots above one.
p2=lambda r:r**3-r-1
lo2,hi2=F(132471795,10**8),F(132471796,10**8)
assert p2(lo2)<0<p2(hi2)
r=I(lo2,hi2);a=(1+(1+r**2).sqrt())/(2*r);b=r*a
assert lt(I(1),a) and lt(a,b) and lt(b,I(2))
assert lt(4*b**2*(a-1),a) # F(a)>b on growth
J2=mm(DC(a,b,a),DG(b,a));mu2=trace(J2)
assert lt(mu2,I(-1))
assert lt(I(0),(1-a)*(1-b)) and lt((1-a)*(1-b),I(1))

p3=lambda r:r**2*(r-1)**2*(r+1)**3-1
lo3,hi3=F(124040630,10**8),F(124040631,10**8)
assert p3(lo3)<0<p3(hi3)
r=I(lo3,hi3);R=r*(1+r).sqrt();a=(1+(1+R**2).sqrt())/(2*R);b=r*a;c=R*a
assert lt(I(0),a) and lt(a,I(1)) and lt(I(1),b) and lt(b,c) and lt(c,I(2))
assert lt(4*c**2*(b-1),b) # F(b)>c on growth
J3=mm(DC(b,c,a),mm(DG(a,b),DG(c,a)));mu3=trace(J3)
assert lt(mu3,I(-1))
assert lt(I(0),(1-a)*(1-b)*(1-c)) and lt((1-a)*(1-b)*(1-c),I(1))
# A cap Jacobian has determinant zero, so each return spectrum is {0,mu}.
print('PASS: exact root intervals, strict branches, one zero and one unstable multiplier, primal contraction')
print('nonzero multipliers:',mu2,mu3)
