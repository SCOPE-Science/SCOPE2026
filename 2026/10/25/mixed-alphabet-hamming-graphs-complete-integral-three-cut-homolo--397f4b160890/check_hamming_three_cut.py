#!/usr/bin/env python3
"""Finite consistency checks for the connected-triple Alexander dual of a Hamming graph.

Builds the complex from its defining forbidden triples, and checks a second,
coordinate-cell construction including modular simplicial homology.
Only finite test instances are checked; the general theorem requires its proof.
"""
from itertools import product, combinations
from math import comb, prod


def parameters(qs):
    n=prod(qs)
    E=sum((n//q)*comb(q,2) for q in qs)
    Q=sum((n//(qs[i]*qs[j]))*comb(qs[i],2)*comb(qs[j],2)
          for i in range(len(qs)) for j in range(i+1,len(qs)))
    b=Q - 1 + n - sum((n//q)*(q-1) for q in qs)
    a=comb(n,2)-E-2*Q
    return n,E,Q,a,b


def cells(qs):
    V=list(product(*(range(q) for q in qs)))
    index={v:i for i,v in enumerate(V)}
    n=len(V)
    by_dimension=[{(i,) for i in range(n)},set(combinations(range(n),2))]
    def ensure(k):
        while len(by_dimension) <= k:
            by_dimension.append(set())
    # Complete coordinate-line simplices.
    for axis,q in enumerate(qs):
        others=[j for j in range(len(qs)) if j!=axis]
        for labs in product(*(range(qs[j]) for j in others)):
            prototype=[0]*len(qs)
            for j,t in zip(others,labs): prototype[j]=t
            line=[]
            for value in range(q):
                prototype[axis]=value
                line.append(index[tuple(prototype)])
            for r in range(3,q+1):
                ensure(r-1)
                by_dimension[r-1].update(combinations(sorted(line),r))
    # Coordinate squares, each taken as a four-vertex tetrahedron.
    for a,b in combinations(range(len(qs)),2):
        rest=[j for j in range(len(qs)) if j not in (a,b)]
        for labs in product(*(range(qs[j]) for j in rest)):
            base=[0]*len(qs)
            for j,t in zip(rest,labs): base[j]=t
            for va in combinations(range(qs[a]),2):
                for vb in combinations(range(qs[b]),2):
                    four=[]
                    for x,y in product(va,vb):
                        base[a],base[b]=x,y
                        four.append(index[tuple(base)])
                    for r in (3,4):
                        ensure(r-1)
                        by_dimension[r-1].update(combinations(sorted(four),r))
    return V,by_dimension


def connected_triple(V,indices):
    a,b,c=(V[i] for i in indices)
    return sum(x!=y for x,y in zip(a,b))==1 and (
        sum(x!=y for x,y in zip(a,c))==1 or
        sum(x!=y for x,y in zip(b,c))==1
    ) or (
        sum(x!=y for x,y in zip(a,c))==1 and
        sum(x!=y for x,y in zip(b,c))==1
    )


def rank_boundary(columns, row_index, prime):
    basis={}
    for simplex in columns:
        v={}
        for i in range(len(simplex)):
            face=simplex[:i]+simplex[i+1:]
            key=row_index[face]
            v[key]=(v.get(key,0)+(1 if i%2==0 else -1))%prime
            if not v[key]: del v[key]
        while v:
            pivot=max(v)
            if pivot not in basis:
                u=pow(v[pivot],-1,prime)
                basis[pivot]={k:(z*u)%prime for k,z in v.items() if z%prime}
                break
            factor=v[pivot]
            for k,z in basis[pivot].items():
                w=(v.get(k,0)-factor*z)%prime
                if w: v[k]=w
                elif k in v: del v[k]
    return len(basis)


def verify(qs):
    V,cells_by_dim=cells(qs)
    n,E,Q,a,b=parameters(qs)
    assert n==len(V) and a>=0 and b>=0
    # Definition: a simplex belongs to the dual iff every triple is connected.
    # This independent enumeration does not use coordinate-line/square classification.
    graph_adjacency={frozenset((i,j)) for i,j in combinations(range(n),2)
                    if sum(x!=y for x,y in zip(V[i],V[j]))==1}
    def triple_ok(t):
        return sum(frozenset(p) in graph_adjacency for p in combinations(t,2))>=2
    for r in (3,4):
        defining={face for face in combinations(range(n),r)
                  if all(triple_ok(t) for t in combinations(face,3))}
        assert defining==cells_by_dim[r-1],(qs,r,len(defining),len(cells_by_dim[r-1]))
    # For q<=4 there are no possible faces of size>=5; for larger q the
    # nonadjacent-pair/common-neighbor proof covers all high-dimensional faces.
    if max(qs)<=4:
        if max(qs)==4:
            for face in combinations(range(n),5):
                assert not all(triple_ok(t) for t in combinations(face,3))
    face_lists=[sorted(x) for x in cells_by_dim]
    assert sum(1 for i,j in combinations(range(n),2) if sum(V[i][k]!=V[j][k] for k in range(len(qs)))>=3)==a
    for p in (2,3,5):
        ranks=[0]
        for k in range(1,len(face_lists)):
            rows={face:i for i,face in enumerate(face_lists[k-1])}
            ranks.append(rank_boundary(face_lists[k],rows,p))
        betti=[len(face_lists[k])-ranks[k]-(ranks[k+1] if k+1<len(ranks) else 0)
               for k in range(len(face_lists))]
        predicted=[1,a,b]+[0]*(len(face_lists)-3)
        assert betti==predicted,(qs,p,betti,predicted)
    print('PASS',qs,'N',n,'E',E,'squares',Q,'extra_edges',a,'sphere_2',b,
          'faces',tuple(map(len,face_lists)))


if __name__=='__main__':
    for parameters_tuple in ((2,2,2),(2,3),(2,3,3),(3,3,3),(2,2,2,2),(2,3,4),(3,3,4)):
        verify(parameters_tuple)
    print('ALL CHECKS PASSED (finite examples only).')
