#!/usr/bin/env python3
"""Independent interleaving-automaton verification of the run characterization."""
from itertools import product
from math import comb

def is_interleaving(w,u,v):
    states = {(0,0)}
    for c in w:
        nxt=set()
        for i,j in states:
            if i<len(u) and u[i]==c:
                nxt.add((i+1,j))
            if j<len(v) and v[j]==c:
                nxt.add((i,j+1))
        states=nxt
        if not states: return False
    return (len(u),len(v)) in states

tests=0; successes=0
for n in range(0,15):
    for k in range(n+1):
        r=n-k
        if r>9: continue
        w='ab'*n;u='ab'*k
        for choice in product((0,1),repeat=r):
            v=''.join(('ab','ba')[b] for b in choice)
            runs=sum(b==1 and (i==0 or choice[i-1]==0) for i,b in enumerate(choice))
            found=is_interleaving(w,u,v)
            assert found==(runs<=k),(n,k,choice,found,runs)
            tests+=1;successes+=found
print(f'PASS independent interleaving DP, n=0..14, r<=9: {tests} membership equivalences, {successes} positive memberships')
