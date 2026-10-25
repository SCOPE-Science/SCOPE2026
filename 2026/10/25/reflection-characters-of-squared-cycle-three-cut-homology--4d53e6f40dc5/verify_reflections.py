#!/usr/bin/env python3
"""Finite independent checks for reflection characters of squared-cycle 3-cut complexes.
Python >=3.9 standard library. The published shellability and the all-n combinatorial
argument in RESULT.md are the infinite-family proof; these are reproducibility checks.
"""
from itertools import combinations
from collections import Counter


def near(u,v,n):
    return u != v and min((v-u)%n,(u-v)%n)<=2


def connected_three(t,n):
    return any(sum(near(v,w,n) for w in t if w!=v)==2 for v in t)


def dual_faces(n):
    """Directly apply connected-triples condition, independent of face-template proof."""
    F={()}
    for k in range(1,6):
        for s in combinations(range(n),k):
            if all(connected_three(t,n) for t in combinations(s,3)):
                F.add(s)
    return F


def template_faces(n):
    triangles={(tuple(sorted((i+j)%n for j in pattern)))
                for i in range(n)
                for pattern in ((0,1,2),(0,1,3),(0,2,3),(0,2,4))}
    tetra={tuple(sorted((i+j)%n for j in (0,1,2,3)))
           for i in range(n)}
    return ({()}|{(i,) for i in range(n)}|set(combinations(range(n),2))
            |triangles|tetra)


def signed_reduced_lefschetz(faces,n,a):
    g=lambda j:(a-j)%n
    assert {tuple(sorted(g(j) for j in f)) for f in faces}==faces
    L=-1  # empty face in degree -1
    for f in faces:
        if not f:continue
        im=[g(j) for j in f]
        if set(im)!=set(f):continue
        inversions=sum(im[i]>im[j] for i in range(len(im))
                       for j in range(i+1,len(im)))
        L+=(-1)**(len(f)-1+inversions)
    return L


def dual_character(n,a):
    if n%2:
        return (-1)**((n-1)//2)*((7-n)//2)
    if a%2==0:
        return (-1)**((n-2)//2)*((10-n)//2)
    return (-1)**(n//2)*((6-n)//2)


def direct_cut_faces(n):
    facets=[tuple(j for j in range(n) if j not in t)
            for t in combinations(range(n),3) if not connected_three(t,n)]
    faces=set()
    for facet in facets:
        for k in range(len(facet)+1):faces.update(combinations(facet,k))
    return faces


def run():
    cases=0
    for n in range(9,23):
        faces=dual_faces(n)
        templates=template_faces(n)
        assert faces==templates, (n,len(faces),len(templates))
        assert Counter(len(s) for s in faces)==Counter({0:1,1:n,2:n*(n-1)//2,3:4*n,4:n})
        for a in range(n):
            L=signed_reduced_lefschetz(faces,n,a)
            reflection_sign=(-1)**((n-1)//2 if n%2 else
                                  (n-2)//2 if a%2==0 else n//2)
            chi=reflection_sign*(1-(L+1))  # L+1 = ordinary Lefschetz of the dual
            assert chi==dual_character(n,a),(n,a,L,chi,dual_character(n,a))
            cases+=1
    direct=0
    for n in range(9,15):
        faces=direct_cut_faces(n)
        for a in range(n):
            lef=signed_reduced_lefschetz(faces,n,a)
            chi=(-1)**(n-4)*lef
            assert chi==dual_character(n,a), (n,a,chi)
            direct+=1
    print('VERIFY_OK', 'dual_graph_sizes=14', 'dual_symmetry_checks='+str(cases),
          'direct_cut_symmetry_checks='+str(direct),
          'independent_face_template_checks=14')


if __name__=='__main__':run()
