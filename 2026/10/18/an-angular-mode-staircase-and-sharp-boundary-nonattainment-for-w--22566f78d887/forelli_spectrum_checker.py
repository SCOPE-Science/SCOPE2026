#!/usr/bin/env python3
"""Numerical checks of the beta-moment singular spectrum of a disk integral kernel.

These finite checks supplement, and do not replace, the analytical proof.
"""
import math
import random


def sig(n, a, b, c):
    logv = (math.lgamma(n+c)-math.lgamma(c)-math.lgamma(n+1)
            + (math.lgamma(n+1)+math.lgamma(2*a+1)-math.lgamma(n+2*a+2))/2
            + (math.lgamma(n+1)+math.lgamma(2*b+1)-math.lgamma(n+2*b+2))/2)
    return math.exp(logv)


def thresh(n, a, b):
    return math.sqrt((n+2*a+2)*(n+2*b+2))-n


def verify():
    rng = random.Random(38261)
    nchecks = 0
    for _ in range(120):
        a = rng.uniform(-.4, 4)
        b = rng.uniform(-.4, 4)
        if abs(a-b) < .01:
            b += .13
        L = a+b+2
        c = rng.uniform(.03, L*.999)
        assert L > 0
        s = [sig(n,a,b,c) for n in range(150)]
        rr = [(n+c)/math.sqrt((n+2*a+2)*(n+2*b+2)) for n in range(149)]
        for n in range(149):
            assert math.isclose(s[n+1]/s[n],rr[n],rel_tol=4e-12)
            assert (s[n+1] > s[n]) == (c > thresh(n,a,b)) or abs(s[n+1]-s[n])<2e-12
            nchecks += 1
        cs=[thresh(n,a,b) for n in range(149)]
        assert all(cs[i]<cs[i+1]+1e-12 for i in range(148))
        assert cs[0]<L and cs[-1]<L
        peak=max(range(150),key=s.__getitem__)
        if peak<149:
            assert all(s[peak]>=x*(1-2e-12) for x in s)
            nchecks+=1
    # Exact benchmark: a=0,b=1,c=2, L=3, c_0=sqrt(8); optimum n=0.
    assert math.isclose(sig(0,0,1,2),math.sqrt(1/3),rel_tol=1e-12)
    assert math.isclose(thresh(0,0,1),math.sqrt(8),rel_tol=1e-12)
    # Symmetric critical case has constant singular values.
    for a in [0,.5,1,2.4]:
        L=2*a+2
        for n in [0,1,3,20,140]:
            assert math.isclose(sig(n,a,a,L),1/(2*a+1),rel_tol=1e-12)
            nchecks+=1
    # Boundary nonattainment for asymmetric weights and positive power law.
    for a,b in [(0,1),(.1,3),(-.3,.6)]:
        L=a+b+2
        C=math.sqrt(math.gamma(2*a+1)*math.gamma(2*b+1))/math.gamma(L)
        xs=[sig(n,a,b,L) for n in (1,10,100,1000)]
        assert all(xs[i]<xs[i+1] for i in range(3))
        assert abs(xs[-1]/C-1)<.05
        nchecks+=1
    print('VERIFY_OK',nchecks)

if __name__=='__main__':
    verify()
