#!/usr/bin/env python3
"""Exact integer checks for the A-type Lipman toric singularity formulas.

This finite replay is supplementary to the all-rank arguments in RESULT.md.
Requires only Python 3 standard library.
"""
from fractions import Fraction
from itertools import product
from math import gcd


def isprime(p):
    return p >= 2 and all(p % i for i in range(2, int(p ** .5) + 1))


def divs(N):
    return [d for d in range(1, N + 1) if N % d == 0]


def inv_entry(n, i, j):
    N=n+1
    return Fraction(min(i,j)*(N-max(i,j)), N)

checks=0
for n in range(2, 15):
    N=n+1
    # Cartan times proposed inverse, index 1..n.
    for i in range(1,n+1):
        for j in range(1,n+1):
            result=2*inv_entry(n,i,j)
            if i>1: result-=inv_entry(n,i-1,j)
            if i<n: result-=inv_entry(n,i+1,j)
            assert result == (i==j), (n,i,j,result)
            checks+=1
    # Test actual integrality of Cartan inverse against the congruence.
    from random import Random
    rng=Random(731+n)
    tests = ([0]*n, [1]*n, *([1 if k==j else 0 for k in range(n)] for j in range(n)))
    for v in list(tests)+[[rng.randrange(7) for _ in range(n)] for _ in range(350)]:
        m=[sum(inv_entry(n,i+1,j+1)*v[j] for j in range(n)) for i in range(n)]
        in_lattice=all(x.denominator == 1 for x in m)
        in_congruence=sum((j+1)*v[j] for j in range(n)) % N == 0
        assert in_lattice == in_congruence, (n,v)
        checks+=1

for N in range(3, 141):
    n=N-1
    ps=[p for p in divs(N) if isprime(p)]
    components=[frozenset(i for i in range(1,N) if i%p == 0) for p in ps]
    # Each prime fixed space is a maximal nontrivial fixed space.
    for k,S in enumerate(components):
        assert not any(S < T for j,T in enumerate(components) if j != k)
        checks+=1
    for a in range(1,N):
        d=N//gcd(a,N)
        f=[(a*i)%N for i in range(1,N)]
        zero=sum(x == 0 for x in f)
        assert zero == N//d-1
        assert sum(f) == N*(N-N//d)//2
        age=Fraction(sum(f),N)
        assert age == Fraction(N-N//d,2)
        assert sum(1 for x in f if x != 0) >= 2
        checks+=4
    assert min((Fraction(sum((a*i)%N for i in range(1,N)),N)
                +sum((a*i)%N==0 for i in range(1,N))) for a in range(1,N)) == Fraction(n,2)
    assert (min(Fraction(sum((a*i)%N for i in range(1,N)),N) for a in range(1,N)) > 1) == (n>=4)
    # Canonical index from the character of top differential form.
    c=sum(range(1,N))%N
    ind=N//gcd(N,c)
    assert ind == (1 if n%2==0 else 2)
    # Generic fixed loci: precisely one copy of each nontrivial p-character per N/p blocks.
    for p in ps:
        cnt=[sum(i%p==r for i in range(1,N)) for r in range(p)]
        assert cnt == [N//p-1]+[N//p]*(p-1)
        checks+=1
    checks+=3
print('VERIFY_OK',checks)
