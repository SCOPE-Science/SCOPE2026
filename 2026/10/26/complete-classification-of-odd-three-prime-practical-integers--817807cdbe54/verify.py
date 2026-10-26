#!/usr/bin/env python3
"""Exact independent finite checks of cyclotomic degree completeness."""
from itertools import product

def totient_coins(factors):
    coins=[1]
    for p,e in factors:
        coins=[u*(p-1)*p**(j-1) if j else u for u in coins for j in range(e+1)]
    return coins

def complete(coins):
    reach=1
    for w in coins:
        reach |=reach<<w
    n=sum(coins)
    return reach==(1<<(n+1))-1

def largest_gap(coins):
    reach=1
    for w in coins:
        reach|=reach<<w
    prev=None; gap=0
    for k in range(sum(coins)+1):
        if reach>>k&1:
            if prev is not None: gap=max(gap,k-prev)
            prev=k
    return gap

def run():
    tests=0
    for q in (7,11,13,17,19,23,29,31):
        for a,b,c in product(range(1,3),repeat=3):
            expected=q in (7,11,13) or q==17 and (a,b,c)==(1,1,1)
            got=complete(totient_coins(((3,a),(5,b),(q,c))))
            assert got==expected,(q,a,b,c,got,expected)
            tests+=1
    gaps=0
    for a,b,c in product(range(1,3),repeat=3):
        for q in (7,11,13):
            assert largest_gap(totient_coins(((3,a),(5,b))))==3**(a-1)*5**(b-1)
            assert largest_gap(totient_coins(((3,a),(q,c))))==(q-4)*3**(a-1)*q**(c-1)
            assert largest_gap(totient_coins(((5,b),(q,c))))==(3*q-8)*5**(b-1)*q**(c-1)
            gaps+=3
    print('VERIFY_OK', 'three-prime_cases',tests, 'cofactor_gap_cases',gaps)
if __name__=='__main__':run()
