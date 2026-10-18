#!/usr/bin/env python3
"""Exact facet/face/lattice checks for diagonal-free rank-one toric models.
Requires Python >=3.9 and SymPy.  No numerical optimization or floating point.
"""
from itertools import combinations
from math import comb
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def audit(n):
    edges = [(i,j) for i in range(n) for j in range(n) if i != j]
    d = 2*n-2
    L = len(edges)
    allmask = (1 << L) - 1
    facet_names = [(typ,i) for typ in ('x','y','h') for i in range(n)]

    def on_facet(f, e):
        typ, k = f
        i,j = e
        return (i != k if typ == 'x' else j != k if typ == 'y'
                else i == k or j == k)
    facet_mask = [sum((1<<p) for p,e in enumerate(edges) if on_facet(f,e))
                  for f in facet_names]
    # The 3n proposed inequalities are genuine facets: an active set of
    # vertices has affine dimension d-1.
    def dimension(mask):
        used = [edges[p] for p in range(L) if mask & (1<<p)]
        nodes = {i for i,j in used} | {n+j for i,j in used}
        parent = {v:v for v in nodes}
        def root(v):
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v
        for i,j in used:
            a,b = root(i),root(n+j)
            if a != b:parent[a] = b
        c = len({root(u) for u in nodes})
        # Bipartite incidence-polytope dimension: |nodes|-components-1.
        return len(nodes)-c-1
    assert dimension(allmask) == d
    for mask in facet_mask:
        assert dimension(mask) == d-1

    # Every face of this H-polytope is an intersection of facet hyperplanes.
    faces = {allmask}
    queue = [allmask]
    for face in queue:
        for facet in facet_mask:
            nxt = face & facet
            if nxt and nxt not in faces:
                faces.add(nxt)
                queue.append(nxt)

    # Inward primitive facet normals in the affine lattice with x_n,y_n
    # eliminated by their sum-one equations.
    normals=[]
    for typ,k in facet_names:
        v=[0]*d
        offset=0 if typ == 'x' else n-1
        if typ in ('x','y'):
            if k != n-1:v[offset+k]=1
            else:
                for j in range(n-1):v[offset+j]=-1
        else:
            if k != n-1:v[k]=-1;v[n-1+k]=-1
            else:v=[1]*d
        normals.append(v)

    bad={}
    nonsimple=0
    simplicial_nonunimodular=0
    for mask in faces:
        cod=d-dimension(mask)
        active=[q for q,fac in enumerate(facet_mask) if mask & fac == mask]
        if len(active)>cod:
            bad[mask]=cod
            nonsimple+=1
        else:
            assert len(active)==cod
            if cod:
                A=Matrix([normals[i] for i in active])
                S=smith_normal_form(A,domain=ZZ)
                invariant=[abs(int(S[t,t])) for t in range(cod)]
                if any(v!=1 for v in invariant):
                    bad[mask]=cod
                    simplicial_nonunimodular+=1

    # Independently predicted maximal strata: row stars, column stars,
    # and reverse-edge pairs.  Check that the complete singular-face set
    # is exactly the set of their nonempty subfaces.
    candidate=[]
    for i in range(n):
        candidate.append(sum(1<<k for k,e in enumerate(edges) if e[0]==i))
        candidate.append(sum(1<<k for k,e in enumerate(edges) if e[1]==i))
    for i,j in combinations(range(n),2):
        candidate.append(sum(1<<k for k,e in enumerate(edges)
                             if e in ((i,j),(j,i))))
    assert len(candidate)==2*n+comb(n,2)
    assert len(set(candidate))==len(candidate)
    assert all(c in faces and c in bad for c in candidate)
    predicted={f for f in faces if any(f & c == f for c in candidate)}
    assert set(bad)==predicted, ('singular-support mismatch',n)
    maximal=[f for f in bad if not any(f!=q and f&q==f for q in bad)]
    assert set(maximal)==set(candidate), ('component mismatch',n)
    assert {bad[c] for c in candidate[:2*n]}=={n}
    assert {bad[c] for c in candidate[2*n:]}=={2*n-3}
    assert simplicial_nonunimodular==0
    return (len(faces),len(bad),len(maximal),nonsimple)


def main():
    expected={3:(49,15,9),4:(349,50,14),5:(1911,140,20),
              6:(9327,357,27)}
    for n,want in expected.items():
        got=audit(n)
        assert got[:3]==want,(n,got,want)
        print('n=%d faces=%d singular_faces=%d components=%d'
              % (n,got[0],got[1],got[2]))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
