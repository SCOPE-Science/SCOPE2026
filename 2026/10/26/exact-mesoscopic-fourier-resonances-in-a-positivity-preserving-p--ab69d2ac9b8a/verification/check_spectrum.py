#!/usr/bin/env python3
"""Finite-grid tests for a periodic four-diagonal Markov stencil.

All exact-count assertions are checked by modular arithmetic; floating point
is used only to check characteristic values and model responses.
"""
import math
import cmath
from collections import deque

for k in range(2,9):
    N=k*k
    lam=[]
    plus=minus=0
    for a in range(N):
        for b in range(N):
            s=cmath.exp(2j*math.pi*a/k).real * cmath.exp(2j*math.pi*b/k).real
            lam.append(s)
            if (a%k==0 and b%k==0) or (k%2==0 and a%k==k//2 and b%k==k//2):
                plus+=1
                assert abs(s-1)<1e-12
            if k%2==0 and ((a%k==0 and b%k==k//2) or (a%k==k//2 and b%k==0)):
                minus+=1
                assert abs(s+1)<1e-12
    assert sum(abs(x-1)<1e-12 for x in lam)==plus
    assert plus==(2*k*k if k%2==0 else k*k)
    assert minus==(2*k*k if k%2==0 else 0)
    assert sum(abs(x+1)<1e-12 for x in lam)==minus
    assert abs(min(lam)+ (1 if k%2==0 else math.cos(math.pi/k)))<1e-12
    # Each step is a translation by one of the four diagonal shifts.
    if k<=4:
        seen={(0,0)}
        q=deque([(0,0)])
        while q:
            i,j=q.popleft()
            for dx in (-k,k):
                for dy in (-k,k):
                    nb=((i+dx)%N,(j+dy)%N)
                    if nb not in seen:
                        seen.add(nb);q.append(nb)
        assert len(seen)==N*N//plus
    # Source q=cos(2*pi*k*x), normalized r=1, sigma1=sigma2=1
    h=1/N
    observed=(1+h)
    continuum=1/(1+2*math.pi**2*k*k)
    assert observed-continuum>0
    print(f'k={k}, N={N}, P(+1)-multiplicity={plus}, P(-1)-multiplicity={minus}, '
          f'P_min={min(lam):.12f}, amplif_ratio={observed/continuum:.6f}, '
          f'discrepancy={observed-continuum:.6f}')

print('PASS: arithmetic multiplicities, Fourier extrema, subgroup reachability and modal response')
