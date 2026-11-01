#!/usr/bin/env python3
"""Reproducible finite checks for dihedral three-cut homology character.
Uses only Python standard library; finite tests are not the infinite-family proof.
"""
from itertools import combinations
from math import gcd

def graph(n):
    N=2*n
    return {tuple(sorted((i,(i+1)%N))) for i in range(N)} | {tuple(sorted((i,(i+n)%N))) for i in range(n)}

def connected3(x,edge):
    return sum(tuple(sorted(pair)) in edge for pair in combinations(x,2)) >= 2

def trace_simplex(g,vertices):
    s=tuple(sorted(vertices))
    if {g[i] for i in s} != set(s): return 0
    t=[s.index(g[i]) for i in s]
    inversions=sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
    return -1 if inversions%2 else 1

def trace_formula(n,kind,a):
    R=2*n*n-8*n+1
    if kind=='r':return R if a==0 else (-1 if a%2 else 1)
    if n%2==0:return (n-3) if a%2==0 else (3-n)
    return (4-n) if a%2==0 else (n-2)

def fixed_chain_character(n,kind,a,faces):
    N=2*n
    g={i: ((i+a)%N if kind=='r' else (a-i)%N) for i in range(N)}
    t=[sum(trace_simplex(g,s) for s in faces[k]) for k in range(1,5)]
    h=1-t[0]+t[1]-t[2]+t[3]
    return h*trace_simplex(g,range(N)),t

def direct_cut_trace(n,kind,a,edge):
    N=2*n
    g={i: ((i+a)%N if kind=='r' else (a-i)%N) for i in range(N)}
    val=0
    for mask in range(1<<N):
        comp=[i for i in range(N) if not mask>>i&1]
        if not any(not connected3(tri,edge) for tri in combinations(comp,3)):
            continue
        face=[i for i in range(N) if mask>>i&1]
        val-=(-1)**len(face)*trace_simplex(g,face)
    return val

def mod2rank(boundaries):
    basis={}
    for v in boundaries:
        while v:
            k=v.bit_length()-1
            if k not in basis: basis[k]=v;break
            v ^= basis[k]
    return len(basis)

def check(n):
    N=2*n; E=graph(n)
    conn=[tuple(z) for z in combinations(range(N),3) if connected3(z,E)]
    square=[tuple(z) for z in combinations(range(N),4) if all(connected3(t,E) for t in combinations(z,3))]
    expected={tuple(sorted({i,(i+1)%N,(i+n)%N,(i+n+1)%N})) for i in range(n)}
    assert set(square)==expected,(n,len(square),len(expected))
    assert len(conn)==6*n,(n,len(conn))
    faces={1:[(i,) for i in range(N)],2:list(combinations(range(N),2)),3:conn,4:square}
    # Integer-boundary ranks are independently checked modulo two.
    edges=faces[2]; ed_idx={e:i for i,e in enumerate(edges)}
    tri_idx={z:i for i,z in enumerate(conn)}
    d2=[sum(1<<ed_idx[e] for e in combinations(t,2)) for t in conn]
    d3=[sum(1<<tri_idx[t] for t in combinations(s,3)) for s in square]
    assert mod2rank(d2)==5*n and mod2rank(d3)==n,(n,mod2rank(d2),mod2rank(d3))
    for kind in ('r','s'):
        for a in range(N):
            ch,terms=fixed_chain_character(n,kind,a,faces)
            expect=trace_formula(n,kind,a)
            assert ch==expect,(n,kind,a,ch,expect,terms)
            if n<=7:
                observed=direct_cut_trace(n,kind,a,E)
                assert observed==expect,(n,kind,a,observed,expect)
    return 2*N

if __name__=='__main__':
    total=0
    for n in range(5,17):
        total+=check(n)
    print('VERIFY_OK n=5..16; element cases=',total)
    print('DIRECT_CUT_LEFSCHETZ_OK n=5..7; full face enumeration')
    print('DUAL_BOUNDARY_RANK_OK mod2; proof supplies primitive integer minor')
