"""Exact finite checks for pendant-star/leaf covariance in uniform labelled trees.

Run with Python 3. No external dependencies. Finite checks supplement the universal proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb


def prufer_degrees(word, n):
    deg = [1] * n
    for x in word:
        deg[x] += 1
    remaining = list(deg)
    edges = []
    for x in word:
        leaf = next(j for j in range(n) if remaining[j] == 1)
        edges.append((leaf, x))
        remaining[leaf] -= 1
        remaining[x] -= 1
    last = [j for j in range(n) if remaining[j] == 1]
    assert len(last) == 2
    edges.append(tuple(last))
    return deg, edges


def leaf_pendant_counts(deg, edges):
    n = len(deg)
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    L = deg.count(1)
    S = [0] * (n - 2)
    for v in range(n):
        k = deg[v] - 1
        if 1 <= k <= n - 3 and sum(deg[u] == 1 for u in adj[v]) == k:
            S[k] += 1
    return L, S, adj


def f(n):
    return Fraction(n * (n-1)**(n-2), n**(n-2))


def h(b):
    return Fraction((b-1)**(b-1), b**(b-2))


def expected_star(n, k):
    return Fraction(n * comb(n-1, k) * (n-k-1)**(n-k-2), n**(n-2))


def delta(n, k):
    return k + h(n-k-1) - f(n)


def pmf_zeros(b, m):
    """Number of empty bins after m iid uniform draws into b bins."""
    return {z: Fraction(comb(b, z) * sum((-1)**j * comb(b-z, j) * (b-z-j)**m for j in range(b-z+1)), b**m)
            for z in range(b+1)}


def exhaustive():
    checks = 0
    for n in range(4, 9):
        denom = n**(n-2)
        sums = [0] * (n-2)
        mixes = [0] * (n-2)
        totalL = 0
        fixed = defaultdict(lambda: defaultdict(int))
        for word in product(range(n), repeat=n-2):
            deg, edges = prufer_degrees(word, n)
            L, S, adj = leaf_pendant_counts(deg, edges)
            totalL += L
            for k in range(1, n-2):
                sums[k] += S[k]
                mixes[k] += L*S[k]
                if deg[k] == k+1 and all(deg[a] == 1 and k in adj[a] for a in range(k)):
                    fixed[k][L] += 1
        assert Fraction(totalL, denom) == f(n)
        checks += 1
        for k in range(1, n-2):
            ES = expected_star(n, k)
            assert Fraction(sums[k], denom) == ES, (n,k,'mean')
            assert Fraction(mixes[k], denom) - f(n)*ES == ES*delta(n,k), (n,k,'cov')
            zdist = pmf_zeros(n-k-1, n-k-2)
            countE = sum(fixed[k].values())
            assert countE == (n-k-1)**(n-k-2)
            for z, p in zdist.items():
                assert Fraction(fixed[k][k+z], countE) == p, (n,k,z,'conditional pmf')
                checks += 1
            checks += 3
        print('n=',n,'trees=',denom,'signs=',{k: ('-' if delta(n,k)<0 else '+') for k in range(1,n-2)})
    for n in range(4, 251):
        for k in range(1,n-2):
            assert (delta(n,k)<0 if k==1 else delta(n,k)>0), (n,k)
            checks += 1
    print('PASS exact comparisons:',checks)

if __name__ == '__main__':
    exhaustive()
