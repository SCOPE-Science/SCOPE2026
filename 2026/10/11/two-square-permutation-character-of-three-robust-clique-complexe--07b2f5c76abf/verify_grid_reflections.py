#!/usr/bin/env python3
"""Exact finite checks for the rational reflection character of 3-robust grid complexes.

Python 3 standard library only. Face tests use forbidden independent triples;
the proof's matching-based formula is verified separately.
"""
from itertools import combinations
from math import comb


def edges_of_grid(m, n):
    out = set()
    for i in range(m):
        for j in range(n):
            u = i * n + j
            if i + 1 < m:
                out.add(frozenset((u, (i + 1) * n + j)))
            if j + 1 < n:
                out.add(frozenset((u, i * n + j + 1)))
    return out


def is_face(vertices, edges):
    return not any(not any(frozenset(e).issubset(t) for e in edges)
                   for t in combinations(vertices, 3))


def matching_face_four(vertices, edges):
    if len(vertices) != 4:
        return False
    a, b, c, d = vertices
    return any(frozenset(p) in edges and frozenset(q) in edges
               for p, q in (((a,b),(c,d)), ((a,c),(b,d)), ((a,d),(b,c))))


def permutation(m, n, mode):
    def f(i, j):
        if mode == 'row': return m - 1 - i, j
        if mode == 'col': return i, n - 1 - j
        if mode == 'both': return m - 1 - i, n - 1 - j
        if mode == 'id': return i, j
        raise ValueError(mode)
    return tuple(f(i,j)[0]*n + f(i,j)[1] for i in range(m) for j in range(n))


def orbit_trace(m, n, mode):
    perm = permutation(m, n, mode)
    visited = set()
    orbits = []
    for u in range(m * n):
        if u in visited:
            continue
        orbit = []
        v = u
        while v not in visited:
            orbit.append(v)
            visited.add(v)
            v = perm[v]
        orbits.append(tuple(orbit))
    edges = edges_of_grid(m, n)
    out = [0] * 5
    def visit(index, chosen, number):
        if index == len(orbits):
            if is_face(chosen, edges):
                out[len(chosen)] += (-1) ** number
            return
        visit(index + 1, chosen, number)
        if len(chosen) + len(orbits[index]) <= 4:
            visit(index + 1, chosen + orbits[index], number + 1)
    visit(0, (), 0)
    return sum(out)


def predicted(m, n, mode):
    a = (m-1)*(n-1)
    if mode=='id': return comb(a, 2)
    if mode=='row': return (n-1)*(m+n-4)//2
    if mode=='col': return (m-1)*(m+n-4)//2
    if mode=='both': return (m*n-m-n)//2
    raise ValueError(mode)


def direct_signed_trace(m, n, mode):
    """Alternating simplicial trace, including the augmented empty face."""
    perm = permutation(m, n, mode)
    total = -1
    for dim, faces in enumerate(face_groups(m, n)):
        trace = 0
        for face in faces:
            images = tuple(perm[x] for x in face)
            if set(images) != set(face):
                continue
            inversions = sum(images[i] > images[j]
                             for i in range(len(face))
                             for j in range(i + 1, len(face)))
            trace += (-1) ** inversions
        total += (-1) ** dim * trace
    return -total


def face_groups(m,n):
    edges=edges_of_grid(m,n)
    V=tuple(range(m*n))
    return [list(x for x in combinations(V,k) if is_face(x,edges))
            for k in range(1,5)]


def rank_gf2(columns):
    pivots={}
    for x in columns:
        while x:
            bit=x.bit_length()-1
            if bit not in pivots:
                pivots[bit]=x
                break
            x^=pivots[bit]
    return len(pivots)


def betti_gf2(m,n):
    faces=face_groups(m,n)
    ranks=[0]
    for k in range(1,4):
        index={f:i for i,f in enumerate(faces[k-1])}
        cols=[]
        for f in faces[k]:
            word=0
            for t in combinations(f,k):
                word ^= (1<<index[t])
            cols.append(word)
        ranks.append(rank_gf2(cols))
    betti=[]
    for k in range(4):
        boundary_below=ranks[k]
        boundary_above=ranks[k+1] if k<3 else 0
        betti.append(len(faces[k])-boundary_below-boundary_above-(1 if k==0 else 0))
    return betti, [len(f) for f in faces], ranks


def main():
    exact_character=0
    for m in (2,4,6,8):
        for n in (2,4,6,8):
            for mode in ('row','col','both'):
                actual=orbit_trace(m,n,mode)
                expected=predicted(m,n,mode)
                assert actual==expected, (m,n,mode,actual,expected)
                exact_character+=1
            d=predicted(m,n,'id')
            h=predicted(m,n,'row')
            v=predicted(m,n,'col')
            z=predicted(m,n,'both')
            multiplicities=[(d+e*h+f*v+e*f*z)//4
                            for e in (1,-1) for f in (1,-1)]
            assert sum(multiplicities)==d
            assert min(multiplicities)>=0
            assert all((d+e*h+f*v+e*f*z)%4==0
                       for e in (1,-1) for f in (1,-1))
    signed_cases=0
    for m, n in ((2,2),(2,4),(4,2),(4,4),(4,6)):
        for mode in ('row','col','both'):
            got = direct_signed_trace(m,n,mode)
            expect = predicted(m,n,mode)
            assert got == expect, (m,n,mode,got,expect)
            signed_cases += 1
    exact_faces=0
    for m,n in ((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)):
        faces=face_groups(m,n)
        edges=edges_of_grid(m,n)
        for F in faces[3]:
            assert matching_face_four(F,edges)
            exact_faces+=1
        betti,fvec,ranks=betti_gf2(m,n)
        want=[0,0,0,comb((m-1)*(n-1),2)]
        assert betti==want,(m,n,betti,want)
        print('HOMOLOGY_OK',m,n,betti,'faces',fvec,'boundary_ranks',ranks)
    print('VERIFY_OK','reflection_characters',exact_character,'tetrahedra',exact_faces,
          'direct_signed_trace_cases',signed_cases,
          'independent_mod2_homology_cases',6)

if __name__=='__main__':
    main()
