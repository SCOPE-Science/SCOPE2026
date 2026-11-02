#!/usr/bin/env python3
"""Exact rational checks for affine Dirichlet simplex projection constants.

Only Python standard library is required. This finite checker tests the
reproducing kernel and beta-integral formulas; the stated infinite-family
vertex and parameter extremality are proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial


def inverse(matrix):
    n = len(matrix)
    m = [list(row) + [F(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for i in range(n):
        j = next(k for k in range(i, n) if m[k][i])
        m[i], m[j] = m[j], m[i]
        v = m[i][i]
        m[i] = [z / v for z in m[i]]
        for k in range(n):
            if k == i:
                continue
            v = m[k][i]
            m[k] = [z - v * w for z, w in zip(m[k], m[i])]
    return [row[n:] for row in m]


def beta_cdf_integer(a, b, t):
    assert a > 0 and b > 0 and F(0) <= t <= F(1)
    N = a + b - 1
    return sum((F(comb(N, j)) * t**j * (1 - t)**(N-j)
                for j in range(a, N+1)), F(0))


def negative_beta_integral(a, A):
    b = A-a
    t = F(a, A+1)
    c = F(factorial(A-1), factorial(a-1)*factorial(b-1))
    z = F(0)
    for j in range(b):
        k=a+j
        z += F((-1)**j * comb(b-1, j)) * (
            A*t**k/k - F(A*(A+1), a)*t**(k+1)/(k+1))
    return c*z


def negative_beta_cdf(a,A):
    t=F(a,A+1)
    return A*beta_cdf_integer(a,A-a,t) - (A+1)*beta_cdf_integer(a+1,A-a,t)


def run():
    profiles = 0
    kernel_rows = 0
    negative_integrals = 0
    monotonicity = 0
    specializations = 0
    strict_vertex_sign_tests = 0
    for n in range(2, 6):
        for a in product(range(1, 4), repeat=n):
            A=sum(a)
            G=[[F(a[i]*(a[j]+int(i==j)),A*(A+1))
                for j in range(n)] for i in range(n)]
            H=inverse(G)
            for i in range(n):
                for j in range(n):
                    expected=F(A*(A+1),a[i])*int(i==j)-A
                    assert H[i][j]==expected,(a,i,j,H[i][j],expected)
                    kernel_rows += 1
                lhs=negative_beta_integral(a[i],A)
                rhs=negative_beta_cdf(a[i],A)
                assert lhs==rhs,(a,i,lhs,rhs)
                assert F(0)<lhs<F(A)
                negative_integrals+=1
            # A strict ordering of row norms agrees with the smallest alpha.
            nrm=[1+2*negative_beta_cdf(ai,A) for ai in a]
            for i in range(n):
                for j in range(n):
                    assert (nrm[i]>nrm[j])==(a[i]<a[j])
                    strict_vertex_sign_tests += 1
            profiles+=1
    for A in range(2,31):
        last = None
        for a in range(1,A):
            v=1+2*negative_beta_cdf(a,A)
            assert F(1)<v<F(1+2*A)
            if last is not None:
                assert last > v,(A,a,last,v)
                monotonicity+=1
            last=v
    for n in range(2, 101):
        val=1+2*negative_beta_cdf(1,n)
        q=F(n,n+1)
        expect=2*n*q**(n-1)-1
        assert val==expect,(n,val,expect)
        specializations+=1
    print('PASS: %d nonuniform profiles, %d rational Gram-inverse coefficient tests, '
          '%d independent beta-integral comparisons, %d strict row-order '
          'tests, %d fixed-total monotonicity comparisons, '
          '%d uniform-simplex specializations' %
          (profiles,kernel_rows,negative_integrals,strict_vertex_sign_tests,
           monotonicity,specializations))


if __name__=='__main__':
    run()
