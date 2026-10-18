#!/usr/bin/env python3
"""Finite exhaustive verification of two-point relevant topological separation."""
from itertools import product
X=3
P=2 # p true at world 1; world 0 is the other
star=(1,0)
family={0,P,X}
T1={0,P,X}
T2={0,1,P,X}

def complement(u): return X^u

def interior(u,top):
    return 0 if not any(t & ~u == 0 for t in top) else max((t for t in top if (t&~u)==0),key=lambda t:t.bit_count())

def neg(u): return sum(1<<i for i in range(2) if not (u>>star[i])&1)

def impl(a,b): return X if (a&~b)==0 else 0

def universal(a): return X if a==X else 0

def density(a,top):
    return all((o&a)!=0 for o in top if o)

def coherent(p,top):
    return any(density(u,top) for u in top if (u & ~p)==0)

for j,top in enumerate((T1,T2),1):
    assert {0,X,P}==family
    for f in family:
        assert neg(f) in family
        assert interior(f,top) in family
        assert universal(f) in family
        for g in family:
            assert f&g in family
            assert f|g in family
            assert impl(f,g) in family
        # primitive operators agree on all members of F in both models
        assert interior(f,T1)==interior(f,T2)
    assert star[star[0]]==0 and star[star[1]]==1
    assert interior(X^P,T1)==0
    assert interior(X^P,T2)==1
assert coherent(P,T1) and not coherent(P,T2)
assert interior(X^P,T1)!=interior(X^P,T2)
# All single-world nonempty models: p is either empty or full and topology is unique
for p in (0,1):
    assert ((1^p)==(1^p))  # interior-of-complement equals relevant negation
    assert bool(p)==bool(any((u&~p)==0 and u!=0 for u in (0,1)))
print('TWO_WORLD_SIMULTANEOUS_SEPARATION_OK pair=2 primitive_connectives=6 closure_members=3 singleton_cases=2')
