#!/usr/bin/env python3
"""Exact finite checks of coprime-residue avalanche complexes and their homology.

Uses only the Python standard library. Tests actual parallel chip-firing,
full maximal-facet equality under modular relabeling, and independent
GF(2) boundary-matrix ranks on computationally feasible cases.
"""
from collections import defaultdict
from itertools import combinations
from math import gcd


def initial_support(n, k, a, complement=False):
    r={j for j in range(n) if j%k==a}
    return set(range(n))-r if complement else r


def firing_facets(n, support):
    initial=[int(j in support) for j in range(n)]
    c=initial.copy()
    facets=set()
    for _ in range(n):
        active={j for j in range(n) if c[j]>=1}
        facets.add(frozenset(active))
        next_c=c.copy()
        for j in active:
            next_c[j]-=1
            next_c[(j+1)%n]+=1
        c=next_c
    assert c==initial,('not periodic',n,support)
    return facets


def cyclic_arcs(n,length):
    return {frozenset((i+j)%n for j in range(length)) for i in range(n)}


def face_levels(facets):
    d=defaultdict(set)
    for F in facets:
        v=sorted(F)
        for r in range(1,len(v)+1):
            d[r-1].update(combinations(v,r))
    return {i:sorted(x) for i,x in d.items()}


def binary_rank(columns):
    pivot={}
    for x in columns:
        while x:
            b=x.bit_length()-1
            if b in pivot: x^=pivot[b]
            else: pivot[b]=x; break
    return len(pivot)


def reduced_gf2_betti(faces):
    # augmented chain complex: boundary rank C_0 -> C_{-1} is one
    ranks={-1:1}
    for d in sorted(faces):
        if d==0:continue
        row={v:i for i,v in enumerate(faces[d-1])}
        columns=[]
        for v in faces[d]:
            col=0
            for i in range(len(v)):
                col ^= 1<<row[v[:i]+v[i+1:]]
            columns.append(col)
        ranks[d-1]=binary_rank(columns)
    b={d:len(faces[d])-ranks.get(d-1,0)-ranks.get(d,0) for d in faces}
    assert all(x>=0 for x in b.values())
    return {d:x for d,x in b.items() if x}


def check(n,k,a,comp=False,homology=False):
    s=initial_support(n,k,a,comp)
    assert len(s)>1 and len(s)<n-1
    f=firing_facets(n,s)
    inv=pow(k,-1,n)
    transported={frozenset(inv*x%n for x in facet) for facet in f}
    expected=cyclic_arcs(n,len(s))
    assert transported==expected,(n,k,a,comp,'facet-model')
    if homology:
        b=reduced_gf2_betti(face_levels(f))
        q,t=divmod(n,k)
        delta=int(a<t)
        L=q+delta
        transition=q+t-(delta+1)*(k-1)
        if not comp:
            prediction={1:1}
        elif transition>0:
            prediction={2*k-3:1}
        elif transition==0:
            prediction={2*k-4:L}
        else:
            prediction=None
        if prediction is not None:
            assert b==prediction,(n,k,a,comp,b,prediction)
    return len(f)


def run():
    checks=0
    for n in range(5,71):
        for k in range(2,min(10,n)):
            if gcd(n,k)!=1: continue
            for a in range(k):
                for comp in (False,True):
                    if 1<len(initial_support(n,k,a,comp))<n-1:
                        check(n,k,a,comp)
                        checks+=1
    gfcases=[]
    for n,k in [(5,2),(7,2),(9,2),(11,2),(13,2),(8,3),(10,3),(13,3),(14,3),(9,4)]:
        for a in range(k):
            for comp in (False,True):
                check(n,k,a,comp,homology=True)
                gfcases.append((n,k,a,comp))
    n=5
    assert firing_facets(n,initial_support(n,2,1))=={frozenset({j,(j+2)%n}) for j in range(n)}
    print('VERIFY_OK')
    print('exact_firing_and_nerve_cases=',checks)
    print('independent_mod2_homology_cases=',len(gfcases))
    assert reduced_gf2_betti(face_levels(firing_facets(8,initial_support(8,3,0,True))))=={2:3}
    assert reduced_gf2_betti(face_levels(firing_facets(8,initial_support(8,3,2,True))))=={3:1}
    print('boundary_n8_k3_3spheres2_vs_1sphere3=TRUE')
    print('first_counterexample_n5_k2_S1=TRUE')

if __name__=='__main__':run()
