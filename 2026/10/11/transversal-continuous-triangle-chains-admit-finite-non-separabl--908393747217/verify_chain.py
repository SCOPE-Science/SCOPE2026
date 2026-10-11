#!/usr/bin/env python3
"""Exact outward-rounded fixed-point certificate for a non-separable triangle-chain bound.

All scalar interval arithmetic uses integers on the 10^40 grid, directed rounding,
and elementary Taylor enclosures for the exponential. No binary floating point is used.
"""
from fractions import Fraction
from math import factorial

Q=10**40

def floor_div(a,b):
    assert b>0
    return a//b

def ceil_div(a,b):
    assert b>0
    return -((-a)//b)

class I:
    def __init__(self, lo, hi=None):
        self.lo=int(lo);self.hi=int(hi if hi is not None else lo)
        assert self.lo<=self.hi
    @classmethod
    def frac(cls,x):
        x=Fraction(x)
        return cls(floor_div(x.numerator*Q,x.denominator),ceil_div(x.numerator*Q,x.denominator))
    def __add__(self,o):
        o=toI(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-toI(o)
    def __rsub__(self,o):return toI(o)+-self
    def __mul__(self,o):
        o=toI(o);q=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(floor_div(min(q),Q),ceil_div(max(q),Q))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=toI(o);assert not (o.lo<=0<=o.hi)
        vals=[Fraction(a*Q,b) for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(min(floor_div(x.numerator,x.denominator) for x in vals),max(ceil_div(x.numerator,x.denominator) for x in vals))
    def __rtruediv__(self,o):return toI(o)/self
    def upper(self):return self.hi/Q
    def lower(self):return self.lo/Q
    def __str__(self):
        return f'[{self.lo/Q:.18g},{self.hi/Q:.18g}]'

def toI(x):
    return x if isinstance(x,I) else I.frac(Fraction(x))

def exp_i(x):
    x=toI(x)
    assert -Q < x.lo and x.hi < Q
    y=toI(1); out=toI(1)
    for j in range(1,19):
        y=y*x/j
        out=out+y
    # Absolute Taylor remainder <= 3 |x|^19/19! < 3/19! for |x|<1.
    err=toI(Fraction(3,factorial(19)))
    return I(out.lo-err.hi,out.hi+err.hi)

d=I.frac(Fraction(415868,1000000))
tau=I.frac(Fraction(67376,100000))
a=I.frac(Fraction(1110182,1000000))
b=I.frac(Fraction(1110185,1000000))
den=1+tau+tau*tau
v=(1-d+d*tau)/den
u=tau*v
k=(d+(1-d)*tau*tau)/den
D=v-d
Ef=k*(v-u)+D*(v-k)
assert D.hi<0 and k.lo>0 and (k+D).lo>0

def continuum(s):
    c=v-((v-u)*d/v)*exp_i(-(k+D)*s)
    E0=d*(k+D)-k*c
    return c,E0-d*Ef/v*exp_i(-k*s),E0
ca,fa,e0a=continuum(a)
cb,fb,e0b=continuum(b)
assert fa.hi<0, (fa,fb)
assert fb.lo>0, (fa,fb)
span=I(a.lo,b.hi)
Acoef=(v-u)*d/v
Fp= -k*Acoef*(k+D)*exp_i(-(k+D)*span)+(d*Ef*k/v)*exp_i(-k*span)
assert Fp.lo>0, Fp
assert ca.lo>0 and cb.hi<v.lo
assert (1-u-cb-d).lo>0 and e0b.lo>0
assert 0<u.lo and u.hi<v.lo and v.hi<d.lo and d.hi<(1-u).lo
assert (u+v-d).lo>0 and (v-k).lo>0

# Uniform enclosure for c at the unknown continuous root, then R0,Y0.
cr=I(ca.lo,cb.hi)
e0=d*(k+D)-k*cr
assert e0.lo>0
R0=(v-cr)/e0
Y0=d/e0
assert R0.hi<Y0.lo
# R/Y increases with time, but is always below 1; hence E(t) is strictly increasing.
assert ((v-ca)/d*exp_i((k+D)*b)).hi<Q

def E(z):
    R=R0*exp_i(D*z)
    Y=Y0*exp_i(-k*z)
    K=k*R+D*Y-1
    assert K.hi<0, (z,K)
    ei=D*k/K
    assert ei.lo>0
    return ei
N=16384
# Upper rectangle sum: monotonic E(t), hence integral to s <= integral to b
# <= b/N sum_{j=1}^N E(jb/N), for every root s in (a,b).
rect=toI(0)
for j in range(1,N+1):
    rect=rect+E(b*j/N)
I_upper=(b/N*rect).hi
# Worst-case scale uses lower c and upper integral.
S_upper=(3*(1-ca-d)).hi+3*I_upper
threshold=I.frac(Fraction(10000,10633)) # 1/1.0633 = 10000/10632
displayed=I.frac(Fraction(940465236,10**9))
assert S_upper<displayed.lo, (S_upper/Q,displayed.lo/Q)
assert displayed.hi<threshold.lo
assert S_upper<threshold.lo, (S_upper/Q,threshold.lo/Q)

print('VERIFY_OK')
print('F(a) enclosure',fa)
print('F(b) enclosure',fb)
print('Fprime enclosure',Fp)
print('c interval',cr)
print('initial E0 interval',e0)
print('integral upper',f'{I_upper/Q:.15f}')
print('S_upper',f'{S_upper/Q:.15f}')
print('1/1.0633 lower',f'{threshold.lo/Q:.15f}')
print('margin',f'{(threshold.lo-S_upper)/Q:.15f}')
