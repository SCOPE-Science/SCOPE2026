#!/usr/bin/env python3
"""Checks for the homogeneous cyclic spherical quotient distance law.

Standard library only. Checks are finite corroboration, not universal proofs.
"""
from fractions import Fraction
from math import acos, atan2, comb, cos, exp, gamma, pi, sin, sqrt, tan
import random


def simpson(f, a, b, n=4000):
    assert n % 2 == 0
    h = (b-a)/n
    return h/3 * (f(a)+f(b)+4*sum(f(a+(2*i-1)*h) for i in range(1,n//2+1)) + 2*sum(f(a+2*i*h) for i in range(1,n//2)))


def cdf_angle(d,p,t):
    if t <= 0: return 0.
    if t >= pi/2: return 1.
    a=pi/p
    c=cos(t)
    return simpson(lambda theta: max(0.,1-(c/cos(theta))**2)**(d-1), 0., min(t,a), 3000)/a


def cdf_radius(d,p,t):
    if t <= 0: return 0.
    if t >= pi/2: return 1.
    a=pi/p
    c=cos(t)
    def f(r):
        if r<=c: return 0.
        x=c/r
        ph=1. if x<=cos(a) else acos(x)/a
        return 2*(d-1)*r*(1-r*r)**(d-2)*ph
    return simpson(f,c,1.,16000)


def cdf_prior_d2(p,t):
    a=pi/p
    if t<=0:return 0.
    if t>=pi/2:return 1.
    if p==2 or t<=a:return p/pi*(t-sin(t)*cos(t))
    return 1-p/pi*tan(a)*cos(t)**2


def tailpoly_coeff(j):
    # Integral of sec^(2j) theta dtheta, with u=tan(angle)
    return [Fraction(comb(j-1,k),2*k+1) for k in range(j)]


def poly_eval(coeff,u):
    return sum(float(c)*u**(2*k+1) for k,c in enumerate(coeff))


def tail(d,p,eps):
    assert p>=3 and 0<eps<pi/2-pi/p
    u=tan(pi/p)
    z=sin(eps)**2
    return p/pi*sum((-1)**(j+1)*comb(d-1,j)*poly_eval(tailpoly_coeff(j),u)*z**j for j in range(1,d))


def check():
    tests=0
    # Exact identity for all polynomial tail coefficients.
    for d in range(2,13):
        for j in range(1,d):
            cs=tailpoly_coeff(j)
            for k,c in enumerate(cs):
                assert c==Fraction(comb(j-1,k),2*k+1)
                tests+=1
        for u in [Fraction(1,2),Fraction(1,1),Fraction(3,2)]:
            for w in [Fraction(1,9),Fraction(1,17)]:
                # Integrate the polynomial 1-(1-w*(1+v^2))^(d-1)
                # in v over [0,u] in two algebraically independent orders.
                a=sum((-1)**(j+1)*comb(d-1,j)*w**j*sum(Fraction(comb(j-1,k),2*k+1)*u**(2*k+1) for k in range(j)) for j in range(1,d))
                numer=[Fraction(1) if h==0 else Fraction(0) for h in range(d)]
                for h in range(d):
                    numer[h]-=comb(d-1,h)*(1-w)**(d-1-h)*(-w)**h
                quot=[]
                for h in range(d-1):
                    quot.append(numer[h]-(quot[h-1] if h else 0))
                assert quot[-1]==numer[-1]
                b=sum(c*u**(2*h+1)/Fraction(2*h+1) for h,c in enumerate(quot))
                assert a==b,(d,u,w,a,b)
                tests+=1
    # Two independent 1D integrations represent conditional angle and radial laws.
    for d in [2,3,4,6,9]:
        for p in [2,3,4,7]:
            for j in range(1,9):
                t=(pi/2)*(j/9)
                a=cdf_angle(d,p,t)
                b=cdf_radius(d,p,t)
                assert abs(a-b)<3.5e-6,(d,p,j,a,b)
                tests+=1
    # Exact published dimension-three CDF is recovered by this formula.
    for p in range(2,11):
        for j in range(1,23):
            t=pi*j/46
            assert abs(cdf_angle(2,p,t)-cdf_prior_d2(p,t))<2e-9,(p,t)
            tests+=1
    # Full finite polynomial at the diameter, not merely its leading coefficient.
    for d in [3,4,7,10]:
        for p in [3,4,6,9]:
            for c in [0.08,0.25,0.50]:
                eps=c*(pi/2-pi/p)
                assert abs(tail(d,p,eps)-(1-cdf_angle(d,p,pi/2-eps)))<3e-9,(d,p,eps)
                tests+=1
    # Distinct proof of tail exponent: compare numerical boundary mass to coefficients.
    for d in [3,5,8]:
        eps=0.012
        approx=(1-cdf_angle(d,2,pi/2-eps))/eps
        coeff=2*gamma(d)/(sqrt(pi)*gamma(d-.5))
        assert abs(approx/coeff-1)<0.035,(d,approx,coeff)
        tests+=1
        for p in [3,4,6]:
            eps=min(.01,0.1*(pi/2-pi/p))
            approx=(1-cdf_angle(d,p,pi/2-eps))/eps**2
            coeff=(d-1)*p/pi*tan(pi/p)
            assert abs(approx/coeff-1)<0.04,(d,p,approx,coeff)
            tests+=1
    # Coupling checks for both stochastic directions over a fixed parameter grid.
    for t in [0.13,0.41,0.82,1.2,1.48]:
        for d in [3,4,8]:
            assert all(cdf_angle(d,p+1,t)>cdf_angle(d,p,t) for p in range(2,8))
            tests+=6
        for p in [2,3,6]:
            assert all(cdf_angle(d+1,p,t)<cdf_angle(d,p,t) for d in range(3,8))
            tests+=5
    # Independent quotient formula on sphere: brute minimum over all deck rotations.
    rng=random.Random(1749293)
    for d,p in [(3,2),(3,5),(5,3),(6,7)]:
        thresholds=[0.28,0.65,1.0,1.38]
        counts=[0]*len(thresholds)
        N=19000
        for _ in range(N):
            z=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(d)]
            norm=sqrt(sum(abs(v)**2 for v in z))
            first=z[0]/norm
            # e_1 and the entire orbit, calculated without angle folding.
            maxdot=max((first*complex(cos(2*pi*k/p),sin(2*pi*k/p))).real for k in range(p))
            distance=acos(max(-1.,min(1.,maxdot)))
            for j,t in enumerate(thresholds):
                counts[j]+=distance<=t
        for j,t in enumerate(thresholds):
            expected=cdf_angle(d,p,t)
            assert abs(counts[j]/N-expected)<0.02,(d,p,t,counts[j]/N,expected)
            tests+=1
    print('PASS',tests,'checks; independent radial/angle quadratures, prior 3D law, exact polynomials, Monte Carlo sphere orbits')


if __name__=='__main__':check()
