#!/usr/bin/env python3
"""Supplementary arithmetic tests for the cubic causal-exponential Gabor theorem.
No external packages or network access. These tests do not prove the universal result.
"""
import cmath
import math
from fractions import Fraction


def pval(r, u):
    v = (1 + r) * u - r
    return v**3 - 3*r*v + r*r-r


def zval(r, c, x, theta):
    z = r*cmath.exp(1j*theta)
    u = c+x
    # Exact generating function sum_n (n+u)^3 z^n.
    value = (u**3/(1-z) + 3*u*u*z/(1-z)**2
             + 3*u*z*(1+z)/(1-z)**3 + z*(1+4*z+z*z)/(1-z)**4)
    return (r**x)*value


def roots(r):
    crit=(r+math.sqrt(r))/(1+r)
    lo=0.0
    hi=max(2.0,crit+2.0)
    assert pval(r,crit)<0 and pval(r,hi)>0
    for _ in range(100):
        mid=(lo+hi)/2
        if pval(r,mid)>0:
            hi=mid
        else:
            lo=mid
    high=(lo+hi)/2
    low=None
    if r>2-math.sqrt(3)+1e-10:
        lo,hi=0.0,crit
        assert pval(r,lo)>0
        for _ in range(100):
            mid=(lo+hi)/2
            if pval(r,mid)>0:lo=mid
            else:hi=mid
        low=(lo+hi)/2
    return low,high


def main():
    checks=0
    # Exact finite-sum algebra checks for the Euler generating identity.
    for ra in [Fraction(1,7),Fraction(1,3),Fraction(1,2),Fraction(4,5)]:
        for ua in [Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(5,4),Fraction(9,4)]:
            z=-ra
            s0=1/(1-z);s1=z/(1-z)**2
            s2=z*(1+z)/(1-z)**3
            s3=z*(1+4*z+z*z)/(1-z)**4
            summed=ua**3*s0+3*ua**2*s1+3*ua*s2+s3
            assert summed==pval(ra,ua)/(1+ra)**4
            assert pval(ra,ua+1)/(1+ra)**4==(summed-ua**3)/(-ra)
            checks+=2
    r0=2-math.sqrt(3)
    for r in [0.015,0.07,0.16,0.21,0.265,0.27,0.3,0.42,0.5,0.67,0.88,0.97]:
        low,high=roots(r)
        crit=(r+math.sqrt(r))/(1+r)
        assert high>crit
        if r<r0: assert low is None and high<1
        if r>r0:
            assert 0<low<crit<1<high<low+1
        assert abs(pval(r,high))<2e-12
        checks+=6
        for x in [0,0.14,0.41,0.73,0.999]:
            for c in [high+0.005,high+0.1,high+1.0]:
                # In stable parameter range no grid point is zero.
                for j in range(36):
                    theta=2*math.pi*j/36
                    assert abs(zval(r,c,x,theta))>1e-11
                    checks+=1
        # The quadratic onset constant is checked directly at the zero boundary.
        v=(1+r)*high-r
        K=9*(v*v-r)**2/(1+r)**6
        for delta in [1e-4,3e-5,1e-5]:
            at_zero=abs(zval(r,high+delta,0,math.pi))**2
            assert abs(at_zero/(K*delta*delta)-1)<0.001
            checks+=1
    # Additional exact points: r=1/2, the transition at r=2-sqrt(3).
    low,high=roots(0.5)
    assert 0.2<low<0.23 and 1.19<high<1.21
    assert abs(pval(r0,1.0))<1e-13 and abs(pval(r0,0.0))<1e-13
    checks+=3
    print('PASS:',checks,'supplementary checks')

if __name__=='__main__':
    main()
