#!/usr/bin/env python3
"""Exact small-instance regression for even-cycle stable-set toric varieties.

Requires Python >=3.10 and sympy. Full face-lattice exhaustion is limited
explicitly to n=6 and 8; the arbitrary-n theorem uses a separate proof.
"""
import itertools
import math
from functools import lru_cache
from sympy import Matrix


def binary_stable_sets(n):
    return [w for w in itertools.product((0,1),repeat=n)
            if all(w[j]+w[(j+1)%n] <= 1 for j in range(n))]


def all_faces_and_max_singular(n):
    pts=binary_stable_sets(n)
    rows=[tuple(-int(j==i) for j in range(n)) for i in range(n)]
    rows += [tuple(int(j==i or j==(i+1)%n) for j in range(n)) for i in range(n)]
    bs=[0]*n+[1]*n
    masks=[sum(1<<q for q,p in enumerate(pts) if sum(a*b for a,b in zip(row,p))==bnd)
           for row,bnd in zip(rows,bs)]
    all_bits=(1<<len(pts))-1
    faces={all_bits}
    for mask in masks:
        faces |= {f&mask for f in tuple(faces) if f&mask}
    sing=[]
    for face in faces:
        active=[j for j,mask in enumerate(masks) if face & mask == face]
        if not active:
            continue
        rank=Matrix([rows[j] for j in active]).rank()
        if len(active)>rank:
            sing.append((face,rank,active))
    maximal=[(f,r,a) for f,r,a in sing
             if not any(f!=g and f&g==f for g,_,_ in sing)]
    expected=[]
    for i in range(n):
        expected.append(tuple(sorted(((i-1)%n,(i+1)%n,n+(i-1)%n,n+i))))
    expected.append(tuple(range(n,2*n)))
    actual=[tuple(sorted(a)) for _,_,a in maximal]
    assert set(actual)==set(expected), (n,actual,expected)
    assert len(actual)==n+1
    assert sorted((r,len(a)) for _,r,a in maximal)==[(3,4)]*n+[(n-1,n)]
    # All listed minimal singular faces have precisely the predicted vertices.
    for f,r,a in maximal:
        vertices=[pts[i] for i in range(len(pts)) if f>>i&1]
        if r==3:
            edge_ids=sorted(q-n for q in a if q>=n)
            center=edge_ids[1] if (edge_ids[0]+1)%n==edge_ids[1] else edge_ids[0]
            assert all(w[center]==1 for w in vertices)
        else:
            assert len(vertices)==2
            assert all(all(w[j]+w[(j+1)%n]==1 for j in range(n)) for w in vertices)
    # Entire intersection poset of the n principal components, and line incidences.
    kfaces=[sum(1<<q for q,v in enumerate(pts) if v[k]==1) for k in range(n)]
    line_face=sum(1<<q for q,v in enumerate(pts)
                  if all(v[j]+v[(j+1)%n]==1 for j in range(n)))
    assert line_face.bit_count()==2
    assert all((kfaces[k]&line_face).bit_count()==1 for k in range(n))
    for subset in range(1<<n):
        selected=[j for j in range(n) if (subset>>j)&1]
        inter=all_bits
        for j in selected:
            inter &= kfaces[j]
        independent=all(((subset>>((j+1)%n))&1)==0 for j in selected)
        assert bool(inter)==independent
        if selected:
            selected_parities={j%2 for j in selected}
            assert bool(inter & line_face)==(len(selected_parities)==1)
    return len(pts),len(faces),len(sing),len(maximal)


@lru_cache(None)
def zigzag(d):
    # Explicit alternating permutation enumeration: small d only.
    if d<=1:
        return 1
    return sum(all((p[j]<p[j+1]) if j%2==0 else (p[j]>p[j+1])
                   for j in range(d-1)) for p in itertools.permutations(range(d)))


def ehrhart_path(d,k):
    if d==0:
        return 1
    # Number of lattice points in k * STAB(P_d), via transfer DP.
    dp=[1]*(k+1)
    for _ in range(1,d):
        prefix=list(itertools.accumulate(dp))
        dp=[prefix[k-a] for a in range(k+1)]
    return sum(dp)


def volume_from_ehrhart(d):
    # Leading coefficient of degree-d Ehrhart polynomial, times d!:
    # its dth forward difference.
    return sum((-1)**(d-k)*math.comb(d,k)*ehrhart_path(d,k) for k in range(d+1))


def main():
    for n in (6,8):
        stats=all_faces_and_max_singular(n)
        print('n=%d stable_vertices=%d all_nonempty_faces=%d singular_faces=%d maximal_singular=%d' % (n,*stats))
    for d in (1,3,5,7):
        v=volume_from_ehrhart(d)
        z=zigzag(d)
        assert v==z, (d,v,z)
        print('path dimension=%d normalized_volume=%d alternating_permutations=%d' %(d,v,z))
    for n in (6,8,10):
        d=n-3
        degree=n*volume_from_ehrhart(d)
        print('cycle n=%d maximal_component_count=%d total_top_degree=%d transverse_line_multiplicity=%d' % (
           n,n,degree,math.comb(n-2,n//2-1)))
    print('CHECKER_OK (finite instances only)')


if __name__=='__main__':
    main()
