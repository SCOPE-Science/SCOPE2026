#!/usr/bin/env python3
"""Finite independent tests for geometric fixed matching faces under strip reversal.
Checks all labeled base graphs on 2, 3, and 4 vertices with an edge, and
reflection depths k=1,2,3, in both even and odd strip parity.
"""
from itertools import combinations
from collections import Counter


def edge(a,b):
    return tuple(sorted((a,b)))


def cartesian_edges(vertices,edges,layers):
    return set(edge((u,i),(v,i)) for i in range(layers) for u,v in edges) | set(
        edge((v,i),(v,i+1)) for i in range(layers-1) for v in vertices)


def is_matching(F):
    points=[]
    for a,b in F:points.extend((a,b))
    return len(points)==len(set(points))


def orbit_description(vertices,edges,layers):
    E=cartesian_edges(vertices,edges,layers)
    R=lambda e:edge((e[0][0],layers-1-e[0][1]),(e[1][0],layers-1-e[1][1]))
    remaining=set(E);orbits=[]
    while remaining:
        e=min(remaining)
        orb=frozenset((e,R(e)))
        assert orb<=remaining
        remaining-=orb
        if is_matching(orb):orbits.append(orb)
    return orbits


def lower_graph(vertices,edges,k,parity):
    F=cartesian_edges(vertices,edges,k)
    if parity=='even':
        F|={edge((v,k-1),(v,k)) for v in vertices}
    else:
        # Center copy is separate: represent it with index k.
        F|={edge((u,k),(v,k)) for u,v in edges}
    return F


def all_orbit_vertices(vertices,edges,k,parity):
    layers=2*k+(parity=='odd')
    orbits=orbit_description(vertices,edges,layers)
    F=lower_graph(vertices,edges,k,parity)
    tags=[]
    for orb in orbits:
        lower=[e for e in orb if all(p[1]<k for p in e)]
        if len(orb)==2:
            assert len(lower)==1
            tags.append(lower[0])
        else:
            assert len(orb)==1 and not lower
            tags.append(next(iter(orb)))
    assert set(tags)==F and len(tags)==len(F),(k,parity,edges,tags,F)
    return orbits,tags


def check_one(vertices,edges,k,parity):
    orbits,tags=all_orbit_vertices(vertices,edges,k,parity)
    for i,j in combinations(range(len(orbits)),2):
        x=is_matching(orbits[i]|orbits[j])
        y=is_matching((tags[i],tags[j]))
        assert x==y,(vertices,edges,k,parity,i,j)
    return len(orbits)


def face_vector(F):
    F=list(F);out=Counter()
    for k in range(len(F)+1):
        for sub in combinations(F,k):
            if is_matching(sub):out[k]+=1
    return out


def exhaust(vertices,edges,k,parity):
    orbits,tags=all_orbit_vertices(vertices,edges,k,parity)
    actual=Counter()
    for r in range(len(orbits)+1):
        for sub in combinations(orbits,r):
            if is_matching(frozenset().union(*sub)):
                actual[r]+=1
    predicted=face_vector(tags)
    assert actual==predicted,(vertices,edges,k,parity,actual,predicted)
    return sum(actual.values()),len(actual)


def main():
    tests=0;vertices_checked=0
    for n in (2,3,4):
        vs=tuple(range(n));possible=list(combinations(vs,2))
        for mask in range(1,1<<len(possible)):
            edges=tuple(e for i,e in enumerate(possible) if mask>>i&1)
            for k in (1,2,3):
                for parity in ('even','odd'):
                    vertices_checked+=check_one(vs,edges,k,parity)
                    tests+=1
    print('PASS folded-orbit flag-complex isomorphisms:',tests)
    print('PASS total nonconflicting orbit vertices:',vertices_checked)
    complete=0
    for vs,ee,kset in (
        ((0,1),((0,1),),(1,2,3)),
        ((0,1,2),((0,1),(1,2)),(1,2)),
        ((0,1,2),((0,1),(1,2),(0,2)),(1,2)),
        ((0,1,2,3),((0,1),(1,2),(2,3)),(1,)),
    ):
        for k in kset:
            for parity in ('even','odd'):
                count,dims=exhaust(vs,ee,k,parity)
                print('PASS total orbit faces:',len(vs),len(ee),k,parity,count,dims)
                complete+=1
    print('PASS exhaustive face vectors:',complete)
    print('VERIFY_OK')
if __name__=='__main__':main()
