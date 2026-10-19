"""Reproducible exact-arithmetic checks for a two-compartment Patankar step.

Uses only Python's standard library. The universal statements are analytical;
these finite checks independently implement the two linear solves.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, sqrt


def lin2(A, B, C, D, r, s):
    det = A*D - B*C
    assert det > 0
    return ((r*D-B*s)/det, (A*s-r*C)/det)


def direct(u,v,a,h,c):
    in12=a*v+c*u*v
    in21=c*u*v
    z1,z2=lin2(1+h*in21/u,-h*in12/v,-h*in21/u,1+h*in12/v,u,v)
    av12=(in12+a*z2+c*z1*z2)/2
    av21=(in21+c*z1*z2)/2
    q1,q2=lin2(1+h*av21/z1,-h*av12/z2,-h*av21/z1,1+h*av12/z2,u,v)
    return z1,z2,q1,q2


def closed(u,v,a,h,c):
    d=h*a*v/(1+h*(a+c*(u+v)))
    U,V=u+d,v-d
    Q=c*(u*v+U*V)/2
    P=Q+a*(v+V)/2
    De=1+h*(P/V+Q/U)
    D=h*(P*v/V-Q*u/U)/De
    return d,D


checks=0
for u,v,a,h,c in product((F(1,5),F(2),F(7,3)),
                           (F(1,4),F(3),F(5,2)),
                           (F(1,3),F(3,2),F(5)),
                           (F(1,7),F(1),F(9,2)),
                           (F(0),F(1,2),F(7),F(200))):
    z1,z2,q1,q2=direct(u,v,a,h,c)
    d,D=closed(u,v,a,h,c)
    assert z1==u+d and z2==v-d
    assert q1==u+D and q2==v-D
    checks+=4
    assert min(z1,z2,q1,q2)>0 and z1+z2==u+v and q1+q2==u+v
    checks+=3
    assert D>d>=0 and D<v
    checks+=2

for c in (10**4,10**5,10**6,10**7,10**8):
    u=v=a=h=F(1)
    d,D=closed(u,v,a,h,F(c))
    assert abs(float(c*d-F(1,2)))<2/c
    assert abs(float(c*D-F(1)))<5/c
    assert abs(float(c*(D-d)-F(1,2)))<5/c
    checks+=3

u=v=a=h=F(1)
for c in (10**7,10**8,10**9):
    d,D=closed(u,v,a,h,F(c))
    error=abs(1-exp(-1)-float(D))
    w=abs(float(D-d))/(1e-6+1e-3*max(float(u+D),float(u+d)))
    assert error>0.63
    assert w<0.1
    checks+=2

print(f"PASS: {checks} independently constructed exact-rational and numerical assertions")
print("Example u=v=a=h=1,c=0: stage/final =",closed(F(1),F(1),F(1),F(1),F(0)))
print("Example u=v=a=h=1,c=1e9: stage/final =",*[float(x) for x in closed(F(1),F(1),F(1),F(1),F(10**9))])
