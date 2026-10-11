#!/usr/bin/env python3
"""Numerical diagnostics of a mathematical two-ball-lens mixed-volume ratio.

Exact proof, definitions and quantifiers are in RESULT.md. The sampled checks
are not claimed to certify continuum-wide monotonicity.
"""
import math


def kappa(j):
    return math.pi ** (j / 2) / math.gamma(j / 2 + 1)


def simpson(f, a, b, count=8192):
    step = (b-a)/count
    s = f(a)+f(b)
    for k in range(1,count):
        s += (4 if k % 2 else 2)*f(a+k*step)
    return s*step/3


def evaluate(n,a):
    angle=math.asin(a)
    r=math.sqrt(1-a*a)
    c=2*(n-1)*kappa(n-1)/(n*kappa(n))
    first=simpson(lambda theta: math.cos(theta)**(n-1),0,angle)
    second=simpson(lambda theta:(1-a*math.sin(theta))*math.cos(theta)**(n-2),angle,math.pi/2)
    negative=simpson(lambda theta:(a-math.sin(theta))*math.cos(theta)**(n-2),angle,math.pi/2)
    reciprocal=c*(first+second/r)
    derivative=c*negative/r**3
    return 1/reciprocal,derivative


def main():
    for n in (2,3,4,5,8,20):
        limit=n/(n-1)*kappa(n)*kappa(n-2)/kappa(n-1)**2
        points=(0.001,0.2,0.5,0.8,0.999)
        vals=[evaluate(n,a) for a in points]
        assert all(1 < v < limit+1e-11 for v,d in vals)
        assert all(d < 0 for v,d in vals)
        assert all(vals[i][0] < vals[i+1][0] for i in range(4))
        for a,(value,derivative) in zip(points,vals):
            if n==2:
                exact=math.pi*math.sqrt(1-a*a)/(2*math.acos(a))
                assert abs(value-exact)<2e-9
            if n==3:
                exact=1/(math.sqrt((1-a)/(1+a))+math.asin(a)/2)
                assert abs(value-exact)<2e-9
    print('VERIFY_OK')


if __name__=='__main__':
    main()
