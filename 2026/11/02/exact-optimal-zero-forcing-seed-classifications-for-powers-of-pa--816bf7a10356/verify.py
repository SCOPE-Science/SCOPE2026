#!/usr/bin/env python3
"""Finite reproducibility checks for optimal zero-forcing seeds in graph powers."""
from itertools import combinations
from math import comb


def adjacencies(n, k, cyclic):
    rows = []
    for u in range(n):
        rows.append(sum(1 << v for v in range(n) if v != u and
            ((min((v-u) % n, (u-v) % n) <= k) if cyclic else (abs(u-v) <= k))))
    return rows


def forces_all(adjs, initial):
    full = (1 << len(adjs)) - 1
    black = initial
    while black != full:
        added = 0
        for u, near in enumerate(adjs):
            if black & (1 << u):
                white = near & ~black
                if white and white & (white-1) == 0:
                    added |= white
        if not added:
            return False
        black |= added
    return True


def mask(a):
    return sum(1 << x for x in a)


def candidate_seeds(n, k, cyclic):
    if cyclic:
        if n == 2*k+1:
            return {((1 << n)-1) ^ (1 << v) for v in range(n)}
        ans=set()
        for v in range(n):
            near=[u for u in range(n) if u!=v and min((u-v)%n,(v-u)%n)<=k]
            for w in near:
                ans.add(mask([v]+[u for u in near if u!=w]))
        return ans
    ans=set()
    for e in (0,n-1):
        near=[u for u in range(n) if 0<abs(u-e)<=k]
        for w in near:
            ans.add(mask([e]+[u for u in near if u!=w]))
    return ans


def formula(n,k,cyclic):
    if not cyclic: return 2*k
    if n==2*k+1: return n
    if n==2*k+2: return n*k
    return n*(2*k-1)


def check(n,k,cyclic,exhaustive):
    adj=adjacencies(n,k,cyclic)
    expected=candidate_seeds(n,k,cyclic)
    assert len(expected)==formula(n,k,cyclic), (n,k,cyclic,'formula',len(expected))
    assert all(forces_all(adj,s) for s in expected), (n,k,cyclic,'candidate failure')
    if exhaustive:
        level=2*k if cyclic else k
        actual={mask(s) for s in combinations(range(n),level) if forces_all(adj,mask(s))}
        assert actual==expected,(n,k,cyclic,'classification',len(actual),len(expected))
        return comb(n,level)
    return 0


def run():
    examined=0; cases=0; largecases=0
    for k in range(1,6):
        for n in range(k+2,min(k+10,17)):
            examined+=check(n,k,False,True);cases+=1
    for k in range(1,6):
        for n in range(2*k+1,min(2*k+10,18)):
            examined+=check(n,k,True,True);cases+=1
    for k in range(1,13):
        for n in (2*k+1,2*k+2,2*k+3,2*k+5,3*k+11):
            check(n,k,True,False);largecases+=1
        for n in (k+2,k+3,2*k+7):
            check(n,k,False,False);largecases+=1
    print(f'VERIFY_OK exhaustive_cases={cases} examined_minimum_cardinality_subsets={examined} additional_constructive_cases={largecases}')

if __name__=='__main__':
    run()
