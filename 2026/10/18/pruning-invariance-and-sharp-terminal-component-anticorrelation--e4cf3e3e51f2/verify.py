"""Exact finite-sample checks for the random-mapping pruning identities.

Run with Python 3 standard library: python verify.py
The universal statements and asymptotic limit require the accompanying proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial, exp


def falling(n, r):
    if r > n:
        return 0
    ans = 1
    for i in range(r):
        ans *= n-i
    return ans


def cycle_profile(f):
    n = len(f)
    counts = [0] * (n + 1)
    indegrees = [0] * n
    for v in f:
        indegrees[v] += 1
    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        where = {}
        v = start
        while not visited[v] and v not in where:
            where[v] = len(where)
            v = f[v]
        if v in where:
            counts[len(where) - where[v]] += 1
        for v in where:
            visited[v] = True
    return sum(a == 0 for a in indegrees), tuple(counts)


def enumerate_mappings(n):
    hist = Counter()
    for f in product(range(n), repeat=n):
        leaves, profile = cycle_profile(f)
        hist[(leaves, profile)] += 1
    return hist


def mean_cycles(n):
    return sum((Fraction(falling(n, k), k * n**k) for k in range(1,n+1)), Fraction(0))


def mean_cycle_k(n, k):
    return Fraction(falling(n, k), k * n**k) if k <= n else Fraction(0)


def check():
    hist = {n: enumerate_mappings(n) for n in range(1, 7)}
    checks = 0
    for n in range(2, 7):
        h = hist[n]
        total = n**n
        expectation = lambda func: sum((Fraction(c * func(l, p), total) for (l,p),c in h.items()), Fraction(0))
        cmean = expectation(lambda l,p:sum(p))
        assert cmean == mean_cycles(n)
        checks += 1
        e_l = expectation(lambda l,p:l)
        assert e_l == Fraction(n*(n-1)**n, n**n)
        checks += 1
        expected_cov = Fraction(n*(n-1)**n, n**n) * (mean_cycles(n-1) - mean_cycles(n))
        direct_cov = expectation(lambda l,p:l*sum(p)) - e_l*cmean
        assert direct_cov == expected_cov and expected_cov < 0
        checks += 1
        for k in range(1,n+1):
            cv = expectation(lambda l,p:l*p[k]) - e_l*expectation(lambda l,p:p[k])
            formula = Fraction(n*(n-1)**n,n**n)*(mean_cycle_k(n-1,k)-mean_cycle_k(n,k))
            assert cv==formula and (cv==0 if k==1 else cv<0)
            checks += 1
        for r in range(n):
            for c in range(1,n+1):
                direct=expectation(lambda l,p:falling(l,r)*(sum(p)==c))
                hm=hist[n-r]
                p_small=Fraction(sum(v for (l,p),v in hm.items() if sum(p)==c),(n-r)**(n-r))
                right=Fraction(falling(n,r)*(n-r)**n,n**n)*p_small
                assert direct==right,(n,r,c,direct,right)
                checks += 1
        for k in range(1,n+1):
            observed=expectation(lambda l,p:sum(i*p[i] for i in range(1,n+1))>=k)
            assert observed==Fraction(falling(n,k),n**k)
            checks += 1
        print('exhausted all',n**n,'mappings on',n,'vertices')
    for n in range(2,501):
        assert mean_cycles(n)>mean_cycles(n-1)
        checks+=1
    # Floating diagnostic only; it is not an asymptotic proof.
    def fast_diff(n):
        a=b=1.0
        delta=0.0
        for k in range(1,n+1):
            a*=1-(k-1)/n
            b=b*(1-(k-1)/(n-1)) if k<=n-1 else 0.0
            delta+=(a-b)/k
        return -n*((n-1)/n)**n*delta
    target=-1/(2*exp(1))
    estimate=fast_diff(10000)
    assert abs(estimate-target)<0.001
    print('CHECKS_OK',checks,'asymptotic_numeric',estimate,'target',target)


if __name__ == '__main__':
    check()
