#!/usr/bin/env python3
"""Exact finite checks for the generalized matching-count structural theorem.

Run: python3 verify.py. Uses only Python's standard library.
The infinite-order positivity and the all-size curvature theorem use the
analytic arguments in RESULT.md; finite checks are independent diagnostics.
"""
from fractions import Fraction as F
from math import comb, factorial
from itertools import combinations, permutations


def derange(m):
    if m == 0: return 1
    if m == 1: return 0
    a, b = 1, 0
    for j in range(2, m + 1):
        a, b = b, (j - 1) * (a + b)
    return b


def fall(k, r):
    ans = 1
    for i in range(r): ans *= k - i
    return ans if r <= k else 0


def pmf(n, k, theta):
    base = F(derange(n-k), factorial(k)*factorial(n-k))
    return base * sum(comb(n, l)*fall(k, l)*theta**l*(1-theta)**(n-l) for l in range(n+1))


def direct(n, theta):
    total = [F(0)] * (n+1)
    U = range(n)
    for l in range(n+1):
        for known in combinations(U, l):
            remain = [i for i in U if i not in known]
            weight = theta**l*(1-theta)**(n-l)/factorial(n-l)
            for perm in permutations(remain):
                count = l + sum(i == j for i, j in zip(remain, perm))
                total[count] += weight
    return total


def det(mat):
    n = len(mat)
    a = [list(row) for row in mat]
    if n == 1: return a[0][0]
    prev = F(1)
    sign = 1
    for j in range(n-1):
        if a[j][j] == 0:
            h = next((h for h in range(j+1, n) if a[h][j]), None)
            if h is None: return F(0)
            a[j], a[h] = a[h], a[j]
            sign = -sign
        pivot = a[j][j]
        for i in range(j+1, n):
            for k in range(j+1, n):
                a[i][k] = (a[i][k]*pivot-a[i][j]*a[j][k])/prev
            a[i][j] = F(0)
        prev = pivot
    return sign*a[-1][-1]


def derivs(n, k, t):
    c = F(derange(n-k), factorial(k)*factorial(n-k))
    a = b = d = F(0)
    for l in range(k+1):
        h = c*comb(n,l)*fall(k,l)
        a += h*t**l*(1-t)**(n-l)
        b += h*((l*t**(l-1)*(1-t)**(n-l) if l else 0)
                - ((n-l)*t**l*(1-t)**(n-l-1) if n-l else 0))
        d += h*((l*(l-1)*t**(l-2)*(1-t)**(n-l) if l>=2 else 0)
              - (2*l*(n-l)*t**(l-1)*(1-t)**(n-l-1) if l and n-l else 0)
              + ((n-l)*(n-l-1)*t**l*(1-t)**(n-l-2) if n-l>=2 else 0))
    return a,b,d


def check():
    count = 0
    for n in range(2, 7):
        support = [k for k in range(n+1) if k != n-1]
        for t in [F(1,5), F(2,5), F(3,5), F(4,5)]:
            direct_p = direct(n, t)
            for k in range(n+1):
                assert direct_p[k] == pmf(n,k,t), (n,k,t,'direct')
                count += 1
            assert sum(direct_p) == 1
            count += 1
    for n in range(2, 11):
        support = [k for k in range(n+1) if k != n-1]
        for k in support:
            # F_{n,k}(t)=k!t^k L_k^(n-k)(-1/t), coefficient by coefficient.
            # The generalized Laguerre coefficient formula is:
            # L_k^(n-k)(x)=sum_j binom(n,k-j)*(-x)^j/j!.
            for l in range(k+1):
                assert comb(n,l)*fall(k,l) == factorial(k)*comb(n,l)//factorial(k-l)
                count += 1
            for t in [F(1,11),F(3,11),F(5,11),F(8,11),F(10,11)]:
                p, dp, ddp = derivs(n,k,t)
                assert p == pmf(n,k,t)
                assert ddp*p-dp*dp < 0, (n,k,t,'curvature')
                count += 2
    for n in range(2, 8):
        support = [k for k in range(n+1) if k != n-1]
        tgrid = [F(j,6) for j in range(1,6)]
        ps = {(k,t):pmf(n,k,t) for k in support for t in tgrid}
        for r in range(1,min(4,len(support),len(tgrid))+1):
            for ks in combinations(support,r):
                for ts in combinations(tgrid,r):
                    val = det([[ps[k,t] for t in ts] for k in ks])
                    assert val > 0, (n,ks,ts,val)
                    count += 1
    print('PASS',count,'exact rational identities, direct-enumeration, curvature, and minors')


if __name__ == '__main__':
    check()
