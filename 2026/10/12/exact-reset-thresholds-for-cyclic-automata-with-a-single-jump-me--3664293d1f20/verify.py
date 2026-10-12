#!/usr/bin/env python3
"""Independent finite checks of a cyclic permutation plus one state merge."""
from collections import deque
from math import gcd

def action_A(S,n):
    return frozenset((s+1)%n for s in S)

def action_B(S,h):
    return frozenset(h if s==0 else s for s in S)

def inverse_B(S,h):
    return (S-{0})|({0} if h in S else set())

def shortest_reset(n,h):
    start=frozenset(range(n));q=deque([(start,0)]);seen={start}
    while q:
        subset,d=q.popleft()
        if len(subset)==1:return d
        for T in (action_A(subset,n),action_B(subset,h)):
            if T not in seen:seen.add(T);q.append((T,d+1))
    return None

def check_interval(n,h):
    if gcd(n,h)!=1:return 0
    order=[(j*h)%n for j in range(n)];where={x:j for j,x in enumerate(order)}
    def interval(S):
        if not S:return False
        i={where[x] for x in S};k=len(i)
        return any(all(((j+t)%n in i) for t in range(k)) for j in range(n))
    c=0
    for left in range(n):
        for k in range(1,n+1):
            S={order[(left+t)%n] for t in range(k)}
            X=inverse_B(S,h)
            assert not X or interval(X),(n,h,S,X)
            c+=1
    return c

def main():
    cases=0; intervals=0
    for n in range(2,13):
        for h in range(1,n):
            got=shortest_reset(n,h)
            exp=(n-2)*(n-h+1)+1 if gcd(n,h)==1 else None
            assert got==exp,(n,h,got,exp)
            if exp is not None:
                S=frozenset(range(n));S=action_B(S,h)
                for _ in range(n-2):
                    for __ in range(n-h):S=action_A(S,n)
                    S=action_B(S,h)
                assert len(S)==1,(n,h,S)
            intervals+=check_interval(n,h)
            cases+=1
    for n in range(13,101):
        for h in range(1,n):
            if gcd(n,h)!=1:continue
            S=set(range(n)); S=action_B(S,h)
            for _ in range(n-2):
                S={(x+n-h)%n for x in S};S=action_B(S,h)
            assert len(S)==1,(n,h,S)
    print('VERIFY_OK exhaustive_BFS_n=2..12 cases=%d inverse_intervals=%d constructive_witness_n=2..100' %(cases,intervals))
if __name__=='__main__':main()
