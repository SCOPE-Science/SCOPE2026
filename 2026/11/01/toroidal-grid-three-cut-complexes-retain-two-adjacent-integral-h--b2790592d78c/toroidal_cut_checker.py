#!/usr/bin/env python3
"""Finite reproducibility tests for the ordinary three-cut complex of toroidal grids."""
from itertools import combinations
from math import comb

def mod2_rank(cols):
    basis={}
    for vec in cols:
        while vec:
            pivot=vec.bit_length()-1
            if pivot in basis: vec ^=basis[pivot]
            else:
                basis[pivot]=vec
                break
    return len(basis)

def check(m,n):
    assert m>=5 and n>=5
    V=[(i,j) for i in range(m) for j in range(n)]
    index={v:i for i,v in enumerate(V)}
    N=len(V)
    def adjacent(x,y):
        return ((x[0]==y[0] and (x[1]-y[1])%n in (1,n-1))
          or (x[1]==y[1] and (x[0]-y[0])%m in (1,m-1)))
    edges_G={tuple(sorted((i,j))) for i,j in combinations(range(N),2) if adjacent(V[i],V[j])}
    assert len(edges_G)==2*N
    def connected_triple(t):
        return sum(tuple(sorted(e)) in edges_G for e in combinations(t,2))==2
    faces={1:[(i,) for i in range(N)],2:list(combinations(range(N),2))}
    faces[3]=[t for t in combinations(range(N),3) if connected_triple(t)]
    face3=set(faces[3])
    faces[4]=[q for q in combinations(range(N),4) if all(t in face3 for t in combinations(q,3))]
    assert len(faces[3])==6*N, (m,n,len(faces[3]))
    assert len(faces[4])==N,(m,n,len(faces[4]))
    # The tetrahedra are exactly the graph's elementary coordinate squares.
    sqs={tuple(sorted((index[i,j],index[(i+1)%m,j],index[(i+1)%m,(j+1)%n],index[i,(j+1)%n])))
         for i in range(m) for j in range(n)}
    assert set(faces[4])==sqs
    # Check local elementary free-face pairs for all squares, including periodic seams.
    tri_to_tets={t:0 for t in faces[3]}
    for q in faces[4]:
        for t in combinations(q,3): tri_to_tets[t]+=1
    assert all(tri_to_tets[t]==1 for q in sqs for t in combinations(q,3))
    # Verify every declared elementary collapse against its live free faces.
    left_edges=set(faces[2]); left_tris=set(faces[3]); left_tets=set(faces[4])
    for i in range(m):
      for j in range(n):
        a=index[i,j]; b=index[(i+1)%m,j]
        c=index[(i+1)%m,(j+1)%n]; d=index[i,(j+1)%n]
        tet=tuple(sorted((a,b,c,d)))
        t1=tuple(sorted((a,b,c)))
        t2=tuple(sorted((a,c,d)))
        diag=tuple(sorted((a,c)))
        assert tet in left_tets and t1 in left_tris
        assert sum(set(t1).issubset(q) for q in left_tets)==1
        left_tets.remove(tet);left_tris.remove(t1)
        assert t2 in left_tris and diag in left_edges
        assert sum(set(diag).issubset(t) for t in left_tris)==1
        assert not any(set(diag).issubset(q) for q in left_tets)
        left_tris.remove(t2);left_edges.remove(diag)
    for i in range(m):
      for j in range(n):
        v=index[i,j]
        for a,b in ((index[(i-1)%m,j],index[(i+1)%m,j]),
                    (index[i,(j-1)%n],index[i,(j+1)%n])):
          tri=tuple(sorted((a,v,b))); chord=tuple(sorted((a,b)))
          assert tri in left_tris and chord in left_edges
          assert sum(set(chord).issubset(t) for t in left_tris)==1
          assert not any(set(chord).issubset(q) for q in left_tets)
          left_tris.remove(tri);left_edges.remove(chord)
    assert not left_tets and len(left_tris)==2*N
    assert len(left_edges)==comb(N,2)-3*N
    # The retained triangles triangulate exactly the usual toroidal square cells.
    torus_tris=set();torus_edges=set(edges_G)
    for i in range(m):
      for j in range(n):
        a=index[i,j];b=index[(i+1)%m,j];c=index[(i+1)%m,(j+1)%n];d=index[i,(j+1)%n]
        torus_tris.update([tuple(sorted((a,b,d))),tuple(sorted((b,c,d)))])
        torus_edges.add(tuple(sorted((b,d))))
    assert left_tris==torus_tris and torus_edges<=left_edges and len(torus_edges)==3*N
    # Independently calculate the mod-two chain ranks of the complete Alexander dual.
    idx={s:{v:i for i,v in enumerate(faces[s])} for s in (1,2,3,4)}
    b1=[(1<<a)|(1<<b) for a,b in faces[2]]
    b2=[sum(1<<idx[2][e] for e in combinations(t,2)) for t in faces[3]]
    b3=[sum(1<<idx[3][t] for t in combinations(q,3)) for q in faces[4]]
    r1,r2,r3=map(mod2_rank,(b1,b2,b3))
    betti1=len(faces[2])-r1-r2
    betti2=len(faces[3])-r2-r3
    assert (r1,r2,r3)==(N-1,5*N-1,N),(m,n,r1,r2,r3)
    assert (betti1,betti2)==(comb(N,2)-6*N+2,1)
    print(f'C_{m} x C_{n}: V={N}, dual faces=({N},{comb(N,2)},{6*N},{N}), boundary ranks=({r1},{r2},{r3}), beta1={betti1}, beta2={betti2}: OK')
    return betti1,betti2

if __name__=='__main__':
    for m,n in [(5,5),(5,6),(6,6)]: check(m,n)
    print('TOROIDAL_THREE_CUT_DUAL_CHAIN_CHECKS_OK')
