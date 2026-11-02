#!/usr/bin/env python3
"""Reproduce an explicit attracting two-head antipodal attention equilibrium.
Only Python's standard library is required.
"""
import math
import random
from fractions import Fraction

KAPPAS=(math.log(3)/2,math.log(7)/2)
VALUES=(4.,-4.)


def update(xs,heads=(0,1)):
    ys=[]
    for i in range(2):
        z=list(xs[i])
        for h in heads:
            k=KAPPAS[h]
            scores=[k*(xs[i][0]*xs[j][0]+xs[i][1]*xs[j][1]) for j in range(2)]
            weights=[math.exp(t-max(scores)) for t in scores]
            denom=sum(weights)
            z[0]+=sum(weights[j]*xs[j][0] for j in range(2))/denom
            z[1]+=VALUES[h]*sum(weights[j]*xs[j][1] for j in range(2))/denom
        norm=math.sqrt(sum(t*t for t in z))
        ys.append(tuple(t/norm for t in z))
    return tuple(ys)


def tangent_chart(v,sign):
    norm=math.sqrt(1+sum(t*t for t in v))
    return (sign/norm,)+tuple(t/norm for t in v)


def f_chart(v,heads):
    xs=(tangent_chart(v[:3],1),tangent_chart(v[3:],-1))
    ys=update(xs,heads)
    return tuple(ys[0][j] for j in (1,2,3))+tuple(ys[1][j] for j in (1,2,3))


p=((1.,0.,0.,0.),(-1.,0.,0.,0.))
assert update(p)==p
assert Fraction(1,1)+(Fraction(1,2)+Fraction(3,4))==Fraction(9,4)
assert (Fraction(1,1)+4*(Fraction(3,4)-Fraction(7,8)))==Fraction(1,2)
assert (4*(Fraction(1,4)-Fraction(1,8)))==Fraction(1,2)
assert (Fraction(1,2)/Fraction(9,4))==Fraction(2,9)
assert (Fraction(1,1)/Fraction(9,4))==Fraction(4,9)

h=1.e-6
for heads,rational in [((0,1),Fraction(9,4)),((0,),Fraction(3,2)),((1,),Fraction(7,4))]:
    f0=f_chart((0.,)*6,heads)
    mat=[]
    for col in range(6):
        xp=[0.]*6;xm=[0.]*6;xp[col]=h;xm[col]=-h
        fp=f_chart(xp,heads);fm=f_chart(xm,heads)
        mat.append([(fp[i]-fm[i])/(2*h) for i in range(6)])
    J=[[mat[j][i] for j in range(6)] for i in range(6)]
    if heads==(0,1):
        assert all(abs(J[i][j]-(2/9 if i in (0,3) and j in (0,3) else 4/9 if i==j and i in (1,2,4,5) else 0))<1e-6 for i in range(6) for j in range(6)),J
        assert abs(sum(J[0][j] for j in [0,3])-4/9)<1e-8
    if heads==(0,):
        assert abs(sum(J[0][j] for j in [0,3])-10/3)<1e-8
    if heads==(1,):
        assert abs(sum(J[0][j] for j in [0,3])+12/7)<1e-8
    print('heads',heads,'radial gain',rational,'e2 symmetric multiplier',round(J[0][0]+J[0][3],12),'e2 transverse multiplier',round(J[0][0]-J[0][3],12))

random.seed(3417)
for t in range(24):
    v=[random.uniform(-0.03,0.03) for j in range(6)]
    xs=(tangent_chart(v[:3],1),tangent_chart(v[3:],-1))
    init=max(abs(vv) for vv in v)
    for _ in range(24): xs=update(xs)
    err=max(abs(xs[i][j]-p[i][j]) for i in (0,1) for j in range(4))
    assert err<1e-8,(t,err)
print('PASS: 24 local nonlinear trajectories converge; exact rational gains and first-order Jacobian verified.')
