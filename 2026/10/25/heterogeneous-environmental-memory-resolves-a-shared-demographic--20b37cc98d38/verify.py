#!/usr/bin/env python3
"""Exact-rational tests for a two-site linear environmental-filter model."""
from fractions import Fraction as F
from math import isqrt


def square_root_fraction(z):
    assert z >= 0
    a, b = isqrt(z.numerator), isqrt(z.denominator)
    assert a*a == z.numerator and b*b == z.denominator
    return F(a, b)


def moments(lam, alpha, variance):
    g0 = variance * (1+lam*alpha) / ((1-lam*lam)*(1-alpha*alpha)*(1-lam*alpha))
    g1 = g0*(lam+alpha)/(1+lam*alpha)
    g2 = (lam+alpha)*g1-lam*alpha*g0
    return g0, g1, g2


def roots_of_moments(g):
    g0,g1,g2 = g
    r, q = g1/g0, g2/g0
    t = (r*r-q)/(1-r*r)
    s = r*(1+t)
    d = square_root_fraction(s*s-4*t)
    return tuple(sorted(((s-d)/2, (s+d)/2)))


def cross_cov(lam, a, b, tau):
    return tau*(1-lam*lam*a*b)/((1-a*b)*(1-lam*lam)*(1-lam*a)*(1-lam*b))


def recover(a,b,lam,var1,var2,tau):
    G1,G2 = moments(lam,a,var1), moments(lam,b,var2)
    roots1,roots2 = roots_of_moments(G1), roots_of_moments(G2)
    common = set(roots1).intersection(roots2)
    assert len(common)==1
    ll=next(iter(common))
    aa=next(z for z in roots1 if z!=ll) if roots1[0]!=roots1[1] else ll
    bb=next(z for z in roots2 if z!=ll) if roots2[0]!=roots2[1] else ll
    v1=G1[0]*(1-ll*ll)*(1-aa*aa)*(1-ll*aa)/(1+ll*aa)
    v2=G2[0]*(1-ll*ll)*(1-bb*bb)*(1-ll*bb)/(1+ll*bb)
    C=cross_cov(lam,a,b,tau)
    tt=C*(1-aa*bb)*(1-ll*ll)*(1-ll*aa)*(1-ll*bb)/(1-ll*ll*aa*bb)
    assert (ll,aa,bb,v1,v2,tt)==(lam,a,b,var1,var2,tau)
    assert G1==moments(a,lam,var1)
    assert G2==moments(b,lam,var2)
    return G1,G2,C


def main():
    checks=0
    examples=[
        (F(1,2),F(1,4),F(3,4),F(1),F(4),F(1)),
        (F(1,3),F(1,3),F(2,3),F(3),F(5),F(-1)),
        (F(1,5),F(3,5),F(1,5),F(7),F(9),F(0)),
        (F(4,5),F(1,5),F(2,5),F(2),F(3),F(1)),
        (F(1,10),F(7,10),F(9,10),F(11),F(13),F(-2)),
    ]
    for lam,a,b,u,v,tau in examples:
        assert a!=b and tau*tau<u*v
        recover(a,b,lam,u,v,tau)
        checks += 1
    # Distinct parameter tuples with equal full univariate Gaussian laws.
    l,a=F(1,3),F(2,3)
    g=moments(l,a,F(7))
    assert g==moments(a,l,F(7))
    checks+=1
    # Equal site noise colours: swapping the shared biological and environmental
    # poles preserves all auto and cross spectra, not just the first few moments.
    t=F(2,5);l=F(3,5)
    assert moments(l,t,F(2))==moments(t,l,F(2))
    assert moments(l,t,F(3))==moments(t,l,F(3))
    assert cross_cov(l,t,t,F(1))==cross_cov(t,l,l,F(1))
    checks+=3
    # First example's exact moments and its cross-site contemporaneous covariance.
    m1,m2,c=recover(F(1,4),F(3,4),F(1,2),F(1),F(4),F(1))
    assert m1==(F(64,35),F(128,105),F(24,35))
    assert m2==(F(2816,105),F(512,21),F(2144,105))
    assert c==F(3904,1365)
    checks+=3
    # A grid of many valid rational parameter choices, including coincident poles.
    for l in [F(1,5),F(1,2),F(3,4)]:
        for a in [F(1,5),F(2,5),F(3,5)]:
            for b in [F(1,5),F(2,5),F(3,5)]:
                if a==b:continue
                recover(a,b,l,F(1),F(4),F(1))
                checks+=1
    print('PASS: %d exact recovery/invariance checks; five parameter examples and a rational grid.'%checks)
    print('Example autocovariances: site1=%s; site2=%s; cross lag0=%s'%(m1,m2,c))


if __name__=='__main__':main()
