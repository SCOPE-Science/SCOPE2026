#!/usr/bin/env python3
"""Exact combinatorial checks for the Petersen graph Hom-complex homology."""
from itertools import combinations, permutations
from collections import deque
P=list(combinations(range(5),2))
assert len(P)==10
adj={(a,b) for a in P for b in P if set(a).isdisjoint(b)}
assert len(adj)==30
for a in P:
    assert sum((a,b) in adj for b in P)==3
# Square-freeness: any distinct a,b have at most one common neighbor.
for a in P:
    for b in P:
        if a!=b:
            assert sum((a,c) in adj and (b,c) in adj for c in P)<=1
# Vertices are two colored copies of P, and directed edges from color 0 to 1.
W={(a,i) for a in P for i in (0,1)}
assert len(W)==20
E={((a,0),(b,1)) for a,b in adj}
assert len(E)==30
neighbors={v:set() for v in W}
for x,y in E:
    neighbors[x].add(y);neighbors[y].add(x)
seen=set();q=deque([next(iter(W))]);seen.add(q[0])
while q:
    for u in neighbors[q.popleft()]:
        if u not in seen:seen.add(u);q.append(u)
assert len(seen)==20
assert len(E)-len(W)+1==11
# Enumerate all cells as bicliques A x B: square-free implies one singleton.
allcells=set()
for a in P:
    nbrs=[b for b in P if (a,b) in adj]
    for k in range(1,len(nbrs)+1):
        for B in combinations(nbrs,k):allcells.add((frozenset((a,)),frozenset(B)))
for b in P:
    nbrs=[a for a in P if (a,b) in adj]
    for k in range(1,len(nbrs)+1):
        for A in combinations(nbrs,k):allcells.add((frozenset(A),frozenset((b,))))
assert len(allcells)==(20*(2**3-1)-30)
# Verify maximal cells are the twenty source/target triangles, with only singleton cross intersections.
U0={a:{(a,b) for b in P if (a,b) in adj} for a in P}
U1={b:{(a,b) for a in P if (a,b) in adj} for b in P}
for a in P:
    for b in P:
        assert len(U0[a]&U1[b])==(1 if (a,b) in adj else 0)
for a in P:
    for b in P:
        if a!=b:assert not (U0[a]&U0[b]) and not(U1[a]&U1[b])
# Character of integral cycle lattice: fixed oriented edges minus fixed vertices plus one.
expected={(1,1,1,1,1):11,(2,1,1,1):-1,(2,2,1):-1,(3,1,1):-1,(3,2):-1,(4,1):1,(5,):1}
def typ(p):
    seen=set();out=[]
    for x in range(5):
        if x not in seen:
            y=x;n=0
            while y not in seen:
                seen.add(y);n+=1;y=p[y]
            out.append(n)
    return tuple(sorted(out,reverse=True))
def act(a,p):return tuple(sorted(p[x] for x in a))
seen_types={}
for p in permutations(range(5)):
    fv=sum(act(a,p)==a for a in P)
    fe=sum(act(a,p)==a and act(b,p)==b for a,b in adj)
    chi=fe-2*fv+1
    t=typ(p)
    assert expected[t]==chi,(t,chi,expected[t])
    seen_types[t]=chi
assert seen_types==expected and len(seen_types)==7
print('PETERSEN_HOM_VERIFY_OK: 10 target vertices, 30 double-cover edges, 120 permutations, 7 character classes')
