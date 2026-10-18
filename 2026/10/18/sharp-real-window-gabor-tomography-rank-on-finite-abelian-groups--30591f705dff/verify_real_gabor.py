#!/usr/bin/env python3
"""Exact cyclotomic checks for real finite-abelian Gabor projector ranks.
Uses only the Python standard library; finite examples corroborate the general proof.
"""
from itertools import product
from math import gcd, lcm
from functools import lru_cache


def div_exact(a, b):
    a = a[:]
    q = [0] * (len(a) - len(b) + 1)
    while len(a) >= len(b):
        k = len(a) - len(b)
        c = a[-1] // b[-1]
        assert a[-1] == c * b[-1]
        q[k] = c
        for i, v in enumerate(b):
            a[k+i] -= c*v
        while a and a[-1] == 0:
            a.pop()
    assert not a, a
    return q


@lru_cache(None)
def cyclo(n):
    p = [-1] + [0] * (n-1) + [1]
    for d in range(1, n):
        if n % d == 0:
            p = div_exact(p, cyclo(d))
    return p


def is_zero_cyclotomic(coeffs, n):
    a = coeffs[:]
    b = cyclo(n)
    while len(a) >= len(b):
        if not a[-1]:
            a.pop()
            continue
        coef = a[-1] // b[-1]
        assert coef * b[-1] == a[-1]
        idx = len(a)-len(b)
        for j, bj in enumerate(b):
            a[idx+j] -= coef*bj
        while a and a[-1] == 0:
            a.pop()
    return all(v == 0 for v in a)


def elements(mods):
    return list(product(*(range(n) for n in mods)))


def char_power(x, k, mods, L):
    return sum((ki * xi * (L // ni)) for xi,ki,ni in zip(x,k,mods)) % L


def rank_by_ambiguity(mods, S):
    G=elements(mods)
    N=len(G)
    L=lcm(*mods)
    index={x:i for i,x in enumerate(G)}
    # One uniform positive integer witness for any support, deterministic.
    B=2*N+1
    g={x:B**(2**i) for i,x in enumerate(S)}
    D={tuple((xj-yj)%nj for xj,yj,nj in zip(x,y,mods)) for x in S for y in S}
    two={x for x in G if all((2*xj)%nj==0 for xj,nj in zip(x,mods))}
    e=len((D & two)-{tuple(0 for _ in mods)})
    expected=N*len(D)-N*e//2
    zeros=[]
    for a in G:
        for k in G:
            coeff=[0]*L
            for x in S:
                xm=tuple((xi-ai)%ni for xi,ai,ni in zip(x,a,mods))
                if xm in g:
                    coeff[char_power(x,k,mods,L)] +=g[x]*g[xm]
            actual=is_zero_cyclotomic(coeff,L)
            forced=(a not in D) or (a in two and any(a) and char_power(a,k,mods,L)==L//2 and L%2==0)
            assert actual == forced,(mods,S,a,k,actual,forced)
            if actual: zeros.append((a,k))
    assert N*N-len(zeros)==expected,(mods,S,N*N-len(zeros),expected)
    return expected


def run():
    examples=[(2,),(3,),(4,),(5,),(6,),(8,),(2,2),(2,4),(2,2,2),(3,3)]
    cases=0
    for mods in examples:
        G=elements(mods)
        N=len(G)
        counts=set()
        # Full exact support census for every subset of groups with <=9 elements.
        for mask in range(1,1<<N):
            S=[x for i,x in enumerate(G) if mask & (1<<i)]
            counts.add(rank_by_ambiguity(mods,S))
            cases+=1
        t=sum(all(2*xj%nj==0 for xj,nj in zip(x,mods)) for x in G)
        full_rank=N*N-(N//2)*(t-1) if N%2==0 else N*N
        assert rank_by_ambiguity(mods,G)==full_rank
        print(f'GROUP {mods} N={N} torsion={t} full_max_rank={full_rank} ranks={sorted(counts)} all_supports={2**N-1}')
    print(f'EXACT_CHECK_OK support_patterns={cases}')

if __name__=='__main__':
    run()
