#!/usr/bin/env python3
from fractions import Fraction as F
from math import sqrt

D=62841
knots=[F(i,5) for i in range(6)]
X=[F(0),F(13,5),F(56,5),F(58,5),F(59,5),F(64,5)]
Y=[F(0),F(13,5),F(56,5),F(66,5),F(67,5),F(72,5)]

sx=[(X[i+1]-X[i])/(knots[i+1]-knots[i]) for i in range(5)]
sy=[(Y[i+1]-Y[i])/(knots[i+1]-knots[i]) for i in range(5)]
assert sx == [F(13),F(43),F(2),F(1),F(5)]
assert sy == [F(13),F(43),F(10),F(1),F(5)]
assert all(s>0 for s in sx+sy)

gap=[Y[i]-X[i] for i in range(6)]
assert gap == [F(0),F(0),F(0),F(8,5),F(8,5),F(8,5)]
assert all(gap[i+1]>=gap[i] for i in range(5))

def tauX(p):
    return (25*p*p+143)/(2*(25*p*p-25*p+86))

def tauY(p):
    return (25*p*p+183)/(2*(25*p*p-25*p+106))

u=F(24,25)
v=F(159,164)
assert u<v
assert tauY(F(3,5)) == u
assert tauX(F(79,115)) == u
assert tauX(F(4,5)) == v

# Exact arithmetic in Q(sqrt(D)): a pair (a,b) means a+b*sqrt(D).
def add(z,w):
    return (z[0]+w[0],z[1]+w[1])
def mul(z,w):
    return (z[0]*w[0]+z[1]*w[1]*D,z[0]*w[1]+z[1]*w[0])
def scale(c,z):
    return (c*z[0],c*z[1])

p=(F(159,154),-F(1,770))
poly=add(add(scale(F(-1925),mul(p,p)),scale(F(3975),p)),(F(-1848),F(0)))
assert poly == (F(0),F(0))
p_float=float(p[0])+float(p[1])*sqrt(D)
assert 0.6 < p_float < 0.8

du=F(174,115)
dv_float=(1411-sqrt(D))/770
assert float(du)>dv_float

square_margin=D*23*23-5657*5657
assert square_margin == 1241240
assert square_margin>0

print(f"VERIFY_OK u={u.numerator}/{u.denominator} v={v.numerator}/{v.denominator} square_margin={square_margin}")
