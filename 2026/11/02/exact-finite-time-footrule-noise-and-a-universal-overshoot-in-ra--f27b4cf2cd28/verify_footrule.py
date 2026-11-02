#!/usr/bin/env python3
"""Reproduce exact small-deck and asymptotic checks of the footrule noise law.

Requires Python 3 standard library only. This is a consistency checker,
not a substitute for the all-deck representation-theoretic proof.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import exp


def theoretical(n,t):
    a=F(n-2,n)
    c=F(n-4,n)
    mean=F(n*n-1,3)*(1-a**t)
    var=(F((n+1)*(2*n*n+7),45)
         +F(4*(n*n-1)*(n+2),45)*a**t
         -F((n+1)*(3*n**3+9*n*n-4*n+10),90)*a**(2*t)
         +F((n*n-1)*(n*n-4),30)*c**t)
    return mean,var


def exact_step(dist,n):
    out=defaultdict(F)
    for state,weight in dist.items():
        for i in range(n):
            for j in range(n):
                q=list(state)
                q[i],q[j]=q[j],q[i]
                out[tuple(q)]+=weight/F(n*n)
    return dict(out)


def footrule(state):
    return sum(abs(i-v) for i,v in enumerate(state))


def profile(s):
    return (2+4*exp(-s)-(6+3*s)*exp(-2*s))/45


def main():
    checks=0
    for n in range(4,13):
        triple=sum(24*(k-i)**2 for i,j,k in combinations(range(n),3))
        quadruple=sum(8*(((j-i)+(l-k))**2+2*((k-i)+(l-j))**2)
                        for i,j,k,l in combinations(range(n),4))
        assert 5*triple==2*n*(n-2)*(n-1)*(n+1)*(3*n+1)
        assert 45*quadruple==n*(n-3)*(n-2)*(n-1)*(n+1)*(25*n+8)
        checks+=2
        if n>6:
            continue
        dist={tuple(range(n)):F(1)}
        for t in range(6):
            m=sum(prob*footrule(state) for state,prob in dist.items())
            e2=sum(prob*footrule(state)**2 for state,prob in dist.items())
            mean,var=theoretical(n,t)
            assert m==mean,(n,t,'mean')
            assert e2-m*m==var,(n,t,'variance')
            checks+=2
            dist=exact_step(dist,n)
    lo,hi=0.0,4.0
    for _ in range(110):
        m=(lo+hi)/2
        if 4*exp(m)-9-6*m<0:lo=m
        else:hi=m
    optimum=(lo+hi)/2
    assert 1.506<optimum<1.507
    assert 1.1848<profile(optimum)/(2/45)<1.1850
    checks+=2
    for n in [100,1000,10000]:
        t=int(optimum*n/2)
        mean,var=theoretical(n,t)
        if n==10000:
            assert abs(float(var)/n**3-profile(optimum))<0.0002
        checks+=1
    print('PASS: %d checks; optimal s %.13f; variance ratio %.13f' % (
        checks,optimum,profile(optimum)/(2/45)))

if __name__=='__main__':
    main()
