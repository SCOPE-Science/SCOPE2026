#!/usr/bin/env python3
"""Exact rational interval proof of the strict conditional-brightness order."""
from fractions import Fraction as F
from math import factorial

def I(lo,hi=None):return(F(str(lo)),F(str(lo if hi is None else hi)))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    v=[x*y for x in a for y in b];return(min(v),max(v))
def inv(a):
    assert a[0]>0
    return (1/a[1],1/a[0])
def div(a,b):return mul(a,inv(b))
def pos(a):assert a[0]>0,(float(a[0]),float(a[1]));return a

def cos_bounds(x):
    # Taylor theorem: the absolute remainder after degree 26 is at most x^27/27!.
    # More sharply use degree 26 and standard |cos^(27)| <= 1 bound.
    m=x
    s=sum(((-1)**k*m**(2*k)/factorial(2*k) for k in range(14)),F(0))
    e=abs(m)**27/F(factorial(27))
    return (s-e,s+e)
def prove_acos(lo,hi,target):
    # cos decreasing on [0,pi]; hence cos(lo)>target>cos(hi).
    assert 0<lo<hi< F(3.2)
    c0=cos_bounds(lo);c1=cos_bounds(hi)
    assert c0[0]>target[1],('low',float(c0[0]),float(target[1]))
    assert c1[1]<target[0],('high',float(c1[1]),float(target[0]))

root5=I('2.2360679774997','2.2360679775000')
root2=I('1.414213562372','1.414213562374')
assert root5[0]**2<5<root5[1]**2
assert root2[0]**2<2<root2[1]**2
al=I('1.23095941733','1.23095941736')
be=I('0.72972765621','0.72972765625')
h=I('0.38813951535','0.38813951540')
p=I('0.27091852043','0.27091852049')
prove_acos(*al,I(F(1,3)))
prove_acos(*be,div(root5,I(3)))
prove_acos(*h,div(add(I(3),root5),mul(I(4),root2)))
prove_acos(*p,div(add(I(1),mul(I(3),root5)),I(8)))
# Machin's exact identity pi = 16 atan(1/5)-4 atan(1/239)
def atan_bounds(x,terms=24):
    z=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    e=x**(2*terms+1)/F(2*terms+1)
    return (z-e,z+e)
pi=sub(mul(I(16),atan_bounds(F(1,5))),mul(I(4),atan_bounds(F(1,239))))
assert pi[0]>F('3.14159265358') and pi[1]<F('3.14159265360')
# Probabilities for N in {6,8,10}.
P6=div(mul(I(5),sub(mul(I(2),pi),mul(I(3),add(al,be)))),pi)
P8=div(mul(I(15),sub(add(mul(I(2),al),be),pi)),pi)
P10=div(mul(I(3),sub(mul(I(2),pi),mul(I(5),al))),pi)
# Mixed first moments of W=area/facet_area.
M6=div(mul(mul(I(5),add(I(3),root5)),h),pi)
M8=div(mul(I(5),add(mul(add(I(1),root5),p),mul(I(2),mul(sub(I(3),root5),h)))),mul(I(2),pi))
M10=div(mul(I(5),mul(sub(I(5),root5),p)),mul(I(2),pi))
for x in (P6,P8,P10,M6,M8,M10):pos(x)
assert sub(add(add(P6,P8),P10),I(1))[0]<0
# Cross multiply, denominators strictly positive
D68=pos(sub(mul(M6,P8),mul(M8,P6)))
D810=pos(sub(mul(M8,P10),mul(M10,P8)))
EN=add(add(mul(I(6),P6),mul(I(8),P8)),mul(I(10),P10))
ENW=add(add(mul(I(6),M6),mul(I(8),M8)),mul(I(10),M10))
cov=sub(ENW,mul(I(5),EN))
assert cov[1]<0
print('RATIONAL_ANGLE_BRACKETS_AND_PI_OK')
print('STRICT_CONDITIONAL_MEAN_ORDER_OK lower crossproducts=',float(D68[0]),float(D810[0]))
print('NEGATIVE_COVARIANCE_RIGOROUS_OK interval=',tuple(map(float,cov)))
