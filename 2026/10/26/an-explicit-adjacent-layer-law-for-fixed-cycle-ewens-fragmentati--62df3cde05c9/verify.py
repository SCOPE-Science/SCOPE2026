"""Exact reproducibility checks for fixed-cycle-count partition fragmentation."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial, prod
from random import Random


def esym(v):
    a=[F(1)]
    for x in v:
        a=[a[0]]+[a[t]+x*a[t-1] if t<len(a) else x*a[t-1]
                   for t in range(1,len(a)+1)]
    return a


def split_prob(j,n,r):
    tail=esym([F(1,i-1) for i in range(j+1,n+1)])
    e=lambda s:tail[s] if 0<=s<len(tail) else F(0)
    num=F(1,j-1)*e(r-1)
    den=e(r)+num
    assert den>0
    return num/den


def all_levels(n,rng):
    rank_left=list(range(n))
    cuts=[set() for _ in range(n)]
    for j in range(2,n+1):
        u=rng.random()
        hit=[int(u<float(split_prob(j,n,r))) for r in rank_left]
        for r,x in enumerate(hit):
            if x:cuts[r].add(j)
            rank_left[r]-=x
    assert rank_left==[0]*n
    return cuts


def partition_from_cuts(perm,cuts):
    n=len(perm)
    blocks=[]
    start=0
    for i in range(2,n+2):
        if i==n+1 or i in cuts:
            blocks.append(frozenset(perm[start:i-1]))
            start=i-1
    return frozenset(blocks)


def exact_check(n):
    checks=0
    P=list(permutations(range(1,n+1)))
    for k in range(1,n+1):
        masses=defaultdict(F)
        subsets=list(combinations(range(2,n+1),k-1))
        weights={S:F(1,prod(j-1 for j in S)) for S in subsets}
        z=sum(weights.values())
        for S,w in weights.items():
            for perm in P:
                masses[partition_from_cuts(perm,S)]+=w/(z*factorial(n))
        assert sum(masses.values())==1
        norm=sum(prod(factorial(len(b)-1) for b in part) for part in masses)
        for part,prob in masses.items():
            assert len(part)==k
            assert prob==F(prod(factorial(len(b)-1) for b in part),norm)
            checks+=1
    return checks


def pair_probability(n,r,S,h):
    """Exact probability of consecutive cut sets (S, S union {h})."""
    assert h not in S and len(S)==r
    q=F(1)
    for j in range(2,n+1):
        budget=r-sum(t in S for t in range(2,j))
        if j<h:
            q*=split_prob(j,n,budget) if j in S else 1-split_prob(j,n,budget+1)
        elif j==h:
            q*=split_prob(j,n,budget+1)-split_prob(j,n,budget)
        else:
            q*=split_prob(j,n,budget) if j in S else 1-split_prob(j,n,budget)
    return q


def exact_pair_check(n):
    checks=0
    U={}
    for r in range(n):
        for S in combinations(range(2,n+1),r):
            U[frozenset(S)]=prod(F(1,j-1) for j in S)
    z={r:sum(w for S,w in U.items() if len(S)==r) for r in range(n)}
    for r in range(n-1):
        for SS in combinations(range(2,n+1),r):
            S=frozenset(SS)
            row=sum((pair_probability(n,r,S,h) for h in range(2,n+1) if h not in S),F(0))
            assert row==U[S]/z[r],(n,r,S,row,U[S]/z[r])
            checks+=1
        for TT in combinations(range(2,n+1),r+1):
            T=frozenset(TT)
            col=sum((pair_probability(n,r,T-{h},h) for h in T),F(0))
            assert col==U[T]/z[r+1],(n,r,T,col,U[T]/z[r+1])
            checks+=1
    return checks


def coupled_check(n,reps=200):
    rng=Random(105891+n)
    checks=0
    for _ in range(reps):
        S=all_levels(n,rng)
        order=list(range(1,n+1));rng.shuffle(order)
        P=[partition_from_cuts(order,c) for c in S]
        for r in range(n):
            assert len(S[r])==r
            assert len(P[r])==r+1
            if r+1<n:
                assert S[r].issubset(S[r+1])
                assert all(any(b.issubset(c) for c in P[r]) for b in P[r+1])
                checks+=1
    return checks


def proof_lemma_check(n):
    checks=0
    for j in range(2,n+1):
        for r in range(n-j+1):
            assert split_prob(j,n,r)<=split_prob(j,n,r+1)
            checks+=1
    return checks


if __name__=='__main__':
    exact=sum(exact_check(n) for n in range(1,6))
    coupling=sum(coupled_check(n,12) for n in range(1,18))
    lemma=sum(proof_lemma_check(n) for n in range(2,26))
    pair=sum(exact_pair_check(n) for n in range(2,9))
    print(f'PASS exact partition probabilities: {exact}; coupling edges: {coupling}; choice monotonicity: {lemma}; exact adjacent transitions: {pair}.')
