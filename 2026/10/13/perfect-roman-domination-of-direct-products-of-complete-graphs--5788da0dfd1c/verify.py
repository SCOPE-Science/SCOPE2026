#!/usr/bin/env python3
"""Finite tests for perfect Roman domination on complete-graph direct products.

Uses a vertex-subset enumeration of the 2-support, then an independent
ternary-label enumeration on the smallest instances. No external packages.
"""
from itertools import product, combinations
from collections import defaultdict
import random


def adjacencies(m, n):
    return [sum(1 << (u*n+v) for u in range(m) for v in range(n)
                if u != i and v != j) for i in range(m) for j in range(n)]


def canonical_weight(A, adj, N):
    t = A.bit_count()
    if t == 0:
        return N
    private = sum(1 for v in range(N) if not(A >> v & 1)
                  and (A & adj[v]).bit_count() == 1)
    return N+t-private


def support_search(m, n):
    N = m*n
    adj = adjacencies(m, n)
    target = m+n
    optimum, count, sizes = N+1, 0, defaultdict(int)
    for A in range(1 << N):
        w = canonical_weight(A, adj, N)
        if w < optimum:
            optimum, count, sizes = w, 0, defaultdict(int)
        if w == optimum:
            count += 1
            sizes[A.bit_count()] += 1
    exp_count = N + (6 if (m,n)==(3,3) else 0)
    exp_sizes = {1:N, 3:6} if (m,n)==(3,3) else {1:N}
    assert optimum == target, (m,n,optimum,target)
    assert count == exp_count, (m,n,count,exp_count)
    assert dict(sizes) == exp_sizes, (m,n,dict(sizes),exp_sizes)
    print(f'SUPPORTS_OK ({m},{n}) masks={1<<N} optimum={optimum} minimum_count={count} support_sizes={dict(sizes)}')
    return 1 << N


def ternary_search(m, n):
    N=m*n
    adj=adjacencies(m,n)
    expected=m+n
    opt=N+1
    num=0
    for f in product(range(3),repeat=N):
        weight=sum(f)
        if weight>opt: continue
        two=sum(1<<i for i,z in enumerate(f) if z==2)
        if any((two&adj[i]).bit_count()!=1 for i,z in enumerate(f) if z==0):
            continue
        if weight<opt:
            opt=weight
            num=0
        if weight==opt:
            num+=1
    exp=N+(6 if (m,n)==(3,3) else 0)
    assert (opt,num)==(expected,exp), (m,n,opt,num,expected,exp)
    print(f'TERNARY_OK ({m},{n}) assignments={3**N} optimum={opt} minimum_count={num}')
    return 3**N


def structured_random(m,n,reps=15000):
    rng=random.Random(20261010+m*100+n)
    N=m*n
    adj=adjacencies(m,n)
    count=0
    for _ in range(reps):
        A=rng.getrandbits(N)
        if canonical_weight(A,adj,N)<m+n:
            raise AssertionError((m,n,A))
        count+=1
    for t in range(4):
        for subset in combinations(range(N),t):
            A=sum(1<<v for v in subset)
            assert canonical_weight(A,adj,N)>=m+n
            count+=1
    print(f'SAMPLED_OK ({m},{n}) support_masks={count} lower_bound={m+n}')

if __name__=='__main__':
    masks=sum(support_search(m,n) for m,n in
              [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3)])
    assigns=sum(ternary_search(m,n) for m,n in [(3,3),(3,4)])
    for m,n in [(5,5),(5,7),(7,6),(3,12)]:structured_random(m,n)
    print(f'REPLAY_OK exhaustive_support_masks={masks} exhaustive_ternary_assignments={assigns}')
