#!/usr/bin/env python3
"""Exact interval checks for cyclic stepsizes of an adaptive proximal gradient rule."""
from fractions import Fraction as F
from math import isqrt

PREC = 10**15

class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __repr__(self):return f'[{float(self.lo):.14g},{float(self.hi):.14g}]'
    def __add__(self,x):
        x=asI(x);return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,x):return self+-asI(x)
    def __rsub__(self,x):return asI(x)+-self
    def __mul__(self,x):
        x=asI(x);z=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)];return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=asI(x);assert x.lo*x.hi>0
        return self*I(1/x.hi,1/x.lo)
    def __rtruediv__(self,x):return asI(x)/self
    def __pow__(self,k):
        assert k>=0 and isinstance(k,int)
        if k==0:return I(1)
        if k%2==0 and self.lo<0<self.hi:return I(0,max(abs(self.lo),abs(self.hi))**k)
        z=[self.lo**k,self.hi**k];return I(min(z),max(z))
    def sqrt(self):
        assert self.lo>=0
        def lower(q):return F(isqrt((q.numerator*PREC**2)//q.denominator),PREC)
        a,b=lower(self.lo),lower(self.hi)
        return I(a,b+F(1,PREC))

def asI(x):return x if isinstance(x,I) else I(x)
def dec(x):return F(str(x))

def strictly(x,y):
    x=asI(x);y=asI(y);return x.hi<y.lo

# Defining ratio for growth/growth/cap period 3.
p3=lambda r: r**2*(r-1)**2*(r+1)**3-1
rlo=F(124040630,10**8); rhi=F(124040631,10**8)
assert p3(rlo)<0<p3(rhi)
r=I(rlo,rhi)
s=(1+r).sqrt(); R=r*s
a=(1+(1+R**2).sqrt())/(2*R)
b=r*a; c=R*a
print('three ratio/steps',r,a,b,c)
assert strictly(I(0),a) and strictly(a,I(1))
assert strictly(I(1),b) and strictly(b,c)
# Growth selected at b: F(b)>c. Squares used to bound exact F(b).
assert strictly(4*c**2*(b-1),b)
# Cap at c: G(b,c)>c>a, obvious because G(b,c)>c and c>a.
assert strictly(a,c) and strictly(c,I(2))
# Principal multiplier of T^3 at (c,a), calculated from chain rule.
def DG(u,v):
    q=v/u; s=(1+q).sqrt()
    return [[I(0),I(1)],[-q**2/(2*s),(2+3*q)/(2*s)]]
def DC(u,v,fv):return [[I(0),I(1)],[I(0), -fv/(2*v*(v-1))]]
def mul(A,B):return [[sum((A[i][k]*B[k][j] for k in range(2)),I(0)) for j in range(2)] for i in range(2)]
J3=mul(DC(b,c,a),mul(DG(a,b),DG(c,a)))
mu3=J3[0][0]+J3[1][1]
print('3-cycle nonzero multiplier bound',mu3)
assert strictly(mu3,I(-1))
# Derivative of each cap branch vanishes in first input, so det(J3)=0 exactly.
# The quadratic reduction gives the primal contraction.
q3=(1-a)*(1-b)*(1-c)
print('primal 3-factor interval',q3)
assert strictly(I(0),q3) and strictly(q3,I(1))
# Defining plastic ratio for growth/cap period 2.
p2=lambda x:x**3-x-1
rlo=F(132471795,10**8);rhi=F(132471796,10**8)
# actual plastic constant ~1.32471795724
assert p2(rlo)<0<p2(rhi)
r2=I(rlo,rhi)
a2=(1+(1+r2**2).sqrt())/(2*r2);b2=r2*a2
print('two ratio/steps',r2,a2,b2)
assert strictly(I(1),a2) and strictly(a2,b2) and strictly(b2,I(2))
# growth branch wins at a2: F(a2)>b2
assert strictly(4*b2**2*(a2-1),a2)
# cap branch wins at b2: G(a2,b2)>b2>a2
assert strictly(a2,b2)
J2=mul(DC(a2,b2,a2),DG(b2,a2));mu2=J2[0][0]+J2[1][1]
q2=(1-a2)*(1-b2)
print('two nonzero multiplier bound',mu2, 'primal2',q2)
assert strictly(mu2,I(-1))
assert strictly(I(0),q2) and strictly(q2,I(1))
print('PASS: rational root isolation, active branches, period-2/3 repulsion and primal contraction')
