#!/usr/bin/env python3
"""Exact arithmetic checks for the three-adic valuation law of involution partial sums."""
from math import comb

MOD = 3**8
EXPECTED27=(1,2,4,8,18,17,12,1,9,10,2,4,26,18,26,3,19,18,19,2,4,17,18,8,21,10,0)

def v3_mod(x, cap=8):
    x%=3**cap
    if x==0:return cap
    k=0
    while x%3==0:
        x//=3;k+=1
    return k

def expected(n):
    r=n%9
    if r==4:return 2
    if r==6:return 1
    if r==8:
        a=n+1;k=0
        while a%3==0:a//=3;k+=1
        return k
    return 0

def closed(n):
    total=0;fact=1
    for k in range(n//2+1):
        if k: fact*=2*k-1
        total+=comb(n,2*k)*fact
    return total

def main():
    i0,i1=1,1
    partial=1
    sample=[]
    for n in range(40000):
        if n==0: i=1
        elif n==1:i=1;partial+=1
        else:
            i0,i1=i1,(i1+(n-1)*i0)%MOD
            i=i1;partial=(partial+i)%MOD
        if n<27:sample.append(partial%27)
        assert v3_mod(partial)==min(expected(n),8),(n,partial,expected(n))
        if n<80:
            independent_i=closed(n)
            assert independent_i%MOD==i,(n,independent_i,i)
    assert tuple(sample)==EXPECTED27,tuple(sample)
    # Verify binomial quotient and exceptional terms for the first 100 multiples of 27.
    for z in range(1,101):
        N=27*z
        assert comb(N-1,2)%9==1
        assert comb(N-1,8)%9==1
        assert (comb(N-1,2)+35*comb(N-1,8))%9==0
    odd=1
    for k in range(1,101):
        odd*=2*k-1
        j=2*k+1
        def val(t):
            u=0
            while t%3==0:u+=1;t//=3
            return u
        if k not in (1,4):assert val(odd)-val(j)>=1,k
    print('VERIFY_OK indices=40000 modulus=6561 base_residues=27 binomial_checks=80 exceptional_cancellations=100 coefficient_checks=100')

if __name__=='__main__':main()
