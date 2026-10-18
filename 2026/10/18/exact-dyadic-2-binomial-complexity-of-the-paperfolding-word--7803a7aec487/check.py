#!/usr/bin/env python3
"""Exact dyadic recursion and sliding-window tests for paperfolding 2-binomial signatures."""
from collections import Counter


def p(i):
    assert i >= 1
    while i % 2 == 0:
        i //= 2
    return int(i % 4 == 1)


def recurse(max_k):
    sets = [{(0, 0), (1, 0), (1, 1), (2, 1)} for _ in (0,1)]
    yield 1, sets
    for k in range(2, max_k+1):
        m=1 << (k-1)
        new=[set(),set()]
        for parity in (0,1): # parity of halved starting index
            for c,t in sets[parity]:
                new[0].add((c+m//2, 2*t + m*(m-1)//2 + parity*m))
                new[1].add((c+m//2, 2*t+c + (m*m//2 if parity==0 else m*(m-2)//2)))
        sets=new
        yield k,sets


def sliding(n,L):
    s=[p(j) for j in range(1,L+1)]
    c=sum(s[:n]); t=sum(j*s[j] for j in range(n))
    found=[set(),set()]
    for start0 in range(L-n+1):
        found[(start0+1)%2].add((c,t))
        if start0+n < L:
            old=s[start0]; new=s[start0+n]
            t=t-(c-old)+(n-1)*new
            c=c-old+new
    return found


def verify():
    for k,S in recurse(11):
        n=1<<k
        universe=S[0]|S[1]
        if k>=2:
            assert len(universe)==2*n+k+1,(k,len(universe))
            assert len(S[0])==len(S[1])==n+k+1,(k, len(S[0]),len(S[1]))
            mid=sorted(t for c,t in universe if c==n//2)
            exact=[n*(n-1-k)//4+j*n//2 for j in range(k+1)]
            assert mid==exact,(k,mid,exact)
            for side in (n//2-1,n//2+1):
                assert sum(c==side for c,t in universe)==n
                assert sum(c==side for c,t in S[0])==n//2
                assert sum(c==side for c,t in S[1])==n//2
                assert not ({t for c,t in S[0] if c==side} & {t for c,t in S[1] if c==side})
        if k<=9:
            observed=sliding(n,1<<17)
            assert observed==S,(k,[len(x) for x in observed],[len(x) for x in S])
        print(f'PASS n={n} conditional={len(S[0])},{len(S[1])} total={len(universe)}')
    print('PAPERFOLDING_DYADIC_2_BINOMIAL_ALL_CHECKS_PASSED')


if __name__=='__main__': verify()
