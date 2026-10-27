#!/usr/bin/env python3
"""Finite exact-rational checks of an adjacent marked M/M/1 pair theorem.

The proof is in RESULT.md. Finite calculations and simulation here do not
establish the infinite sums, stochastic independence or general quantifiers.
"""
from fractions import Fraction as F
from random import Random


def forms(r, p):
    u = 1-p
    a = 1/(1+r*p)
    d = 1/(1+r)
    b = r/(1+r)
    s0 = (1-r)/(1-p) * (a/(1-r*u*a) - p*d/(1-r*u*d))
    s1 = (1-r) * (a + r*a*a/(1-r*u*a))
    j0 = (1-r)*a/(1-r*u*d) * (d+b*a/(1-r*u*a))
    s = (1-r)*(1+2*p*r)/((1+p*r)*(1-r+2*p*r))
    j = s/(1+p*r)
    cov = 2*p*r*r*(1-r)*(1+2*p*r)/((1+p*r)**2*(1-r+2*p*r)**2)
    corr = 2*r/(1+r+2*p*r)
    return u, a, d, b, s0, s1, j0, s, j, cov, corr


def exhaustive_rational_tests():
    checks = 0
    for r in [F(1,20), F(1,6), F(1,3), F(1,2), F(3,5), F(4,5), F(9,10), F(19,20)]:
        for p in [F(1,20), F(1,10), F(1,3), F(1,2), F(2,3), F(4,5), F(19,20)]:
            u,a,d,b,s0,s1,j0,s,j,cov,corr = forms(r,p)
            for x,y in [(s0,s),(s1,s),(j0,j),(j-s*s,cov),
                         (cov/(s*(1-s)),corr), (j/s,1/(1+p*r))]:
                assert x==y
                checks+=1
            for flag in [0<s<1,0<j<s,cov>0,0<corr<1,
                         1-2*s+j>=0,s-j>=0]:
                assert flag
                checks+=1
            # Direct nonnegative finite sum over the pre-first queue length
            # and over the number of potential exponential-service events
            # preceding the next Poisson arrival.
            L=50
            trunc = F(0)
            for q in range(L+1):
                moment = d**(q+1)
                for g in range(q+1):
                    moment += b*d**g * a**(q+1-g)
                trunc += (1-r)*(r*u)**q * a*moment
            rem = (1-r)*a*(r*u)**(L+1)/(1-r*u)
            assert trunc <= j <= trunc + rem
            checks+=2
            assert (1-r)/(1-r+2*p*r)*((1+2*p*r)/(1+p*r))==s
            checks+=1
    return checks


def poisson(rng, mean):
    # Jump-time construction; no third-party numerical library.
    t=0
    n=0
    while True:
        t+=rng.expovariate(1.0/mean)
        if t>=1:
            return n
        n+=1


def simulate(r, p, n, seed):
    rng=Random(seed)
    sum0=sum1=sumboth=0
    for _ in range(n):
        # Stationary queue seen by the first of the consecutive arrivals.
        q=0
        while rng.random()<r:
            q+=1
        prior_mark=[rng.random()<p for _ in range(q)]
        remaining=[rng.expovariate(1.) for _ in range(q+1)]
        depart=[]
        elapsed=0.
        for x in remaining:
            elapsed+=x
            depart.append(elapsed)
        d0=elapsed
        interarrival=rng.expovariate(r)
        d1=max(interarrival,d0)+rng.expovariate(1.)
        inf0=any(prior_mark)
        inf1=any(label and leave>interarrival
                 for label,leave in zip(prior_mark,depart))
        # There are no intervening arrivals: the tagged customers are
        # consecutive in the original arrival-index order and both forced safe.
        t=interarrival
        while True:
            t+=rng.expovariate(r)
            if t>=d1: break
            label=rng.random()<p
            if label:
                inf1=True
                if t<d0: inf0=True
        a0=not inf0
        a1=not inf1
        sum0+=a0
        sum1+=a1
        sumboth+=a0 and a1
    u,a,d,b,s0,s1,j0,s,j,cov,corr=forms(r,p)
    return r,p,n,sum0/n,sum1/n,sumboth/n,float(s),float(j)


def main():
    checks=exhaustive_rational_tests()
    print(f"PASS: {checks} exact rational identities, nonnegativity checks and bounded partial sums")
    print("PASS: exact covariance and correlation are strictly positive on the rational test grid")
    print("Independent path-simulation estimates (finite checks, not proofs):")
    for j,(r,p) in enumerate([(0.3,0.2),(0.8,0.4),(0.92,0.7)]):
        vals=simulate(r,p,12000,20261024+j)
        print('r=%.2f p=%.2f n=%d P(safe first)=%.5f P(safe second)=%.5f P(both)=%.5f exact marginal=%.5f exact joint=%.5f' % vals)
        assert max(abs(vals[3]-vals[6]),abs(vals[4]-vals[6]),abs(vals[5]-vals[7]))<.035
    print("PASS: three independent finite Monte Carlo comparisons, within loose sampling tolerances")


if __name__=='__main__':
    main()
