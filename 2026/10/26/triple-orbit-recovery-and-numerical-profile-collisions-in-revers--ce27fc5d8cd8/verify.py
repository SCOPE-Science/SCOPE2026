#!/usr/bin/env python3
"""Direct finite-type group-orbit checks for two dense linear orders."""
from itertools import permutations, product
from math import factorial
from collections import defaultdict

def apply(g, x):
    a,b,s = g
    p,q=x if not s else (x[1],x[0])
    return (p[::-1] if a else p, q[::-1] if b else q)

def mul(g,h):
    # Return composition g(h(x)), determined by signed coordinate composition.
    a,b,s=g; c,d,t=h
    if not s:
        return (a^c,b^d,t)
    return (a^d,b^c,1^t)

E=(0,0,0); R1=(1,0,0); R2=(0,1,0); S=(0,0,1)
D=tuple(product(range(2),repeat=3))
assert set(mul(g,h) for g in D for h in D)==set(D)

def subgroup(gens):
    ans={E}; frontier=[E]
    while frontier:
        a=frontier.pop()
        for b in gens:
            for c in (mul(a,b),mul(b,a)):
                if c not in ans: ans.add(c); frontier.append(c)
    return frozenset(ans)

subgroups={subgroup([g]) for g in D}
for g in D:
    for h in D: subgroups.add(subgroup([g,h]))
assert len(subgroups)==10

def orbits(H,n):
    ps=list(permutations(range(n)))
    X={(p,q) for p in ps for q in ps}
    groups=[]
    while X:
        x=min(X)
        o={apply(g,x) for g in H}
        assert o <= X
        X-=o
        groups.append(frozenset(o))
    return frozenset(groups)

lookup={}
for h in subgroups:
    s=sum(g in ((0,0,1),(1,1,1)) for g in h)
    lookup[h]=(len(h),s)
assert sorted(set(lookup.values()))==[(1,0),(2,0),(2,1),(4,0),(4,2),(8,2)]
for n in range(2,6):
    calculated={}
    for h in subgroups:
        o=orbits(h,n)
        count=len(o)
        z=(factorial(n)**2 + lookup[h][1]*factorial(n))//lookup[h][0]
        assert count==z,(n,h,z,count)
        calculated[h]=o
    equiv={}
    for h in subgroups:
        equiv.setdefault(calculated[h],[]).append(h)
    assert len(equiv)==(7 if n==2 else 10),(n,len(equiv))
    print('arity',n,'distinct_orbit_partitions',len(equiv),'distinct_orbit_counts',len(set(map(len,equiv))) if False else len({len(v) for v in calculated.values()}))

# n=3 has a truly free witness; n=2 does not
p=(0,1,2);q=(0,2,1); x=(p,q)
assert len({apply(g,x) for g in D})==8
assert all(len({apply(g,y) for g in D})<8 for y in product(permutations(range(2)), repeat=2))
print('subgroup_signature_multiplicities')
ct=defaultdict(int)
for v in lookup.values():ct[v]+=1
for pair in sorted(ct):print(pair,ct[pair])
print('ALL_CHECKS_PASS')
