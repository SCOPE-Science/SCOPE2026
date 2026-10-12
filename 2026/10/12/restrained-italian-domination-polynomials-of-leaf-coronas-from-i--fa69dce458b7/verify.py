"""Independent finite checks of restrained Italian domination on leaf coronas.
Run: python verify.py
The finite checks support, but do not replace, the stated general proof.
"""
from itertools import product
from math import comb
from collections import Counter
import random


def edges_to_adj(n, edge_mask):
    out = [0] * n
    q = 0
    for i in range(n):
        for j in range(i + 1, n):
            if edge_mask & (1 << q):
                out[i] |= 1 << j
                out[j] |= 1 << i
            q += 1
    return out


def formula(adj):
    n = len(adj)
    coeff = Counter()
    for S in range(1 << n):
        if any(S & (1 << i) and not (adj[i] & S) for i in range(n)):
            continue
        b = sum(bool((S >> i) & 1) and bool(adj[i] & ~S) for i in range(n))
        power = 2 * n - b
        d = 2 * (n - S.bit_count()) + b
        for j in range(d + 1):
            coeff[power + j] += comb(d, j)
    return coeff


def brute(adj):
    n = len(adj)
    coeff = Counter()
    neighbors = [tuple(j for j in range(n) if adj[i] & (1 << j)) + (n+i,)
                 for i in range(n)]
    neighbors += [(i,) for i in range(n)]
    # Full ternary enumeration, including initially possible zero leaves.
    for labels in product(range(3), repeat=2*n):
        if all(any(labels[u] == 0 for u in neighbors[v]) and
               sum(labels[u] for u in neighbors[v]) >= 2
               for v in range(2*n) if labels[v] == 0):
            coeff[sum(labels)] += 1
    return coeff


def cycle(n):
    a = [0] * n
    for i in range(n):
        a[i] = (1 << ((i - 1) % n)) | (1 << ((i + 1) % n))
    return a


def cycle_closed(n):
    coeff = Counter()
    for exp, mult in ((2*n,1),):
        coeff[exp] += mult
    for j in range(2*n+1):
        coeff[2*n+j] += comb(2*n,j)
    for k in range(1,n//3+1):
        for s in range(2*k,n-k+1):
            numer=n*comb(s-k-1,k-1)*comb(n-s-1,k-1)
            assert numer % k == 0
            mult=numer//k
            for j in range(2*n-2*s+2*k+1):
                coeff[2*n-2*k+j]+=mult*comb(2*n-2*s+2*k,j)
    return coeff


def min_count(n):
    k=n//3
    r=n-3*k
    numer=n*comb(r+2*k-1,2*k-1)
    assert numer % k == 0
    return numer//k


def run():
    checks=0
    for n in range(0,5):
        for mask in range(1 << (n*(n-1)//2)):
            a=edges_to_adj(n,mask)
            got=brute(a)
            expected=formula(a)
            assert got == expected, ('all graphs',n,mask,got,expected)
            checks+=1
    print('all simple graphs through four vertices:',checks,'passed')
    rng=random.Random(314159)
    for n,cases in ((5,30),(6,5)):
        for _ in range(cases):
            a=edges_to_adj(n,rng.getrandbits(n*(n-1)//2))
            assert brute(a)==formula(a)
            checks+=1
    print('including deterministic sampled graphs on five and six vertices:',checks,'passed')
    for n in range(3,12):
        a=cycle(n)
        p=formula(a)
        assert p==cycle_closed(n),('cycle closed form',n)
        k=n//3
        assert min(p)==2*n-2*k,('minimum',n)
        assert p[min(p)]==min_count(n),('min count',n)
        if n<=7:
            assert brute(a)==p,('cycle brute',n)
    print('cycle closed polynomial and minimum/census identities, n=3..11: passed')
    print('sunlet first coefficients (n, weight, multiplicity):',
          [(n,2*n-2*(n//3),min_count(n)) for n in range(3,12)])
    print('VERIFIED_FINITE_CHECKS_OK')

if __name__=='__main__':
    run()
