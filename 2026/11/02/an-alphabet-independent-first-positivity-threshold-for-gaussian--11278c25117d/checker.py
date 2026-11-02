#!/usr/bin/env python3
"""Finite supplementary checks for Gaussian Hamming squared-distance kernel threshold.
Run with Python >=3.9; standard library only. These are tests, not a proof of arbitrary dimensions.
"""
from fractions import Fraction
from itertools import product
from math import comb, cos, pi


def F(n, q):
    return sum(((-1)**j * comb(n, j) * q**(j*j) for j in range(n+1)), Fraction())


def eigenvalue(n, r, k, q):
    result = Fraction()
    for a in range(n-k+1):
        g = sum(((-1)**j * comb(k, j) * q**((a+j)*(a+j)) for j in range(k+1)), Fraction())
        result += comb(n-k, a) * (r-1)**a * g
    return result


def check_eigenvectors(n, r, q):
    points = list(product(range(r), repeat=n))
    N = len(points)
    assert N <= 81
    for k in range(n+1):
        char = lambda v: complex(1.0) if k==0 else complex(cos(2*pi*sum(v[:k])/r), __import__('math').sin(2*pi*sum(v[:k])/r))
        v = [char(p) for p in points]
        ev = float(eigenvalue(n, r, k, q))
        for row in points:
            lhs = sum(float(q**(sum(a!=b for a,b in zip(row,col))**2)) * vc for col,vc in zip(points,v))
            rhs = ev*char(row)
            assert abs(lhs-rhs) < 2e-9, (n,r,k,q,lhs,rhs)


def run():
    checks = 0
    for n in range(2, 17):
        qlo = Fraction(1, n)
        qhi = Fraction(n*n + 1, n**3)
        assert F(n, qlo) > 0 and F(n, qhi) < 0
        assert qhi < Fraction(1, n-1)
        checks += 3
        for r in (2,3,5):
            for q in (qlo, qlo/2):
                for k in range(n+1):
                    assert eigenvalue(n,r,k,q) > 0
                    checks += 1
            assert eigenvalue(n, r, n, qhi) < 0
            for k in range(n):
                assert eigenvalue(n, r, k, qhi) > 0
                checks += 1
            checks += 1
        assert F(n, qhi) == eigenvalue(n, 2, n, qhi)
        checks += 1
    for n,r,q in ((2,2,Fraction(2,5)),(2,3,Fraction(1,2)),(3,2,Fraction(1,4)),(3,3,Fraction(1,3)),(4,2,Fraction(1,5)),(4,3,Fraction(1,6))):
        check_eigenvectors(n,r,q)
        checks += (n+1)*r**n
    print('FINITE CHECKS PASS',checks)


if __name__ == '__main__':
    run()
