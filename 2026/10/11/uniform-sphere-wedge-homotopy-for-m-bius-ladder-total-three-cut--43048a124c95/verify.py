#!/usr/bin/env python3
"""Independent finite consistency checks for a uniform family of graph cut complexes."""
from itertools import combinations
from collections import deque
from math import comb


def graph(n):
    m = 2*n
    return m, frozenset(tuple(sorted(x)) for x in
        ([ (i, (i+1)%m) for i in range(m) ] + [(i, i+n) for i in range(n)]))


def has_independent_triple(vertices, edges):
    return any(all(tuple(sorted(p)) not in edges for p in combinations(t, 2))
               for t in combinations(vertices, 3))


def bounded_faces(m, edges, limit=5):
    layers = []
    for k in range(1, min(limit, m)+1):
        faces = [t for t in combinations(range(m),k)
                 if not has_independent_triple(t, edges)]
        layers.append(faces)
    return layers


def rank(columns):
    pivots={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def homology(faces):
    boundary_ranks = [1]
    for k in range(1, len(faces)):
        prev={simplex:i for i,simplex in enumerate(faces[k-1])}
        columns = [sum(1 << prev[s[:j]+s[j+1:]] for j in range(k+1))
                   for s in faces[k]]
        boundary_ranks.append(rank(columns))
    assert all(boundary_ranks[i] <= len(faces[i-1]) for i in range(1,len(faces)))
    b=[len(lev)-boundary_ranks[i]-(boundary_ranks[i+1] if i+1<len(faces) else 0)
       for i,lev in enumerate(faces)]
    return boundary_ranks,b


def relative_telescope(n,edges):
    m=2*n
    tree=frozenset((i,i+1) for i in range(m-1))
    kt_faces={t for t in combinations(range(m),3)
              if not has_independent_triple(t,tree)}
    count=0
    for t in combinations(range(m),3):
        if has_independent_triple(t, edges) or t in kt_faces:
            continue
        ab=next(e for e in combinations(t,2) if e in edges and e not in tree)
        a,b=ab
        c=next(v for v in t if v not in ab)
        step=1 if c < a else -1
        path=list(range(c,a+step,step))
        hit=next((i for i,v in enumerate(path) if v in (a,b)),None)
        assert hit is not None and hit>0
        path=path[:hit]
        assert path[-1] not in (a,b)
        assert tuple(sorted((a,b,path[-1]))) in kt_faces
        chain=[]
        for c0,c1 in zip(path,path[1:]):
            q=tuple(sorted((a,b,c0,c1)))
            assert not has_independent_triple(q,edges)
            chain.append(q)
        rel=0
        other=[t] if not chain else []
        for q in chain:
            for triple in combinations(q,3):
                if triple not in kt_faces:
                    other.append(triple)
        parity={}
        for triple in other:
            parity[triple]=1-parity.get(triple,0)
        # For chains, relative boundary is exactly the first new 2-simplex.
        if chain:
            assert {x for x,v in parity.items() if v} == {t}, (t,chain,parity)
        count+=1
    return count


def dual_complex(m,edges):
    independent=[set(t) for t in combinations(range(m),3)
                 if all(tuple(sorted(e)) not in edges for e in combinations(t,2))]
    layers=[]
    for k in range(1,m+1):
        layer=[s for s in combinations(range(m),k)
               if any(all(v not in t for v in s) for t in independent)]
        if layer:layers.append(layer)
        else:break
    return layers


def main():
    for n in range(5,15):
        m,edges=graph(n)
        assert len(edges)==3*n
        faces=bounded_faces(m,edges,5)
        expected=[2*n,comb(2*n,2),6*n*(n-2),comb(3*n,2)-7*n,0]
        sizes=[len(f) for f in faces]
        assert sizes==expected,(n,sizes,expected)
        r,b=homology(faces[:-1])
        expected_beta=1+comb(n+1,2)
        assert b==[0,0,0,expected_beta],(n,b,expected_beta,r)
        assert relative_telescope(n,edges)>0
        print('BI3',n,'faces',sizes,'reduced_GF2_betti',b,flush=True)
    for n in (5,6):
        m,edges=graph(n)
        layers=dual_complex(m,edges)
        r,b=homology(layers)
        expected=[0]*len(b)
        expected[2*n-6]=1+comb(n+1,2)
        assert b==expected,(n,b,expected)
        print('TOTAL3',n,'faces',[len(f) for f in layers],'reduced_GF2_betti',b,flush=True)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
