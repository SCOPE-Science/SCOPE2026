#!/usr/bin/env python3
"""Exact verification of recursive-tree subtree and leaf identities.

No external dependencies. Enumerates every increasing parent map through n=9.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial


def conditional_mean(n, k, s):
    if not (n >= 3 and 2 <= k <= n and 1 <= s <= n-k+1):
        raise ValueError('Invalid parameters')
    if k == 2 and s == n-1:
        return Fraction(n-1, 2)
    N = n-s
    return Fraction(n, 2) + Fraction(int(s == 1), 2) - Fraction(k-2, 2*(N-1))


def local_mean(s):
    return Fraction(s, 2) + Fraction(int(s == 1), 2)


def cov_global(n, k):
    return Fraction(-(n-k), 2*(n-1))


def cov_local(n, k):
    return Fraction((n-k)*(k-1)*(n*(n-1)-k*(k+1)),
                    2*k*k*(k+1)*(n-1))


def subtree_size_probability(n, k, s):
    # Beta-binomial: one marked vertex versus k-1 older unmarked vertices.
    r = s-1
    a = n-k
    if not 0 <= r <= a:
        return Fraction(0)
    return Fraction(comb(a, r)*factorial(r)*factorial(k-2+a-r)*factorial(k-1),
                    factorial(k-2)*factorial(n-1))


def exhaustive(n):
    totals = defaultdict(lambda: [0,0,0])
    moments = defaultdict(lambda: [0,0,0,0,0,0])
    num = 0
    for par in product(*(range(1,j) for j in range(2,n+1))):
        p = [0,0] + list(par)
        children = [0]*(n+1)
        for j in range(2,n+1):
            children[p[j]] += 1
        leaf = [int(children[j] == 0) for j in range(n+1)]
        L = sum(leaf[1:])
        num += 1
        for k in range(2,n+1):
            inside = [False]*(n+1)
            inside[k] = True
            for j in range(k+1,n+1):
                inside[j] = inside[p[j]]
            S = sum(inside)
            U = sum(leaf[j] for j in range(1,n+1) if inside[j])
            arr = totals[k,S]
            arr[0] += 1
            arr[1] += L
            arr[2] += U
            m = moments[k]
            for pos, value in enumerate((S,L,U,S*L,S*U,S*S)):
                m[pos] += value
    assert num == factorial(n-1)
    for k in range(2,n+1):
        meanS,meanL,meanU,meanSL,meanSU,_ = map(lambda v: Fraction(v,num), moments[k])
        assert meanS == Fraction(n,k)
        assert meanL == Fraction(n,2)
        assert meanSL-meanS*meanL == cov_global(n,k), (n,k,'global')
        assert meanSU-meanS*meanU == cov_local(n,k), (n,k,'local')
        assert sum(subtree_size_probability(n,k,s) for s in range(1,n-k+2)) == 1
        for s in range(1,n-k+2):
            cnt,totalL,totalU = totals[k,s]
            assert Fraction(cnt,num) == subtree_size_probability(n,k,s)
            assert Fraction(totalL,cnt) == conditional_mean(n,k,s), (n,k,s,'conditional-global')
            assert Fraction(totalU,cnt) == local_mean(s), (n,k,s,'conditional-local')
        seq = [conditional_mean(n,k,s) for s in range(1,n-k+2)]
        assert all(seq[i] >= seq[i+1] for i in range(len(seq)-1))
        if k>=3:
            assert all(seq[i] > seq[i+1] for i in range(len(seq)-1))
        assert cov_global(n,k) <= 0 and cov_local(n,k) >= 0
    return num


def analytic_grid():
    cases = 0
    for n in range(3,201):
        for k in range(2,n+1):
            prob = [subtree_size_probability(n,k,s) for s in range(1,n-k+2)]
            assert sum(prob) == 1
            muS = sum(s*p for s,p in enumerate(prob,1))
            assert muS == Fraction(n,k)
            l = [conditional_mean(n,k,s) for s in range(1,n-k+2)]
            u = [local_mean(s) for s in range(1,n-k+2)]
            assert sum(a*b for a,b in zip(prob,l)) == Fraction(n,2)
            assert sum(s*a*b for s,(a,b) in enumerate(zip(prob,l),1))-muS*Fraction(n,2) == cov_global(n,k)
            muU = sum(a*b for a,b in zip(prob,u))
            assert sum(s*a*b for s,(a,b) in enumerate(zip(prob,u),1))-muS*muU == cov_local(n,k)
            cases += 1
    return cases


if __name__ == '__main__':
    tree_count = sum(exhaustive(n) for n in range(3,10))
    cases = analytic_grid()
    print('PASS: exhaustive recursive trees =',tree_count)
    print('PASS: exact-rational parameter pairs =',cases)
    print('PASS: conditional distributions, local/global regressions and covariances')
