#!/usr/bin/env python3
"""Exact-rational stage replay and analytic checks for randomized row-reflection dynamics."""
from fractions import Fraction as F
from collections import defaultdict
from math import sqrt,cos,sin,exp,isclose


def reflect(i, xy, d):
    x,y=xy
    if i==0:
        return (-x,y)
    if i==1:
        return (2*d-x,y)
    if i==2:
        return (x,-y)
    raise ValueError('row')

def paired_step(i,j,xy,d):
    rx,ry=reflect(j,reflect(i,xy,d),d)
    return ((xy[0]+rx)/2,(xy[1]+ry)/2)

def predicted(i,j,xy,d):
    x,y=xy
    if i==2 and j==2:
        return x,y
    if i==2 or j==2:
        return (F(0) if i==0 or j==0 else d,F(0))
    return x+ (F(1) if (i,j)==(0,1) else F(-1) if (i,j)==(1,0) else F(0))*d,y


def check(q,d,x0):
    assert F(0)<q<F(1)
    w=((1-q)/2,(1-q)/2,q)
    for x,y in ((F(-7,3)*d,F(5,2)*d),(F(13,7)*d,F(-3,2)*d),(F(0),F(0))):
        xy=(x,y)
        for i in range(3):
            for j in range(3):
                assert paired_step(i,j,xy,d)==predicted(i,j,xy,d)
        nxt=[(w[i]*w[j], paired_step(i,j,xy,d)) for i in range(3) for j in range(3)]
        center=d/2
        theta=2*q*(1-q)
        mu=sum((p*(z[0]-center) for p,z in nxt),F(0))
        ms=sum((p*(z[0]-center)**2 for p,z in nxt),F(0))
        ys=sum((p*z[1]**2 for p,z in nxt),F(0))
        assert mu==(1-theta)*(x-center)
        assert ms==(1-theta)*(x-center)**2+d*d*(1-q)/2
        assert ys==(1-theta)*y*y
    dist={x0:F(1)}
    theta=2*q*(1-q)
    for n in range(12):
        prob=sum(dist.values(),F(0))
        assert prob==1
        expect=sum((p*(xy[0]-d/2) for xy,p in dist.items()),F(0))
        err=sum((p*((xy[0]-d/2)**2+xy[1]**2) for xy,p in dist.items()),F(0))
        assert expect == (1-theta)**n*(x0[0]-d/2)
        assert err == (1-theta)**n*((x0[0]-d/2)**2+x0[1]**2)+d*d/(4*q)*(1-(1-theta)**n)
        new=defaultdict(F)
        for xy,p in dist.items():
            for i in range(3):
                for j in range(3):
                    new[paired_step(i,j,xy,d)]+=p*w[i]*w[j]
        dist=dict(new)
    return len(dist)

for q,d in ((F(1,3),F(7,5)),(F(2,3),F(5,2)),(F(1,5),F(3,7)),(F(4,5),F(9,4))):
    print('rational',q,'states',check(q,d,(F(13,12)*d,F(8,9)*d)))

# Stationary centered characteristic function matches the explicit discrete-Laplace law.
for q in (0.001,0.01,0.1,0.333333333333,0.5,0.9):
    r=(sqrt(1+q)-sqrt(2*q))/(sqrt(1+q)+sqrt(2*q))
    assert 0<r<1
    for t in (0.03,0.31,0.77,1.4,2.7):
        char_formula=(2*q*cos(t/2))/(2*q+(1-q)*sin(t/2)**2)
        char_geo=((1-r)**2*cos(t/2))/(1-2*r*cos(t)+r*r)
        assert isclose(char_formula,char_geo,rel_tol=2e-9,abs_tol=1e-9),(q,t,char_formula,char_geo)
    # The centered law is the equal-sign mixture of positions +(k+1/2) and -(k+1/2).
    moment=(1-r)*sum(r**k*(k+0.5)**2 for k in range(40000))
    assert isclose(moment,1/(4*q),rel_tol=1e-8,abs_tol=1e-8),(q,moment,1/(4*q))
for q in (1e-3,1e-4,1e-5):
    for t in (0.1,1.0,4.0):
        phi=2*q*cos(t*sqrt(q)/2)/(2*q+(1-q)*sin(t*sqrt(q)/2)**2)
        laplace=1/(1+t*t/8)
        assert abs(phi-laplace)<0.002,(q,t,phi,laplace)
print('VERIFY_OK: 4 rational parameter families, exact 9-branch reflections, 48 finite-time moment identities, discrete-Laplace inversion, stationary moments, Laplace weak-scaling check')
