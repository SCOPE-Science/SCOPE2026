#!/usr/bin/env python3
"""Exact-rational algebra and an independent conditional-integration check.

Requires Python 3 and scipy for the numerical integration layer only.
"""
from fractions import Fraction as F
from math import comb
from scipy.integrate import quad
from scipy.optimize import brentq


def harmonic(n):
    return sum((F(1, j) for j in range(1, n + 1)), F(0))


def covariance(m, t):
    """Proposed finite-sample maximum--exceedance covariance."""
    t = F(t)
    one = F(1)
    ans = ((m - 1) * t + 1 - harmonic(m)) * (one - t) ** (m - 1)
    ans += sum(((-1) ** (j+1) * comb(m-1, j) * max(F(0), one-(j+1)*t) ** m / (j*(j+1)) for j in range(1,m)), F(0))
    return ans


def conditional_mean(m, x):
    """E[M_m | X_1=x] via the distribution of M_{m-1}."""
    x = F(x)
    k=m-1
    if m==2:
        return max(x,1-x)
    if x >= F(1,2):
        return x
    if x == 1:
        return x
    r=x/(1-x)
    return x + (1-x)*sum(((-1)**(j+1) * comb(k,j) * max(F(0),1-j*r)**k / (j*k) for j in range(1,k+1)), F(0))


def covariance_by_integral(m, t):
    """Numerically integrate an independently derived conditional mean."""
    mu=float(harmonic(m)/m)
    # Break at changes in conditional mean's piecewise polynomials.
    cuts=sorted(set([float(t),1.0]+[j/(j+1) for j in range(1,m)]))
    cuts=[z for z in cuts if z >= t]
    if cuts[0] > t:
        cuts.insert(0,float(t))
    total=0.0
    for a,b in zip(cuts,cuts[1:]):
        if b<=a: continue
        val,err=quad(lambda x:m*(m-1)*(1-x)**(m-2)*(float(conditional_mean(m,F(x)))-mu),a,b,epsabs=1e-11,epsrel=1e-11)
        total += val
    return total


def run():
    exact_count=0
    integral_count=0
    threshold_count=0
    for m in range(2,13):
        # Boundary plus dense exact rational parameter grid.
        assert covariance(m,0)==0 and covariance(m,1)==0
        for k in range(1,50):
            t=F(k,50)
            c=covariance(m,t)
            assert c.denominator > 0
            assert (c>0) == (t>F(1,2)) if m==2 else True
            exact_count+=1
        if m >=3:
            c0=covariance(m,F(1,m))
            expr=(1-(1+harmonic(m-1))*(F(m-1,m)**(m-1)))/m
            assert c0==expr and c0<0
            assert covariance(m,F(1,2))>0
        else:
            assert covariance(2,F(1,2))==0
        points=[F(1,13),F(1,m),F(1,2),F(4,5)]
        for t in points:
            if t>=1: continue
            c=float(covariance(m,t))
            ci=covariance_by_integral(m,float(t))
            assert abs(c-ci)<2e-9, (m,t,c,ci)
            integral_count+=1
        if m==2:
            root=F(1,2)
        else:
            root=brentq(lambda x:float(covariance(m,F(x))),1/m,1/2,xtol=1e-13)
            assert (1/m)<root<.5
            assert float(covariance(m,F(root-.001/m)))<0
            assert float(covariance(m,F(root+.001/m)))>0
            threshold_count+=1
    assert conditional_mean(3,F(1,3)) == harmonic(2)/3
    assert conditional_mean(5,F(0))==harmonic(4)/4
    print(f'PASS: {exact_count} exact grid evaluations; {integral_count} independent quadrature comparisons; {threshold_count} bracketing/root checks; endpoint and conditional-mean identities.')

if __name__=='__main__': run()
