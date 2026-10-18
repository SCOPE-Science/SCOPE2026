#!/usr/bin/env python3
"""Finite diagnostic for Bergman monomial-orbit frame eigenvalues.

These tests are not proofs of asymptotic or infinite-dimensional claims.
"""
import math

def h(alpha, n):
    if alpha == 0.0:
        return n+1.0
    return math.exp(math.lgamma(n + alpha + 2)-math.lgamma(n+1)-math.lgamma(alpha+2))

def diagonal_from_seeds(alpha, seeds, N):
    s = set(seeds)
    total = 0.0
    diag = []
    for m in range(N+1):
        if m in s:
            total += h(alpha,m)
        diag.append(total/h(alpha,m))
    return diag

def diagonal_via_finite_orbits(alpha,seeds,N):
    # Explicit finite-column synthesis coefficients, not using prefix formula.
    diagonal = [0.0] * (N+1)
    for sj in seeds:
        for k in range(N-sj+1):
            m=sj+k
            diagonal[m] += h(alpha,sj)/h(alpha,m)
    return diagonal

def main():
    runs=0
    for alpha in [-0.75,0.0,0.5,2.0]:
        beta=alpha+1
        for rho in [1.5,2.0,3.0]:
            J0=0
            while rho**(J0+1)*(rho-1) <= 2:
                J0+=1
            seeds=[0]+[math.ceil(rho**(j+J0)) for j in range(1,30) if rho**(j+J0) <= 2000]
            seeds=sorted(set(seeds))
            N=2000
            a=diagonal_from_seeds(alpha,seeds,N)
            b=diagonal_via_finite_orbits(alpha,seeds,N)
            err=max(abs(x-y) for x,y in zip(a,b))
            assert err < 2e-10, (alpha,rho,err)
            runs+=1
    # Exact rational α=0, dyadic seeds: compare formula for all n<4096.
    seeds=[2**j-1 for j in range(13)]
    diag=diagonal_from_seeds(0.0,seeds,4094)
    for m,v in enumerate(diag):
        J=(m+1).bit_length()-1
        expected=(2**(J+1)-1)/(m+1)
        assert abs(v-expected)<1e-11,(m,v,expected)
    print(f'PASS: {runs} general parameter scenarios with two independent finite-frame diagonal computations')
    print('PASS: 4095 exact dyadic Bergman diagonal values')
    print('finite diagnostics only; analytic proof required for all limits')

if __name__=='__main__':
    main()
