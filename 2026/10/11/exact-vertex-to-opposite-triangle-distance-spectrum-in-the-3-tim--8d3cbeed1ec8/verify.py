#!/usr/bin/env python3
"""Exact finite distance-spectrum verification for marked lattice tetrahedra.

Requires only Python 3's standard library. No numerical tolerance is used.
Run alongside spectrum.csv: python3 verify.py
"""
import csv
import itertools as it
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

LATTICE = tuple(it.product(range(3), repeat=3))

def sub(a, b):
    return tuple(x-y for x, y in zip(a,b))

def dot(a, b):
    return sum(x*y for x,y in zip(a,b))

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

def edge_distance_sq(P,A,B):
    q=sub(P,A); v=sub(B,A)
    d=dot(v,v)
    t=max(Fraction(0),min(Fraction(1),Fraction(dot(q,v),d)))
    displacement=tuple(Fraction(q[i])-t*v[i] for i in range(3))
    return sum(x*x for x in displacement)

def distance_sq_barycentric(P, A, B, C):
    """Proof formula: plane projection if inside, closest boundary edge otherwise."""
    u=sub(B,A); v=sub(C,A); q=sub(P,A)
    normal=cross(u,v)
    gram=dot(normal,normal)
    det=dot(q,normal)
    if not det:
        return None  # no full-dimensional tetrahedron
    guu=dot(u,u); guv=dot(u,v); gvv=dot(v,v)
    qu=dot(q,u); qv=dot(q,v)
    a_num=gvv*qu-guv*qv
    b_num=guu*qv-guv*qu
    if 0<=a_num and 0<=b_num and a_num+b_num<=gram:
        return Fraction(det*det,gram)
    return min(edge_distance_sq(P,A,B),edge_distance_sq(P,A,C),edge_distance_sq(P,B,C))

def distance_sq_candidate_min(P,A,B,C):
    """Independent convex quadratic minimization over seven KKT supports."""
    u=sub(B,A); v=sub(C,A); w=sub(P,A)
    delta=dot(w,cross(u,v))
    if not delta:
        return None
    candidates=[]
    for X in (A,B,C):
        candidates.append(Fraction(dot(sub(P,X),sub(P,X))))
    for X,Y in ((A,B),(A,C),(B,C)):
        candidates.append(edge_distance_sq(P,X,Y))
    aa=dot(u,u);bb=dot(u,v);cc=dot(v,v)
    det=aa*cc-bb*bb
    s=Fraction(cc*dot(w,u)-bb*dot(w,v),det)
    t=Fraction(aa*dot(w,v)-bb*dot(w,u),det)
    if s>=0 and t>=0 and s+t<=1:
        residual=tuple(Fraction(w[i])-s*u[i]-t*v[i] for i in range(3))
        candidates.append(sum(x*x for x in residual))
    return min(candidates)

TRANSFORMS=tuple((perm,sign) for perm in it.permutations(range(3))
                             for sign in it.product((0,1),repeat=3))
def orbit_representative(P,A,B,C):
    def f(x,perm,sign):
        return tuple(2-x[perm[i]] if sign[i] else x[perm[i]] for i in range(3))
    return min((f(P,perm,sign), *sorted((f(x,perm,sign) for x in (A,B,C))))
               for perm,sign in TRANSFORMS)


def verify():
    distribution=Counter(); orbit_counts=defaultdict(Counter)
    total=0; face_projection=0
    for P in LATTICE:
        for A,B,C in it.combinations(LATTICE,3):
            if P in (A,B,C):
                continue
            r=distance_sq_barycentric(P,A,B,C)
            if r is None:
                continue
            total+=1
            r2=distance_sq_candidate_min(P,A,B,C)
            assert r==r2, (P,A,B,C,r,r2)
            distribution[r]+=1
            if r in (Fraction(1,29),Fraction(1,21),Fraction(1,17)):
                orbit_counts[r][orbit_representative(P,A,B,C)]+=1
            normal=cross(sub(B,A),sub(C,A))
            q=sub(P,A)
            a=dot(sub(B,A),sub(B,A));b=dot(sub(B,A),sub(C,A));c=dot(sub(C,A),sub(C,A))
            div=a*c-b*b
            am=c*dot(q,sub(B,A))-b*dot(q,sub(C,A))
            bm=a*dot(q,sub(C,A))-b*dot(q,sub(B,A))
            if am>=0 and bm>=0 and am+bm<=div:
                face_projection+=1
    assert total==58528, total
    assert total//4==14632
    assert face_projection==19744, face_projection
    assert len(distribution)==88, len(distribution)
    assert min(distribution)==Fraction(1,29)
    assert sorted(distribution)[1:3]==[Fraction(1,21),Fraction(1,17)]
    assert max(distribution)==Fraction(17,2)
    assert [distribution[r] for r in (Fraction(1,29),Fraction(1,21),Fraction(1,17))]==[48,96,24]
    reps={
      Fraction(1,29):{((1,1,1),(0,0,0),(0,1,2),(2,2,1)):48},
      Fraction(1,21):{
        ((0,1,1),(0,0,0),(0,1,2),(1,2,0)):48,
        ((1,1,1),(0,0,0),(0,1,2),(2,1,1)):48},
      Fraction(1,17):{((1,1,1),(0,0,0),(1,2,2),(2,1,2)):24},
    }
    assert {k:dict(v) for k,v in orbit_counts.items()}==reps
    with (Path(__file__).parent/'spectrum.csv').open(encoding='utf-8',newline='') as source:
        rows=list(csv.DictReader(source))
    assert len(rows)==88
    recorded={Fraction(r['distance_squared']):int(r['multiplicity']) for r in rows}
    assert len(recorded)==88 and recorded==distribution
    assert sum(recorded.values())==58528
    print('VERIFY_OK: tetrahedra=14632 marked=58528 interior_projection=19744')
    print('VERIFY_OK: 88 distinct squared distances, from 1/29 to 17/2')
    print('VERIFY_OK: first three levels 1/29:48, 1/21:96 (two orbits), 1/17:24')
    print('VERIFY_OK: full 88-level table and all 58528 two-method exact comparisons')

if __name__=='__main__':
    verify()
