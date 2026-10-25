#!/usr/bin/env python3
"""Reproduce the exact dihedral character formulas for cycle higher-independence complexes.
Only the standard Python library is used. No prior output files are needed.
"""
from math import gcd
from itertools import product


def dimension(n, r):
    k, t = divmod(n, r + 2)
    assert k >= 1 and r >= 2
    return r*k-1 if t == 0 else r*k+t-2


def allowed(n, r, mask):
    # For n >= r+2, no r+1 circularly consecutive occupied vertices.
    for a in range(n):
        if all(mask & (1 << ((a+j) % n)) for j in range(r+1)):
            return False
    return True


def orbit_signed_fixed_face_sum(n, r, perm):
    # Direct orbit construction, independent of transfer-matrix and path formulas.
    seen = set()
    orbits = []
    for a in range(n):
        if a in seen:
            continue
        orbit = []
        b = a
        while b not in seen:
            seen.add(b)
            orbit.append(b)
            b = perm[b]
        assert b == a
        orbits.append(orbit)
    masks = [sum(1 << i for i in orbit) for orbit in orbits]
    z = 0
    for choices in product((0, 1), repeat=len(orbits)):
        mask = 0
        for use, orbit_mask in zip(choices, masks):
            if use:
                mask |= orbit_mask
        if allowed(n, r, mask):
            z += (-1) ** sum(choices)
    return z


def a_coeff(j, degree):
    return (-1)**degree if 0 <= degree <= j else 0


def formal_coefficient(length, r, left, right):
    # Coefficient in z(1+z) A_left(z) A_right(z)/(1-(-z)^(r+2)).
    result = 0
    for d in range(length // (r+2)+1):
        degree = length - 1 - d*(r+2)
        for i in range(left+1):
            for j in range(right+1):
                if degree-i-j in (0,1):
                    result += (-1)**(d*(r+2) + i+j)
    return result


def formula(n, r, kind, a):
    q=dimension(n,r)
    if kind == 'rotation':
        h=gcd(n,a)
        z=(-1)**h * ((r+2 if h % (r+2) == 0 else 0)-1)
    else:
        m=n//2
        u=(r+1)//2
        v=r//2
        if n % 2:
            L, left, right=m+1,u,v
        elif a % 2 == 0:
            L, left, right=m+1,u,u
        else:
            L, left, right=m,v,v
        z=formal_coefficient(L,r,left,right)
    return (-1)**(q+1)*z


def reduced_betti_mod101(n, r):
    # Independent chain check in degrees >=0, with a rank-one augmentation C_0->C_-1.
    faces_by_dim = {}
    for mask in range(1,1<<n):
        if allowed(n,r,mask):
            face=tuple(i for i in range(n) if mask&(1<<i))
            faces_by_dim.setdefault(len(face)-1,[]).append(face)
    levels=sorted(faces_by_dim)
    ranks={0:1} # augmentation of the nonempty vertex set
    for dim in levels[1:]:
        before={f:i for i,f in enumerate(faces_by_dim[dim-1])}
        pivots={}
        for face in faces_by_dim[dim]:
            col={before[face[:j]+face[j+1:]]: (1 if j%2==0 else 100)
                  for j in range(len(face))}
            while col:
                pivot=min(col)
                if pivot not in pivots:
                    inv=pow(col[pivot],-1,101)
                    pivots[pivot]={a:(b*inv)%101 for a,b in col.items()}
                    break
                coef=col[pivot]
                for a,b in pivots[pivot].items():
                    value=(col.get(a,0)-coef*b)%101
                    if value:col[a]=value
                    else:col.pop(a,None)
        ranks[dim]=len(pivots)
    return {dim:len(faces_by_dim[dim])-ranks.get(dim,0)-ranks.get(dim+1,0)
            for dim in levels}


def check():
    num=0
    examples=[]
    for r in range(2,7):
        for n in range(r+2, min(17, r+15)):
            for a in range(n):
                for kind in ('rotation','reflection'):
                    perm=[(i+a)%n if kind=='rotation' else (a-i)%n for i in range(n)]
                    z=orbit_signed_fixed_face_sum(n,r,perm)
                    actual=(-1)**(dimension(n,r)+1)*z
                    target=formula(n,r,kind,a)
                    assert actual==target,(r,n,kind,a,actual,target)
                    num+=1
            assert formula(n,r,'rotation',0)== (r+1 if n%(r+2)==0 else 1)
            if (r,n) in ((2,6),(2,8),(3,10)):
                examples.append((r,n,[formula(n,r,'rotation',a) for a in range(n)],
                    [formula(n,r,'reflection',a) for a in range(2)]))
    print('PASS',num,'exact signed fixed-face character comparisons')
    chain_cases=0
    for r in range(2,5):
        for n in range(r+2,11):
            q=dimension(n,r)
            ranks=reduced_betti_mod101(n,r)
            assert ranks.get(q)==(r+1 if n%(r+2)==0 else 1),(r,n,ranks,q)
            assert all(b==0 for deg,b in ranks.items() if deg!=q),(r,n,ranks,q)
            chain_cases+=1
    print('PASS',chain_cases,'independent modular simplicial boundary calculations')
    for r,n,rots,refs in examples:
        print('example',r,n,'rotations',rots,'reflection types',refs)

if __name__=='__main__':
    check()
