#!/usr/bin/env python3
"""Exact tests for simplex-code absorbers on binary hypercubes."""
from itertools import combinations, combinations_with_replacement
from math import comb
import random

PRIME = 2305843009213693951

def syndrome_ranks(columns, m):
    n = len(columns)
    reach = [set() for _ in range(n+1)]
    reach[0].add(0)
    for i, a in enumerate(columns):
        for w in range(i+1, 0, -1):
            reach[w].update(s ^ a for s in reach[w-1])
    return [len(v) for v in reach]

def gf2_rank(values):
    basis = {}
    for v in values:
        while v:
            j = v.bit_length()-1
            if j not in basis:
                basis[j] = v
                break
            v ^= basis[j]
    return len(basis)

def rank_columns_mod_p(columns, row_count):
    basis = {}
    for vector in columns:
        v = [x % PRIME for x in vector]
        for pivot, b in sorted(basis.items()):
            c = v[pivot]
            if c:
                for i in range(pivot, row_count):
                    v[i] = (v[i]-c*b[i]) % PRIME
        pivot = next((i for i,x in enumerate(v) if x), None)
        if pivot is not None:
            scale = pow(v[pivot], -1, PRIME)
            for i in range(pivot, row_count):
                v[i] = v[i]*scale % PRIME
            basis[pivot] = v
    return len(basis)

def direct_walsh_ranks(m):
    n = (1 << m)-1
    q = 1 << m
    ranks = []
    for w in range(n+1):
        cols = []
        for subset in combinations(range(1,n+1), w):
            syndrome = 0
            for c in subset:
                syndrome ^= c
            cols.append([1 if ((t & syndrome).bit_count()%2)==0 else -1
                         for t in range(q)])
        ranks.append(rank_columns_mod_p(cols, q))
    return ranks

def physical_krylov_rank(m):
    n = (1 << m)-1
    Q = 1 << n
    traps = [sum(((t & a).bit_count() & 1) << (a-1)
                 for a in range(1,n+1)) for t in range(1<<m)]
    columns = []
    for z in traps:
        vector = [0]*Q
        vector[z] = 1
        for _ in range(n+1):
            columns.append(vector)
            vector = [sum(vector[x ^ (1<<j)] for j in range(n)) for x in range(Q)]
    return rank_columns_mod_p(columns, Q)

def c_w(n, w):
    L = (n+1)//2
    j = w//2
    return (-1)**(j+(w & 1))*comb(L-1,j)

def analytic_rank(m,w):
    n = (1<<m)-1
    q = n+1
    c = c_w(n,w)
    a = comb(n,w)
    return (int(a+n*c != 0) + n*int(a-c != 0))

def check():
    counters = {'exact_walsh':0,'gram_eigenvalues':0,'generator_multisets':0,'random_generator':0,'krylov':0}
    for m in (3,4):
        n=(1<<m)-1
        expected=[1,n,n]+[n+1]*(n-5)+[n,n,1]
        cols=list(range(1,n+1))
        got=syndrome_ranks(cols,m)
        assert got==expected,(m,got,expected)
        brute=direct_walsh_ranks(m)
        assert brute==expected,(m,brute)
        counters['exact_walsh']+=n+1
        for w in range(n+1):
            assert analytic_rank(m,w)==expected[w],(m,w)
            a=comb(n,w)
            c=c_w(n,w)
            assert (a+n*c) >= 0 and (a-c)>=0
            counters['gram_eigenvalues']+=1
        assert sum(got)==n*n-3
    assert physical_krylov_rank(3)==46
    counters['krylov']=1
    m=3;n=7;best=0;attainers=0
    for cols in combinations_with_replacement(range(1<<m),n):
        if gf2_rank(cols)<m:
            continue
        bright=sum(syndrome_ranks(cols,m))
        assert bright<=n*n-3,(cols,bright)
        best=max(best,bright)
        attainers+=(bright==n*n-3)
        counters['generator_multisets']+=1
    assert best==46 and attainers>0
    m=4;n=15
    rng=random.Random(1031)
    for _ in range(400):
        cols=[rng.randrange(1<<m) for _ in range(n)]
        if gf2_rank(cols)<m:
            continue
        assert sum(syndrome_ranks(cols,m))<=n*n-3
        counters['random_generator']+=1
    assert counters['random_generator']>=390
    print('VERIFY_OK',counters, 'm3_optimal_multisets',attainers)

if __name__=='__main__':
    check()
