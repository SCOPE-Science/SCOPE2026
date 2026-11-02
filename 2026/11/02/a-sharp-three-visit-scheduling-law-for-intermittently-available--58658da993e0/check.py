#!/usr/bin/env python3
"""Reproduce the exact three-occasion occupancy scheduling identity.

Only Python's standard library is needed.  Values x and y stand for the
strictly positive Markov-state correlation factors across the two gaps.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log


def nondetection_direct(pi, ps, x, y):
    # Transition entries Pr(X_next=b | X_previous=a).
    def trans(a, b, corr):
        return (pi if b else 1 - pi) + corr * ((int(a == b)) - (pi if b else 1 - pi))
    total = F(0)
    for i, j, k in product((0, 1), repeat=3):
        weight = (pi if i else 1 - pi) * trans(i, j, x) * trans(j, k, y)
        weight *= (1 - ps[0] if i else 1) * (1 - ps[1] if j else 1) * (1 - ps[2] if k else 1)
        total += weight
    return total


def nondetection_closed(pi, ps, x, y):
    p1,p2,p3=ps
    c=x*y
    constant=1-pi*(p1+p2+p3)+pi*pi*(p1*p2+p2*p3+p1*p3)-pi**3*p1*p2*p3
    constant += pi*(1-pi)*p1*p3*c-pi*(1-pi)**2*p1*p2*p3*c
    A=pi*(1-pi)*p1*p2*(1-pi*p3)
    B=pi*(1-pi)*p2*p3*(1-pi*p1)
    return constant+A*x+B*y


def optimal_hazard(pi,p1,p2,p3,L):
    assert 0<pi<1 and 0<p1<=1 and 0<p2<=1 and 0<p3<=1 and L>0
    ratio=p1*(1-pi*p3)/(p3*(1-pi*p1))
    return max(0.,min(L,(L+log(ratio))/2))


def nondetection_float(pi, ps, L, u):
    return float(nondetection_closed(pi, ps, exp(-u), exp(-(L-u))))


def main():
    q=(F(1,4), F(2,5), F(3,4))
    p=(F(1,5), F(1,2), F(4,5))
    corr=(F(1,4),F(1,2),F(3,4))
    exact=0
    for pi in q:
        for ps in product(p, repeat=3):
            for x,y in product(corr, repeat=2):
                actual=nondetection_direct(pi,ps,x,y)
                formula=nondetection_closed(pi,ps,x,y)
                assert actual == formula,(pi,ps,x,y,actual,formula)
                exact+=1
    assert exact==729

    n=0
    for pi in (0.13,0.4,0.82):
        for ps in product((0.08,0.31,0.65,1.),repeat=3):
            for L in (0.1,0.7,2.,5.):
                opt=optimal_hazard(pi,*ps,L)
                val=nondetection_float(pi,ps,L,opt)
                for u in (0.,0.03*L,0.25*L,0.5*L,0.75*L,0.97*L,L):
                    assert val < nondetection_float(pi,ps,L,u)+2e-14,(pi,ps,L,opt,u)
                # Testing strict convexity at 3 separated points by actual identity.
                lo,mid,hi=0.,L/2,L
                assert nondetection_float(pi,ps,L,mid) < (nondetection_float(pi,ps,L,lo)+nondetection_float(pi,ps,L,hi))/2+2e-14
                n+=1
    assert n==768
    # Prove via formula that middle-occasion quality scales A and B together.
    for pi in (0.2,0.5,0.8):
        for p1,p3 in product((0.1,0.3,0.9),repeat=2):
            for L in (0.5,2.,4.):
                vals=[optimal_hazard(pi,p1,p2,p3,L) for p2 in (0.01,0.2,0.7,1.)]
                assert max(vals)-min(vals)<1e-12

    # A reproducible interior asymmetric example and a boundary/co-location example.
    pi,p1,p2,p3,L=0.3,0.8,0.5,0.4,3.0
    u=optimal_hazard(pi,p1,p2,p3,L)
    print('Exact rational Markov/closed-form comparisons: ',exact)
    print('Independent optimality/convexity parameter grids: ',n)
    print('Interior example: pi=0.3, detections=(0.8,0.5,0.4), total hazard=3')
    print('  optimal hazard coordinate:',format(u,'.14f'))
    print('  nondetection at optimum:',format(nondetection_float(pi,(p1,p2,p3),L,u),'.14f'))
    print('  nondetection at midpoint:',format(nondetection_float(pi,(p1,p2,p3),L,L/2),'.14f'))
    pi,p1,p2,p3,L=0.35,0.95,0.6,0.10,1.0
    u=optimal_hazard(pi,p1,p2,p3,L)
    assert u==L
    print('Boundary example: pi=0.35, detections=(0.95,0.6,0.1), total hazard=1')
    print('  optimal hazard coordinate:',u,'(third-visit co-location)')
    print('PASS')


if __name__=='__main__':
    main()
