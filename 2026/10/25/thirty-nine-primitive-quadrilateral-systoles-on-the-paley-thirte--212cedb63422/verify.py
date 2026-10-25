#!/usr/bin/env python3
"""Exact finite checks for the 13-vertex Paley torus's integral 1-systoles.
Uses only Python's standard library. The uniform-cover argument is in RESULT.md.
"""
from itertools import combinations
from collections import Counter
from math import comb, gcd

N=13
Q={1,3,4,9,10,12}
STEP={1:(1,0),12:(-1,0),3:(0,1),10:(0,-1),4:(1,1),9:(-1,-1)}
ADJ={x:{(x+d)%N for d in Q} for x in range(N)}
EDGES={frozenset((x,y)) for x in range(N) for y in ADJ[x]}
FACES={frozenset((i,i+1,i+4)) for i in range(N)}|{frozenset((i,i+3,i+4)) for i in range(N)}
FACES={frozenset(x%N for x in t) for t in FACES}
TRIS={frozenset(t) for t in combinations(range(N),3) if all(frozenset(e) in EDGES for e in combinations(t,2))}
assert len(EDGES)==39 and len(FACES)==len(TRIS)==26 and FACES==TRIS
assert all(not all(frozenset(e) in EDGES for e in combinations(t,2)) for t in combinations(range(N),4))
assert all(len(ADJ[x]&ADJ[y])==(2 if y in ADJ[x] else 3) for x in range(N) for y in range(x+1,N))
assert sum(comb(len(ADJ[x]&ADJ[y]),2) for x in range(N) for y in range(x+1,N))//2==78
for x in range(N):
    L=ADJ[x]
    assert len(L)==6 and all(len(ADJ[v]&L)==2 for v in L)
    seen={next(iter(L))};frontier=list(seen)
    while frontier:
        z=frontier.pop()
        for w in ADJ[z]&L:
            if w not in seen:seen.add(w);frontier.append(w)
    assert seen==L

def canonical(path):
    t=tuple(path); m=len(t)
    return min(tuple(seq[j:]+seq[:j]) for seq in (t,t[::-1]) for j in range(m))

def homology_coordinates(c):
    a=b=0
    for x,y in zip(c,c[1:]+c[:1]):
        da,db=STEP[(y-x)%N]; a+=da;b+=db
    assert (a+3*b)%N==0
    return ((a+3*b)//N,b)

def simple_cycles(k):
    cycles=set()
    for start in range(N):
        def visit(path):
            if len(path)==k:
                if start in ADJ[path[-1]]:cycles.add(canonical(path))
                return
            for v in ADJ[path[-1]]:
                if v not in path:visit(path+[v])
        visit([start])
    return cycles

C3=simple_cycles(3); C4=simple_cycles(4)
assert len(C3)==26 and all(frozenset(c) in FACES and homology_coordinates(c)==(0,0) for c in C3)
assert len(C4)==78
induced={c for c in C4 if c[2] not in ADJ[c[0]] and c[3] not in ADJ[c[1]]}
chorded=C4-induced
assert len(induced)==len(chorded)==39
assert all(homology_coordinates(c)!=(0,0) for c in induced)
assert all(homology_coordinates(c)==(0,0) for c in chorded)

A=(0,1,2,3)
B=(0,1,5,9)
C=(0,3,6,9)
assert homology_coordinates(A)==(0,-1)
assert homology_coordinates(B)==(1,3)
assert homology_coordinates(C)==(1,4)
assert homology_coordinates(B)==tuple(x+y for x,y in zip(homology_coordinates(A),homology_coordinates(C)))
a,c=homology_coordinates(A),homology_coordinates(C)
assert abs(a[0]*c[1]-a[1]*c[0])==1
assert all(canonical(t) in induced for t in (A,B,C))
translation_orbits=[]
for rep in (A,B,C):
    orbit={canonical(tuple((v+t)%N for v in rep)) for t in range(N)}
    assert len(orbit)==13
    translation_orbits.append(orbit)
assert not (translation_orbits[0]&translation_orbits[1] or translation_orbits[0]&translation_orbits[2] or translation_orbits[1]&translation_orbits[2])
assert set.union(*translation_orbits)==induced
assert len({canonical(tuple((b*v+t)%N for v in A)) for b in Q for t in range(N)})==39
assert {canonical(tuple((b*v+t)%N for v in A)) for b in Q for t in range(N)}==induced
assert canonical(tuple(3*v%N for v in A)) in translation_orbits[2]
assert canonical(tuple(3*v%N for v in C)) in translation_orbits[1]
assert canonical(tuple(3*v%N for v in B)) in translation_orbits[0]

# Check a complete six-orbit representative list for ALL four-cycles.
ALL_REPS=(A,(0,1,4,3),(0,1,5,4),B,C,(0,3,7,4))
all_orbits=[{canonical(tuple((v+t)%N for v in rep)) for t in range(N)} for rep in ALL_REPS]
assert all(len(orbit)==13 for orbit in all_orbits)
assert sum(len(orbit) for orbit in all_orbits)==len(set.union(*all_orbits))==78
assert set.union(*all_orbits)==C4
assert Counter(homology_coordinates(rep)==(0,0) for rep in ALL_REPS)=={True:3,False:3}
print('FACE_VECTOR vertices=13 edges=39 triangles=26; links=C6; higher_faces=0')
print('SIMPLE_CYCLES length3=26 facial=26 length4=78 chorded_null=39 induced_essential=39')
print('THREE_TRANSLATION_ORBITS counts=(13,13,13) homology_coordinates=(0,-1),(1,3),(1,4)')
print('AFFINE_ORBIT size=39 group_order=78 multiplier_3_cycles_directions=yes')
print('INTEGRAL_H1_BASIS determinant=1; one_systole=4; all_39_systoles_primitive=yes')
print('VERIFY_OK_PALEY13_THREE_DIRECTION_FLAG_TORUS_SYSTOLES')
