"""Finite diagnostics for positive-polynomial Hardy shift averages.

Run: python checker.py (requires NumPy and SciPy).
These finite evaluations test asymptotic formulas; they do not prove them.
"""
import math
from functools import reduce
from math import gcd
import numpy as np
from scipy.optimize import minimize_scalar


def parameters(exponents, probabilities, h):
    assert len(exponents) >= 2 and len(exponents) == len(probabilities)
    assert exponents == sorted(set(exponents)) and exponents[0] >= 0
    assert all(v > 0 for v in probabilities)
    assert abs(sum(probabilities)-1) < 1e-12
    d = reduce(gcd, (k-exponents[0] for k in exponents[1:]))
    q = d // gcd(d, exponents[0]); Q = q // gcd(q, h)
    mean = sum(k*p for k,p in zip(exponents,probabilities))
    variance = sum((k-mean)**2*p for k,p in zip(exponents,probabilities))
    return d, q, Q, mean, variance


def exact_max(exponents, probabilities, n, h, grid_size=30000):
    grid = np.linspace(0, 2*math.pi, grid_size, endpoint=False)
    Z = sum(p*np.exp(1j*k*grid) for k,p in zip(exponents,probabilities))
    f = np.abs(Z)**n * np.abs(1-Z**h)
    candidates = np.argpartition(f, -min(16,grid_size))[-min(16,grid_size):]
    best = float(max(f))
    def objective(t):
        z = sum(p*complex(math.cos(k*t),math.sin(k*t)) for k,p in zip(exponents,probabilities))
        return -(abs(z)**n) * abs(1-z**h)
    step = 2*math.pi/grid_size
    for i in candidates:
        t = float(grid[i]); r=minimize_scalar(objective,bounds=(t-step,t+step),method='bounded',options={'xatol':1e-13})
        best=max(best,-float(r.fun))
    return best


def leading(exponents, probabilities, h):
    d,q,Q,mu,v = parameters(exponents,probabilities,h)
    if Q == 1:
        return 0., h*mu/math.sqrt(math.e*v)
    if Q%2 == 0:
        return 2., 0.
    B=2*math.cos(math.pi/(2*Q))
    coeff=(h*mu)**2*math.sin(math.pi/Q)**2/(2*B**3*v)
    return B,coeff


def check():
    cases = [([0,1],[.5,.5]),([1,3],[.4,.6]),([1,4],[.5,.5]),
             ([2,4],[.6,.4]),([2,8],[.2,.8]),([1,6],[.2,.8]),
             ([2,5,8],[.15,.6,.25]),([0,5,10],[.2,.4,.4])]
    counter=0
    for exps,probs in cases:
        for h in (1,2,3,4,5):
            d,q,Q,mu,v=parameters(exps,probs,h)
            B,C=leading(exps,probs,h)
            for j in range(d):
                z=sum(p*complex(math.cos(2*math.pi*j*k/d),math.sin(2*math.pi*j*k/d)) for k,p in zip(exps,probs))
                assert abs(abs(z)-1)<1e-11
                counter+=1
            if Q%2==0:
                assert abs(exact_max(exps,probs,32,h)-2)<1e-10
                counter+=1
            elif Q==1:
                n=800
                observed=exact_max(exps,probs,n,h)*math.sqrt(n)
                assert abs(observed-C) <= .04*C + 1e-6, (exps,h,Q,observed,C)
                counter+=1
            else:
                n=5000
                observed=exact_max(exps,probs,n,h)
                assert 0 < observed-B < C/n*1.2 + 1e-8,(exps,h,Q,observed-B,C/n)
                assert abs(n*(observed-B)-C)<.055*C+1e-5,(exps,h,Q,observed,B,C)
                counter+=2
    print(f"PASS: {counter} deterministic phase-geometry and norm diagnostics")


if __name__ == '__main__':
    check()
