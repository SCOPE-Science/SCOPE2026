#!/usr/bin/env python3
"""Finite exact-arithmetic diagnostics for the illumination of pair-sum polytopes.
The all-dimensional theorem uses an analytic argument; grid tests alone cannot prove it.
"""
from itertools import product, combinations
from fractions import Fraction

def vertices(d):
    axes=[tuple(2*s if i==j else 0 for i in range(d)) for j in range(d) for s in (-1,1)]
    corners=list(product((-1,1),repeat=d))
    return axes+corners

def normals(d):
    ns=[]
    for i,j in combinations(range(d),2):
        for a,b in product((-1,1),repeat=2):
            ns.append(tuple(a if t==i else b if t==j else 0 for t in range(d)))
    return ns

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def norm2(l):return sum(sorted(map(abs,l),reverse=True)[:2])
def active(nlist,v):return [n for n in nlist if dot(n,v)==2]
def lit(l,acts):return all(dot(n,l)>2 for n in acts)

nchecked=0
for d,lim in [(3,6),(4,3),(5,2),(6,1)]:
    vv=vertices(d); nn=normals(d); aa=[active(nn,v) for v in vv]
    assert len(vv)==2*d+2**d
    for v,act in zip(vv,aa):
        assert max(dot(n,v) for n in nn)==2
        expected=2*(d-1) if 2 in map(abs,v) else d*(d-1)//2
        assert len(act)==expected, (d,v,len(act),expected)
        lv=tuple(Fraction(38,37)*x for x in v)
        assert lit(lv,act)
        assert norm2(lv)==Fraction(76,37)
    for l in product(range(-lim,lim+1),repeat=d):
        k=sum(lit(l,act) for act in aa)
        if k:
            assert k<=3, (d,l,k)
            assert Fraction(norm2(l),2)>k,(d,l,k,norm2(l))
        nchecked+=1
print('VERIFY_OK',nchecked,'exact lattice test sources; analytic proof handles all sources and dimensions')
