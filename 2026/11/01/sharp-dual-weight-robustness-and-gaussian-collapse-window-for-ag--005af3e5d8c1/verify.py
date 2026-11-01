#!/usr/bin/env python3
"""Standalone arithmetic checks for a weighted-surrogate LP sensitivity theorem.

Requires Python 3 only; deterministic pseudo-random seeds are fixed. Tests are
finite corroboration, not proofs of any asymptotic or all-dimensional claim.
"""
from fractions import Fraction
from itertools import product
from math import sqrt, pi, erf
from random import Random


def predicted_gap(w):
    a = sum(abs(x) for x in w[1:])
    if not w[0]:
        return type(a)(1)
    return min(1, a / abs(w[0]))


def direct_vertex_lp(w):
    """Enumerate hypercube vertices and single-edge slice intersections."""
    m = len(w)
    best = None
    for vert in product((-1, 1), repeat=m):
        x = tuple(Fraction(v) for v in vert)
        if sum(w[i]*x[i] for i in range(m)) == 0:
            best = x[0] if best is None else max(best, x[0])
    for j in range(m):
        if not w[j]:
            continue
        for other in product((-1, 1), repeat=m-1):
            x = list(map(Fraction, other))
            x.insert(j, Fraction(0))
            x[j] = -sum(w[i]*x[i] for i in range(m) if i != j)/w[j]
            if abs(x[j])<=1:
                best = x[0] if best is None else max(best, x[0])
    assert best is not None
    return best


def exact_tests():
    rng=Random(341926)
    count=0
    for m in range(2,8):
        for _ in range(75):
            w = [Fraction(rng.randint(-15,15),rng.randint(1,11)) for _ in range(m)]
            actual=direct_vertex_lp(w)
            expected=predicted_gap(w)
            assert actual==expected,(m,w,actual,expected)
            count+=1
    for m in range(2,31):
        for denominator in (m, m+1, 2*m, 7*m, 97):
            d=Fraction(1,denominator)
            e=[d]*m
            w=[-1+e[0]]+e[1:]
            actual=predicted_gap(w)
            expected=min(1,Fraction(m-1)*d/(1-d))
            assert actual==expected
            count+=1
    for m in range(2,30):
        e=[Fraction(1,m)]*m
        w=[-1+e[0]]+e[1:]
        assert sum(w)==0 and predicted_gap(w)==1
        count+=1
    return count


def euclidean_test():
    rng=Random(342326)
    count=0
    for m in (2,3,5,11,31):
        for rho in (.005,.03,.15,.5,.9):
            # An exact optimizer of the Cauchy/one-variable upper envelope.
            ep1=rho*rho
            other=rho*sqrt(1-rho*rho)/sqrt(m-1)
            ep=[ep1]+[other]*(m-1)
            w=[-1+ep1]+ep[1:]
            opt=min(1,rho*sqrt(m-1)/sqrt(1-rho*rho))
            assert abs(predicted_gap(w)-opt)<2.e-12
            assert abs(sqrt(sum(e*e for e in ep))-rho)<1.e-12
            count+=2
            for _ in range(120):
                eps=[rng.uniform(-1.,1.) for _ in range(m)]
                nn=sqrt(sum(t*t for t in eps))
                if nn==0: continue
                eps=[rho*e/nn for e in eps]
                test=predicted_gap([-1+eps[0]]+eps[1:])
                assert test<=opt+1e-12,(m,rho,test,opt)
                count+=1
    return count


def gaussian_checks():
    rng=Random(346626)
    mu=sqrt(2/pi)
    c_star=1/mu
    trials=1200
    count=0
    table=[]
    for m in (100,500,2000):
        for c in (0.50*c_star, c_star, 1.50*c_star):
            values=[]
            saturation=0
            sig=c/m
            for _ in range(trials):
                g1=rng.gauss(0,1)
                other=sum(abs(rng.gauss(0,1)) for _ in range(m-1))
                d=min(1,sig*other/abs(1-sig*g1))
                values.append(d)
                saturation+= d==1
            mean=sum(values)/trials
            predicted=min(1,c*mu)
            table.append((m,round(c/c_star,2),round(mean,4),round(saturation/trials,4)))
            assert abs(mean-predicted)<(.055 if m==100 else .028)
            if m==2000 and c==c_star:
                assert abs(saturation/trials-.5)<.09
            count+=trials
    # Critical window probability prediction with tau=+/-1; finite m check.
    v=sqrt(1-2/pi)
    for tau in (-1.,0.,1.):
        m=1800
        sig=c_star/m*(1+tau/sqrt(m))
        saturation=0
        for _ in range(trials):
            g1=rng.gauss(0,1)
            other=sum(abs(rng.gauss(0,1)) for _ in range(m-1))
            saturation+= (sig*other>=abs(1-sig*g1))
        empirical=saturation/trials
        limit=(1+erf(tau*mu/v/sqrt(2)))/2
        assert abs(empirical-limit)<.12,(tau,empirical,limit)
        table.append(('window',tau,round(empirical,4),round(limit,4)))
        count+=trials
    return count,table

if __name__=='__main__':
    n1=exact_tests()
    n2=euclidean_test()
    n3,t=gaussian_checks()
    print('Exact rational LP and extremal tests:',n1)
    print('Euclidean tests:',n2)
    print('Seeded Gaussian trials:',n3)
    print('Gaussian results:',t)
    print('PASS',n1+n2+n3, 'checks/trials')
