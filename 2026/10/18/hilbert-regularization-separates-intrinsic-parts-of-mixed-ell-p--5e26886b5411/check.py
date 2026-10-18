#!/usr/bin/env python3
"""Finite diagnostic checks for mixed ell_p triangular defects.

The mathematical proof is analytic; this code samples inputs and tests
numerical consequences without claiming exhaustive verification.
"""
import math
import random

def norm(x, p):
    return sum(abs(t)**p for t in x)**(1/p)

def defect(x, y, p):
    return norm(x, p)+norm(y, p)-norm([a+b for a,b in zip(x,y)], p)

def run():
    rng=random.Random(20261013)
    for n in (2,3):
        for p in (1.2,1.5,1.9,2.1,3.0,4.0):
            k=(p-1)*n**(-(p-1)*(1/p-.5)) if p<2 else (p-1)*n**((p-1)*(.5-1/p))
            for _ in range(1000):
                x=[rng.gauss(0,1) for _ in range(n)]
                y=[rng.gauss(0,1) for _ in range(n)]
                dp=defect(x,y,p)
                d2=defect(x,y,2)
                if p<2:
                    assert dp >= k*d2-1e-9
                else:
                    assert dp <= k*d2+1e-9
    for p in (1.5,3.0,4.0):
        A=(1-2**(1-p))/p
        for t in (0.1, 0.03, 0.01):
            x=(1.0,0.0)
            y=(1.0,t)
            expected=A*t**p
            measured=defect(x,y,p)
            assert abs(measured/expected-1)<0.05
    for a,b in ((0.01,1),(0.1,1),(0.1,0.2)):
        lower=math.log(b*(1+a)/(a*(1+b)))
        upper=math.log(b/a)
        assert 0<=lower<=upper
    print('Finite diagnostics passed. These are not universal proofs.')

if __name__=='__main__':
    run()
