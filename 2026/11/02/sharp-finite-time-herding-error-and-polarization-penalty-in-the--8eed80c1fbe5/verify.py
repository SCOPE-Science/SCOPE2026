#!/usr/bin/env python3
"""Exact rational finite-time checker for complete-mixing Bernoulli-action opinion dynamics.
All enumerations involve finite-time small systems only; infinite-time conclusions use the proof.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product

def formula(x0, alpha, t):
    n = len(x0)
    p0 = sum(x0, F(0)) / n
    d0 = sum((z-p0)**2 for z in x0)
    r = 1 - alpha**2 / n
    s = (1-alpha)**2
    h0 = p0*(1-p0)
    h = h0*r**t + alpha**2*d0/n**2 * (r**t-s**t)/(r-s)
    return h

def step(states, x0, alpha, t):
    n = len(x0); p0 = sum(x0, F(0))/n
    nextstates = defaultdict(F)
    for p, mass in states.items():
        probs = [p+(1-alpha)**t*(x-p0) for x in x0]
        assert all(F(0) <= x <= F(1) for x in probs)
        # independent conditional Bernoulli actions: exact Poisson-binomial count
        dist = [F(1)]
        for x in probs:
            out = [F(0)]*(len(dist)+1)
            for k,w in enumerate(dist):
                out[k] += w*(1-x)
                out[k+1] += w*x
            dist=out
        for k,w in enumerate(dist):
            nextstates[(1-alpha)*p+alpha*F(k,n)] += mass*w
    assert sum(nextstates.values(),F(0))==1
    return dict(nextstates)

def check(x0,alpha,tmax):
    n=len(x0)
    p0=sum(x0,F(0))/n
    states={p0:F(1)}
    for t in range(tmax+1):
        E=sum((w*p for p,w in states.items()),F(0))
        h=sum((w*p*(1-p) for p,w in states.items()),F(0))
        assert E==p0,(x0,alpha,t,'martingale',E,p0)
        assert h==formula(x0,alpha,t),(x0,alpha,t,'heterozygosity',h,formula(x0,alpha,t))
        second=sum((w*p*p for p,w in states.items()),F(0))
        assert second-p0*p0==p0*(1-p0)-h
        for xi in x0:
            d=(1-alpha)**t*(xi-p0)
            exi2=sum((w*(p+d)**2 for p,w in states.items()),F(0))
            assert exi2-(p0+d)**2==p0*(1-p0)-h
            expected_error = h+d*d
            # conditional terminal bit has conditional success probability p_t
            direct_error=sum((w*((p+d)**2-2*(p+d)*p+p) for p,w in states.items()),F(0))
            assert direct_error==expected_error
        if t<tmax: states=step(states,x0,alpha,t)
    return tmax+1

def main():
    tests = 0; steps=0
    for n in range(2,6):
        cases = [[F(i,n+2) for i in range(1,n+1)],
                 [F(1,3)]*n,
                 [F(i%2) for i in range(n)],
                 [F(0)]*(n-1)+[F(1,2)],
                 [F(1)]*n]
        for x0 in cases:
            for alpha in (F(1,4),F(1,2),F(3,4),F(1)):
                tmax=4 if n<=4 else 3
                steps+=check(x0,alpha,tmax)
                tests+=1
    # for same mean, a fully heterogeneous vector has a larger exact error
    for n in (2,3,4,5):
        p=F(1,n)
        hetero=[F(1)]+[F(0)]*(n-1)
        homo=[p]*n
        for alpha in (F(1,4),F(1,2),F(1)):
            for t in range(1,8):
                assert formula(hetero,alpha,t)>formula(homo,alpha,t)
    # Extremal dispersion at fixed mean: rational grid profiles, n<=4.
    maxima_checked=0
    for n in (2,3,4):
        for xx in product((F(0),F(1,2),F(1)),repeat=n):
            S=sum(xx,F(0)); m=S.numerator//S.denominator; theta=S-m
            p=S/n; D=sum((x-p)**2 for x in xx)
            extremal=m+theta*theta-n*p*p
            assert D<=extremal,(n,xx,D,extremal)
            maxima_checked+=1
    print('PASS',tests,'exact finite-state configurations,',steps,'time slices;',
          maxima_checked,'dispersion-boundary grid profiles; individual/covariance/strict comparisons PASS')

if __name__=='__main__':main()
