#!/usr/bin/env python3
"""Finite-instance checks for exact quantile-selected Kaczmarz dynamics.
No experimental sample is treated as a proof of the all-size or asymptotic results.
"""
from itertools import combinations
from math import comb, exp, log, pi, sqrt
from fractions import Fraction


def hyper_tail(m, c, s, low):
    n = sum(comb(c, j) * comb(m-c, s-j)
            for j in range(max(0, low), min(c, s)+1)
            if 0 <= s-j <= m-c)
    return Fraction(n, comb(m, s))


def transition(m, c, s, k):
    p = hyper_tail(m, c, s, s-k+1)
    q = 1 - hyper_tail(m, c, s, k)
    return p, q


def quantile_update(subset, x, c, k):
    # Ties within one row class do not alter the next scalar iterate.
    selected = sorted(subset, key=lambda i: (abs(x - int(i<c)), i))[k-1]
    return int(selected < c)


def exhaustive():
    checks = 0
    for m in range(3, 13):
        for c in range(1, (m - 1)//2+1):
            if 2*c >= m: continue
            for s in range(1,m+1):
                samples = list(combinations(range(m),s))
                assert len(samples) == comb(m,s)
                for k in range(1,s+1):
                    p,q = transition(m,c,s,k)
                    assert p == Fraction(sum(quantile_update(S,0,c,k) for S in samples),len(samples))
                    assert q == Fraction(sum(1-quantile_update(S,1,c,k) for S in samples),len(samples))
                    checks += 2
                    if s%2==1 and k==(s+1)//2:
                        assert p+q==1
                        assert (p==0)==(s>=2*c+1)
                        if p>0: assert p<1
                        checks += 3
                    if s%2==1 and s<=c:
                        lamb = 1-p-q
                        if k<(s+1)//2: assert lamb>0
                        elif k==(s+1)//2: assert lamb==0
                        else: assert lamb<0
                        checks += 1
                    # Reconstructed update for both Markov states, every sample.
                    for S in samples:
                        h = sum(i<c for i in S)
                        assert quantile_update(S,0,c,k) == int(h>=s-k+1)
                        assert quantile_update(S,1,c,k) == int(h>=k)
                        checks += 2
    return checks


def asymptotic_numerics():
    checks=0
    for beta in (.02,.1,.3):
        rate=-.5*log(4*beta*(1-beta))
        const=sqrt(2*beta*(1-beta)/pi)/(1-2*beta)
        for s in (101,301):
            p=sum(comb(s,j)*beta**j*(1-beta)**(s-j) for j in range((s+1)//2,s+1))
            approx=const/sqrt(s)*exp(-rate*s)
            assert .93<p/approx<1.01
            checks+=1
    m,c,s=50000,1000,11
    p,_=transition(m,c,s,6)
    assert 2.67e-8<float(p)<2.68e-8
    assert 3.73e7<1/float(p)<3.75e7
    checks+=2
    return checks

if __name__=='__main__':
    n=exhaustive()+asymptotic_numerics()
    print('VERIFIED',n,'deterministic exact-combinatorial and numerical assertions')
