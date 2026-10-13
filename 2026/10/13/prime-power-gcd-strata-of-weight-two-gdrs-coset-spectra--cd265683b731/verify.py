#!/usr/bin/env python3
"""Exact finite checks for prime-power-index GDRS coset strata.

All computations use integers and rational arithmetic; no external modules.
"""
from math import comb, gcd
from itertools import combinations
from collections import Counter


def mobius(n):
    t, ans, p = n, 1, 2
    while p*p <= t:
        if t % p == 0:
            t //= p
            if t % p == 0:
                return 0
            ans = -ans
        while t % p == 0:
            t //= p
        p += 1
    if t > 1:
        ans = -ans
    return ans


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def ramanujan(e, lam):
    return sum(h*mobius(e//h) for h in divisors(gcd(e, lam)))


def cyclic_count(M, k, lam):
    g = gcd(M,k)
    v = sum(((-1)**(k+k//e))*comb(M//e,k//e)*ramanujan(e,lam)
            for e in divisors(g))
    assert v % M == 0
    return v//M


def prime_power(g):
    if g == 1:
        return None
    for p in range(2,g+1):
        if g%p == 0:
            a, t = 0, g
            while t%p == 0:
                a, t = a+1, t//p
            return (p,a) if t==1 else None


def class_values(M,k,p,a):
    A=[((-1)**(k+k//(p**j)))*comb(M//(p**j),k//(p**j)) for j in range(a+1)]
    F=[]
    for s in range(a):
        numer=A[0]+sum((p**j-p**(j-1))*A[j] for j in range(1,s+1))-p**s*A[s+1]
        assert numer%M==0
        F.append(numer//M)
    numer=A[0]+sum((p**j-p**(j-1))*A[j] for j in range(1,a+1))
    assert numer%M==0
    F.append(numer//M)
    assert len(set(F))==a+1
    return F


def val_class(lam,p,a):
    s=0
    while s<a and lam%(p**(s+1))==0:
        s+=1
    return s


def main():
    checked=0
    for M in range(5,18):
        for k in range(3,M):
            g=gcd(M,k)
            pa=prime_power(g)
            if pa is None: continue
            p,a=pa
            F=class_values(M,k,p,a)
            count=[0]*M
            for cc in combinations(range(M),k):
                count[sum(cc)%M]+=1
            for lam in range(M):
                v=cyclic_count(M,k,lam)
                assert v==count[lam]
                assert v==F[val_class(lam,p,a)]
            assert sum(count)==comb(M,k)
            for s,v in enumerate(F):
                count_s=sum(val_class(lam,p,a)==s for lam in range(M))
                if s<a:
                    phi=p**(a-s)-p**(a-s-1)
                    assert count_s==M//g*phi
                else:
                    assert count_s==M//g
            checked+=1
    M,k,p,a=8,4,2,2
    assert class_values(M,k,p,a)==[8,10,9]
    # For q=9, d=6, there are 45 support pairs and 8 choices of
    # the first nonzero symbol for each of the 8 ratio classes.
    assert sorted([comb(10,2)*M*sum(val_class(lam,p,a)==s for lam in range(M))
                   for s in range(a+1)])==[720,720,1440]
    print('VERIFY_OK',checked,'exhaustively enumerated (M,k) pairs;',
          'q=9 class values',class_values(M,k,p,a))


if __name__=='__main__':
    main()
