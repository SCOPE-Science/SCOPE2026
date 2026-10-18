"""Independent binary-vector construction of the Fano-plane guard-shift graph."""
from itertools import combinations, permutations
from collections import Counter
import json

points=range(1,8)
subspaces=sorted({frozenset({a,b,a^b}) for a,b in combinations(points,2)},key=lambda s:tuple(sorted(s)))
assert len(subspaces)==7 and all(len(s)==3 for s in subspaces)
N=14
A=[0]*N
for k,S in enumerate(subspaces):
    for p in S:
        u=p-1;v=7+k
        A[u]|=1<<v;A[v]|=1<<u
assert all(mask.bit_count()==3 for mask in A)
closed=[A[v]|(1<<v) for v in range(N)]
full=(1<<N)-1
by_size={}
for k in (3,4):
    vals=[]
    for vs in combinations(range(N),k):
        seen=0
        for v in vs: seen|=closed[v]
        if seen==full: vals.append(vs)
    by_size[k]=vals
assert not by_size[3] and len(by_size[4])==21
F={}
for k,S in enumerate(subspaces):
    for p in S:
        state=tuple(sorted([q-1 for q in S if q!=p]+[7+t for t,T in enumerate(subspaces) if p in T and t!=k]))
        assert state in by_size[4]
        F[state]=(p,k)
assert len(F)==21

# Simple backtracking with bitset tracking, independent of permutation generation.
def can_shift(X,Y):
    options=[[j for j,y in enumerate(Y) if y==x or ((A[x]>>y)&1)] for x in X]
    def rec(i,used):
        if i==len(X):return True
        return any(rec(i+1,used|(1<<j)) for j in options[i] if not ((used>>j)&1))
    return rec(0,0)

states=by_size[4]; E=[]; C=Counter()
for X,Y in combinations(states,2):
    f,g=F[X],F[Y]
    yes=can_shift(X,Y)
    assert yes == (f[0]!=g[0] and f[1]!=g[1])
    C['movable' if yes else 'blocked']+=1
    if yes:E.append((X,Y))
assert C==Counter(movable=168,blocked=42)
for X in states:
    for v in range(N):
        if v not in X:
            assert any((X==a and v in b) or (X==b and v in a) for a,b in E)
# Explicit 4-regular graph whose vertices are Fano incidences, and line graph complement.
linegraph_edges=sum(1 for (X,Y) in combinations(states,2) if F[X][0]==F[Y][0] or F[X][1]==F[Y][1])
assert linegraph_edges==42
print(json.dumps({"verification":"VERIFY_OK","construction":"nonzero vectors of GF(2)^3","domination_number":4,"minimum_dominating_sets":21,"incidence_edges":21,"moving_pairs":C['movable'],"nonmoving_pairs":C['blocked'],"underlying_line_graph_edges":linegraph_edges,"every_minimum_configuration_winning":True},sort_keys=True))
