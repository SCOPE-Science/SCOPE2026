#!/usr/bin/env python3
"""Finite corroboration of dihedral orientation degrees for cyclic Rips spheres.
Uses only the Python standard library. The uniform theorem relies on a mathematical proof.
"""
from itertools import combinations
from collections import Counter

def dist(n, x, y):
    r = (x-y) % n
    return min(r,n-r)

def fixed_lefschetz(n,k,action):
    visited=set(); orbits=[]
    for i in range(n):
        if i in visited: continue
        orb=[];j=i
        while j not in visited:
            visited.add(j);orb.append(j);j=action(j)
        if all(dist(n,a,b)<=k for a,b in combinations(orb,2)):
            orbits.append(orb)
    total=0
    for bit in range(1,1<<len(orbits)):
        face=[v for j,orb in enumerate(orbits) if bit>>j & 1 for v in orb]
        if not all(dist(n,a,b)<=k for a,b in combinations(face,2)): continue
        ordered=sorted(face)
        reord=[ordered.index(action(v)) for v in ordered]
        inversions=sum(reord[a]>reord[b] for a in range(len(reord)) for b in range(a+1,len(reord)))
        total+=(-1)**(len(face)-1+inversions)
    return total

def band(n,k):
    for l in range(n):
        if l*n < k*(2*l+1) and k*(2*l+3) < (l+1)*n:
            return l
    return None

checks=0;perband=Counter()
for n in range(4,29):
    for k in range(1,n//2):
        l=band(n,k)
        if l is None or l>3:continue
        # Known homotopy type is S^(2l+1). The Hopf trace identity yields
        # degree(g) = 1 - Lefschetz_number(g) in odd top dimension.
        for a in (0,1):
            lefs=fixed_lefschetz(n,k,lambda i,a=a:(a-i)%n)
            degree=1-lefs
            assert degree==(-1)**(l+1),(n,k,l,a,degree)
            checks+=1
        lr=fixed_lefschetz(n,k,lambda i:(i+1)%n)
        assert 1-lr==1,(n,k,l,lr)
        checks+=1;perband[l]+=1
        if n<=12:
            for mask in range(1,1<<n):
                face=[i for i in range(n) if mask>>i&1]
                if not all(dist(n,i,j)<=k for i,j in combinations(face,2)):
                    continue
                enlarged=set(face)|{(i+1)%n for i in face}
                assert all(dist(n,i,j)<=k+1 for i,j in combinations(enlarged,2))
for l in range(6):
    m=2*l+2; n=2*m;k=m-1
    assert band(n,k)==l
    # Reflection permutes m antipodal pairs by i -> (-i) mod m,
    # flipping the sign of all pairs except axis i=0.
    perm=[(-i)%m for i in range(m)]
    inversion=sum(perm[i]>perm[j] for i in range(m) for j in range(i+1,m))
    flips=m-1
    assert (-1)**(inversion+flips)==(-1)**(l+1)
    # Rotation sends i -> i+1 modulo m, with one pair-coordinate flip.
    rperm=[(i+1)%m for i in range(m)]
    inversion=sum(rperm[i]>rperm[j] for i in range(m) for j in range(i+1,m))
    assert (-1)**(inversion+1)==1
print('GENERIC_CYCLIC_RIPS_CASES_BY_BAND',dict(sorted(perband.items())))
print('EXACT_SIGNED_LEFSCHETZ_TESTS',checks)
print('CROSSPOLYTOPE_BASE_ORIENTATION_TESTS',6)
print('SMALL_SIMPLEX_CONTIGUITY_TESTS','passed')
print('UNIFORM_THEOREM_INPUT','Adamaszek-Adams cyclic-homomorphism theorem; not established by finite enumeration')
print('VERIFY_OK_DIHEDRAL_ORIENTATION_CYCLIC_RIPS')
