#!/usr/bin/env python3
"""Direct exact checks for the outer-independent total Roman rook enumerator.

Run with Python 3.9+: python verify_oit_rook.py
The direct tests use the original three conditions; no external dependencies.
"""
from collections import Counter
from itertools import product, combinations, permutations
from math import comb, factorial


def claimed_coefficients(m, n):
    N = m*n
    p = Counter()
    for k in range(min(m,n)+1):
        placements = comb(m,k)*comb(n,k)*factorial(k)
        for s in range(k+1):
            blocked = s*(m+n-s-1)
            rem = N-k-blocked
            assert rem >= 0
            c = placements*(-1)**s*comb(k,s)
            for j in range(rem+1):
                p[N-k+j] += c*comb(rem,j)
    if m==n==2:
        p[3] -= 4
        p[4] -= 2
    return {w:c for w,c in p.items() if c}


def claimed_minimum(m, n):
    N=m*n
    if m==n==2:
        return (4,9)
    k=min(m,n)
    q=k//2
    def matchings(t):
        return comb(m,t)*comb(n,t)*factorial(t)
    result=matchings(2*q)*factorial(2*q)//factorial(q)
    if k%2:
        result += (matchings(k)*factorial(k)*(m+n-k-1)//factorial(q))
    return (N-q,result)


def neighbors(m,n):
    return [sum(1<<v for v in range(m*n)
                if v!=u and (u//n==v//n or u%n==v%n))
            for u in range(m*n)]


def valid(zero, two, neigh, N):
    universe=(1<<N)-1
    pos=universe^zero
    if two & zero: return False
    for v in range(N):
        if zero>>v & 1:
            if neigh[v]&zero: return False
            if not neigh[v]&two: return False
        else:
            if not neigh[v]&pos: return False
    return True


def direct_ternary(m,n):
    N=m*n
    adj=neighbors(m,n)
    p=Counter()
    for vals in product((0,1,2),repeat=N):
        zero=sum(1<<v for v,x in enumerate(vals) if x==0)
        two=sum(1<<v for v,x in enumerate(vals) if x==2)
        if valid(zero,two,adj,N): p[sum(vals)]+=1
    return dict(p)


def direct_by_zero_matchings(m,n):
    N=m*n
    adj=neighbors(m,n)
    out=Counter()
    for k in range(min(m,n)+1):
        for rows in combinations(range(m),k):
            for cols in combinations(range(n),k):
                for assigned in permutations(cols):
                    z=sum(1 << (r*n+c) for r,c in zip(rows,assigned))
                    available=[j for j in range(N) if not(z>>j & 1)]
                    for selection in range(1<<len(available)):
                        two=sum(1<<v for i,v in enumerate(available) if selection>>i&1)
                        if valid(z,two,adj,N):
                            out[N-k+selection.bit_count()]+=1
    return dict(out)


def check(m,n,by_matchings=False):
    direct=direct_by_zero_matchings(m,n) if by_matchings else direct_ternary(m,n)
    claimed=claimed_coefficients(m,n)
    assert direct==claimed, (m,n,direct,claimed)
    optimum=min(direct),direct[min(direct)]
    assert optimum==claimed_minimum(m,n), (m,n,optimum,claimed_minimum(m,n))
    print('%dx%d: all %d weight coefficients, minimum %s, valid count %d: OK' %
          (m,n,len(direct),str(optimum),sum(direct.values())))


if __name__=='__main__':
    for m,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4)]:
        check(m,n)
    for m,n in [(3,5),(4,4)]:
        check(m,n,True)
    print('VERIFY_OK')
