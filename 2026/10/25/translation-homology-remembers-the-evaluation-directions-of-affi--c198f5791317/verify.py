#!/usr/bin/env python3
"""Standalone finite checks for the simple-homotopy reduction of orthogonal-array realization complexes.
Runs solely on standard Python. All samples are prime-field affine line evaluation arrays.
"""
from itertools import combinations, product
from math import comb
from cmath import exp, pi


def affine_oa(q, n):
    """Rows (x,y,x+a*y for a=1..n-2) over prime field F_q."""
    assert q >= 3 and 4 <= n <= q+1
    rows = [tuple([x, y] + [(x + a*y) % q for a in range(1, n-1)])
            for x in range(q) for y in range(q)]
    assert len(set(rows)) == q*q
    return rows


def all_faces(rows):
    n = len(rows[0])
    faces = {frozenset()}
    for word in rows:
        row = [(i,word[i]) for i in range(n)]
        for k in range(1,n+1):
            for indices in combinations(range(n),k):
                faces.add(frozenset(row[i] for i in indices))
    return faces


def independent_faces_by_extension(rows):
    n = len(rows[0]); q = len(set(r[0] for r in rows))
    res=set()
    for values in product(range(-1,q),repeat=n):
        if any(all(val==-1 or row[i]==val for i,val in enumerate(values)) for row in rows):
            res.add(frozenset((i,v) for i,v in enumerate(values) if v>=0))
    return res


def verify(q,n, full_independent=False):
    rows=affine_oa(q,n)
    for i,j in combinations(range(n),2):
        projections={(r[i],r[j]) for r in rows}
        assert projections==set(product(range(q),repeat=2))
    for r,s in combinations(rows,2):
        assert sum(r[i]==s[i] for i in range(n))<=1
    faces=all_faces(rows)
    if full_independent: assert faces==independent_faces_by_extension(rows)
    expected_f=[n*q]+[comb(n,r)*q*q for r in range(2,n+1)]
    actual_f=[sum(1 for f in faces if len(f)==r) for r in range(1,n+1)]
    assert actual_f==expected_f,(q,n,actual_f,expected_f)
    active=faces.copy()
    pairs=0
    # Descending order makes each selected nonroot face free.
    for size in range(n-1,1,-1):
        for w in rows:
            root=(0,w[0])
            others=[(i,w[i]) for i in range(1,n)]
            for sub in combinations(others,size):
                low=frozenset(sub)
                high=low|{root}
                assert low in active and high in active
                higher=[f for f in active if len(f)==size+1 and low.issubset(f)]
                assert higher==[high],('not a free pair',q,n,sub,higher)
                active.remove(low)
                active.remove(high)
                pairs+=1
    graph_vertices={frozenset({(i,a)}) for i in range(n) for a in range(q)}
    graph_edges={frozenset({(0,a),(i,b)}) for a in range(q) for i in range(1,n) for b in range(q)}
    expected={frozenset()}|graph_vertices|graph_edges
    assert active==expected,('terminal complex not complete bipartite',q,n)
    rank=len(graph_edges)-len(graph_vertices)+1
    assert rank==(q-1)*((n-1)*q-1)
    # Verify the complete translation Lefschetz character by enumerating all
    # fixed faces, independently of the collapsed graph.
    trace = {}
    for tx,ty in product(range(q),repeat=2):
        shift=[tx,ty]+[(tx+a*ty)%q for a in range(1,n-1)]
        signed_euler=0
        for f in faces:
            if not f: continue
            translated=frozenset((i,(a+shift[i])%q) for i,a in f)
            if translated==f:
                signed_euler+=(-1)**(len(f)-1)
        trace[(tx,ty)]=1-signed_euler
        if tx==ty==0:
            expected_trace=rank
        else:
            expected_trace=1-sum(q for s in shift if s==0)
        assert trace[(tx,ty)]==expected_trace,(q,n,tx,ty,trace[(tx,ty)],expected_trace)
    # Fourier-decompose the independently enumerated fixed-face character.
    dirs={(1,0),(0,1)}|{(1,a) for a in range(1,n-1)}
    assert len(dirs)==n
    for u,v in product(range(q),repeat=2):
        mult=sum(trace[(tx,ty)]*exp(-2j*pi*((u*tx+v*ty)%q)/q)
                 for tx,ty in product(range(q),repeat=2))/(q*q)
        in_direction=any((u,v)==((c*a)%q,(c*b)%q)
                         for a,b in dirs for c in range(1,q))
        expected=0 if (u,v)==(0,0) else n-2 if in_direction else n-1
        assert abs(mult-expected)<1e-7,(q,n,u,v,mult,expected)
    print('q=%d n=%d rows=%d faces=%d elementary_pairs=%d final_V=%d final_E=%d H1_rank=%d tested_group_elements=%d checked_characters=%d independent_enumeration=%s'%(
       q,n,len(rows),len(faces),pairs,len(graph_vertices),len(graph_edges),rank,q*q,q*q,full_independent))

if __name__=='__main__':
    verify(3,4,True)
    verify(5,4,True)
    verify(5,5,True)
    verify(5,6,True)
    verify(7,8,False)
    print('VERIFY_OK')
