#!/usr/bin/env python3
"""Exact rational checks for the hypercube Poisson Green-kernel theorem.

Uses Python's standard library. No finite computation proves the
all-dimensional asymptotic estimate; see the analytic proof in RESULT.md.
"""
from fractions import Fraction
from math import comb


def krawtchouk(d, j, k):
    return sum((-1)**r * comb(k, r) * comb(d-k, j-r)
               for r in range(max(0, j-(d-k)), min(j, k)+1))


def radial_green(d):
    return [sum((Fraction(krawtchouk(d,j,k),j) for j in range(1,d+1)),
                Fraction(0)) / (2**(d+1)) for k in range(d+1)]


def invert(A):
    n = len(A)
    T = [[Fraction(A[i][j]) for j in range(n)] +
         [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if T[i][j])
        T[j], T[pivot] = T[pivot], T[j]
        z = T[j][j]
        T[j] = [v/z for v in T[j]]
        for i in range(n):
            if i != j:
                z = T[i][j]
                if z:
                    T[i] = [v-z*w for v,w in zip(T[i], T[j])]
    return [row[n:] for row in T]


def main():
    checks = 0
    for d in range(1, 31):
        g = radial_green(d)
        assert sum(comb(d,k)*g[k] for k in range(d+1)) == 0
        checks += 1
        assert g[0]>0 and g[-1]<0
        checks += 1
        for k in range(d):
            assert g[k]>g[k+1]
            checks += 1
        C = sum(comb(d,k)*abs(g[k]) for k in range(d+1))
        assert C == 2*sum(comb(d,k)*g[k] for k in range(d+1) if g[k]>0)
        checks += 1
        # A finite identity from the analytically derived integral difference.
        for k in range(d):
            z = sum(Fraction(comb(d-k-1,a)*comb(k,b)*(-1)**b, a+b+1)
                    for a in range(d-k) for b in range(k+1))
            assert 2**d*(g[k]-g[k+1]) == z
            checks += 1
    for d in range(1, 6):
        N=1<<d
        L=[[Fraction(d if x==y else -int((x^y).bit_count()==1))
            for y in range(N)] for x in range(N)]
        J=Fraction(1,N)
        inv=invert([[L[i][j]+J for j in range(N)] for i in range(N)])
        g=radial_green(d)
        for x in range(N):
            assert sum(inv[x][y]-J for y in range(N))==0
            checks += 1
            for y in range(N):
                assert inv[x][y]-J==g[(x^y).bit_count()]
                checks += 1
        for x in range(N):
            for y in range(N):
                assert sum(L[x][z]*(inv[z][y]-J) for z in range(N)) == (int(x==y)-J)
                checks += 1
    print(f'PASS: {checks} exact rational identities across dimensions 1..30; independent Laplacian inversions in dimensions 1..5')
    for d in (2,4,8,16,30):
        g=radial_green(d)
        print(f'd={d}: norm={float(sum(comb(d,k)*abs(g[k]) for k in range(d+1))):.10f}; positive last shell={max(k for k in range(d+1) if g[k]>0)}')

if __name__ == '__main__':
    main()
