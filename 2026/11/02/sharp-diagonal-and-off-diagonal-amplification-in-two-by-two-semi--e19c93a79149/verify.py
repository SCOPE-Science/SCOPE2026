#!/usr/bin/env python3
"""Exact-rational derivative checks for the real two-by-two PSD projection.

Run with Python 3 standard library: python3 verify.py
The proof in RESULT.md supplies the parameter-uniform inequalities.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext

class Dual:
    def __init__(self, v, d=0):
        self.v=F(v); self.d=F(d)
    def __add__(self, o):
        o=as_dual(o);return Dual(self.v+o.v,self.d+o.d)
    __radd__=__add__
    def __neg__(self):return Dual(-self.v,-self.d)
    def __sub__(self,o):return self+(-as_dual(o))
    def __rsub__(self,o):return as_dual(o)-self
    def __mul__(self,o):
        o=as_dual(o);return Dual(self.v*o.v,self.d*o.v+self.v*o.d)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_dual(o);return Dual(self.v/o.v,(self.d*o.v-self.v*o.d)/(o.v*o.v))
    def __rtruediv__(self,o):return as_dual(o)/self

def as_dual(x):return x if isinstance(x,Dual) else Dual(x)

def rational_sqrt(x):
    from math import isqrt
    n=isqrt(x.numerator);d=isqrt(x.denominator)
    assert n*n==x.numerator and d*d==x.denominator, x
    return F(n,d)

def dsqrt(x):
    y=rational_sqrt(x.v)
    return Dual(y,x.d/(2*y))

def positive_part_coordinate(x,y,z,coordinate):
    m=(x+y)/2;d=(x-y)/2;r=dsqrt(d*d+z*z)
    if coordinate=='11':return (m+r)*(1+d/r)/2
    if coordinate=='12':return (m+r)*z/(2*r)
    if coordinate=='22':return (m+r)*(1-d/r)/2
    raise ValueError(coordinate)

def check():
    checks=0
    ts=[F(-99,100),F(-3,4),F(-1,4),F(0),F(1,3),F(3,4),F(99,100),F(1)]
    cs=[(F(0),F(1)),(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(8,17),F(15,17)),(F(12,13),F(5,13)),(F(1),F(0))]
    for c,s in cs:
        assert c*c+s*s==1
        checks+=1
        for t in ts:
            x=t+c;y=t-c;z=s
            a11x=((1+c)**2+(1+t)*(1-c*c))/4
            a11y=-t*(1-c*c)/4
            a11z=s*(1-t*c)/2
            a12x=s*(1-t*c)/4
            a12y=s*(1+t*c)/4
            a12z=(1+t*c*c)/2
            for coordinate,coeffs in [('11',(a11x,a11y,a11z)),('12',(a12x,a12y,a12z))]:
                for j in range(3):
                    vals=[Dual(x),Dual(y),Dual(z)]
                    vals[j].d=F(1)
                    actual=positive_part_coordinate(*vals,coordinate).d
                    assert actual==coeffs[j],(coordinate,j,t,c,s,actual,coeffs[j])
                    checks+=1
            drow=abs(a11x)+abs(a11y)+abs(a11z)
            orow=abs(a12x)+abs(a12y)+abs(a12z)
            assert drow<=F(3,2) and orow<=F(9,8)
            checks+=2
    c=F(0);s=F(1);t=F(1)
    assert ((1+c)**2+(1+t)*(1-c*c))/4 + t*(1-c*c)/4 + s*(1-t*c)/2 == F(3,2)
    checks+=1
    # An independent finite-perturbation check of the limiting sharpness witness.
    with localcontext() as ctx:
        ctx.prec=70
        for k in (2,3,4,5,6,7,8,9):
            e=Decimal(10)**(-k)
            r=(1+2*e+2*e*e).sqrt()
            p11=(1+r)*(1+e/r)/2
            ratio=(p11-1)/e
            assert abs(ratio-Decimal('1.5')) < Decimal(4)*e
            checks+=1
            r2=(1-e+e*e).sqrt()
            p12=(1-e+r2)*(Decimal('0.5')-e)/(2*r2)
            ratio2=(Decimal('0.5')-p12)/e
            assert abs(ratio2-Decimal('1.125')) < Decimal(4)*e
            checks+=1
    return checks

if __name__=='__main__':
    print('PASS:',check(),'exact rational and high-precision assertions')
