#!/usr/bin/env python3
"""Independent exact three-round extension-type checker for homogeneous rooted-tree ancestor orders.
The infinite statement follows from the inequalities in pair_type, not from finite runs.
"""
from functools import lru_cache

def pair_type(b,h,d,e,l):
    # Ordered selected nodes x,y of depths d,e and common-prefix length l.
    # For comparable nodes, l=min(d,e); for incomparable, l<min(d,e).
    if d==e==l:
        s={(0,0,0)}
        if d>0: s.add((0,2,2))
        if h>d: s.add((0,1,1))
        if d>0 and b>=2: s.add((0,3,3))
        return (0,frozenset(s))
    if l==min(d,e):
        if d<e:
            a=d;gap=e-d;t=h-e
            s={(1,0,2),(1,1,0),(1,1,3)}
            if a>0:s.update({(1,2,2),(1,3,3)})
            if gap>=2:s.add((1,1,2))
            if t>0:s.add((1,1,1))
            return (1,frozenset(s))
        a=e;gap=d-e;t=h-d
        s={(1,0,2),(1,1,0),(1,1,3)}
        if a>0:s.update({(1,2,2),(1,3,3)})
        if gap>=2:s.add((1,1,2))
        if t>0:s.add((1,1,1))
        return (2,frozenset((2,z,y) for _,y,z in s))
    u=d-l;v=e-l
    s={(3,0,3),(3,3,0),(3,2,2)}
    if h>d:s.add((3,1,3))
    if h>e:s.add((3,3,1))
    if u>=2:s.add((3,2,3))
    if v>=2:s.add((3,3,2))
    if b>=3 or l>=1 or u>=2 or v>=2:s.add((3,3,3))
    return (3,frozenset(s))

@lru_cache(None)
def pointed(b,h,d):
    return frozenset(pair_type(b,h,d,e,l) for e in range(h+1) for l in range(min(d,e)+1))

def root(b,h):return frozenset(pointed(b,h,d) for d in range(h+1))

def run():
    # Verify geometry-derived full triple diagrams against independent inequality classification.
    from tree3_explore import canonical_pair,z_orbits,diag
    cases=0
    for b in (2,3,4):
      for h in range(0,12):
       for d in range(h+1):
        for e in range(h+1):
         for l in range(min(d,e)+1):
          x,y=canonical_pair(d,e,l)
          geometric=(diag((x,y))[0],frozenset(diag((x,y,z)) for z in z_orbits(x,y,b,h)))
          algebraic=pair_type(b,h,d,e,l)
          assert geometric==algebraic,(b,h,d,e,l,geometric,algebraic)
          cases+=1
    print('PAIR_CHECKS',cases,'PASS')
    # Prove finite point-type table provides correct parameter classification:
    # for all tested heights, every point type has a unique capped depth pair,
    # and vice versa across heights.
    mapping={}; reverse={}
    for b in (2,3,4,5):
     for h in range(45):
      for d in range(h+1):
       key=(min(b,3),min(d,3),min(h-d,3))
       typ=pointed(b,h,d)
       assert key not in mapping or mapping[key]==typ,(key,h,d)
       mapping[key]=typ;reverse[typ]=key
    print('CAPPED_POINT_TYPE_KEYS',len(mapping),'PASS')
    labels={}; classes={}
    for b in (2,3,4,5):
      for h in range(45):
       typ=root(b,h)
       key=(0,) if h==0 else (min(b,3),min(h,6))
       assert key not in labels or labels[key]==typ,(b,h)
       assert typ not in classes or classes[typ]==key,(b,h)
       labels[key]=typ;classes[typ]=key
    print('ROOT_CLASSES',len(labels),'PASS')
    print('SMALLEST_HEIGHTS binary',list(range(0,7)))
    print('SMALLEST_HEIGHTS branching>=3',list(range(1,7)))
    print('SYMBOLIC_PAIR_CASES 0 equal, 1 ancestor, 2 descendant, 3 incomparable')
    print('FINITE_STRESS_MAX_HEIGHT',44)
if __name__=='__main__':run()
