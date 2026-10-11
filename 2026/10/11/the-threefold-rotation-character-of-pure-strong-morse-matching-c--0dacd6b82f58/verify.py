#!/usr/bin/env python3
"""Finite exact checks for the cyclic Lefschetz character of pure cycle matching complexes."""
from itertools import combinations
from math import gcd

def pure_facets(n):
    out=set()
    for gap in range(n):
        arc=[(gap+2+t)%n for t in range(n-2)]
        for split in range(n-1):
            out.add(frozenset(2*e+(t>=split) for t,e in enumerate(arc)))
    assert len(out)==n*(n-1)
    return out

def all_faces(facets):
    out={frozenset()}
    for facet in facets:
        xs=sorted(facet)
        for j in range(1,len(xs)+1):
            out.update(map(frozenset,combinations(xs,j)))
    return out

def signed_trace(faces,n,step):
    value=-1  # reduced empty simplex
    for f in faces:
        if not f: continue
        a=sorted(f)
        image=[2*((v//2+step)%n)+v%2 for v in a]
        if frozenset(image)!=f: continue
        permutation=[a.index(v) for v in image]
        inversions=sum(permutation[i]>permutation[j]
                       for i in range(len(a)) for j in range(i+1,len(a)))
        value+=(-1)**(len(a)-1+inversions)
    return value

def target(n,k):
    return 5 if gcd(n,k)%3==0 else -1

def main():
    comparisons=0
    for n in range(6,12):
        faces=all_faces(pure_facets(n))
        for k in range(n):
            value=signed_trace(faces,n,k)
            assert value==target(n,k),(n,k,value,target(n,k))
            comparisons+=1
        print('n',n,'face_count',len(faces),'rotations',n)
    assert comparisons==sum(range(6,12))
    print('VERIFY_OK',comparisons,'exact signed character comparisons')
if __name__=='__main__':main()
