#!/usr/bin/env python3
"""Exact finite checks for 3-adic mask cancellation on two triangular digit sets.
This code is supplemental; the all-level result follows from the cyclotomic proof.
"""
from collections import Counter
from math import gcd

SIX = ((0,0),(1,0),(2,0),(0,1),(1,1),(0,2))
THREE = ((0,0),(1,0),(0,1))

def remainder_zero_mod_phi(a,b,k,digits):
    """Exact coefficient test in Z[t]/Phi_{3**k}, no complex tolerance."""
    n=3**k
    block=n//3
    coeff=[0]*n
    for x,y in digits:
        coeff[(a*x+b*y)%n]+=1
    return all(coeff[r]==coeff[r+block]==coeff[r+2*block]
               for r in range(block))

def v3_pair(a,b):
    if a==b==0: return None
    v=0
    while a%3==b%3==0:
        a//=3; b//=3; v+=1
    return v,a%3,b%3

def predicts_zero(a,b):
    item=v3_pair(a,b)
    return item is not None and (item[1],item[2]) in ((1,2),(2,1))

if __name__ == '__main__':
    levels=5
    count_tested=0
    for k in range(1,levels+1):
        n=3**k
        n_six=0
        n_three=0
        for a in range(n):
            for b in range(n):
                if a%3==b%3==0:
                    continue  # test only primitive characters of order 3**k
                z6=remainder_zero_mod_phi(a,b,k,SIX)
                z3=remainder_zero_mod_phi(a,b,k,THREE)
                assert z6==z3
                if k==1:
                    assert z6==((a,b) in ((1,2),(2,1)))
                else:
                    assert not z6
                n_six+=z6; n_three+=z3
                count_tested+=1
        print('primitive level',k,'tested',n*n-(n//3)**2,'six zeros',n_six,'three zeros',n_three)
    for L in range(1,6):
        n=3**L
        predicted=(n*n-1)//4
        c=0
        for a in range(n):
            for b in range(n):
                def finite_product_has_zero(digits):
                    return any(remainder_zero_mod_phi(a//3**v,b//3**v,j-v,digits)
                               for j in range(1,L+1)
                               for v in range(j)
                               if a%3**v==b%3**v==0
                               and ((a//3**v)%3!=0 or (b//3**v)%3!=0)
                               and j>v)
                # first nonzero scale check: independent from the counting formula
                u=finite_product_has_zero(SIX)
                assert u==finite_product_has_zero(THREE)==predicts_zero(a,b)
                c+=u
        assert c==predicted,(L,c,predicted)
        print('full resolution',L,'zeros',c,'total',n*n)
    print('SIX_TRIANGLE_FOURIER_ZERO_EQUIVALENCE_OK',count_tested,'primitive pairs')
