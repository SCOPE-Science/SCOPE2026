#!/usr/bin/env python3
"""Independent numerical corroborations of the exact Haar-qutrit orbit formula.

Python standard library only. The finite computations do not prove the theorem.
"""
import math
import random


def exact_minimum(p0, p1, p2):
    y, s, d = p1, p0 + p2, p0 - p2
    a = s*s - d*d
    if a > 0:
        c = -y*s/a
        if c >= -1:
            return max(0.0, y*y+d*d-y*y*s*s/a)
    return (2*y-1)**2


def phase_grid_minimum(p0, p1, p2, nodes=5000):
    result = 1.0
    for j in range(nodes+1):
        c = math.cos(math.pi*j/nodes)
        val = (p1+(p0+p2)*c)**2+(p0-p2)**2*(1-c*c)
        result = min(result, val)
    return result


def integral_cdf(h, nodes=16000):
    if h <= 0: return 0.0
    if h >= 1: return 1.0
    # w=h+(1-h)t**2 removes the square-root endpoint cusp.
    def f(t):
        w = h+(1-h)*t*t
        s = (1+w)/2
        disc = max(0.0,(1-h*h)*(w*w-h*h))
        den = w+h*h+math.sqrt(disc)
        root = math.sqrt(2)*h*s/math.sqrt(den)
        return 2*(1-h)*t*root
    dt = 1.0/nodes
    v = f(0)+f(1)
    for j in range(1,nodes):
        v += (4 if j % 2 else 2)*f(j*dt)
    return h+v*dt/3


def run():
    assert integral_cdf(0)==0 and integral_cdf(1)==1
    table = {0.1:0.20206389493451052,0.2:0.3742906235963266,
             0.5:0.7584183762028036}
    for h, expected in table.items():
        assert abs(integral_cdf(h)-expected)<4e-8,(h,integral_cdf(h))
    rng=random.Random(8020)
    for _ in range(30):
        a,b,c=[rng.expovariate(1.0) for j in range(3)]
        s=a+b+c
        p0,p1,p2=a/s,b/s,c/s
        assert abs(exact_minimum(p0,p1,p2)-phase_grid_minimum(p0,p1,p2))<4e-7
    # Direct sampling independent of the one-dimensional formula.
    n=110000
    counts=[0,0,0]
    hs=list(table)
    for _ in range(n):
        a,b,c=[rng.expovariate(1.0) for j in range(3)]
        s=a+b+c
        f=exact_minimum(a/s,b/s,c/s)
        for i,h in enumerate(hs):
            if f<=h*h: counts[i]+=1
    for i,h in enumerate(hs):
        assert abs(counts[i]/n-table[h])<0.011,(h,counts[i]/n,table[h])
    # Continuity and increasing CDF; small-window ratios approach 7/3.
    assert integral_cdf(0.0001)/0.0001>2.31
    assert abs(integral_cdf(0.0001)/0.0001-7/3)<0.02
    assert 0<integral_cdf(0.001)<integral_cdf(0.01)<integral_cdf(0.1)<1
    print('VERIFY_OK exact_phase_min=30 integration_cases=3 independent_haar_samples=110000 small_tolerance=passed')

if __name__=='__main__': run()
