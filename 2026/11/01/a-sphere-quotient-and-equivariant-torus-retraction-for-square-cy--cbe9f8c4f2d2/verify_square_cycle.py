#!/usr/bin/env python3
"""Exact finite checks supporting the cycle-square neighborhood quotient theorem.
The infinite extension uses the explicit local construction in RESULT.md.
"""
from itertools import combinations
from collections import Counter, defaultdict

def parity(seq):
    inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return (-1)**inv

def perm_sign_on_simplex(simplex,f):
    images=[f(x) for x in simplex]
    return parity(images)

def complex_for(n):
    facets=[frozenset((i-2,i-1,i+1,i+2)[j]%n for j in range(4)) for i in range(n)]
    triangles=[frozenset(((i+a)%n for a in D)) for i in range(n) for D in [(0,1,3),(0,2,3)]]
    N=set();T=set()
    for f in facets:
        for k in range(1,len(f)+1):N.update(frozenset(x) for x in combinations(sorted(f),k))
    for tr in triangles:
        for k in range(1,4):T.update(frozenset(x) for x in combinations(sorted(tr),k))
    return facets,triangles,N,T

def trace_on_cells(cells,g):
    return sum(perm_sign_on_simplex(sorted(f),g) for f in cells if frozenset(g(v) for v in f)==f)

def verify(n):
    facets,triangles,K,T=complex_for(n)
    assert len(set(facets))==n and len(set(triangles))==2*n
    assert Counter(map(len,K))=={1:n,2:4*n,3:4*n,4:n}
    assert Counter(map(len,T))=={1:n,2:3*n,3:2*n}
    assert T<=K
    # Exact gluing condition for the explicit local strong deformation retraction:
    # every intersection of two tetrahedra lies in the retained triangulated surface.
    for i,j in combinations(range(n),2):
        common=facets[i]&facets[j]
        for k in range(1,len(common)+1):
            assert all(frozenset(t) in T for t in combinations(sorted(common),k)),(n,i,j,common)
    # The outer edge of each tetrahedron is the sole deleted edge there.
    outer=[frozenset({(i-2)%n,(i+2)%n}) for i in range(n)]
    assert len(set(outer))==n and set(outer)=={x for x in K-T if len(x)==2}
    assert {x for x in K-T if len(x)==3}=={frozenset(facets[i]-{(i-1)%n}) for i in range(n)}|{frozenset(facets[i]-{(i+1)%n}) for i in range(n)}
    # Each core edge occurs in exactly two triangles, and every vertex link is a six-cycle.
    incid=Counter(e for tr in triangles for e in map(frozenset,combinations(tr,2)))
    assert len(incid)==3*n and set(incid.values())=={2}
    for v in range(n):
        link=[frozenset(t-{v}) for t in triangles if v in t]
        deg=Counter(x for e in link for x in e)
        assert len(link)==6 and len(deg)==6 and set(deg.values())=={2}
        graph=defaultdict(set)
        for a,b in map(tuple,link):graph[a].add(b);graph[b].add(a)
        visited=set();pending=[next(iter(deg))]
        while pending:
            x=pending.pop()
            if x in visited:continue
            visited.add(x);pending.extend(graph[x]-visited)
        assert len(visited)==6
    # All simplices preserved by the natural dihedral action.
    for k in range(n):
        for reflection in (False,True):
            g=lambda x,k=k,reflection=reflection: (k-x if reflection else k+x)%n
            assert {frozenset(g(x) for x in f) for f in facets}==set(facets)
            assert {frozenset(g(x) for x in f) for f in triangles}==set(triangles)
    # Orientable: sum of A_i - B_i with compatible vertex orders is a 2-cycle.
    boundary=Counter()
    for i in range(n):
        for tri,coef in [((i,(i+1)%n,(i+3)%n),1),((i,(i+2)%n,(i+3)%n),-1)]:
            for j in range(3):
                edge=tuple(x for l,x in enumerate(tri) if l!=j)
                canonical=tuple(sorted(edge));sgn=parity(edge)
                boundary[canonical]+=coef*(-1)**j*sgn
    assert all(v==0 for v in boundary.values()), (n,boundary)
    # The same orientation cycle is fixed by all rotations and by reflection.
    def oriented_triangles():
        cy=Counter()
        for i in range(n):
            for t,sgn in [((i,(i+1)%n,(i+3)%n),1),((i,(i+2)%n,(i+3)%n),-1)]:
                cy[tuple(sorted(t))]+=sgn*parity(t)
        return cy
    z=oriented_triangles()
    for k in range(n):
        for refl in (False,True):
            g=lambda x,k=k,refl=refl: (k-x if refl else k+x)%n
            result=Counter()
            for t,coef in z.items():
                im=tuple(g(x) for x in t)
                result[tuple(sorted(im))]+=coef*parity(im)
            assert result==z,(n,k,refl)
    # Lefschetz traces on the entire finite simplicial complex.
    for k in range(n):
        for refl in (False,True):
            g=lambda x,k=k,refl=refl: (k-x if refl else k+x)%n
            L=sum((-1)**(dim-1)*trace_on_cells((f for f in T if len(f)==dim),g) for dim in range(1,4))
            assert L==(4 if refl else (0 if k else 0)),(n,k,refl,L)
            # Euler characteristic 0 even for identity (torus).
    return n,len(K),len(T)

if __name__=='__main__':
    for n in range(9,65):print('OK',*verify(n))
    print('CYCLE_SQUARE_DIHEDRAL_VERIFY_OK')
