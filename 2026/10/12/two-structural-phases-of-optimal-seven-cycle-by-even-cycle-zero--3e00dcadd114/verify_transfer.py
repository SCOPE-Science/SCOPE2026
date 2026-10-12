#!/usr/bin/env python3
"""Check local transition multiplicities and two structural type counts.
Uses independent combinatorial subsets, distinct from cyclic all-state DP.
"""
from itertools import combinations

def is_independent(s):
    return all((a-b)%7 not in (1,6) for a,b in combinations(s,2))

def compatible(s,t):
    return len(set(s)|set(t))==len(s)+len(t) and is_independent(set(s)|set(t))

singles=[frozenset((i,)) for i in range(7)]
pairs=[frozenset(p) for p in combinations(range(7),2) if is_independent(p)]
triples=[frozenset(t) for t in combinations(range(7),3) if is_independent(t)]
assert len(triples)==7 and len(pairs)==14
M=[[sum(compatible(a,p) and compatible(b,p) for p in pairs) for b in singles] for a in singles]
assert all(M[i][j] == (3 if i==j else 1 if (j-i)%7 in (1,6) else 0) for i in range(7) for j in range(7))
print('compatible singleton-pair-singleton multiplicities = 3 I7 + A(C7)')

def count_traces(k):
    s=0
    def visit(init,cur,depth,mult):
        nonlocal s
        if depth==k:
            s+=mult*M[cur][init]
            return
        for t in range(7):
            a=M[cur][t]
            if a:visit(init,t,depth+1,mult*a)
    for a in range(7):visit(a,a,1,1)
    return s

# Counts independently via weighted cyclic walks, not all-column DP.
for k in range(3,9):
    t0=2*len(triples)**k
    t1=2*count_traces(k)
    print(f'C7 strong C{2*k}: type (0,3) {t0}, type (1,2) {t1}, total {t0+t1}')
