"""Finite consistency tests for the dihedral torus core of cycle-square neighborhood complexes.

The infinite proof is mathematical, not an inference from these finite checks.
Run: python3 cycle_neighborhood_orbifold_checker.py
"""
from collections import Counter, defaultdict
from itertools import combinations


def faces_from_facets(facets):
    return [set(tuple(sorted(s)) for f in facets for s in combinations(f,k))
            for k in range(1, len(facets[0])+1)]


def sig(permutation):
    return (-1) ** sum(permutation[i] > permutation[j]
                        for i in range(len(permutation))
                        for j in range(i+1,len(permutation)))


def check(n):
    mod=lambda x:x%n
    facets=[tuple(map(mod,(i-2,i-1,i+1,i+2))) for i in range(n)]
    allfaces=faces_from_facets(facets)
    A=[tuple(map(mod,(i-2,i+1,i+2))) for i in range(n)]
    B=[tuple(map(mod,(i-2,i+2,i-1))) for i in range(n)]
    K=faces_from_facets(A+B)
    assert [len(f) for f in allfaces]==[n,4*n,4*n,n]
    assert [len(f) for f in K]==[n,3*n,2*n]
    assert all(K[k] <= allfaces[k] for k in range(3))
    assert allfaces[1]-K[1]=={tuple(sorted((mod(i-1),mod(i+1)))) for i in range(n)}
    # Each omitted edge and the two triangles through it occur in one tetrahedron.
    for i in range(n):
        forbidden={mod(i-1),mod(i+1)}
        assert sum(forbidden<=set(tet) for tet in facets)==1
        assert len([tri for tri in allfaces[2] if forbidden<=set(tri)])==2
    # An explicit oriented fundamental cycle on the triangulated torus.
    boundary=Counter()
    for tri in A+B:
        for j in range(3):
            e=tri[:j]+tri[j+1:]
            sorted_e=tuple(sorted(e))
            sign=sig([sorted_e.index(v) for v in e])
            boundary[sorted_e]+=(-1)**j*sign
    assert all(x==0 for x in boundary.values())
    # Every vertex link is a single six-cycle, so K is a closed surface.
    for v in range(n):
        links=[set(s)-{v} for s in K[2] if v in s]
        assert len(links)==6
        graph=defaultdict(set)
        for edge in links:
            a,b=tuple(edge)
            graph[a].add(b);graph[b].add(a)
        assert len(graph)==6 and all(len(neigh)==2 for neigh in graph.values())
        found={next(iter(graph))}
        stack=list(found)
        while stack:
            for y in graph[stack.pop()]:
                if y not in found:found.add(y);stack.append(y)
        assert len(found)==6
    # r and all reflections preserve K, and the latter preserve orientation.
    for t in range(n):
        s=lambda x:mod(t-x)
        for k in range(3):
            assert {tuple(sorted(map(s, f))) for f in K[k]}==K[k]
        # No reflection fixes a 2-simplex and exactly four isolated points are fixed.
        f0=sum(all(s(v)==v for v in f) for f in K[0])
        f1=sum(set(map(s,f))==set(f) for f in K[1])
        f2=sum(set(map(s,f))==set(f) for f in K[2])
        assert (f0,f1,f2)==((1 if n%2 else (2 if t%2==0 else 0)),
                             3 if n%2 else (2 if t%2==0 else 4),0)
        assert f0+f1==4
        for tri in A:
            image=tuple(map(s,tri))
            j=mod(t-(tri[0]+2))
            target=B[j]
            assert set(image)==set(target)
            assert sig([target.index(v) for v in image])==1
    for a in range(1,n):
        r=lambda x:mod(x+a)
        for k in range(3):
            assert sum(set(map(r,f))==set(f) for f in K[k])==0
    # Count barycentric chain orbits to compute quotient Euler independently.
    F=[sorted(level) for level in K]
    chains=[]
    chains.extend(((0,f),) for f in F[0])
    chains.extend(((1,f),) for f in F[1])
    chains.extend(((2,f),) for f in F[2])
    E=[];T=[]
    for i in range(3):
        for j in range(i+1,3):
            for f in F[i]:
                for g in F[j]:
                    if set(f)<=set(g):E.append(((i,f),(j,g)))
    for a in F[0]:
        for b in F[1]:
            if not set(a)<=set(b):continue
            for c in F[2]:
                if set(b)<=set(c):T.append(((0,a),(1,b),(2,c)))
    def orbit_count(cells,group):
        def act(c,g):
            x,s=g
            return tuple((i,tuple(sorted(mod(x+s*v) for v in f))) for i,f in c)
        return len({min(act(c,g) for g in group) for c in cells})
    rot=[(t,1) for t in range(n)]
    dihedral=rot+[(t,-1) for t in range(n)]
    chi_cyc=sum((-1)**k*orbit_count(C,rot) for k,C in enumerate((chains,E,T)))
    chi_dih=sum((-1)**k*orbit_count(C,dihedral) for k,C in enumerate((chains,E,T)))
    assert chi_cyc==0 and chi_dih==2
    return {'n':n,'N_fvector':[len(f) for f in allfaces],
            'torus_fvector':[len(f) for f in K],
            'reflection_fixed_points':4,
            'cyclic_quotient_chi':chi_cyc,
            'dihedral_quotient_chi':chi_dih}

if __name__=='__main__':
    for n in range(9,25):
        print(check(n))
    print('PASS: 16 sizes; finite evidence only')
