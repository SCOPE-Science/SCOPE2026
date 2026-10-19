"""Standalone numerical cross-checks for a two-by-two Gaussian GEPP growth law.

Python 3 standard library only. These tests do not substitute for the analytic proof.
"""
import math
import random

PI = math.pi


def simpson(func, low, high, n=512):
    assert n > 0 and n % 2 == 0
    dx = (high-low)/n
    total = func(low) + func(high)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * func(low+i*dx)
    return total*dx/3


def bounds(r, a):
    t = math.tan(a)
    lo = math.atan(r-t)
    hi = PI/2 if r == 1 else math.atan(t/(r-1))
    return lo, hi


def primitive(z, c):
    return z - c/math.sqrt(1+c*c)*math.atan2(math.sqrt(1+c*c)*math.sin(z), c*math.cos(z))


def tail_1d(r, n=512):
    assert 1 <= r < 2
    def integrand(a):
        lo,hi = bounds(r,a)
        c = r*math.cos(a)**2
        return primitive(a+hi,c)-primitive(a+lo,c)
    return 4/(PI*PI)*simpson(integrand, math.atan(r-1), PI/4, n)


def tail_2d(r, n=100):
    assert 1 <= r < 2
    def integrand(a):
        lo,hi = bounds(r,a)
        if hi <= lo: return 0.
        c2 = r*r*math.cos(a)**4
        return simpson(lambda phi: math.sin(a+phi)**2/(math.sin(a+phi)**2+c2),lo,hi,n)
    return 4/(PI*PI)*simpson(integrand,math.atan(r-1),PI/4,n)


def growth(a,b,c,d):
    if abs(a) >= abs(c):
        p,q,y1,y2 = a,c,b,d
    else:
        p,q,y1,y2 = c,a,d,b
    M = max(abs(a),abs(b),abs(c),abs(d))
    return max(1.,abs(y2-q/p*y1)/M)


def test():
    for r in [1.,1.1,1.25,1.5,1.75,1.9]:
        a,b=tail_1d(r),tail_2d(r)
        assert abs(a-b)<8e-8,(r,a,b)
        print('CDF cross-check',r,'tail',format(a,'.13g'),'quad_diff',format(a-b,'.2e'))
    for r in [1.9,1.99,1.999]:
        ratio=tail_1d(r)/(2-r)**2
        expected=1/(2*PI*PI)
        assert 0 < ratio-expected < .006,(r,ratio,expected)
        print('Endpoint',r,'ratio',format(ratio,'.12g'),'limit',format(expected,'.12g'))
    rng=random.Random(20261013)
    N=160000
    ks=[1.,1.25,1.5]
    count=[0]*len(ks)
    for _ in range(N):
        a,b,c,d=[rng.gauss(0.,1.) for j in range(4)]
        q=growth(a,b,c,d)
        for i,r in enumerate(ks):
            count[i]+=q>r
        assert 1 <= q < 2+1e-12
    for n,r in zip(count,ks):
        observed=n/N; target=tail_1d(r)
        assert abs(observed-target) < .004,(r,observed,target)
        print('Monte Carlo',r,'empirical',round(observed,6),'quadrature',round(target,6))
    print('GEPP_GROWTH_CHECK_OK')


if __name__=='__main__':
    test()
