#!/usr/bin/env python3
"""Direct state-space verification of open-neighborhood NOR on KG(n,2)."""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb

def formulas(n):
    g=2**(n-1)-n-comb(n-1,2)
    h=g+1+comb(n-3,2)
    e=1+2*(2**(n-2)-n+1)**2-comb(n-2,2)
    total=2**comb(n,2)
    b=total-(n*g+comb(n,3)+comb(n,2)*e+3*comb(n,3)*h+18*comb(n,4))
    return {1:comb(n,3),2:9*comb(n,4),g:n,h:3*comb(n,3),e:comb(n,2),b:1}, b

def check(n):
    edges=list(combinations(range(n),2)); m=len(edges)
    conflicting=[sum(1<<j for j,(c,d) in enumerate(edges) if a!=c and a!=d and b!=c and b!=d) for a,b in edges]
    def update(s):
        return sum(1<<i for i,neigh in enumerate(conflicting) if not (s & neigh))
    basins=defaultdict(int)
    for s in range(1<<m):
        a=update(s); b=update(a)
        assert update(b)==a, ('third iterate',n,s)
        basins[tuple(sorted((a,b)))]+=1
    got=Counter(basins.values())
    expect,b0=formulas(n)
    assert got==expect, ('basins',n,got,expect)
    nfixed=sum(1 for a,b in basins if a==b)
    ntwo=sum(1 for a,b in basins if a!=b)
    assert nfixed==n+comb(n,3)
    assert ntwo==1+comb(n,2)+3*comb(n,3)+9*comb(n,4)
    assert basins[(0,(1<<m)-1)]==b0
    print(f'n={n} states={1<<m} attractors={len(basins)} fixed={nfixed} two_cycles={ntwo} dominant={b0} histogram={dict(sorted(got.items()))}')

if __name__=='__main__':
    for n in (5,6): check(n)
    print('PYTHON_VERIFY_OK')
