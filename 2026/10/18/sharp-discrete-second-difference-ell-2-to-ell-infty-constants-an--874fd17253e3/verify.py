#!/usr/bin/env python3
"""Exact finite diagnostics for a sharp second-difference Sobolev inequality.

The analytical result for all lengths is established in RESULT.md. This
script checks small lengths only, with exact rational arithmetic.
"""
from fractions import Fraction as F


def formula(n, j):
    return F(j * (j + 1) * (n + 2 - j) * (n + 1 - j)
             * (2 * j * (n + 1 - j) + n + 3),
             6 * (n + 1) * (n + 2) * (n + 3))


def solve(A, rhs):
    n = len(A)
    aug = [[F(A[i][k]) for k in range(n)] + [F(rhs[i])]
           for i in range(n)]
    for k in range(n):
        t = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[t] = aug[t], aug[k]
        u = aug[k][k]
        aug[k] = [x/u for x in aug[k]]
        for i in range(n):
            if i != k:
                u = aug[i][k]
                aug[i] = [aug[i][z] - u*aug[k][z] for z in range(n+1)]
    return [row[-1] for row in aug]


def diff2_matrix(n):
    D = [[F((1 if k == i else 0) - (2 if k == i+1 else 0)
            + (1 if k == i+2 else 0)) for i in range(n)]
         for k in range(n+2)]
    Q = [[sum(D[k][i]*D[k][j] for k in range(n+2))
          for j in range(n)] for i in range(n)]
    return D, Q


def extremal(n, j):
    m = n + 2
    a = F(j * (j+1) * (2*m - 1-j), m * (m-1))
    b = F(j * (j+1) * (2*j - 3*m+1), m*(m-1)*(m+1))
    r = [F(max(j+1-k, 0)) - a - b*k for k in range(1,m+1)]
    u = [sum((i+1-k)*r[k-1] for k in range(1,i+1))
         for i in range(1,n+1)]
    return r,u


def main():
    count = 0
    for n in range(1, 18):
        D,Q = diff2_matrix(n)
        values = [formula(n,j) for j in range(1,n+1)]
        for j in range(1,n+1):
            e = [F(int(i==j-1)) for i in range(n)]
            green = solve(Q,e)
            assert green[j-1] == formula(n,j)
            r,u = extremal(n,j)
            assert sum(r)==0 and sum(k*r[k-1] for k in range(1,n+3))==0
            assert [sum(D[k][i]*u[i] for i in range(n)) for k in range(n+2)]==r
            assert u[j-1]==formula(n,j)
            assert sum(v*v for v in r) == formula(n,j)
            count += 5
            if j<n:
                assert formula(n,j+1)-formula(n,j) == F(
                    (j+1)**2*(n+1-j)**2*(n-2*j),
                    (n+1)*(n+2)*(n+3))
                count += 1
        centers = [j for j in range(1,n+1) if values[j-1]==max(values)]
        assert centers==([n//2,n//2+1] if n%2==0 else [(n+1)//2])
        count += 1
        if n%2:
            r=(n-1)//2
            expect=F((r+1)*(r+2)*(r*r+3*r+3),12*(2*r+3))
        else:
            r=n//2
            expect=F(r*(r+1)*(r+2)*(2*r*r+4*r+3),12*(2*r+1)*(2*r+3))
        assert max(values)==expect
        count += 1
    from math import sqrt
    for n in (100, 1000, 10000):
        j=(n+1)//2
        ratio=sqrt(float(formula(n,j)))/n**1.5
        assert abs(ratio - 1/(8*sqrt(3))) < 2/n
        count += 1
    print(f'PASS: {count} exact rational/finite-limit diagnostic assertions; n=1,...,17')


if __name__=='__main__':
    main()
