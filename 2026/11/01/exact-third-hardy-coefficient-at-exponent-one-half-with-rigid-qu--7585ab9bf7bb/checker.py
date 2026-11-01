#!/usr/bin/env python3
"""Reproducibility checks for a third-coefficient Hardy extremal constant.

Only the Python standard library is required. The infinite-dimensional
extremal statement is established analytically in RESULT.md.
"""
import math
from fractions import Fraction

def prod(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out

def add(p, q):
    out = [0] * max(len(p),len(q))
    for i,a in enumerate(p): out[i] += a
    for i,b in enumerate(q): out[i] += b
    return out

def scale(p,n): return [n*x for x in p]

# Symbolic exact polynomial identity after setting t=x*x and R=x*y.
# (R^2 - 3*t*R - 9*t)*(3-t)^2 = 9*F(t)*(3-t)^2? Instead substitute
# R=6*(3*t-1)/(3-t) and clear exactly (3-t)^2.
N=[-6,18]  # R numerator
D=[3,-1]   # R denominator
expr=add(add(prod(N,N),scale(prod(prod([0,1],N),D),-3)),scale(prod(prod([0,1],D),D),-9))
assert expr==[36,-243,198,45], (expr,'incorrect expansion') if False else expr
# Exact target = 9(5t^3+22t^2-27t+4)
assert expr==[36,-243,198,45]

def F(t): return (5*t+22)*t*t-27*t+4
assert F(Fraction(1,3))==Fraction(-64,27)
assert F(Fraction(2,3))==Fraction(-74,27)
assert F(Fraction(1,1))==4
assert F(Fraction(849,1000))<0<F(Fraction(850,1000))
lo,hi=0.849,0.850
for _ in range(64):
    mid=(lo+hi)/2
    if F(mid)>0: hi=mid
    else: lo=mid
t=(lo+hi)/2
x=math.sqrt(t)
y=1.5*(x+math.sqrt(t+4))
D=1+t+(9*t+1)/(y*y)
a=1/math.sqrt(D)
b=a*x;c=3*a*x/y;d=a/y
q=4*a**3*d+12*a*a*b*c+4*a*b**3
exact=math.sqrt(729*(5*t+1)**3/(16*(3-t)*(9*t*t+20*t+3)**2))
assert abs(q-y/D)<2e-13
assert abs(q-exact)<2e-13
assert abs((a*a+b*b+c*c+d*d)-1)<2e-14
assert a>b>c>d>0
assert abs(q-2.0889657962257755)<5e-13
print('PASS: exact elimination, rational root brackets, normalization and sharp value')
print('t=',format(t,'.16g'),'C(3,1/2)=',format(q,'.16g'))
