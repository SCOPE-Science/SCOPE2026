#!/usr/bin/env python3
from itertools import product, combinations
from math import prod

# Direct finite-product-of-prime-fields implementation of Badawi's annihilator graph.
def ring_elements(qs):
    return list(product(*[range(q) for q in qs]))

def mul(x,y,qs):
    return tuple((a*b)%q for a,b,q in zip(x,y,qs))

def zero(x):
    return all(a==0 for a in x)

def unit(x):
    # qs are prime in the direct arithmetic replay.
    return all(a!=0 for a in x)

def annihilator(x,elems,qs):
    return frozenset(z for z in elems if zero(mul(z,x,qs)))

def graph(qs):
    elems=ring_elements(qs)
    verts=[x for x in elems if not zero(x) and not unit(x)]
    anns={x:annihilator(x,elems,qs) for x in elems}
    adj={x:set() for x in verts}
    for i,x in enumerate(verts):
        for y in verts[i+1:]:
            if anns[mul(x,y,qs)] != (anns[x] | anns[y]):
                adj[x].add(y); adj[y].add(x)
    return verts,adj

def support(x):
    return frozenset(i for i,a in enumerate(x) if a!=0)

def dominates_pair(x,y,verts,adj):
    return y in adj[x] and all(v in (x,y) or v in adj[x] or v in adj[y] for v in verts)

def predicted_count(qs):
    r=len(qs)
    return (2**(r-1)-1)*prod(q-1 for q in qs)

profiles=[(2,2),(2,3),(3,3),(2,5),(3,5),(2,2,2),(2,2,3),(2,3,3),(2,3,5)]
for qs in profiles:
    verts,adj=graph(qs)
    actual=[]
    for x,y in combinations(verts,2):
        if dominates_pair(x,y,verts,adj):
            actual.append((x,y))
    assert len(actual)==predicted_count(qs),(qs,len(actual),predicted_count(qs))
    for x,y in actual:
        A=support(x); B=support(y)
        assert A.isdisjoint(B)
        assert A|B==frozenset(range(len(qs)))
    # Converse: every complementary-support pair is a dominating edge.
    for x,y in combinations(verts,2):
        A=support(x); B=support(y)
        complementary=A.isdisjoint(B) and A|B==frozenset(range(len(qs)))
        assert dominates_pair(x,y,verts,adj)==complementary

# Pure support-level exhaustive classification up to seven field factors.
for r in range(2,8):
    subs=[frozenset(i for i in range(r) if (mask>>i)&1) for mask in range(1,2**r-1)]
    good=0
    for ai,A in enumerate(subs):
        for B in subs[ai+1:]:
            adjacent=not (A<=B or B<=A)
            if not adjacent:
                continue
            dominating=True
            for C in subs:
                if C==A or C==B:
                    continue
                incA=(C<=A or A<=C)
                incB=(C<=B or B<=C)
                if incA and incB:
                    dominating=False; break
            if dominating:
                good+=1
                assert A.isdisjoint(B) and A|B==frozenset(range(r))
    assert good==2**(r-1)-1,(r,good)

print('VERIFY_OK')
print(f'direct_ring_profiles={len(profiles)}')
print('largest_direct_ring_order=30')
print('support_levels_r=2..7')
print('complementary_support_classification=passed')
print('minimum_pair_count_formula=passed')
