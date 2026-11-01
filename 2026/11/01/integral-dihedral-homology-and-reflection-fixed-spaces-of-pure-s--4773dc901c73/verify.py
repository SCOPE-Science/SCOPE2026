#!/usr/bin/env python3
"""Standalone bounded checks for an integral dihedral cycle-complex theorem."""
from itertools import combinations

def facets(n):
    out=set()
    for deleted in range(n):
        path=[(deleted+1+i)%n for i in range(n-1)]
        for root in range(n-1):
            f=frozenset(2*v if i<root else 2*((v-1)%n)+1 for i,v in enumerate(path) if i!=root)
            out.add(f)
    assert len(out)==n*(n-1)
    return out

def reflection(n,v,j):
    i=v//2
    return (2*((j-i-1)%n)+1) if v%2==0 else 2*((j-i-1)%n)

def orbit_faces(n,j):
    orbits=[frozenset((2*i,reflection(n,2*i,j))) for i in range(n)]
    assert all(reflection(n,reflection(n,a,j),j)==a for a in range(2*n))
    possible={frozenset()}
    for f in facets(n):
        avail=[i for i,o in enumerate(orbits) if o<=f]
        for mask in range(1<<len(avail)):
            possible.add(frozenset(avail[k] for k in range(len(avail)) if mask>>k&1))
    return possible

def expected(n,j):
    m=n//2
    if n%2: return {frozenset(range(1,m)),frozenset(range(m+2,n))}
    if j%2==0: return {frozenset(range(1,m)),frozenset(range(m+1,n))}
    return {frozenset(range(2,m)),frozenset(range(m+2,n))}

def run():
    checks=0;orbits=0
    for n in range(7,19):
        for j in (range(2) if n%2==0 else range(1)):
            faces=orbit_faces(n,j)
            maxima={s for s in faces if not any(s<t for t in faces)}
            assert maxima==expected(n,j),(n,j,maxima)
            L=-sum((-1)**len(f) for f in faces)
            assert L==1,(n,j,L)
            checks+=1;orbits+=len(faces)
    print('VERIFY_OK', 'reflection_classes_checked=',checks,'orbit_faces=',orbits)

if __name__=='__main__':run()
