#!/usr/bin/env python3
"""Reproduce constructive exact bounds for binary Hamming-weight-two three-read codes."""
from itertools import combinations
from functools import lru_cache


def target(n):
    assert n >= 6
    m = n // 3
    return m * (3*m - 1)//2 if n % 3 == 0 else (n*m)//2


def construction(n):
    assert n >= 6
    m = n // 3
    edges = set()

    def add(a,b):
        a, b = a % n, b % n
        assert a != b
        edges.add(tuple(sorted((a,b))))

    if n % 3 == 0:
        R = [[r+3*k for k in range(m)] for r in range(3)]
        for a in R[0]:
            for b in R[1]:
                add(a,b)
        for a,b in combinations(R[2],2):
            add(a,b)
        return sorted(edges)

    h = m//2
    jumps = [3*j-1 for j in range(1,h+1)]
    for a in range(n):
        for d in jumps:
            add(a,a+d)
    if m % 2 == 1:
        if n % 2 == 0:
            for a in range(n//2):
                add(a,a+n//2)
        else:
            step=(n-1)//2
            assert __import__('math').gcd(step,n)==1
            pos=[(step*k)%n for k in range(n)]
            assert len(set(pos))==n
            for i in range(0,n-1,2):
                add(pos[i],pos[i+1])
    return sorted(edges)


def distance(n,A,B):
    s=set(A)^set(B)
    return sum(any((i+t)%n in s for t in range(3)) for i in range(n))


def check_construction(n):
    es=construction(n)
    assert len(es)==target(n), (n,len(es),target(n))
    adj=[[] for _ in range(n)]
    for a,b in es:
        adj[a].append(b)
        adj[b].append(a)
    assert max(map(len,adj))<=n//3
    for neighbors in adj:
        for a,b in combinations(neighbors,2):
            diff=(a-b)%n
            assert min(diff,n-diff)>=3, (n,neighbors,a,b)
    if n<=24:
        for A,B in combinations(es,2):
            assert distance(n,A,B)>=6, (n,A,B,distance(n,A,B))
    return len(es)


def exact_small(n):
    # Independent computation of the *read-metric* conflict graph; no use of
    # the cyclic-neighborhood construction or its mathematical degree bound.
    words=list(combinations(range(n),2))
    N=len(words)
    conflict=[0]*N
    for i,j in combinations(range(N),2):
        if distance(n,words[i],words[j])<6:
            conflict[i]|=1<<j
            conflict[j]|=1<<i
    # Maximum independent set, exhaustive deletion-branching with memoization.
    @lru_cache(None)
    def solve(left):
        if not left:
            return 0
        z=left
        v=-1
        d=-1
        while z:
            b=z&-z
            i=b.bit_length()-1
            c=(conflict[i]&left).bit_count()
            if c>d:
                v,d=i,c
            z-=b
        bit=1<<v
        a=solve(left&~bit)
        b=1+solve(left&~bit&~conflict[v])
        return max(a,b)
    return solve((1<<N)-1)


def main():
    for n in range(6,181):
        check_construction(n)
    print('ALL_N_6_TO_180_CONSTRUCTIONS_OK')
    for n in range(6,12):
        val=exact_small(n)
        assert val==target(n),(n,val,target(n))
        print('EXHAUSTIVE',n,val)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
