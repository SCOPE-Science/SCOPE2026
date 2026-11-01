#!/usr/bin/env python3
"""Independent finite and exact checks for five-tap phase-only Fourier zeros.

The all-prime statements follow from the written proof, not these samples.
This script requires only the Python standard library.
"""
from itertools import permutations
from math import cos, sqrt, pi
from cmath import exp


def determinant_integer(M):
    n=len(M)
    out=0
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        v=sign
        for i, j in enumerate(perm):
            v*=M[i][j]
        out+=v
    return out


def prime(n):
    return n>=2 and all(n%d for d in range(2,int(sqrt(n))+1))


def coefficients(p):
    c=cos(2*pi/p)
    t=c*c
    alpha=(16*t*t-12*t+3)/(8*c*(1-2*t))
    assert -1 < alpha < 1
    a=complex(alpha,sqrt(1-alpha*alpha))
    b=2-4*t-2*c*a
    return [1+0j,a,b,a,1+0j]


def check():
    # Sylvester determinant in the reduction modulo 1-zeta_p:
    # F=3u²+9u+3, G=9u²+17u+9.
    M=[[3,9,3,0],[0,3,9,3],[9,17,9,0],[0,9,17,9]]
    assert determinant_integer(M)==900
    samples=[7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,71,97,101,127,257,509,1009]
    for p in samples:
        assert prime(p)
        co=coefficients(p)
        assert all(abs(abs(a)-1)<5e-12 for a in co)
        z=exp(2j*pi/p)
        assert abs(sum(co[j]*z**j for j in range(5)))<1e-9
        assert abs(sum(co[j]*z**(-j) for j in range(5)))<1e-9
        allvals=[sum(co[j]*exp(2j*pi*k*j/p) for j in range(5)) for k in range(p)]
        zeros=[k for k in range(p) if abs(allvals[k])<1e-8]
        assert zeros==[1,p-1], (p,zeros)
    vals=[sum(exp(2j*pi*j*k/5) for j in range(5)) for k in range(5)]
    assert abs(vals[0]-5)<1e-12 and all(abs(v)<1e-12 for v in vals[1:])
    print(f'FIVE_TAP_PHASE_ONLY_PRIME_FOURIER_OK; exact Sylvester resultant=900; {len(samples)} prime witnesses, including 1009; p=5 cyclotomic extremizer')


if __name__=='__main__':
    check()
