#!/usr/bin/env python3
"""Deterministic finite checks of Fourier similarity and projection norms."""
import cmath, math, random
from math import sqrt

def h_eval(theta, alpha, a, b, coeffs):
    return sum(v*cmath.exp(1j*k*theta)/(b-a*cmath.exp(1j*k*alpha)) for k,v in coeffs.items())

def c_eval(theta, coeffs):
    return sum(v*cmath.exp(1j*k*theta) for k,v in coeffs.items())

def check():
    rng=random.Random(42621)
    alpha=math.pi*math.sqrt(2.0)/3.0
    assertions=0
    for j in range(140):
        a=0.4+2*rng.random(); b=0.4+2*rng.random()
        if abs(a-b)<0.02: b+=0.04
        coeffs={k: complex(rng.uniform(-1,1),rng.uniform(-1,1)) for k in (-3,-1,0,1,4)}
        for _ in range(22):
            theta=2*math.pi*rng.random()
            h=h_eval(theta,alpha,a,b,coeffs)
            lhs=b*h-a*h_eval(theta+alpha,alpha,a,b,coeffs)
            assert abs(lhs-c_eval(theta,coeffs))<2e-10, (j,theta,lhs)
            assertions+=1
    # Two-mode exact supremum and Riesz projection row norm.
    for j in range(50):
        a=0.5+rng.random(); b=0.5+rng.random()
        c0=complex(rng.uniform(-1,1),rng.uniform(-1,1))
        c1=complex(rng.uniform(-1,1),rng.uniform(-1,1))
        n=rng.choice([-3,-2,-1,1,2,3])
        q0=c0/(b-a);q1=c1/(b-a*cmath.exp(1j*n*alpha))
        exact=abs(q0)+abs(q1)
        grid=max(abs(q0+q1*cmath.exp(1j*n*2*math.pi*t/3500)) for t in range(3500))
        assert grid <= exact+1e-12
        assert exact-grid < 0.006  # deterministic dense-grid corroboration
        assertions+=2
    # At collision, zero harmonic is the sole obstruction.
    for j in range(200):
        r=0.3+2*rng.random()
        coeffs={k: complex(rng.uniform(-1,1),rng.uniform(-1,1)) for k in (-5,-3,-1,1,2)}
        for _ in range(6):
            x=2*math.pi*rng.random()
            h=h_eval(x,alpha,r,r,coeffs)
            assert abs(r*(h-h_eval(x+alpha,alpha,r,r,coeffs))-c_eval(x,coeffs))<5e-10
            assertions+=1
    return assertions

if __name__=='__main__':
    print('PASS',check(),'finite deterministic checks; analytic proof independent')
