#!/usr/bin/env python3
"""Finite sanity checks for the membership-graph proof."""
from itertools import combinations

def powerset(s):
    xs=list(s)
    return {frozenset(xs[i] for i in range(len(xs)) if mask>>i & 1)
            for mask in range(1<<len(xs))}

V=[set()]
for _ in range(4):
    V.append(powerset(V[-1]))
# V_n is transitive at these stages.
U=V[4]

def rank(x, memo={}):
    if x in memo: return memo[x]
    r=0 if not x else 1+max(rank(y) for y in x)
    memo[x]=r
    return r

def adj(x,y):
    return x!=y and (x in y or y in x)

# Rank-compatible order: earlier neighbors of x are exactly x.
order=sorted(U, key=lambda x:(rank(x), repr(sorted(map(repr,x)))))
pos={x:i for i,x in enumerate(order)}
for x in U:
    earlier={y for y in U if pos[y]<pos[x] and adj(x,y)}
    assert earlier==set(x)

# Von Neumann ordinals 0,1,2,3 form a K4 inside V4.
ords=[frozenset()]
for _ in range(3):
    ords.append(frozenset(ords))
assert all(o in U for o in ords)
assert all(adj(ords[i],ords[j]) for i in range(4) for j in range(i))

# Exhaust the witness z=A union {B} for disjoint A,B subsets of V2.
base=list(V[2])
for maskA in range(1<<len(base)):
    A={base[i] for i in range(len(base)) if maskA>>i & 1}
    for maskB in range(1<<len(base)):
        B={base[i] for i in range(len(base)) if maskB>>i & 1}
        if A & B: continue
        Bset=frozenset(B)
        z=frozenset(A | {Bset})
        assert z in V[4]
        assert all(adj(z,a) for a in A)
        assert all(not adj(z,b) for b in B)
        assert z not in A|B
print('VERIFY_OK')
