#!/usr/bin/env python3
"""Independent enumeration of linear stabilizer orbits and first-round witnesses."""
from itertools import product
from collections import defaultdict

def binary_rank(vectors):
    span={0}
    for x in vectors: span |= {y^x for y in tuple(span)}
    return (len(span).bit_length()-1)

def matrices(d):
    n=1<<d
    for columns in product(range(n),repeat=d):
        if binary_rank(columns)!=d:continue
        def transform(x, cols=columns):
            ans=0
            for i in range(d):
                if x & (1<<i):ans ^= cols[i]
            return ans
        yield transform

def predicted(x,y,H):return (x if x in H else None,
                                y if y in H else None,
                                (x^y) if (x^y) in H else None)

def check_orbits(d,u,v):
    n=1<<d
    H={0,u,v,u^v}
    autom=[f for f in matrices(d) if f(u)==u and f(v)==v]
    unvisited=set(product(range(n),repeat=2))
    actual=set()
    while unvisited:
        p=next(iter(unvisited))
        orbit=frozenset((f(p[0]),f(p[1])) for f in autom)
        assert orbit<=unvisited
        actual.add(orbit)
        unvisited-=orbit
    groups=defaultdict(set)
    for x,y in product(range(n),repeat=2):
        groups[predicted(x,y,H)].add((x,y))
    expected={frozenset(z) for z in groups.values()}
    assert expected==actual, (d,u,v,len(expected),len(actual))
    # Individually marked cells have unique colors. A cell sharing two differently
    # directed marked equivalence lines has a unique first-round signature.
    A=(0,0);B=(u,v)
    seen=defaultdict(list)
    for x,y in product(range(n),repeat=2):
        def incidence(q):
            return tuple(int(lhs==rhs) for lhs,rhs in zip((x,y,x^y),
                        (q[0],q[1],q[0]^q[1])))
        signature=(1 if (x,y)==A else 2 if (x,y)==B else 0,
                   incidence(A),incidence(B))
        seen[signature].append((x,y))
    singles={vv[0] for vv in seen.values() if len(vv)==1}
    for h in H:
        for rel in range(3):
            assert any((s[0],s[1],s[0]^s[1])[rel]==h for s in singles), (d,u,v,h,rel)
    return len(autom),len(actual),len(singles)

total=0
for d in (1,2,3):
    BS=[(0,1),(1,0),(1,1)]
    if d>=2:BS += [(1,2),(1,3),(2,3)]
    for u,v in BS:
        autom,orbits,witnesses=check_orbits(d,u,v)
        print(f'd={d} marked=({u},{v}) stabilizer={autom} orbits={orbits} first_round_singletons={witnesses}')
        total+=1
print('PASS: explicit GL(d,2) stabilizer orbits and first-round witnesses,',total,'configurations')
