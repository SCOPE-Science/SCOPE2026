#!/usr/bin/env python3
"""Independent transfer-matrix trace and composition coefficient comparison."""
from itertools import product,combinations
from collections import defaultdict
from math import comb


def coefficient_trace(n,k,L,f):
    states=[t for t in product(range(1,L+1),repeat=f) if sum(t)<L]
    states=set(states)
    edges={t:[] for t in states}
    for t in states:
        for b in range(1,L-sum(t)+1):
            v=t[1:]+(b,)
            if v in states:edges[t].append((v,t[0]))
    trace=0
    for start in states:
        dp={(start,0):1}
        for _ in range(k):
            nxt=defaultdict(int)
            for (state,weight),num in dp.items():
                for target,increment in edges[state]:
                    if weight+increment<=n:
                        nxt[(target,weight+increment)]+=num
            dp=nxt
        trace+=dp.get((start,n),0)
    return trace


def coefficient_compositions(n,k,L,f):
    num=0
    for cut in combinations(range(1,n),k-1):
        stops=(0,)+cut+(n,)
        g=[stops[i+1]-stops[i] for i in range(k)]
        if all(sum(g[(i+j)%k] for j in range(f+1))<=L for i in range(k)):
            num+=1
    return num


def main():
    tests=nonzero=0
    for n in range(3,10):
        for f in range(1,min(3,n-1)+1):
            for L in range(f+1,min(n,7)+1):
                for k in range(f+1,n+1):
                    x=coefficient_trace(n,k,L,f)
                    y=coefficient_compositions(n,k,L,f)
                    assert x==y,(n,k,L,f,x,y)
                    tests+=1
                    nonzero+=x>0
    print('PASS: independent finite transfer trace versus cyclic compositions')
    print('parameter profiles:',tests)
    print('nonzero trace profiles:',nonzero)

if __name__=='__main__':main()
