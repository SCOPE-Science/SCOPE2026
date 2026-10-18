#!/usr/bin/env python3
"""Finite stress tests for the ordinary four-cut complexes of Möbius ladders.

The proof for all sizes is combinatorial; finite checks do not certify its
unbounded quantifier. Run with `python verify.py` (Python standard library).
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def graph(n):
    N = 2*n
    return {tuple(sorted((i, j))) for i in range(N)
            for j in ((i+1) % N, (i+n) % N)}


def is_connected(vertices, edges):
    V = set(vertices)
    if not V:
        return False
    seen = {next(iter(V))}
    while True:
        nxt = seen | {y for x, y in edges if x in seen and y in V} \
                   | {x for x, y in edges if y in seen and x in V}
        if nxt == seen:
            return seen == V
        seen = nxt


def normal(*V):
    return tuple(sorted(set(V)))


def classified_four_sets(n):
    N = 2*n
    fam = {}
    for i in range(N):
        fam[normal(i-1 if i else N-1, i, (i+1)%N, (i+n)%N)] = 'S'
        fam[normal(*( (i+t)%N for t in range(4)))] = 'R'
        fam[normal(i, (i+1)%N, (i+2)%N, (i+n)%N)] = 'E'
        fam[normal(i, (i+1)%N, (i+2)%N, (i+n+2)%N)] = 'E'
        fam[normal(i, (i+1)%N, (i+n+1)%N, (i+n+2)%N)] = 'M'
        fam[normal(i, (i+1)%N, (i+n)%N, (i+n+1)%N)] = 'Q'
    return fam


def expected_counts(n):
    return {'S':2*n,'R':2*n,'E':4*n,'M':2*n,'Q':n}


def collapse_certificate(four, n):
    remaining=set(four)
    co=defaultdict(set)
    for F in four:
        for tri in combinations(F,3):
            co[tri].add(F)
    cert=[]
    for typ in ('S','R','E','M','Q'):
        batch=sorted(F for F in four if four[F]==typ)
        while batch:
            chosen=None
            for F in batch:
                for tri in combinations(F,3):
                    if co[tri] == {F}:
                        chosen=(F,tri)
                        break
                if chosen:
                    break
            assert chosen, ('no free triangle',n,typ,len(batch))
            F,tri=chosen
            assert F in remaining and len(co[tri]) == 1
            cert.append((tri,F))
            remaining.remove(F)
            batch.remove(F)
            for tr in combinations(F,3):
                co[tr].remove(F)
    assert not remaining
    assert len(cert)==11*n
    return cert



def explicit_formula_certificate(n):
    """Check the six *stated* triangle formulas, not just existence of free faces."""
    N=2*n
    fs=set(classified_four_sets(n))
    def face(*vs):
        return normal(*(v % N for v in vs))
    families = [
      (range(N), lambda i: face(i-1,i,i+1,i+n),
       lambda i: face(i-1,i+1,i+n)),
      (range(N), lambda i: face(i,i+1,i+2,i+3),
       lambda i: face(i,i+1,i+3)),
      (range(N), lambda i: face(i,i+1,i+2,i+n),
       lambda i: face(i,i+2,i+n)),
      (range(N), lambda i: face(i,i+1,i+2,i+n+2),
       lambda i: face(i,i+2,i+n+2)),
      (range(N), lambda i: face(i,i+1,i+n+1,i+n+2),
       lambda i: face(i,i+1,i+n+2)),
      (range(n), lambda i: face(i,i+1,i+n,i+n+1),
       lambda i: face(i,i+1,i+n))
    ]
    for ids, Ff, Tf in families:
        for i in ids:
            F,T=Ff(i),Tf(i)
            assert F in fs
            assert [G for G in fs if set(T) <= set(G)] == [F],(n,i,F,T)
            fs.remove(F)
    assert not fs


def rank_mod(columns, prime):
    pivot={}
    for c in columns:
        a={r:(v%prime) for r,v in c.items() if v%prime}
        while a:
            row=min(a)
            if row not in pivot:
                mul=pow(a[row],-1,prime)
                pivot[row]={i:(v*mul)%prime for i,v in a.items()}
                break
            mul=a[row]
            for i,v in pivot[row].items():
                nv=(a.get(i,0)-mul*v)%prime
                if nv:a[i]=nv
                else:a.pop(i,None)
    return len(pivot)


def boundary_test(n):
    N=2*n
    edges=graph(n)
    facets=[tuple(i for i in range(N) if i not in T)
            for T in combinations(range(N),4)
            if not is_connected(T,edges)]
    # The reduced homology of the full (N-6)-skeleton has the basis of
    # (N-5)-vertex sets not containing vertex 0.
    rowsets=list(combinations(range(1,N),N-5))
    rows={t:i for i,t in enumerate(rowsets)}
    cols=[]
    for F in facets:
        col={}
        for j in range(N-4):
            T=F[:j]+F[j+1:]
            if T in rows:
                col[rows[T]]=(-1)**j
        cols.append(col)
    ranks={p:rank_mod(cols,p) for p in (2,3,5,101)}
    assert all(r==len(rows) for r in ranks.values()),(n,ranks)
    beta=len(cols)-len(rows)
    assert beta == comb(N-1,3)-11*n
    return len(facets),len(rows),beta


def main():
    for n in range(5,13):
        N=2*n
        edges=graph(n)
        four=classified_four_sets(n)
        actual={T for T in combinations(range(N),4)
                if is_connected(T,edges)}
        assert set(four)==actual,('four-set classification',n)
        assert Counter(four.values())==expected_counts(n)
        # The dual has no five-vertex faces: every five-set has a
        # disconnected induced four-subset.
        if n<=10:
            assert all(any(not is_connected([v for v in S if v!=x],edges)
                           for x in S)
                       for S in combinations(range(N),5)), n
        explicit_formula_certificate(n)
        cert=collapse_certificate(four,n)
        # Check elementary collapse by reconstructing the upper coface
        # incidences after every move, independently of the certificate
        # generation's mutable incidence index.
        alive=set(four)
        for tri,F in cert:
            assert F in alive
            assert [G for G in alive if set(tri)<=set(G)] == [F],(n,tri,F)
            alive.remove(F)
        assert not alive
        sample=(n,len(four),len(cert))
        if n<=7:
            sample += boundary_test(n)
        print('n, connected fours, collapse pairs, [facets, basis rows, top rank]:', sample)
    print('All finite stress tests passed; the uniform proof is in RESULT.md.')

if __name__=='__main__':
    main()
