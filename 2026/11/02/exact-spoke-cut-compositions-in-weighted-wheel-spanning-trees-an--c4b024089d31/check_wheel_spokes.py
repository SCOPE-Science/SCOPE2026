#!/usr/bin/env python3
"""Exact finite checks of a wheel spanning-tree gap/deletion theorem.

Run with Python 3 standard library. This is a bounded, non-certifying test;
the general proof and limiting arguments are in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, cosh, factorial, prod, sinh, sqrt

N_ASSERT = 0

def eq(a, b):
    global N_ASSERT
    assert a == b, (a, b)
    N_ASSERT += 1


def union_tree(n, edge_indices):
    # Vertices are 0,...,n-1 on the rim and n at center.
    parent = list(range(n+1))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    edges = [(i,(i+1)%n) for i in range(n)] + [(n,i) for i in range(n)]
    for index in edge_indices:
        u, v = edges[index]
        a, b = find(u), find(v)
        if a == b:
            return False
        parent[a] = b
    return True


def gap_tuple(n, edge_indices):
    """For a tree containing spoke 0, return its 2k half-step gaps."""
    chosen = set(edge_indices)
    spokes = sorted(i for i in range(n) if (n+i) in chosen)
    cuts = sorted(i for i in range(n) if i not in chosen)
    eq(len(spokes), len(cuts))
    marks = sorted([(2*i,'S') for i in spokes] + [(2*i+1,'D') for i in cuts])
    assert marks[0] == (0,'S')
    assert [kind for _,kind in marks] == ['S','D'] * len(spokes)
    coordinates = [m[0] for m in marks]
    result = []
    for i in range(len(marks)):
        gap = (coordinates[(i+1)%len(marks)] - coordinates[i]) % (2*n)
        assert gap > 0 and gap % 2 == 1
        result.append((gap-1)//2)
    eq(sum(result), n-len(spokes))
    return tuple(result)


def compositions(m, length):
    if length == 1:
        yield (m,)
    else:
        for k in range(m+1):
            for tail in compositions(m-k, length-1):
                yield (k,) + tail


def bareiss(a):
    a = [list(row) for row in a]
    n = len(a)
    sign, denom = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None: return 0
            a[j],a[k] = a[k],a[j]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = a[i][j]*pivot-a[i][k]*a[k][j]
                assert num % denom == 0
                a[i][j] = num//denom
        for i in range(k+1,n):a[i][k]=0
        denom=pivot
    return sign*a[-1][-1]


def laplacian(n,t):
    a = [[0]*n for _ in range(n)]
    for i in range(n):
        a[i][i]=2+t
        a[i][(i+1)%n]=-1
        a[i][(i-1)%n]=-1
    return a


for n in range(3,9):
    cnt = Counter()
    gaps_by_k = {}
    all_forest = 0
    # Every n-edge subset is acyclic exactly when it is a spanning tree.
    for chosen in combinations(range(2*n),n):
        if not union_tree(n,chosen): continue
        all_forest += 1
        k = sum(i>=n for i in chosen)
        cnt[k] += 1
        if n in chosen:
            gaps_by_k.setdefault(k,Counter())[gap_tuple(n,chosen)] += 1
    eq(sum(cnt.values()), all_forest)
    for k in range(1,n+1):
        predicted = n*comb(n+k-1,2*k-1)//k
        eq(cnt[k], predicted)
        expected = set(compositions(n-k,2*k))
        eq(set(gaps_by_k.get(k,{})), expected)
        for value in gaps_by_k[k].values():eq(value,1)
        # Each size composition is weighted by product of component sizes.
        sizes=Counter()
        for gap in gaps_by_k[k]:
            s=tuple(1+gap[(2*j+1)%(2*k)]+gap[(2*j+2)%(2*k)] for j in range(k))
            sizes[s] +=1
        eq(sum(sizes.values()), comb(n+k-1,2*k-1))
        for s,mult in sizes.items(): eq(mult,prod(s))
    # Weighted spanning-tree normalizer independently via reduced Laplacian.
    for t in [1,2,3,5]:
        polynomial_sum=sum(cnt[k]*t**k for k in cnt)
        eq(polynomial_sum,bareiss(laplacian(n,t)))

# For each k, asymptotic count coefficient is 2/(2k)!.
for k in range(1,8):
    for n in range(max(k,3),45):
        c=Fraction(n,k)*comb(n+k-1,2*k-1)
        eq(c.denominator,1)
    seq=[(Fraction(n,k)*comb(n+k-1,2*k-1))/n**(2*k)
         for n in [100,1000,10000]]
    target=Fraction(2,factorial(2*k))
    eq(abs(seq[-1]-target)<=abs(seq[0]-target),True)

# Check the limiting Poisson-even normalizer and mean numerically.
for x in [0.15,0.7,1.3,3.1,11.]:
    z=sum(x**k/factorial(2*k) for k in range(1,51))
    assert abs(z-(cosh(sqrt(x))-1))<1e-10
    m=sum(k*x**k/factorial(2*k) for k in range(1,51))/z
    target=sqrt(x)/2*sinh(sqrt(x))/(cosh(sqrt(x))-1)
    assert abs(m-target)<1e-10
    N_ASSERT+=2

print('PASS',N_ASSERT,'exact assertions/comparison checks, with analytic finite- and limit-law proofs in RESULT.md')
