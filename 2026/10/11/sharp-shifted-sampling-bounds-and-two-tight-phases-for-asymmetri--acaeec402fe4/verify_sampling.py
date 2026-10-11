#!/usr/bin/env python3
"""Independent numerical consistency checks for explicit exponential sampling formulas.

Runs with the Python standard library only. Finite checks complement the analytic proof.
"""
import cmath
import math


def kernel(a, b, t):
    return math.exp(a * t) if t < 0 else math.exp(-b * t)


def constants(a, b):
    r, s = math.exp(-b), math.exp(-a)
    if abs(a-b) < 1e-14:
        c = a
        u = (1-r**4)/c-4*r*r
        v = 2*r*(1+r*r)-2*r*(1-r*r)/c
    else:
        h = (a+b)/(2*(a-b))
        u = h*((1-r*r)*(1+s*s)/b-(1-s*s)*(1+r*r)/a)
        v = 2*h*(r*(1-s*s)/a-s*(1-r*r)/b)
    assert u > v > 0
    return r, s, u, v


def endpoint(a, b, y):
    r, s, u, v = constants(a, b)
    P = math.exp(-b*y)-r*s*math.exp(a*y)
    Q = s*(math.exp(a*y)-math.exp(-b*y))
    return ((P+Q)**2/(u+v), (P-Q)**2/(u-v))


def autocorrelation(a, b, n):
    n = abs(n)
    if abs(a-b) < 1e-14:
        return math.exp(-a*n)*(n+1/a)
    return (a+b)/(2*(a-b))*(math.exp(-b*n)/b-math.exp(-a*n)/a)


def phases(a, b):
    r, s, u, v = constants(a, b)
    q = math.sqrt(u*u-v*v)
    lo, hi = (u-q)/v, (u+q)/v
    fun = lambda L: math.log((L+s)/(s*(1+r*L)))/(a+b)
    y0 = math.log((1+s)/(s*(1+r)))/(a+b)
    return fun(lo), y0, fun(hi)


def run():
    # Avoid near-equal parameters where subtractive cancellation spoils floats.
    pairs = [(1,1),(.5,2),(2,.5),(.25,.25),(3,4),(1.5,.75)]
    checked = 0
    for a,b in pairs:
        r,s,u,v = constants(a,b)
        low,zero,high = phases(a,b)
        assert 0<low<zero<high<1
        assert abs(endpoint(a,b,low)[0]-endpoint(a,b,low)[1]) < 2e-11
        assert abs(endpoint(a,b,high)[0]-endpoint(a,b,high)[1]) < 2e-11
        assert min(endpoint(a,b,zero)) < 2e-27
        best = min(endpoint(a,b,0))
        for k in range(1,100):
            assert min(endpoint(a,b,k/100)) < best + 3e-12
        # Verify the Zak transform and translate Gramian against convergent
        # uncombined Fourier series, rather than merely re-evaluating ratios.
        for y in (0.0, .17, low, zero, high, .93):
            P = math.exp(-b*y)-r*s*math.exp(a*y)
            Q = s*(math.exp(a*y)-math.exp(-b*y))
            for theta in (0,.43,1.41,2.31,math.pi):
                c = math.cos(theta)
                denominator = (1+r*r-2*r*c)*(1+s*s-2*s*c)
                Z2 = (P*P+Q*Q+2*P*Q*c)/denominator
                G = (u+v*c)/denominator
                Zd = sum(kernel(a,b,y-j)*cmath.exp(1j*j*theta)
                         for j in range(-320,321))
                Gd = autocorrelation(a,b,0)+sum(
                    2*autocorrelation(a,b,n)*math.cos(n*theta)
                    for n in range(1,321))
                assert abs(abs(Zd)**2-Z2)<2e-9,(a,b,y,theta)
                assert abs(Gd-G)<2e-9,(a,b,y,theta)
                checked += 1
        h=(1+s)*math.exp(-b*zero)
        lead = (a+b)**2*h*h/(u-v)
        for delta in (.0005,.0001):
            left=min(endpoint(a,b,zero-delta))
            right=min(endpoint(a,b,zero+delta))
            assert abs((left+right)/(2*delta*delta)/lead-1)<3e-5
    print('PASS',checked,'Zak/Gram frequency tests; tight phases; sharp lower bounds; quadratic onset')


if __name__=='__main__':
    run()
