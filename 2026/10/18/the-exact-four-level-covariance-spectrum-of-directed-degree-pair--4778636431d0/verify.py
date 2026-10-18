#!/usr/bin/env python3
"""Exact rational replay for the finite directed degree-pair covariance identity.

This checks finite instances only; the general theorem is proved in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import comb


def run_case(n, p):
    q = 1 - p
    m = n - 1
    b = [Fraction(comb(m, r)) * p**r * q**(m-r) for r in range(n)]
    a = [Fraction(comb(m-1, r))*p**r*q**(m-1-r) if r < m else Fraction(0) for r in range(n)]
    d = [a[r] - (a[r-1] if r else Fraction(0)) for r in range(n)]
    cells = list(product(range(n), repeat=2))
    w = [b[r]*b[s] for r, s in cells]
    u = [d[r]*b[s] for r, s in cells]
    v = [b[r]*d[s] for r, s in cells]
    z = [d[r]*d[s] for r, s in cells]
    l = n*n
    cov_formula = [
        [n*((w[i] if i == j else Fraction(0))-w[i]*w[j])
         + n*m*(p*q*(u[i]*v[j]+v[i]*u[j]) + p*p*q*q*z[i]*z[j])
         for j in range(l)] for i in range(l)
    ]
    edges = [(i,j) for i in range(n) for j in range(n) if i != j]
    expected = [Fraction(0) for _ in range(l)]
    second = [[Fraction(0) for _ in range(l)] for _ in range(l)]
    for bits in product((0, 1), repeat=len(edges)):
        prob = p**sum(bits)*q**(len(edges)-sum(bits))
        outgoing = [0]*n
        incoming = [0]*n
        for (x, y), bit in zip(edges, bits):
            outgoing[x] += bit
            incoming[y] += bit
        counts = [0]*l
        for x in range(n):
            counts[n*outgoing[x]+incoming[x]] += 1
        for i in range(l):
            expected[i] += prob*counts[i]
            for j in range(l):
                second[i][j] += prob*counts[i]*counts[j]
    for i in range(l):
        assert expected[i] == n*w[i], ('mean',n,p,i)
        for j in range(l):
            assert second[i][j] - expected[i]*expected[j] == cov_formula[i][j], ('cov',n,p,i,j)
    vectors = (w,u,v,z)
    for s in range(1,4):
        for t in range(s+1,4):
            assert sum(vectors[s][k]*vectors[t][k]/w[k] for k in range(l)) == 0
    assert sum(w) == 1 and sum(d) == 0
    assert sum(u[k]*u[k]/w[k] for k in range(l)) == Fraction(1)/(m*p*q)
    assert sum(v[k]*v[k]/w[k] for k in range(l)) == Fraction(1)/(m*p*q)
    assert sum(z[k]*z[k]/w[k] for k in range(l)) == Fraction(1)/(m*m*p*p*q*q)
    basis = [(w, 0), ([u[k]-v[k] for k in range(l)], 0),
             ([u[k]+v[k] for k in range(l)], 2*n), (z, Fraction(n*n,m))]
    for vec, eigenvalue in basis:
        for i in range(l):
            image = sum(cov_formula[i][j]*vec[j]/w[j] for j in range(l))
            assert image == eigenvalue*vec[i], ('eigen',n,p,i,eigenvalue)
    assert l - 4 >= 0
    return 2**len(edges)


def main():
    total = 0
    for n in (2,3,4):
        for p in (Fraction(1,3), Fraction(1,2), Fraction(2,3)):
            total += run_case(n,p)
    assert total == 12492
    print('VERIFY_OK: 9 exact rational parameter cases, 12492 enumerated weighted directed graphs')

if __name__ == '__main__':
    main()
