#!/usr/bin/env python3
"""Exact integer verification for the three-consecutive-return-length theorem.

No external dependencies. Finite checks support, but do not prove, the infinite claim.
"""
from itertools import product


def mobius(d):
    if d == 1:
        return 1
    p = 2
    sign = 1
    while p*p <= d:
        if d % p == 0:
            d //= p
            if d % p == 0:
                return 0
            sign = -sign
        p += 1
    if d > 1:
        sign = -sign
    return sign


def orbit_counts(a, N):
    gaps = (a, a+1, a+2)
    c = [0]*(N+1)
    c[0] = 1
    for n in range(1,N+1):
        c[n] = sum(c[n-g] for g in gaps if g <= n)
    fixed = [0]*(N+1)
    for n in range(1,N+1):
        fixed[n] = sum(g*c[n-g] for g in gaps if g <= n)
    q = [0]*(N+1)
    for n in range(1,N+1):
        s = sum(mobius(d)*fixed[n//d] for d in range(1,n+1) if n%d==0)
        assert s%n == 0
        q[n] = s//n
        assert q[n]>=0
    return q, fixed


def conductor(a):
    if a == 2:
        return 6
    if a % 2:
        return (a+1)*(a+2)//2
    return a*(a+2)//2+1


def primitive(w):
    l=len(w)
    return not any(l%p==0 and w==w[:p]*(l//p) for p in range(1,l))


def canonical(w):
    return min(w[i:]+w[:i] for i in range(len(w)))


def brute_counts(a, max_gap_letters):
    labels = {}
    for l in range(1,max_gap_letters+1):
        for w in product((a,a+1,a+2),repeat=l):
            if primitive(w):
                n=sum(w)
                labels.setdefault(n,set()).add(canonical(w))
    return {n:len(xs) for n,xs in labels.items()}


def validate():
    checks=0
    for a in range(2,47):
        M=conductor(a)
        N=M+4*(a+2)
        q, fixed=orbit_counts(a,N)
        assert q[M]==1,(a,M,q[M]);checks+=1
        for n in range(M+1,N+1):
            assert q[n]>=2,(a,n,q[n])
            checks+=1
        # Test zeta/period identity by divisor sums.
        for n in range(1,N+1):
            assert fixed[n]==sum(d*q[d] for d in range(1,n+1) if n%d==0)
            checks+=1
    direct_checks=0
    for a in range(2,10):
        # All possible lengths n<=7*a have at most 7 return blocks.
        q,_=orbit_counts(a,7*a)
        brute=brute_counts(a,7)
        for n in range(1,7*a+1):
            assert q[n]==brute.get(n,0),(a,n,q[n],brute.get(n,0))
            direct_checks+=1
    print('VERIFIED: exact conductor and all larger tested counts;',
          checks,'integer checks;',direct_checks,'independent necklace comparisons.')

if __name__=='__main__':
    validate()
