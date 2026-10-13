#!/usr/bin/env python3
from itertools import permutations, product, combinations
from collections import deque
from pathlib import Path
import json

N=4
Q=set(range(N))

def parity(p):
    inv=0
    for i in range(N):
        for j in range(i+1,N):
            inv += p[i]>p[j]
    return inv%2

A4=[tuple(p) for p in permutations(range(N)) if parity(p)==0]
assert len(A4)==12

def compose(g,f):
    return tuple(g[f[i]] for i in range(N))

def rank(t):
    return len(set(t))

def image(S,t):
    return frozenset(t[x] for x in S)

def monoid(gens):
    ident=tuple(range(N))
    seen={ident}
    q=deque([ident])
    while q:
        h=q.popleft()
        for g in gens:
            z=compose(g,h)
            if z not in seen:
                seen.add(z)
                q.append(z)
    return seen

pairs=[frozenset(c) for c in combinations(range(N),2)]

def all_2sets_distinguishable(G,f):
    M=monoid(list(G)+[f])
    for i,X in enumerate(pairs):
        for Y in pairs[i+1:]:
            if not any((len(image(X,h))==1) != (len(image(Y,h))==1) for h in M):
                return False,(X,Y,len(M))
    return True,len(M)

# A4 is 2-transitive: the stabilizer of 0 contains the 3-cycle on 1,2,3.
stab0=[g for g in A4 if g[0]==0]
assert {tuple(g[i] for i in (1,2,3)) for g in stab0} == {
    (1,2,3),(2,3,1),(3,1,2)
}

f=(0,0,1,1)
X=frozenset((0,1))
Y=frozenset((2,3))
M=monoid(A4+[f])
assert len(M)==52

# Direct indistinguishability check.
for h in M:
    assert len(image(X,h))==len(image(Y,h))
ok,detail=all_2sets_distinguishable(A4,f)
assert not ok
assert detail[0]==X and detail[1]==Y

# Independent symbolic invariant on ordered pairs of subsets.
def invariant_class(U,V):
    if len(U)==len(V)==1:
        return "singletons"
    if U==V and len(U)==2:
        return "same2"
    if len(U)==len(V)==2 and U.isdisjoint(V) and U|V==Q:
        return "complement2"
    return None

assert invariant_class(X,Y)=="complement2"
reachable={(X,Y)}
q=deque([(X,Y)])
for_current=list(A4)+[f]
while q:
    U,V=q.popleft()
    assert invariant_class(U,V) is not None
    for g in for_current:
        Z=(image(U,g),image(V,g))
        assert invariant_class(*Z) is not None
        if Z not in reachable:
            reachable.add(Z)
            q.append(Z)
assert len(reachable)==28

# Exhaustive support: all rank-2 and rank-3 transformations.
counts={2:[0,0],3:[0,0]}  # total, failures
for t in product(range(N),repeat=N):
    r=rank(t)
    if r not in counts:
        continue
    counts[r][0]+=1
    good,_=all_2sets_distinguishable(A4,tuple(t))
    if not good:
        counts[r][1]+=1
assert counts=={2:[84,36],3:[144,0]}

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["group_order"]==12
assert cert["witness_transformation"]==[0,0,1,1]
assert cert["exhaustive_support"]["rank2_maps_failing_strong_condition"]==36
assert cert["exhaustive_support"]["rank3_maps_failing_strong_condition"]==0

print("VERIFY_OK A4_order=12 primitive_via_2transitive=1 witness_rank2=0011 "
      "pair=01|23 monoid=52 reachable_pair_states=28 "
      "rank2_failures=36/84 rank3_failures=0/144 proper_subset_primitive=1")
