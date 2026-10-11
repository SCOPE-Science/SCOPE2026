#!/usr/bin/env python3
"""Finite algebraic tests for reflection autocorrelation majorization.
No sampling test is used in place of the general Cauchy--Schwarz proof.
"""
from itertools import product
from math import isqrt

PAIRS = ((0,0,0),(1,7,5),(7,1,5),(5,5,5),(17,31,25),(31,17,25))


def convolution(a,b,n):
    out=[0j]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[(i+j)%n]+=x*y
    return out

def moment(a,s):
    n=len(a)
    out=[1+0j]+[0j]*(n-1)
    for _ in range(s):out=convolution(out,a,n)
    return int(round(sum(abs(x)**2 for x in out)))

def corr(a,h):
    n=len(a)
    return sum(a[i]*a[(i+h)%n] for i in range(n))

def trial(n,t,choose):
    a=[None]*n; b=[None]*n
    orbits=[];seen=set()
    for i in range(n):
        j=(t-i)%n
        if i in seen:continue
        seen.update((i,j));orbits.append((i,j))
    for z,(i,j) in enumerate(orbits):
        if i==j:
            a[i]=b[i]=(z*7+3)%17
        else:
            x,y,r=PAIRS[(choose+z*3)%len(PAIRS)]
            a[i]=x;a[j]=y;b[i]=b[j]=r
    assert all(v is not None for v in a+b)
    assert sum(x*x for x in a)==sum(x*x for x in b)
    A=[corr(a,h) for h in range(n)]
    B=[corr(b,h) for h in range(n)]
    assert B[0]==A[0] and all(x>=y for x,y in zip(B,A))
    asymmetric=any(a[i]!=a[(t-i)%n] for i in range(n))
    for s in (2,3,4):
        x=moment(a,s);y=moment(b,s)
        assert y>=x and ((y>x)==asymmetric), (n,t,choose,s,x,y)
    signs=[-1 if i%3==0 else 1 for i in range(n)]
    complex_a=[a[i]*(1j if i%4==1 else signs[i]) for i in range(n)]
    for s in (2,3,4):
        assert moment(complex_a,s)<=moment(a,s)
    return asymmetric

def main():
    cases=0;strict=0
    for n in range(2,15):
        for t in range(n):
            for seed in range(6):
                flag=trial(n,t,seed);cases+=1;strict+=flag
    # Aperiodic integer example (zero padding past support is implicit).
    for n in range(2,12):
        a=[(i*i+3*i+7)%17 for i in range(n)]
        b=[((a[i]*a[i]+a[n-1-i]*a[n-1-i])/2)**.5 for i in range(n)]
        assert all(sum(b[i]*b[i+h] for i in range(n-h))+1e-9>=sum(a[i]*a[i+h] for i in range(n-h)) for h in range(n))
    print(f'VERIFY_OK exact_cyclic_cases={cases} strict_asymmetric={strict} exact_moments_2_3_4=PASS aperiodic_checks=10')
if __name__=='__main__':main()
