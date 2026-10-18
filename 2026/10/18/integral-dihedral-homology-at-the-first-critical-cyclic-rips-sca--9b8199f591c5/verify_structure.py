"""Finite structural checks for the critical cyclic Rips complex (standard library)."""
from itertools import combinations


def adjacency(n, radius):
    return [{j for j in range(n) if j != i and min((j-i)%n, (i-j)%n) <= radius}
            for i in range(n)]


def maximal_cliques(neighbors):
    result = set()
    def search(R, P, X):
        if not P and not X:
            result.add(tuple(sorted(R)))
            return
        u = max(P|X, key=lambda v: len(P & neighbors[v])) if P or X else None
        for v in list(P - (neighbors[u] if u is not None else set())):
            search(R|{v}, P & neighbors[v], X & neighbors[v])
            P.remove(v); X.add(v)
    search(set(), set(range(len(neighbors))), set())
    return result


def all_faces(maximal):
    faces = {()}
    for maximal_face in maximal:
        for k in range(1, len(maximal_face)+1):
            faces.update(combinations(maximal_face,k))
    return faces


def check(r):
    n=3*r
    W={tuple(sorted((i+j)%n for j in range(r+1))) for i in range(n)}
    T={tuple(sorted((i,i+r,i+2*r))) for i in range(r)}
    full=maximal_cliques(adjacency(n,r))
    assert full==(W|T if r>=2 else T), ('facet classification',r,full^(W|T))
    if r==1:
        return (r,n,len(full),0)
    A=all_faces(W)
    B=all_faces(maximal_cliques(adjacency(n,r-1)))
    assert B<=A
    matching=[]
    for i in range(n):
        e={(i)%n,(i+r)%n}
        a=(i+1)%n
        local=[f for f in A if e<=set(f) and a not in f]
        for f in sorted(local,key=lambda x:-len(x)):
            bigger=tuple(sorted((*f,a)))
            assert f in A and bigger in A
            codim_cofaces=[tuple(sorted((*f,w))) for w in range(n) if w not in f and tuple(sorted((*f,w))) in A]
            assert codim_cofaces==[bigger], ('not free',r,i,f,codim_cofaces)
            A.remove(f);A.remove(bigger)
            matching.append((f,bigger))
    assert A==B, ('not collapsed',r,len(A),len(B),len(A^B))
    assert len(matching)>0
    return (r,n,len(full),len(matching))


if __name__=='__main__':
    for r in range(1,13):
        if r<=6:
            print('FACETS_AND_COLLAPSE',check(r))
        else:
            n=3*r
            W={tuple(sorted((i+j)%n for j in range(r+1))) for i in range(n)}
            T={tuple(sorted((i,i+r,i+2*r))) for i in range(r)}
            assert maximal_cliques(adjacency(n,r))==W|T
            print('FACETS',r,n,len(W)+len(T))
    print('VERIFY_STRUCTURE_OK')
