#!/usr/bin/env python3
"""Exact finite certificate for three-unordered-point Petersen homology."""
from collections import Counter
from itertools import permutations
from fractions import Fraction
import petersen3 as p

EXPECTED_DIMS = [680, 2400, 2700, 960]
EXPECTED_RANKS = [679, 1715, 960]
EXPECTED_CHARS = {
 (1,1,1,1,1):25,(2,1,1,1):-3,(2,2,1):1,
 (3,1,1):-2,(3,2):0,(4,1):1,(5,):0,
}
EXPECTED_MULT = {(3,2):1,(3,1,1):1,(2,2,1):2,(2,1,1,1):1}

def direct_trace(pi,k):
    pv,pe=p.permutation_on_edges(pi)
    out=0
    for gs,mon in p.ch[k]:
        if tuple(sorted(pe[e] for e in mon)) != mon:
            continue
        vimages=[pv[v] for v,e in gs]
        sign=(-1)**sum(vimages[i]>vimages[j] for i in range(k) for j in range(i+1,k))
        terms={():sign}
        for v,e in gs:
            vv=pv[v]
            opts=[(pe[e],1),(pe[p.BASE[v]],-1)]
            nxt={}
            for old,cf in terms.items():
                for edge,c in opts:
                    if edge!=p.BASE[vv]:
                        key=old+((vv,edge),)
                        nxt[key]=nxt.get(key,0)+cf*c
            terms=nxt
        target=tuple(sorted(gs))
        out+=sum(c for key,c in terms.items() if tuple(sorted(key))==target)
    return out

def graph_pentagon_rank():
    adj=[{b for a,b in p.E if a==v} | {a for a,b in p.E if b==v} for v in range(10)]
    cyc={}
    for x in permutations(range(10),5):
        if x[0]!=min(x) or x[1]>x[-1]:continue
        if all(x[(i+1)%5] in adj[x[i]] for i in range(5)):
            vec=[0]*len(p.E)
            for a,b in zip(x,x[1:]+x[:1]):
                e=p.EI[tuple(sorted((a,b)))]
                vec[e]+=1 if a<b else -1
            cyc[x]=vec
    piv={}
    for vec in cyc.values():
        d={i:Fraction(v) for i,v in enumerate(vec) if v}
        while d:
            j=min(d)
            if j not in piv:
                f=d[j];piv[j]={i:v/f for i,v in d.items()};break
            f=d[j]
            for i,v in piv[j].items():
                z=d.get(i,0)-f*v
                if z:d[i]=z
                elif i in d:del d[i]
    return len(cyc),len(piv)

def main():
    assert len(p.V)==10 and len(p.E)==15
    assert all(len(q)==3 for q in p.inc)
    assert [len(p.ch[k]) for k in range(4)]==EXPECTED_DIMS
    for k in (2,3):
        for c in p.ch[k]:
            d={}
            for ix,a in p.boundary(k,c):
                for j,b in p.boundary(k-1,p.ch[k-1][ix]):
                    d[j]=d.get(j,0)+a*b
            assert not any(d.values()),f'd_squared k={k} c={c}'
    print('DIFFERENTIAL_SQUARED_ZERO')
    for field in (3,5):
        ranks=[p.rank_sparse(k,field) for k in (1,2,3)]
        assert ranks==EXPECTED_RANKS,(field,ranks)
        print('MODULAR_RANKS',field,ranks)
    ncycle,rank=graph_pentagon_rank()
    assert ncycle==12 and rank==6,(ncycle,rank)
    print('PENTAGON_GRAPH_H1_SPAN',ncycle,rank)
    # Complete group check: direct signed chain traces vs cycle-index calculation,
    # and class functions under conjugacy for all 120 automorphisms.
    seen=Counter()
    for pi in permutations(range(5)):
        mu=tuple(sorted((len(c) for c in p.cycles(pi)),reverse=True))
        predicted,h1,supertrace=p.hom2_trace(pi)
        assert predicted==EXPECTED_CHARS[mu],(pi,mu,predicted)
        direct=sum((-1)**k*direct_trace(pi,k) for k in range(4))
        assert direct==supertrace,(pi,mu,direct,supertrace)
        assert supertrace==1-h1+predicted
        seen[mu]+=1
    assert len(seen)==7 and sum(seen.values())==120
    print('ALL_120_EQUIVARIANT_LEFSCHETZ_TRACES_OK')
    for lam in p.part(5):
        multiplicity=sum(Fraction(EXPECTED_CHARS[mu]*p.char(lam,mu),p.centralizer(mu)) for mu in EXPECTED_CHARS)
        assert multiplicity==EXPECTED_MULT.get(lam,0),(lam,multiplicity)
    for lam in p.part(5):
        for nu in p.part(5):
            ip=sum(Fraction(p.char(lam,mu)*p.char(nu,mu),p.centralizer(mu)) for mu in EXPECTED_CHARS)
            assert ip==int(lam==nu),(lam,nu,ip)
    print('FULL_S5_CHARACTER_ORTHOGONALITY_OK')
    assert sum((p.char(lam,(1,1,1,1,1))*mult for lam,mult in EXPECTED_MULT.items()))==25
    assert sum(Fraction(EXPECTED_CHARS[mu],p.centralizer(mu)) for mu in EXPECTED_CHARS)==0
    print('CHARACTER_DECOMPOSITION_AND_INVARIANTS_OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
