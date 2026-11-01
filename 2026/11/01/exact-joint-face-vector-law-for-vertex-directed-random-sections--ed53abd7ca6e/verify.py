#!/usr/bin/env python3
"""Independent finite diagnostics for an exact geometric face-vector law."""
from math import comb, erf, erfc, sqrt, exp, pi, atan
from itertools import combinations, product, permutations
import random

def coeff(d,m):
    return [2**j*comb(d,j) - (comb(m,j) if j<=m else 0)
            - sum(comb(m,a)*comb(d-m,j-a)*2**(j-a)
                  for a in range(max(0,j-(d-m)),min(m,j)+1))
            for j in range(2,d+1)]

def independent_enumeration(d,m):
    signs=[(1,-1) if i<m else (-1,-1) for i in range(d)]
    out=[]
    for j in range(2,d+1):
        count=0
        for axes in combinations(range(d),j):
            for chosen in product(range(2),repeat=j):
                x=[signs[axis][k] for axis,k in zip(axes,chosen)]
                count+= int(min(x)<0<max(x))
        out.append(count)
    return out

def simpson(f,a,b,n=16000):
    assert n%2==0
    h=(b-a)/n
    return (f(a)+f(b)+4*sum(f(a+(2*k-1)*h) for k in range(1,n//2+1))
            +2*sum(f(a+2*k*h) for k in range(1,n//2)))*h/3

def mixture(d,t,m):
    def f(x):
        p=erfc(t*x/sqrt(2))
        return sqrt(2/pi)*exp(-x*x/2)*comb(d-1,m-1)*p**(m-1)*(1-p)**(d-m)
    return simpson(f,0,10)

def run():
    checked=0
    for d in range(3,9):
        c=[coeff(d,m) for m in range(1,d+1)]
        for m,vec in enumerate(c,1):
            assert vec==independent_enumeration(d,m)
            assert sum((-1)**k*vec[k] for k in range(d-1))==1+(-1)**(d-2)
            assert vec[0]==m*(2*d-1-m)
            checked+=3
        assert c[-1]==c[-2]
        assert len({tuple(v) for v in c})==d-1
        assert all(all(a<b for a,b in zip(c[k],c[k+1])) for k in range(d-2))
        checked+=3
        for target in range(1,d+1):
            ct=sum(1 for perm in permutations(range(d)) if 1+sum(perm[i]>perm[-1] for i in range(d-1))==target)
            assert ct* d==__import__('math').factorial(d)
            checked+=1
    for t in (0.125,0.25,0.5,0.75,0.9):
        a=mixture(3,t,1)
        b=(2/pi)*atan(t*t/sqrt(1+2*t*t))
        assert abs(a-b)<2e-9, (t,a,b)
        checked+=1
    for d in (3,4,5,7):
        for t in (0.1,0.45,0.8,0.999):
            assert abs(sum(mixture(d,t,m) for m in range(1,d+1))-1)<5e-9
            checked+=1
    rng=random.Random(261028084)
    for d,t in ((3,0.4),(5,0.7)):
        counts=[0]*d
        n=32000
        for _ in range(n):
            gg=[abs(rng.gauss(0,1)) for _ in range(d)]
            m=1+sum(y>t*gg[-1] for y in gg[:-1])
            counts[m-1]+=1
        for m in range(1,d+1):
            p=mixture(d,t,m)
            assert abs(counts[m-1]/n-p)<0.017
            checked+=1
    print('PASS: independent signed-face enumeration, Euler identities, ranks, deterministic integrals, and Monte Carlo:',checked,'checks')

if __name__=='__main__':run()
