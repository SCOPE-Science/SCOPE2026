#!/usr/bin/env python3
"""Exact rational and floating-point checks for the box-plus-axial-point ellipsoid."""
from fractions import Fraction as Q
from itertools import product
from math import sqrt, isclose, prod


def ellipsoid(d,h):
    h=Q(h)
    assert d>=2 and h>1
    if h*h<=d:
        return Q(0),Q(d),Q(d),1
    if h<=d:
        return Q(0),h*h,Q(d-1)*h*h/(h*h-1),2
    return (h-d)/Q(d+1),Q(d*d)*(h+1)**2/Q((d+1)**2),Q(d*d)/Q(d+1),3


def check(d,h):
    h=Q(h)
    c,a2,b2,mode=ellipsoid(d,h)
    assert a2>0 and b2>0 and c>=0
    # Every corner is contained and the apex is contained.
    for first in [-1,1]:
        norm=(Q(first)-c)**2/a2+Q(d-1)/b2
        assert norm<=1,(d,h,first,norm)
        if mode==1 or mode==2 or first==-1:
            assert norm==1,(d,h,first,norm)
        if mode==3 and first==1:
            assert norm<1
    apex=(h-c)**2/a2
    assert apex<=1
    if mode>=2:
        assert apex==1
    elif h*h<d:
        assert apex<1
    # Weights on contact points: verify exact original-coordinate mean/covariance.
    if mode==1:
        means=[Q(0)]*d
        variances=[Q(1)]*d
        cross=[Q(0)]
    elif mode==2:
        lam=(h*h-d)/(Q(d)*(h*h-1))
        bias=(h*h-d)/(Q(d-1)*h)
        assert 0<=lam<=1 and 0<=bias<=1
        mu=lam*h+(1-lam)*(-bias)
        assert mu==c
        v_ax=lam*h*h+(1-lam)*Q(1)-c*c
        assert v_ax==a2/d,(d,h,v_ax,a2/Q(d))
        assert 1-lam==b2/d
        means=[mu]+[Q(0)]*(d-1)
        variances=[v_ax]+[1-lam]*(d-1)
    else:
        lam=Q(1)/Q(d+1)
        mu=lam*h-(1-lam)
        assert mu==c
        v_ax=lam*(h-c)**2+(1-lam)*(-1-c)**2
        assert v_ax==a2/d
        assert 1-lam==b2/d
        means=[mu]+[Q(0)]*(d-1)
        variances=[v_ax]+[1-lam]*(d-1)
    assert means[0]==c
    assert variances[0]==a2/d
    assert all(v==b2/d for v in variances[1:])
    return mode


def run():
    counts=[0,0,0,0]
    for d in range(2,101):
        # h>1; include both thresholds exactly if d is a square, and arbitrary rational values.
        cases=[Q(1)+Q(j,100) for j in range(1,501)]
        cases += [Q(d),Q(d)+Q(1,7), Q(d*2), Q(d*9,4),Q(d*100)]
        if int(sqrt(d))**2==d:
            cases.extend([Q(int(sqrt(d))),Q(int(sqrt(d)))-Q(1,100000),Q(int(sqrt(d)))+Q(1,100000)])
        for h in cases:
            if h>1: counts[check(d,h)]+=1
    assert all(counts[i]>0 for i in (1,2,3))
    # Floating independent random-direction and random-determinant checks.
    import random
    rng=random.Random(4729)
    floats=0
    for d in (2,3,4,5,9,17,31):
        for h in (1.02,sqrt(d)*1.001,(sqrt(d)+d)/2,d*0.999,d*1.001,20*d):
            if h<=1:continue
            c,a2,b2,_=ellipsoid(d,Q.from_float(h))
            c,a2,b2=float(c),float(a2),float(b2)
            for _ in range(100):
                vertex=[rng.choice((-1,1)) for _ in range(d)]
                val=(vertex[0]-c)**2/a2+sum(x*x for x in vertex[1:])/b2
                assert val<1+1e-10
                floats+=1
    print('PASS exact rational configurations',sum(counts),'regime_counts',counts[1:],'random_vertex_checks',floats)


if __name__=='__main__':run()
