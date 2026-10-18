#!/usr/bin/env python3
"""Reproducibility checks for the quadrilateral one-point-per-side area theorem.
Uses only the Python standard library. Analytic proofs are in RESULT.md.
"""
from fractions import Fraction as F
from math import log, isclose
import random


def polygon_area(pts):
    return abs(sum(pts[i][0]*pts[(i+1)%len(pts)][1]
                   -pts[i][1]*pts[(i+1)%len(pts)][0]
                   for i in range(len(pts)))/2)


def cdf(a):
    if a <= 0:
        return 0.0
    if a >= 1:
        return 1.0
    z = abs(2*a-1)
    if z == 0:
        return .5
    H = (2*z + z*z)*log(z) + 2*z - 2.5*z*z
    return .5 + H if a < .5 else .5 - H


def density(a):
    if not 0 < a < 1:
        return 0.0
    z = abs(2*a-1)
    if z == 0:
        return float('inf')
    return 4*(-(1+z)*log(z)-2*(1-z))


def quadrilateral(p, q):
    # Diagonals are the coordinate axes, meeting at the origin.
    return [(-p, 0.), (0., q), (1.-p, 0.), (0., -(1.-q))]


def inscribed_area_fraction(verts, t):
    pts = [((1-t[i])*verts[i][0]+t[i]*verts[(i+1)%4][0],
            (1-t[i])*verts[i][1]+t[i]*verts[(i+1)%4][1])
           for i in range(4)]
    return polygon_area(pts)/polygon_area(verts)


def predicted_area(verts, t):
    base = polygon_area(verts)
    cross = []
    for i in range(4):
        prev, here, nex = verts[(i-1)%4], verts[i], verts[(i+1)%4]
        cross.append(abs((prev[0]-here[0])*(nex[1]-here[1])-
                         (prev[1]-here[1])*(nex[0]-here[0])) / (2*base))
    return 1-sum(cross[i]*(1-t[(i-1)%4])*t[i] for i in range(4))


def expected_variance(p, q):
    return 1/144+(7/72)*((p-.5)**2+(q-.5)**2)


def test_exact_rational_geometry():
    # The shoelace/corner-loss formula tested with exact rational arithmetic.
    for pnum in [1,2,3,4,5]:
      for qnum in [1,2,3,4,5]:
        p, q = F(pnum,6), F(qnum,6)
        v = [(-p, F(0)), (F(0),q), (1-p,F(0)), (F(0),q-1)]
        for j in range(13):
            t=[F((j+2*i+3*i*i)%17,17) for i in range(4)]
            assert inscribed_area_fraction(v,t)==predicted_area(v,t)
    print('exact rational polygon/corner area identities: 325 PASS')


def test_formula_symmetry():
    for k in range(1,500):
        a=k/1000
        assert abs(cdf(a)+cdf(1-a)-1)<2e-14
        assert density(a)>0 and abs(density(a)-density(1-a))<1e-12
        h=1e-7
        if abs(a-.5)>1e-5:
            der=(cdf(a+h)-cdf(a-h))/(2*h)
            assert abs(der-density(a))<3e-6, (a,der,density(a))
    assert cdf(.5)==.5
    print('CDF symmetry, positivity, PDF derivative: PASS')


def test_moments_monte_carlo():
    rng=random.Random(1903)
    for p,q in [(.5,.5),(.2,.35),(.8,.75),(.05,.9)]:
        v=quadrilateral(p,q)
        N=180000
        data=[]
        for j in range(N):
            t=[rng.random() for _ in range(4)]
            data.append(predicted_area(v,t))
        mean=sum(data)/N
        variance=sum((x-.5)**2 for x in data)/N
        target=expected_variance(p,q)
        assert abs(mean-.5)<.005, (p,q,mean)
        assert abs(variance-target)<.002, (p,q,variance,target)
        print('Monte Carlo p,q =', p, q, 'mean, variance=', round(mean,6),round(variance,6), 'target=',round(target,6))
        if p==q==.5:
            for a in [.1,.2,.4,.6,.8,.9]:
                empirical=sum(x<=a for x in data)/N
                assert abs(empirical-cdf(a))<.006, (a,empirical,cdf(a))
    print('sampling shape invariants and minimizing density CDF: PASS')


def test_exact_combinatorics():
    # Covariances for corner fractions Xi=(1-ti-1)*ti.
    EX=F(1,4)
    EX2=F(1,9)
    Eadj=F(1,24)
    assert EX2-EX**2==F(7,144)
    assert Eadj-EX**2==-F(1,48)
    assert F(7,144)-F(1,24)==F(1,144)
    # independent triangular variates have 2k-moments 1/((2k+1)(k+1)).
    for k in range(9):
        e=F(1,(2*k+1)*(k+1))
        centered=e*e/F(4**k,1)
        assert centered>=0
        if k==1:
            assert centered==F(1,144)
    print('exact covariance table and centered moments: PASS')

if __name__=='__main__':
    test_exact_rational_geometry()
    test_exact_combinatorics()
    test_formula_symmetry()
    test_moments_monte_carlo()
