#!/usr/bin/env python3
"""Reproducible exact checks for the three-site expectation commutator.

All arithmetic used in the finite sweep is rational. The general theorem is
proved analytically in RESULT.md; this program verifies its algebraic identities
and representative equality families, not a continuum by enumeration.
"""
from fractions import Fraction as F
from math import sqrt


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def diff(A, B):
    return [[A[i][j]-B[i][j] for j in range(3)] for i in range(3)]


def check(a, b, c):
    x, y = a/(a+b), c/(b+c)
    z = x*y
    P = [[x, 1-x, F(0)], [x, 1-x, F(0)],
         [F(0), F(0), F(1)]]
    Q = [[F(1), F(0), F(0)],
         [F(0), 1-y, y], [F(0), 1-y, y]]
    K = diff(matmul(P,Q), matmul(Q,P))
    formula = [[F(0), -(1-x)*y, (1-x)*y],
               [z, F(0), -z],
               [-x*(1-y), x*(1-y), F(0)]]
    assert K == formula
    linf = max(sum(abs(t) for t in row) for row in K)
    assert linf == 2*max(z, x-z, y-z)
    K2 = matmul(K,K)
    h2 = -sum(K2[i][i] for i in range(3))/2
    assert h2 == z*(1-z)
    zm = min(z,1-z)
    zu = 1-zm
    assert linf <= 2*zu
    assert linf >= 2*zm
    # If max(x-z,y-z) >= sqrt(z)-z, then the lower envelope follows.
    # This is equivalent to max(x,y)^2 >= z, verified exactly.
    assert max(x,y)**2 >= z
    assert linf >= 2*max(zm, F(0))
    low = 2*max(float(zm), sqrt(float(zm))-float(zm))
    assert float(linf) >= low-1e-12
    return linf,h2


def main():
    count = 0
    for i in range(1,17):
        for j in range(1,17):
            for k in range(1,17):
                check(F(i),F(j),F(k))
                count += 1
    # Lower endpoint at z_-=r^2 (r^2<=1/2) for x=y=r.
    for numerator, denominator in [(1,10),(1,4),(1,2),(2,3),(7,10)]:
        r=F(numerator,denominator)
        x=y=r
        a=c=r
        b=1-r
        linf,h2=check(a,b,c)
        z=r*r
        assert linf==2*max(z, r-z)
        assert h2==z*(1-z)
    # Upper endpoint at z_+=r^2>=1/2 for x=y=r.
    for numerator,denominator in [(3,4),(4,5),(9,10),(99,100)]:
        r=F(numerator,denominator)
        if r*r<F(1,2): continue
        linf,h2=check(r,1-r,r)
        assert linf==2*r*r
        assert h2==r*r*(1-r*r)
    print('EXACT_WEIGHTED_COMMUTATOR_IDENTITIES_OK',count)
    print('SHARP_ENDPOINT_FAMILIES_OK')

if __name__=='__main__':
    main()
