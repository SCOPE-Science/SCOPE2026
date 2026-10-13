#!/usr/bin/env python3
"""Reproducible finite checks for polynomial-aspect one-round graded type counts.

This script uses only Python's standard library. Finite tests complement the
asymptotic proof; no finite computation is used to certify an infinite limit.
"""
from itertools import product
from collections import Counter
from math import exp, lgamma, log, pi, sqrt, floor
from random import Random


def signature_count(M):
    m=len(M); n=len(M[0]); row=[sum(x) for x in M]
    col=[sum(M[i][j] for i in range(m)) for j in range(n)]
    types={(M[i][j],row[i],col[j]) for i in range(m) for j in range(n)}
    return len(types),len(set(row)),len(set(col))


def direct_depth_one_count(M):
    """Truth values of every atomic and primitive graded depth-one formula.

    All formulas at modal depth <=1 are Boolean combinations of the atom and
    (row/column) counting formulas on that atom or its complement, so the
    resulting atom partition is exactly depth-one graded equivalence.
    """
    m=len(M);n=len(M[0]); masks=[]
    masks.append(tuple(M[i][j] for i in range(m) for j in range(n)))
    for along_rows in (True,False):
        for bit in (0,1):
            for threshold in range(1,(n if along_rows else m)+1):
                v=[]
                for i in range(m):
                    for j in range(n):
                        count=sum(int(z==bit) for z in (M[i] if along_rows else [M[ii][j] for ii in range(m)]))
                        v.append(int(count>=threshold))
                masks.append(tuple(v))
    return len({tuple(mask[k] for mask in masks) for k in range(m*n)})


def pmf_bin(n,p):
    a=lgamma(n+1)
    return [exp(a-lgamma(k+1)-lgamma(n-k+1)+k*log(p)+(n-k)*log(1-p)) for k in range(n+1)]


def expected_distinct(t,length,p):
    prob=pmf_bin(length,p)
    return sum(-__import__('math').expm1(t*__import__('math').log1p(-min(.99999999999999,x))) for x in prob)


def integral_critical(p):
    v=p*(1-p)
    # Midpoint rule over a 16-sigma interval; bounded smooth integrand.
    dx=.002; L=8*sqrt(v);N=round(2*L/dx);dx=2*L/N
    return sum((1-exp(-exp(-((i+.5)*dx-L)**2/(2*v))/sqrt(2*pi*v)))*dx for i in range(N))


def one_sample(n,a,p,rng):
    m=max(1,floor(n**a))
    M=[bytearray(int(rng.random()<p) for _ in range(n)) for _ in range(m)]
    K,R,C=signature_count(M)
    return m,K,R,C,K/(2*R*C)


def main():
    total=0
    for m in range(1,5):
        for n in range(1,5):
            if m*n>12:continue
            for bits in product((0,1),repeat=m*n):
                M=[bits[i*n:(i+1)*n] for i in range(m)]
                k,_,_=signature_count(M)
                assert k==direct_depth_one_count(M),(m,n,bits,k)
                total+=1
    print('EXHAUSTIVE_OK',total,'binary matrices, literal graded formulas versus profile count')

    for p in (.2,.5,.8):
        Lp=integral_critical(p)
        ratios=[]
        for length in (400,1600,6400):
            t=int(sqrt(length))
            ratios.append(expected_distinct(t,length,p)/sqrt(length))
        # The expected occupancy converges toward the explicit Gaussian integral.
        assert abs(ratios[-1]-Lp)<.015,(p,Lp,ratios)
        print('CRITICAL_OCCUPANCY_OK',p,'integral',round(Lp,6),'samples',[round(x,6) for x in ratios])

    rng=Random(1729)
    cases=[(64,.35),(64,.5),(80,.75),(80,1.0),(60,1.3),(48,1.75),(40,2.0),(32,2.35)]
    samples=0
    obs=[]
    for n,a in cases:
        for seed in range(4):
            m,k,r,c,ratio=one_sample(n,a,.5,rng)
            assert 2<=k<=min(m*n,2*r*c)
            if m*n>=30:assert k>=max(r,c)
            obs.append((n,a,m,k,r,c,round(ratio,4)))
            samples+=1
    print('RECTANGULAR_RANDOM_OK',samples,'draws; sample tuples (n,exponent,m,K,R,C,K/2RC):')
    for i in range(0,len(obs),4):print(' ',obs[i])
    print('VERIFY_OK exhaustive_matrices',total,'critical_PMF_cases',9,'random_rectangular_cases',samples)

if __name__=='__main__': main()
