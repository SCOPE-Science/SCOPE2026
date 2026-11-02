#!/usr/bin/env python3
"""Exact finite checks for the wheel spoke-subprocess theorem.

Only standard-library arithmetic is used. The analytic proof is independent of
these bounded checks.
"""
from fractions import Fraction
from itertools import combinations


def forest(edge_mask, edges, vertices):
    parent = list(range(vertices))
    def root(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for i, (u, v) in enumerate(edges):
        if (edge_mask >> i) & 1:
            u, v = root(u), root(v)
            if u == v:
                return False
            parent[u] = v
    return True


def wheel(n):
    # Rim vertices 0,...,n-1; hub is vertex n. The first n edges are spokes.
    return [(j, n) for j in range(n)] + [(j, (j+1)%n) for j in range(n)]


def recurrence(n, x):
    s0, s1 = 2, 1+3*x
    u0, u1 = 0, x
    if n == 0:
        return 2, 0
    if n == 1:
        return s1-2*x, x
    for _ in range(2, n+1):
        s0, s1 = s1, (1+3*x)*s1-x*(1+x)*s0
        u0, u1 = u1, (1+3*x)*u1-x*(1+x)*u0
    return s1-2*x**n, u1


def numerator_for_forced(n, forced, x):
    if not forced:
        return recurrence(n, x)[0]
    forced = sorted(forced)
    gaps = [(forced[(i+1)%len(forced)]-forced[i])%n for i in range(len(forced))]
    if len(forced) == 1:
        gaps = [n]
    prod = 1
    for gap in gaps:
        prod *= recurrence(gap, x)[1]
    return prod


def check_exact():
    tests = 0
    for n in range(3, 8):
        E = wheel(n)
        for x in (Fraction(1, 2), Fraction(1), Fraction(2)):
            numerators = [Fraction(0) for _ in range(1 << n)]
            for mask in range(1 << (2*n)):
                if not forest(mask, E, n+1):
                    continue
                w = x**mask.bit_count()
                spoke_mask = mask & ((1 << n)-1)
                sub = spoke_mask
                while True:
                    numerators[sub] += w
                    if sub == 0:
                        break
                    sub = (sub-1)&spoke_mask
            for H in range(1 << n):
                forced = [i for i in range(n) if H >> i & 1]
                exact = numerator_for_forced(n, forced, x)
                assert numerators[H] == exact, (n,x,forced,numerators[H],exact)
                tests += 1
            for d in range(1, n):
                z = numerators[0]
                p1 = numerators[1]/z
                p2 = numerators[(1 << 0)|(1 << d)]/z
                assert p2 < p1*p1
                tests += 1
            pair_probs=[numerators[1|(1<<d)]/z for d in range(1,n)]
            for d in range(1,n//2):
                assert pair_probs[d] > pair_probs[d-1]
                tests+=1
    return tests


def det_exact(M):
    # Fraction Gaussian elimination.
    n=len(M)
    A=[[Fraction(v) for v in row] for row in M]
    d=Fraction(1)
    for j in range(n):
        k=next((k for k in range(j,n) if A[k][j]),None)
        if k is None:
            return Fraction(0)
        if k!=j:
            A[k],A[j]=A[j],A[k]
            d=-d
        pivot=A[j][j]
        d*=pivot
        for i in range(j+1,n):
            if A[i][j]:
                fac=A[i][j]/pivot
                for t in range(j,n):
                    A[i][t]-=fac*A[j][t]
    return d


def check_determinant():
    count=0
    for z in (Fraction(1,2),Fraction(2,3),Fraction(1,5)):
        for k in range(1,6):
            for positions in combinations(range(9), k):
                M=[[z**abs(i-j) for j in positions] for i in positions]
                expect=Fraction(1)
                for a,b in zip(positions,positions[1:]):
                    expect*=1-z**(2*(b-a))
                assert det_exact(M)==expect
                count+=1
    return count

if __name__=='__main__':
    a=check_exact()
    b=check_determinant()
    print(f'PASS {a} exact wheel-forest inclusion and covariance tests; {b} exact Toeplitz determinant tests')
