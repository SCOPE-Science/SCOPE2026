#!/usr/bin/env python3
"""Reproduce selected dispersion-resonance and scaling checks (Python stdlib only)."""
import math
import random


def residual(B, n, x):
    return n * (1.0 + B*x*x)*math.tanh(x) - (1.0 + B*n*n*x*x)*math.tanh(n*x)


def root(B, n):
    assert 0 < B < 1/3 and n >= 2
    delta = 1/3 - B
    rough = min(math.sqrt(45*delta/(n*n+1)), 1/math.sqrt(B*n))
    lo = rough * 0.05
    hi = max(rough * 20, 2.0/math.sqrt(B*n))
    while residual(B, n, lo) <= 0: lo *= 2
    while residual(B, n, hi) >= 0: hi *= 2
    for _ in range(90):
        mid = (lo + hi) / 2
        if residual(B, n, mid) > 0: lo = mid
        else: hi = mid
    return (lo + hi) / 2


def f(B, x):
    if x == 0: return 1.0
    return (1 + B*x*x)*math.tanh(x)/x


def long_short_root(B):
    lo, hi = 0.2, max(4.0, 2.0/B)
    while f(B, lo) > 1: lo *= 0.5
    while f(B, hi) < 1: hi *= 2
    for _ in range(90):
        mid=(lo+hi)/2
        if f(B, mid) < 1: lo=mid
        else:hi=mid
    return (lo+hi)/2


def profile(alpha):
    lo = 1e-14
    hi=max(2,2/math.sqrt(alpha),2/alpha)
    for _ in range(90):
        mid=(lo+hi)/2
        if alpha*mid*mid < math.tanh(mid):lo=mid
        else:hi=mid
    return (lo+hi)/2


def main():
    checks = 0
    for B in [0.0001,0.01,0.1,0.2,0.32,1/3-0.0001]:
        yy=long_short_root(B)
        prev=0.0
        for n in [2,3,4,5,10,30,100,1000]:
            x=root(B,n)
            y=n*x
            assert abs(f(B,x)-f(B,y)) < 2e-9, (B,n,'matching')
            assert prev < y < yy, (B,n,'monotone')
            prev=y
            checks+=2
        assert abs(f(B,yy)-1)<1e-10
        checks+=1
    rng=random.Random(1345227)
    for _ in range(200):
        B=math.exp(rng.uniform(math.log(0.0001),math.log(0.32)))
        n=rng.randint(2,300)
        x=root(B,n)
        assert abs(f(B,x)-f(B,n*x)) < 5e-8
        checks+=1
    for delta in [1e-4,1e-5]:
        B=1/3-delta
        for n in [2,3,5,10,100,1000]:
            x=root(B,n)
            scaled=(n*n+1)*x*x/(45*delta)
            assert abs(scaled-1)<0.001, (delta,n,scaled)
            checks+=1
    for B,tol in [(1e-3,0.002),(1e-4,0.0002)]:
        for n in [2,3,10,100,1000,100000]:
            x=root(B,n)
            xx=profile(n*B)
            assert abs(x/xx-1)<tol, (B,n,x/xx)
            checks+=1
    # Fixed-tension cubic coefficient, verified at large harmonic orders.
    for B in [0.05,0.15,0.3]:
        yy=long_short_root(B)
        h=1e-5
        fp=(f(B,yy+h)-f(B,yy-h))/(2*h)
        coefficient=(B-1/3)*yy*yy/fp
        n=10000
        x=root(B,n)
        ratio=(x-yy/n)*n**3/coefficient
        assert abs(ratio-1)<0.001, (B,ratio)
        checks+=1
    print('VERIFICATION_OK', checks)

if __name__=='__main__':main()
