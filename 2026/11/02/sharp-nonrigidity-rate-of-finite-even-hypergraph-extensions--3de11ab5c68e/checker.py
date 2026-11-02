#!/usr/bin/env python3
"""Finite consistency tests for symmetry constraints of even, group-labelled hypergraphs.

Only Python standard library; run with python3 checker.py.
"""
import itertools
import math
from collections import Counter

def rank(vectors):
    piv = {}
    for row in vectors:
        v = row
        while v:
            p = v.bit_length()-1
            if p in piv:
                v ^= piv[p]
            else:
                piv[p] = v
                break
    return len(piv)

def verify(n, k):
    vertices = tuple(range(n))
    faces = list(itertools.combinations(vertices,k+1))
    root_faces = list(itertools.combinations(range(1,n),k))
    index = {S:i for i,S in enumerate(root_faces)}
    masks = {}
    for face in faces:
        if 0 in face:
            mask = 1<<index[tuple(i for i in face if i!=0)]
        else:
            mask=0
            for sub in itertools.combinations(face,k):
                mask ^= 1<<index[sub]
        masks[face] = mask
    r = len(root_faces)
    totals = 0
    bycycle = {}
    total_words = 1<<r
    ntrans = 0
    for p in itertools.permutations(vertices):
        eq = [masks[F]^masks[tuple(sorted(p[x] for x in F))] for F in faces]
        defect=rank(eq)
        fixcount=1<<(r-defect)
        totals+=fixcount
        if sum(p[i]!=i for i in vertices)==2:
            assert defect == math.comb(n-3,k-1), (n,k,p,defect)
            ntrans+=1
        if p[0]==0:
            seen=set()
            orbits=0
            for S in root_faces:
                if S in seen: continue
                orbits+=1
                x=S
                while x not in seen:
                    seen.add(x)
                    x=tuple(sorted(p[j] for j in x))
            assert defect==r-orbits, (n,k,p,defect,r-orbits)
        # In each cycle type, ensure equality of the rank on conjugates.
        seen=set(); lens=[]
        for i in vertices:
            if i in seen: continue
            a=i; l=0
            while a not in seen:
                seen.add(a); l+=1; a=p[a]
            lens.append(l)
        ct=tuple(sorted(lens))
        if ct in bycycle:
            assert bycycle[ct]==defect, (n,k,ct,bycycle[ct],defect)
        else: bycycle[ct]=defect
    assert ntrans==math.comb(n,2)
    assert totals % math.factorial(n)==0
    print('OK', 'vertices',n, 'arity',k+1, 'root_dimension',r,
          'isomorphism_classes',totals//math.factorial(n),
          'cycle_types',len(bycycle),'transposition_defect',math.comb(n-3,k-1))
    return totals

for k in (2,3):
    for n in (k+2,k+3,k+4):
        if n>7: continue
        verify(n,k)
print('ALL_CHECKS_OK')
