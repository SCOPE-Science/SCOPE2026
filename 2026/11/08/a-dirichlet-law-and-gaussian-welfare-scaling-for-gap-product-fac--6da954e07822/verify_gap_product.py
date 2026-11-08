#!/usr/bin/env python3
"""Finite and moment checks for weighted-gap facility sampling.
The proof of the infinite-population convergence is mathematical, not certified by this script.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial, sqrt
from random import Random


def rising(a, r):
    out = 1
    for j in range(r):
        out *= a+j
    return out


def expectation_moments(k):
    alpha = [1]+[2]*(k-1)+[1]
    coeff = [F(1,2)]+[F(1,4)]*(k-1)+[F(1,2)]
    den2 = rising(2*k,2)
    den4 = rising(2*k,4)
    mean = sum((coeff[i]*rising(alpha[i],2) for i in range(k+1)),F(0)) / den2
    sq = sum((coeff[i]**2*rising(alpha[i],4) for i in range(k+1)),F(0))
    for i,j in combinations(range(k+1),2):
        sq += 2*coeff[i]*coeff[j]*rising(alpha[i],2)*rising(alpha[j],2)
    second = sq / den4
    return mean,second-mean*mean


def grid_cost(xs, selected):
    return sum(min(abs(x-y) for y in selected) for x in xs)/len(xs)


def exact_grid_mean(n,k):
    xs=[i/(n-1) for i in range(n)]
    numerator=denominator=0.
    for ss in combinations(xs,k):
        weight=1.
        for i in range(k-1):
            weight*=ss[i+1]-ss[i]
        numerator+=weight*grid_cost(xs,ss)
        denominator+=weight
    return numerator/denominator


def run_checks():
    tests=0
    for k in range(2,65):
        mu,var=expectation_moments(k)
        assert mu == F(3*k+1,4*k*(2*k+1)),(k,mu)
        assert var == F(6*k**3+8*k*k-3*k-3,16*k*k*(k+1)*(2*k+1)**2*(2*k+3)),(k,var)
        assert var > 0
        tests+=3
        regular=F(2*k*(k+3),(k+1)*(k+2))
        weighted=4*k*mu
        assert regular-weighted==F((k-1)*(k*k+5*k+2),(k+1)*(k+2)*(2*k+1))
        tests+=1
    for k in [2,3,4]:
        ns= [10,16,24,32] if k <= 3 else [10,16,24]
        lim=float(F(3*k+1,4*k*(2*k+1)))
        diffs=[]
        for n in ns:
            actual=exact_grid_mean(n,k)
            diffs.append(abs(actual-lim))
        assert diffs[-1]<diffs[0],(k,diffs)
        assert diffs[-1]<0.012,(k,diffs)
        tests+=len(ns)+2
        print('grid',k,'sizes',ns,'absolute errors', [round(d,7) for d in diffs])
    # Separate Gamma sampler validates all fixed-k mean and variance identities,
    # not a proof of weak convergence or CLT.
    rng=Random(20261102)
    for k in [2,3,6,12]:
        samples=[]
        for _ in range(90000):
            a=rng.expovariate(1)
            c=rng.expovariate(1)
            bs=[rng.gammavariate(2,1) for j in range(k-1)]
            den=(a+c+sum(bs))**2
            samples.append((.5*(a*a+c*c)+.25*sum(b*b for b in bs))/den)
        mu,var=expectation_moments(k)
        avg=sum(samples)/len(samples)
        sec=sum((t-float(mu))**2 for t in samples)/len(samples)
        assert abs(avg-float(mu)) < 5.5*sqrt(float(var)/len(samples)),(k,avg,mu)
        assert abs(sec-float(var)) < .09*float(var),(k,sec,var)
        print('gamma',k,'empirical mean',round(avg,7),'exact',float(mu),'empirical var',round(sec,8),'exact var',float(var))
        tests+=2
    print('PASS',tests,'checks; analytic proof remains necessary')


if __name__=='__main__':
    run_checks()
