#!/usr/bin/env python3
"""Exact arithmetic finite sanity checks for a toric Nash Newton-polyhedron theorem.
The all-n statement is proved in RESULT.md, not inferred from these tests.
"""
from itertools import combinations
from math import gcd


def det(u, v, w):
    return (u[0]*(v[1]*w[2]-v[2]*w[1])
            -u[1]*(v[0]*w[2]-v[2]*w[0])
            +u[2]*(v[0]*w[1]-v[1]*w[0]))


def sums(n, p):
    G = [(1,0,0), (0,1,0)] + [(1,1,i) for i in range(1,n+1)]
    return {
        tuple(u[j]+v[j]+w[j] for j in range(3))
        for u,v,w in combinations(G,3)
        if det(u,v,w) != 0 and (p == 0 or det(u,v,w) % p != 0)
    }


def dot(w, v):
    return sum(a*b for a,b in zip(w,v))


def proposed(n, p):
    t = n if p == 0 or n % p != 0 else n-1
    return {(2,2,1), (2,2,t), (3,2,2*n-1), (2,3,2*n-1)}


def check(n, p):
    S, T = sums(n, p), proposed(n, p)
    assert T <= S
    # Four uniquely exposed vertices. The exposed weight for C uses
    # rational coefficient 1/2, rescaled to integral weights.
    weights = [(1,1,1), (2*n+2,2*n+2,-2),
               (1,4*n,-2), (4*n,1,-2)]
    four = [(2,2,1), (2,2,n if p == 0 or n % p else n-1),
            (3,2,2*n-1), (2,3,2*n-1)]
    for w, v in zip(weights, four):
        assert all(dot(w, v) < dot(w, s) for s in S if s != v), (n,p,w,v)
    for c in range(-3, 4):
        for a in (0,1,n-1,n,n+1,2*n):
            for b in (0,1,n-1,n,n+1,2*n):
                w = (a,b,c)
                if a+b+n*c < 0:
                    continue
                assert min(dot(w,s) for s in S) == min(dot(w,t) for t in T), (n,p,w)
    if p != 0 and n % p == 0:
        w0, wp = (n-1,n-1,-1), (n,n,-1)
        S0 = sums(n,0)
        min0 = min(dot(w0,s) for s in S0)
        minp = min(dot(wp,s) for s in S)
        assert {s for s in S0 if dot(w0,s)==min0} == {
            (2,2,n),(3,2,2*n-1),(2,3,2*n-1)}
        assert {s for s in S if dot(wp,s)==minp} == {
            (2,2,n-1),(3,2,2*n-1),(2,3,2*n-1)}
        # One relative interior covector witnesses genuinely different fans.
        # Double a=n-1/2 to avoid rational floating point.
        test = (2*n-1,4*n,-2)
        minzero = min(dot(test,s) for s in S0)
        minprime = min(dot(test,s) for s in S)
        assert {s for s in S0 if dot(test,s)==minzero} == {(2,2,n)}
        assert {s for s in S if dot(test,s)==minprime} == {(3,2,2*n-1)}


def main():
    primes = [2,3,5,7,11,13,17,19,23]
    for n in range(3,25):
        for p in [0] + primes:
            check(n,p)
    # Full direct determinant tests, independent of the displayed formulas.
    for n in range(3,25):
        e,f=(1,0,0),(0,1,0)
        h=lambda i:(1,1,i)
        for i in range(1,n+1):
            assert det(e,f,h(i)) == i
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                assert det(e,h(i),h(j))==j-i
                assert det(f,h(i),h(j))==i-j
    print('TORIC_NASH_ALL_PRIMES_NEWTON_SUPPORT_AND_FAN_TESTS_OK')
    print('Checked n=3..24, characteristics 0,2,3,5,7,11,13,17,19,23.')
    print('All-n proof uses determinant ordering and cone duality, not finite sampling.')

if __name__ == '__main__':
    main()
