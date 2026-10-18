#!/usr/bin/env python3
"""Reproduce finite combinatorial certificates for the Paley-13 torus."""
from collections import Counter
from itertools import combinations

N = 13
STEPS = (1, 3, 4, 9, 10, 12)
LIFTS = {1:(1,0), 12:(-1,0), 3:(0,1), 10:(0,-1),
         4:(1,1), 9:(-1,-1)}
A, B = (4,3), (3,-1)

def edge(u,v):
    return (v-u) % N in STEPS

def key_cycle(c):
    return frozenset(frozenset((c[i], c[(i+1)%4])) for i in range(4))

def walk_cycle(edges):
    nbr = {v:[] for pair in edges for v in pair}
    for u,v in (tuple(pair) for pair in edges):
        nbr[u].append(v)
        nbr[v].append(u)
    v0 = min(nbr)
    c = [v0, min(nbr[v0])]
    while len(c) < 4:
        v = next(x for x in nbr[c[-1]] if x != c[-2])
        assert v not in c
        c.append(v)
    return c

def displacement(c):
    increments = [(c[(i+1)%4]-c[i])%N for i in range(4)]
    assert all(d in LIFTS for d in increments)
    x = sum(LIFTS[d][0] for d in increments)
    y = sum(LIFTS[d][1] for d in increments)
    assert (x+3*y)%13 == 0
    return min((x,y),(-x,-y))

def main():
    vertices = range(N)
    edges = [frozenset((u,v)) for u,v in combinations(vertices,2) if edge(u,v)]
    triangles = [t for t in combinations(vertices,3) if all(edge(u,v) for u,v in combinations(t,2))]
    four_cliques = [t for t in combinations(vertices,4) if all(edge(u,v) for u,v in combinations(t,2))]
    assert (len(edges),len(triangles),len(four_cliques)) == (39,26,0)
    for v in vertices:
        ns = [u for u in vertices if edge(v,u)]
        assert len(ns) == 6
        assert all(sum(edge(u,w) for w in ns if u!=w) == 2 for u in ns)
        assert sum(edge(u,w) for u,w in combinations(ns,2)) == 6
    vectors = [(x,y) for x in range(-4,5) for y in range(-4,5)
               if (x or y) and (x+3*y)%13 == 0
               and max(abs(x),abs(y),abs(x-y)) <= 4]
    assert set(vectors) == {A,(-A[0],-A[1]),B,(-B[0],-B[1]),
                            (1,4),(-1,-4)}
    cycles = set()
    for a,b,c,d in combinations(vertices,4):
        for tour in ((a,b,c,d),(a,b,d,c),(a,c,b,d)):
            if all(edge(tour[i],tour[(i+1)%4]) for i in range(4)):
                cycles.add(key_cycle(tour))
    classes = {c:displacement(walk_cycle(c)) for c in cycles}
    histogram = Counter(classes.values())
    assert histogram == Counter({(0,0):39,(-4,-3):13,(-3,1):13,(-1,-4):13})
    rhombi = set()
    for e in edges:
        u,v=tuple(e)
        common=[w for w in vertices if w not in e and edge(u,w) and edge(v,w)]
        assert len(common)==2 and not edge(common[0], common[1])
        rhombi.add(key_cycle((u,common[0],v,common[1])))
    assert rhombi == {c for c in cycles if classes[c]==(0,0)}
    assert A[0]*B[1]-A[1]*B[0]==-13
    mul3 = lambda x,y: (-y,x-y)
    assert mul3(*A)==(-B[0],-B[1])
    assert mul3(*B)==(A[0]-B[0],A[1]-B[1])
    S = {1,3,4,9,10,12}
    assert len({(m,t) for m in S for t in vertices})==78
    for m in S:
        for t in vertices:
            phi=lambda x: (m*x+t)%N
            assert all(edge(phi(u),phi(v)) for e in edges for u,v in [tuple(e)])
            assert all(tuple(sorted(phi(v) for v in tr)) in triangles for tr in triangles)
    systoles = {c for c in cycles if classes[c]!=(0,0)}
    assert all(not edge(u,v) for c in systoles for u,v in combinations({z for e in c for z in e},2) if frozenset((u,v)) not in c)
    sample = next(iter(systoles))
    orbit = set()
    for m in S:
        for t in vertices:
            phi=lambda x: (m*x+t)%N
            orbit.add(frozenset(frozenset(phi(x) for x in e) for e in sample))
    assert orbit==systoles
    print('VERIFY_OK 13_VERTICES 39_EDGES 26_TRIANGLES 78_FOUR_CYCLES')
    print('SYSTOLES 39 THREE_DIRECTIONS_EACH_13 AFFINE_TRANSITIVE')
    print('LATTICE_SHORTEST_LENGTH 4 BASIS_DETERMINANT -13')

if __name__=='__main__':
    main()
