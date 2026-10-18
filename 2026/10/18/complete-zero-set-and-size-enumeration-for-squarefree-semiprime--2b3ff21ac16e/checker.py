#!/usr/bin/env python3
"""Exact, finite cyclotomic verification of semiprime Fourier-idempotent zero sets.
Run: python3 checker.py. No nonstandard dependencies are used.
The general mathematical proof is separate from these finite checks.
"""
from collections import defaultdict
from itertools import product
from math import comb


def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b): z[i+j]+=ai*bj
    return z


def cyclo_semiprime(p,q):
    N=p*q
    divisor=mul(mul([-1,1],[1]*p),[1]*q)
    dividend=[-1]+[0]*(N-1)+[1]
    quotient=[0]*(N-len(divisor)+2)
    while len(dividend)>=len(divisor):
        coef=dividend[-1]
        d=len(dividend)-len(divisor)
        quotient[d]=coef
        for j,c in enumerate(divisor): dividend[d+j]-=coef*c
        assert dividend[-1]==0
        dividend.pop()
    assert not any(dividend)
    assert quotient[-1]==1
    return quotient


def zero_at_root(mask,N,t,poly):
    a=[0]*N
    for k in range(N):
        if mask>>k&1:
            a[(k*t)%N]+=1
    d=len(poly)-1
    for j in range(N-1,d-1,-1):
        u=a[j]
        if u:
            for i,v in enumerate(poly): a[j-d+i]-=u*v
    return not any(a[:d])


def expected(p,q):
    P=sum(comb(p,r)**q for r in range(p+1))
    Q=sum(comb(q,s)**p for s in range(q+1))
    return {(False,False,False):2**(p*q)-P-Q+2,
            (False,True,False):P-2**p,
            (False,False,True):Q-2**q,
            (True,True,False):2**p-2,
            (True,False,True):2**q-2,
            (True,True,True):2}


def run(p,q):
    N=p*q
    phi=cyclo_semiprime(p,q)
    counts=defaultdict(int)
    by_weight=defaultdict(int)
    for J in range(1<<N):
        flags=tuple(zero_at_root(J,N,t,phi) for t in (1,p,q))
        counts[flags]+=1
        by_weight[flags,J.bit_count()]+=1
    exp=expected(p,q)
    assert dict(counts)==exp, (p,q,dict(counts),exp)
    for k in range(N+1):
        expected0=comb(N,k)
        if k%q==0: expected0-=comb(p,k//q)**q
        if k%p==0: expected0-=comb(q,k//p)**p
        if k==0 or k==N: expected0+=1
        assert by_weight[(False,False,False),k]==expected0,(p,q,k)
        if 0<k<N:
            exp_E=comb(p,k//q)**q-(comb(p,k//q) if k%q==0 else 0) if k%q==0 else 0
            exp_Q=comb(q,k//p)**p-(comb(q,k//p) if k%p==0 else 0) if k%p==0 else 0
            assert by_weight[(False,True,False),k]==exp_E
            assert by_weight[(False,False,True),k]==exp_Q
            assert by_weight[(True,True,False),k]==(comb(p,k//q) if k%q==0 else 0)
            assert by_weight[(True,False,True),k]==(comb(q,k//p) if k%p==0 else 0)
    assert counts.get((True,False,False),0)==0
    assert counts.get((False,True,True),0)==0
    print('EXACT_PASS',p,q,'masks',1<<N,'cyclo',phi,'zero_free',counts[(False,False,False)],'classes',dict(counts))

if __name__=='__main__':
    for p,q in ((2,3),(2,5),(2,7),(3,5)):
        run(p,q)
    print('CHECK_PASS')
