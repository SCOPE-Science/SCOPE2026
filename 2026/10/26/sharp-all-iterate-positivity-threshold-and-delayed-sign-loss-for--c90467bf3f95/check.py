#!/usr/bin/env python3
"""Independent numerical and symbolic checks for a two-step stiff integrator's positive-iterate boundary."""
import math
from fractions import Fraction as Q
import sympy as S

s=S.symbols('s',real=True,positive=True)
A=(16-9*s)/(48+25*s)
B=(32-30*s)/(48+25*s)
q=(2-s)/(2+s)
assert S.factor(q**2-B*q-A)==4*s**3/((s+2)**2*(25*s+48))
assert S.diff(B,s).subs(s,S.Rational(16,15))==-S.Rational(45,112)
assert A.subs(s,S.Rational(16,15))==S.Rational(3,35)
assert B.subs(s,S.Rational(16,15))==0
# Derive the recurrence directly from the reported multistep coefficients.
tmp=(S.Rational(1,3)-S.Rational(3,16)*s)/(1+S.Rational(25,48)*s)
tmp2=(S.Rational(2,3)-S.Rational(5,8)*s)/(1+S.Rational(25,48)*s)
assert S.simplify(A-tmp)==0 and S.simplify(B-tmp2)==0

cases=[1.0,16/15,1.07,1.1,1.2,1.5,1.77,16/9,2.0,5.0]
for x in cases:
    aa=float(A.subs(s,x));bb=float(B.subs(s,x));u,v=1.0,math.exp(-x)
    first=None
    for k in range(2,2500):
        z=aa*u+bb*v
        if z<0:
            first=k
            break
        u,v=v,z
    if x<=16/15:
        assert first is None
    elif x>=16/9:
        assert first==2
    else:
        rp=(bb+math.sqrt(bb*bb+4*aa))/2
        rm=(bb-math.sqrt(bb*bb+4*aa))/2
        cp=(math.exp(-x)-rm)/(rp-rm)
        cm=(rp-math.exp(-x))/(rp-rm)
        assert rp>0>rm and cp>0>cm and math.exp(-x)>rp
        pred=2*(math.floor(math.log(cp/(-cm))/(2*math.log(abs(rm)/rp)))+1)
        assert pred==first, (x,pred,first)
r=math.sqrt(3/35)
e=math.exp(-16/15)
constant=112*r/45*math.log((e+r)/(e-r))
assert 1.8343<constant<1.8344
print('PASS: exact coefficient and root-comparison identities; 10 recurrence/index cases; boundary delay constant =',repr(constant))
