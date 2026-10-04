#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import comb

def closed_cov(m,n,r):
    q=Fraction(m-1,m)
    s=Fraction(m-2,m)
    return Fraction(comb(n,r)*(m-1), m**(r-1)) * (
        q**(2*n-r-1) - s**(n-r)
    )

def decomposed_cov(m,n,r):
    q=Fraction(m-1,m)
    s=Fraction(m-2,m)
    A=Fraction(comb(n,r),m**r)*q**(n-r)
    B=Fraction(comb(n,r),m**r)*s**(n-r)
    same=A*q**n
    off=A*q**n-B
    return m*same + m*(m-1)*off

def brute_cov(m,n,r):
    total=m**n
    EK=Fraction(0)
    ER=Fraction(0)
    EKR=Fraction(0)
    for alloc in product(range(m), repeat=n):
        counts=[0]*m
        for a in alloc:
            counts[a]+=1
        K=sum(c>0 for c in counts)
        Kr=sum(c==r for c in counts)
        w=Fraction(1,total)
        EK+=w*K
        ER+=w*Kr
        EKR+=w*K*Kr
    return EKR-EK*ER

def run():
    formula_checks=0
    brute_checks=0
    singleton_checks=0
    nton_checks=0
    nozero_checks=0
    one_switch_checks=0

    for m in range(2,6):
        for n in range(2,7):
            for r in range(1,n+1):
                c=closed_cov(m,n,r)
                assert c==decomposed_cov(m,n,r)
                formula_checks+=1
                b=brute_cov(m,n,r)
                assert b==c
                brute_checks+=1

    for m in range(2,101):
        for n in range(2,101):
            signs=[]
            for r in range(1,n+1):
                c=closed_cov(m,n,r)
                assert c != 0
                nozero_checks+=1
                signs.append(1 if c>0 else -1)
            assert signs[0]==1
            assert signs[-1]==-1
            singleton_checks+=1
            nton_checks+=1
            switches=sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))
            assert switches==1
            assert all(x==1 for x in signs[:signs.index(-1)])
            assert all(x==-1 for x in signs[signs.index(-1):])
            one_switch_checks+=1

    print(
        "VERIFY_OK "
        f"formula_checks={formula_checks} "
        f"brute_checks={brute_checks} "
        f"singleton_checks={singleton_checks} "
        f"nton_checks={nton_checks} "
        f"nozero_checks={nozero_checks} "
        f"one_switch_checks={one_switch_checks}"
    )

if __name__=="__main__":
    run()
