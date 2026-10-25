#!/usr/bin/env python3
"""Exact finite check for the elementary-collapse torus theorem.

Usage: python3 verify_triangular_cylinder_neighborhood.py
No third-party modules. It checks full simplices, each freeness condition,
final triangulation, edge orientations, and links for n=5,...,14.
The infinite statement has a separate combinatorial proof.
"""
from collections import defaultdict, Counter, deque
from itertools import combinations


def fac(vertices):
    v = tuple(vertices)
    return {frozenset(c) for k in range(1, len(v)+1)
            for c in combinations(v,k)}


def triangles(n):
    out = set()
    oriented = []
    for i in range(n):
        j = (i+1)%n
        for a in range(3):
            x, y = (a+1)%3, (a+2)%3
            A=((i,x),(i,y),(j,a))
            B=((i,a),(j,y),(j,x))
            oriented.extend([A,B])
            out.add(frozenset(A))
            out.add(frozenset(B))
    return out, oriented


def check(n):
    assert n >= 5
    facets = {}
    all_faces = set()
    for i in range(n):
        for a in range(3):
            T=frozenset(((i,(a+1)%3),(i,(a+2)%3),((i-1)%n,a),((i+1)%n,a)))
            assert len(T)==4 and T not in facets.values()
            facets[(i,a)] = T
            all_faces.update(fac(T))
    start=Counter({k:sum(len(f)==k for f in all_faces) for k in range(1,5)})
    assert tuple(start[k] for k in range(1,5))==(3*n,12*n,12*n,3*n), start
    count=0
    for i in range(n):
        for a in range(3):
            left=((i-1)%n,a);right=((i+1)%n,a)
            e=frozenset((left,right))
            T=facets[(i,a)]
            tri=frozenset((left,right,(i,(a+1)%3)))
            assert tri in all_faces and T in all_faces
            # Exactly one maximal coface of codimension one.
            assert sum(tri < f for f in all_faces if len(f)==4)==1
            assert not any(tri < f for f in all_faces if f != T)
            all_faces.remove(tri);all_faces.remove(T)
            count+=1
            rem=frozenset((left,right,(i,(a+2)%3)))
            assert rem in all_faces and e in all_faces
            assert sum(e < f for f in all_faces)==1
            all_faces.remove(e);all_faces.remove(rem)
            count+=1
    expected, oriented = triangles(n)
    assert all_faces==set().union(*(fac(t) for t in expected))
    assert tuple(sum(len(f)==k for f in all_faces) for k in (1,2,3,4))==(3*n,9*n,6*n,0)
    # Each edge lies in exactly two triangles; oriented fundamental cycle.
    incid=defaultdict(list)
    signed=defaultdict(int)
    for A in oriented:
        x,y,z=A
        for p,q in ((y,z),(z,x),(x,y)):
            edge=frozenset((p,q))
            incid[edge].append(A)
            signed[tuple(sorted((p,q)))] += 1 if p<q else -1
    assert all(len(c)==2 for c in incid.values())
    assert not any(signed.values()),signed
    # Every vertex link is a single cycle, hence surface (not only pseudomanifold).
    vertices={(i,a) for i in range(n) for a in range(3)}
    for v in vertices:
        lk=defaultdict(set)
        for t in expected:
            if v in t:
                a,b=t-{v};lk[a].add(b);lk[b].add(a)
        assert lk and all(len(x)==2 for x in lk.values())
        todo={next(iter(lk))}; seen=set()
        while todo:
            p=todo.pop()
            if p not in seen:seen.add(p);todo|=lk[p]-seen
        assert len(seen)==len(lk)
    assert len(vertices)-len(incid)+len(expected)==0
    # A row triangle and adjacent strips connect everything.
    graph=defaultdict(set)
    for e in incid:
        a,b=tuple(e)
        graph[a].add(b);graph[b].add(a)
    seen=set();queue={next(iter(vertices))}
    while queue:
        v=queue.pop()
        if v not in seen:seen.add(v);queue|=graph[v]-seen
    assert seen==vertices
    return count, len(all_faces)

if __name__ == '__main__':
    total=0
    for n in range(5,15):
        pairs,left=check(n)
        total+=pairs
        print(f'n={n} elementary_pairs={pairs} surviving_faces={left} torus_core=PASS')
    print(f'VERIFY_OK cases=10 total_elementary_pairs={total} integer_orientation=PASS vertex_links=PASS')
