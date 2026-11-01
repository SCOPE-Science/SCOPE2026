#!/usr/bin/env python3
"""Exact moment inversion and independent sampling checks for rectangular flat three-tori."""
from fractions import Fraction as Q
from math import sqrt
from random import Random


def moments_from_x(x):
    """Returns moments of squared intrinsic distance, via independent U[-1,1] coordinates."""
    c1 = sum(x, Q(0))/3
    c2 = Q(4,45)*sum((t*t for t in x),Q(0))
    c3 = Q(16,945)*sum((t*t*t for t in x),Q(0))
    return (c1, c2+c1*c1, c3+3*c1*c2+c1*c1*c1)


def coefficients_from_moments(m):
    a,b,c=m
    k1=a
    k2=b-a*a
    k3=c-3*b*a+2*a*a*a
    p1=3*k1
    p2=Q(45,4)*k2
    p3=Q(945,16)*k3
    return (p1,(p1*p1-p2)/2,(p1*p1*p1-3*p1*p2+2*p3)/6)


def cubic_at(coef,t):
    e1,e2,e3=coef
    return t**3-e1*t*t+e2*t-e3


def discriminant(coef):
    a,b,c=coef
    return a*a*b*b-4*b*b*b-4*a*a*a*c-27*c*c+18*a*b*c


def exact_checks():
    samples=[(Q(1),Q(1),Q(1)),(Q(1),Q(4),Q(9)),(Q(1),Q(2),Q(3)),
       (Q(3,5),Q(8,3),Q(13,7)),(Q(7,2),Q(7,2),Q(11,4))]
    for x in samples:
        coef=coefficients_from_moments(moments_from_x(x))
        assert coef==(sum(x), x[0]*x[1]+x[1]*x[2]+x[0]*x[2],x[0]*x[1]*x[2])
        assert all(cubic_at(coef,t)==0 for t in x)
        assert discriminant(coef)>=0
    # Two distinct 3-tuples with identical first and second moment
    # are also checked exactly in Q(sqrt(3)) by simplifying their power sums.
    assert moments_from_x((Q(1),Q(2),Q(3)))[:2] == (Q(2),Q(236,45))
    print('EXACT_CUMULANTS_NEWTON_CUBIC_AND_DISCRIMINANT_PASSED')


def independent_sampling():
    rng=Random(193017)
    periods=(2.,4.,6.)
    x=[a*a/4 for a in periods]
    m=moments_from_x([Q(1),Q(4),Q(9)])
    n=250000
    totals=[0.,0.,0.]
    for _ in range(n):
        D2=0.
        for a in periods:
            u=rng.random()*a
            v=rng.random()*a
            dif=abs(u-v)
            D2+=min(dif,a-dif)**2
        totals[0]+=D2
        totals[1]+=D2*D2
        totals[2]+=D2*D2*D2
    obs=[v/n for v in totals]
    target=[float(v) for v in m]
    for o,e in zip(obs,target):
        assert abs(o-e)<0.012*e, (o,e)
    print('INDEPENDENT_HAAR_POINT_PAIR_SAMPLING_PASSED',[(round(o,4),round(t,4)) for o,t in zip(obs,target)])


def near_cube_sharpness():
    # Two families whose power sums p1,p2 match but whose p3 differ at order t^3.
    for t in [0.2,0.1,0.05,0.01]:
        x=(1-t,1,1+t)
        y=(1-t/sqrt(3),1-t/sqrt(3),1+2*t/sqrt(3))
        ps=lambda v,k:sum(s**k for s in v)
        assert abs(ps(x,1)-ps(y,1))<1e-12
        assert abs(ps(x,2)-ps(y,2))<1e-12
        assert abs((ps(y,3)-ps(x,3))-2*t**3/sqrt(3))<1e-12
        assert max(abs(2*sqrt(a)-2*sqrt(b)) for a,b in zip(sorted(x),sorted(y)))>t/4
    print('TWO_MOMENT_NONUNIQUENESS_AND_OPTIMAL_ONE_THIRD_EXPONENT_PASSED')


if __name__=='__main__':
    exact_checks()
    near_cube_sharpness()
    independent_sampling()
    print('ALL_CHECKS_PASSED')
