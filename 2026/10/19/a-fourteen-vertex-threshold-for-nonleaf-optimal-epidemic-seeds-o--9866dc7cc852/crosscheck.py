#!/usr/bin/env python3
"""Independent path-prefix sum for the stated 14-vertex witness."""
from fractions import Fraction
from verify import adjacency,WITNESS,score

def path_prefix(a,src):
    n=len(a); s=Fraction(1)
    def dfs(u,p,prob):
        nonlocal s
        for w in a[u]:
            if w==p:continue
            nextprob=prob/Fraction(len(a[u]))
            s+=nextprob
            dfs(w,u,nextprob)
    dfs(src,-1,Fraction(1));return s

if __name__=='__main__':
    a=adjacency(14,WITNESS)
    vals=score(14,WITNESS)
    assert tuple(path_prefix(a,i) for i in range(14))==vals
    print('direct root-to-descendant weighted-path summation matches directed-edge recursion at all 14 vertices')
