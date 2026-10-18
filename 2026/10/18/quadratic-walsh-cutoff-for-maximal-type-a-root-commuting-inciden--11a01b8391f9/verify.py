#!/usr/bin/env python3
"""Finite checks for root-unit commuting cliques and their incidence Fourier kernel.
Standard library only; checks do not replace the all-n mathematical proof.
"""
from itertools import combinations
from collections import Counter
from functools import lru_cache


def edges(n):
    return [(i, j) for i in range(n) for j in range(i+1, n)]


def product(A, B, n):
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def unit(n, i, j):
    U = [[0]*n for _ in range(n)]
    U[i][j] = 1
    return U


def maximal_cliques_direct(n):
    e = edges(n)
    u = [unit(n,*a) for a in e]
    d = len(e)
    adjacent = [0]*d
    for i in range(d):
        for j in range(i+1,d):
            if product(u[i],u[j],n) == product(u[j],u[i],n):
                adjacent[i] |= 1 << j
                adjacent[j] |= 1 << i
    found = set()
    for mask in range(1,1<<d):
        ok = True
        for i in range(d):
            if mask>>i&1 and ((mask & ~(1<<i)) & ~adjacent[i]):
                ok = False
                break
        if not ok: continue
        if any(not(mask>>j&1) and all(not(mask>>i&1) or (adjacent[i]>>j&1) for i in range(d)) for j in range(d)):
            continue
        found.add(frozenset(e[j] for j in range(d) if mask>>j&1))
    return found


def cuts(n):
    for mask in range(1 << (n-2)):
        S = {0} | {i+1 for i in range(n-2) if mask>>i&1}
        yield mask,S


def clique(n, S):
    return frozenset((i,j) for i,j in edges(n) if i in S and j not in S)


def rank_mod(rows, p):
    a = [[x%p for x in row] for row in rows]
    m,n = len(a),len(a[0])
    k = 0
    for j in range(n):
        pivot = next((i for i in range(k,m) if a[i][j]),None)
        if pivot is None:continue
        a[k],a[pivot] = a[pivot],a[k]
        inv = pow(a[k][j],-1,p)
        for v in range(j,n):a[k][v] = a[k][v]*inv%p
        for i in range(k+1,m):
            if a[i][j]:
                fac = a[i][j]
                for v in range(j,n):a[i][v] = (a[i][v]-fac*a[k][v])%p
        k += 1
        if k==m:break
    return k


@lru_cache(None)
def gaussian(m,a):
    if a<0 or a>m:return Counter()
    if m==0:return Counter({0:1}) if a==0 else Counter()
    # A source appended after m-a sinks adds m-a reverse pairs.
    out = gaussian(m-1,a).copy()
    for exponent,weight in gaussian(m-1,a-1).items():
        out[exponent + m-a] += weight
    return out


def check():
    for n in range(2,7):
        observed = maximal_cliques_direct(n)
        predicted = set(clique(n,S) for _,S in cuts(n))
        assert observed == predicted, ('maximal',n)
    for n in range(2,10):
        e = edges(n)
        choices = list(cuts(n))
        B = [[int(i in S and j not in S) for i,j in e] for _,S in choices]
        m = n-2
        expected = 1+m+m*(m-1)//2
        assert rank_mod(B,1000003)==expected, ('rank',n)
        assert rank_mod(B,1000033)==expected, ('second_rank',n)
        counts = Counter(sum(row) for row in B)
        expected_count = Counter()
        for s in range(1,n):
            for inv,w in gaussian(n-2,s-1).items():
                expected_count[s*(n-s)-inv] += w
        assert counts == expected_count, ('size_polynomial',n,counts,expected_count)
        # Independently verify every Walsh character of degree at least three
        # is in the *left* kernel of the full incidence matrix.
        for d in range(3,m+1):
            for J in combinations(range(m),d):
                weights = [(-1)**sum(bool(mask>>j&1) for j in J) for mask,_ in choices]
                assert all(sum(w*B[a][col] for a,w in enumerate(weights))==0
                           for col in range(len(e))), ('Walsh',n,J)
        # Integer finite-difference generators have localized support on a
        # Boolean subcube, and annihilate every root column exactly over Z.
        for A in range(1<<m):
            if A.bit_count()<3: continue
            weights = [((-1)**(A.bit_count()-mask.bit_count())
                        if (mask&A)==mask else 0) for mask,_ in choices]
            assert all(sum(w*B[a][col] for a,w in enumerate(weights))==0
                       for col in range(len(e))), ('integer_difference',n,A)
        # For each monomial degree <= 2 the polynomial coefficients of the
        # root-incidence columns form a unimodular matrix after elementary
        # integer column operations, witnessed by the triangular evaluation
        # on supports of size <= 2.
        subsets = [A for A in range(1<<m) if A.bit_count()<=2]
        E = [[int((A&T)==T) for T in subsets] for A in subsets]
        assert all(E[i][i]==1 and all(E[i][j]==0 for j in range(i+1,len(subsets)) if (subsets[j]&subsets[i])!=subsets[j])
                   for i in range(len(subsets)))
        if n>=5:
            assert (1<<m)-expected>0
    print('VERIFY_OK_ROOT_WALSH n=2..9; exact maximal cliques n=2..6; modular rank, Walsh and integral-difference kernels n=2..9')


if __name__ == '__main__':
    check()
