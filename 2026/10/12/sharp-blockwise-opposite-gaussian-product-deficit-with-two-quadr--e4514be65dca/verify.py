#!/usr/bin/env python3
from fractions import Fraction as F
import math
import random

# Complete algebraic identity from Gaussian regression, using rational inputs.
def conditional_normalized(s,a,b,c):
    v2=1-a*a
    v3=1-b*b
    r=c-a*b
    return v2*v3+2*r*r+(a*a*v3+b*b*v2+4*a*b*r)*(1-s)+a*a*b*b*(1-s)*(3-s)

def signed_difference(s,a,b,c):
    return -s*(a*a+b*b+4*a*b*c-(2+s)*a*a*b*b)

# Arbitrary rational test instances, not just optimizer cases.
for s in (F(1,4), F(1,2), F(3,4)):
    for a,b,c in ((F(1,5),F(1,3),F(-1,4)),(F(1,2),F(1,4),F(-1,5)),(F(-1,4),F(2,5),F(1,6))):
        assert conditional_normalized(s,a,b,c)-(1+2*c*c)==signed_difference(s,a,b,c)

for s in (F(1,4),F(1,2),F(3,4)):
    q=1/(6-s)
    c=2*q-1
    # a=b=sqrt(q); only a*b=q and a*a=b*b=q are needed.
    determinant=1-2*q-c*c+2*q*c
    polynomial=2*q+4*q*c-(2+s)*q*q
    assert determinant==0
    assert polynomial==-1/(6-s)
    assert -s*polynomial==s/(6-s)

s=F(1,2)
q=F(2,11)
c=-F(7,11)
assert 1-2*q-c*c+2*q*c==0
assert -s*(2*q+4*q*c-(2+s)*q*q)==F(1,11)

rng=random.Random(204861)
for i in range(10000):
    a=rng.uniform(-0.99,0.99)
    b=rng.uniform(-0.99,0.99)
    rho=rng.uniform(-0.999,0.999)
    c=a*b+rho*math.sqrt((1-a*a)*(1-b*b))
    det=1+2*a*b*c-a*a-b*b-c*c
    assert det>=-1e-12
    s=rng.uniform(0.001,0.999)
    delta=signed_difference(s,a,b,c)
    assert delta<=s/(6-s)+5e-13
    direct=conditional_normalized(s,a,b,c)-(1+2*c*c)
    assert abs(delta-direct)<=2e-11

print('VERIFY_OK exact_extremizers=3 sampled=10000 half_excess=0.090909090909')
