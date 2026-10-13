#!/usr/bin/env python3
"""Exact finite checks and numerical asymptotic diagnostics for a priced hypercube."""
from fractions import Fraction as F
from math import comb, sqrt, isclose


def spectral_index(d, t, x):
    n, vertices = d - 1, 1 << d
    a_sum = sum((F(comb(n, k), k) for k in range(1, n + 1)), F(0))
    b_sum = sum((F(comb(n, k), x + k) for k in range(n + 1)), F(0))
    return F(vertices * vertices, 4) * (n + t * x) * (a_sum + b_sum)


def inverse_exact(mat):
    n = len(mat)
    a = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(mat)]
    for k in range(n):
        r = next(i for i in range(k, n) if a[i][k])
        a[k], a[r] = a[r], a[k]
        pivot = a[k][k]
        a[k] = [v / pivot for v in a[k]]
        for i in range(n):
            if i == k:
                continue
            c = a[i][k]
            if c:
                a[i] = [a[i][j] - c * a[k][j] for j in range(2*n)]
    return [row[n:] for row in a]


def laplacian(d, t, x):
    n, v = d - 1, 1 << d
    b = 1 / (F(1 << (d-1)) * (t*x + n))
    a = x*b
    L = [[F(0) for _ in range(v)] for _ in range(v)]
    for u in range(v):
        for axis in range(d):
            z = u ^ (1 << axis)
            if u < z:
                weight = a if axis == 0 else b
                L[u][u] += weight
                L[z][z] += weight
                L[u][z] -= weight
                L[z][u] -= weight
    return L, a, b


def finite_checks():
    index_count, eigen_count = 0, 0
    for d in (2, 3, 4):
        for t in (F(1, 3), F(1), F(5, 2)):
            for x in (F(1, 4), F(1), F(9, 5)):
                N = 1 << d
                L, a, b = laplacian(d, t, x)
                augmented = [[L[i][j] + F(1, N) for j in range(N)] for i in range(N)]
                inv = inverse_exact(augmented)
                from_matrix = N * (sum((inv[i][i] for i in range(N)), F(0)) - 1)
                assert from_matrix == spectral_index(d, t, x)
                index_count += 1
                for subset in range(1, N):
                    bits = subset.bit_count()
                    epsilon = subset & 1
                    eig = 2*b*(bits - epsilon + epsilon*x)
                    for u in range(N):
                        lhs = sum((L[u][j] * (-1 if (j & subset).bit_count() & 1 else 1)
                                   for j in range(N)), F(0))
                        rhs = eig * (-1 if (u & subset).bit_count() & 1 else 1)
                        assert lhs == rhs
                    eigen_count += 1
    return index_count, eigen_count


def fprime(d, t, x):
    n = d - 1
    terms = [comb(n,k) for k in range(n+1)]
    A = sum(terms[k] / k for k in range(1,n+1))
    B = sum(terms[k] / (k+x) for k in range(n+1))
    C = sum(terms[k] / (k+x)**2 for k in range(n+1))
    return t*(A+B) - (n+t*x)*C


def scalar_checks():
    roots = 0
    for d in range(2, 32):
        for t in (0.25, 0.5, 1.0, 1.25, 2., 4.):
            lo, hi = 1.e-12, 1.e6
            assert fprime(d,t,lo) < 0 < fprime(d,t,hi)
            for _ in range(70):
                mid = (lo+hi)/2
                if fprime(d,t,mid) < 0:
                    lo = mid
                else:
                    hi = mid
            root = (lo+hi)/2
            assert lo > 0 and fprime(d,t,0.99*root)<0<fprime(d,t,1.01*root)
            if t == 1:
                assert abs(root-1) < 1e-8
            roots += 1
    # Convergence tests check diagnostics, not mathematical proof of infinite limits.
    d = 60
    for t in (0.25, 0.5):
        lo, hi = 1e-12, 1e3
        for _ in range(90):
            mid=(lo+hi)/2
            if fprime(d,t,mid)<0:lo=mid
            else:hi=mid
        target = (sqrt((2-t)/t)-1)/2
        assert abs((lo+hi)/2/d-target)<0.025
    for t in (1.5, 2., 4.):
        lo, hi = 1e-13, 1.
        for _ in range(90):
            mid=(lo+hi)/2
            if fprime(d,t,mid)<0:lo=mid
            else:hi=mid
        expected = (d-1)/(2*sqrt(t-1)*sqrt(2**(d-1)))
        assert abs((lo+hi)/2/expected - 1) < 0.055
    return roots

if __name__ == '__main__':
    v, e = finite_checks()
    r = scalar_checks()
    print(f'VERIFY_OK {v} exact Kirchhoff inverse-spectrum identities; '
          f'{e} exact Walsh eigenpairs; {r} bracketed scalar stationary points; '
          'finite tests do not prove the asymptotic theorem')
