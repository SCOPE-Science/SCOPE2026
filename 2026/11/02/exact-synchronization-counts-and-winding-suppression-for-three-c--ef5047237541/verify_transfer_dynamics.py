#!/usr/bin/env python3
"""Independent finite checks of the circular-ladder three-color cyclic automaton."""
from itertools import product
from collections import defaultdict
from math import comb


def transfer_counts(n):
    # Laurent polynomials represented by exponent -> exact integer.
    steps={}
    for i in (-1,0,1):
        for j in (-1,0,1):
            steps[i,j]=[a for a in (-1,0,1) if abs(a+j-i)<=1]
    # Each initial vertical difference d contributes a closed chain.
    ans=0
    for start in (-1,0,1):
        states={(start,0):1}
        for _ in range(n):
            newer=defaultdict(int)
            for (i,s),count in states.items():
                for j in (-1,0,1):
                    for a in steps[i,j]:
                        newer[(j,s+a)]+=count
            states=newer
        ans+=states.get((start,0),0)
    return ans*3

def direct_dynamics(n):
    vertices=2*n
    neigh=[]
    for p in range(2):
        for i in range(n):
            neigh.append((p*n+(i-1)%n,p*n+(i+1)%n,(1-p)*n+i))
    def update(t):
        return tuple((v+1)%3 if (v+1)%3 in (t[u] for u in neigh[i]) else v for i,v in enumerate(t))
    diam=n//2+1
    count=0
    for state in product(range(3),repeat=vertices):
        t=state
        for _ in range(diam): t=update(t)
        if len(set(t))==1: count+=1
    return count

if __name__=='__main__':
    for n in range(3,7):
        t=transfer_counts(n)
        d=direct_dynamics(n)
        print(n,t,d,3**(2*n),t==d,flush=True)
        assert t==d
    print('PASS')
