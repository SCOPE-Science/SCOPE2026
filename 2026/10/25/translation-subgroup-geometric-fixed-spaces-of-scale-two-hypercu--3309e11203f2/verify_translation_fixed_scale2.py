#!/usr/bin/env python3
"""Finite checks for translation-fixed Vietoris--Rips complexes of Boolean cubes.
Only checks finite instances; the mathematical proof is separate.
"""
from itertools import combinations

def weight(x): return x.bit_count()

def span(gs):
    z={0}
    for g in gs: z |= {x^g for x in list(z)}
    return frozenset(z)

def all_short_subgroups(n):
    vs=[v for v in range(1,1<<n) if weight(v)<=2]
    hs={span(())}
    for d in (1,2,3):
        for gs in combinations(vs,d):
            h=span(gs)
            if max(map(weight,h))<=2: hs.add(h)
    return hs

def orbit_graph(n,h):
    seen=set(); orbits=[]
    for x in range(1<<n):
        if x in seen:continue
        o=frozenset(x^a for a in h)
        assert len(o)==len(h)
        seen.update(o);orbits.append(o)
    edges=set()
    for a in range(len(orbits)):
        for b in range(a+1,len(orbits)):
            if all(weight(x^y)<=2 for x in orbits[a] for y in orbits[b]):
                edges.add((a,b))
    return orbits,edges

def canon_coset_coord(x,v,n):
    supp=[i for i in range(n) if v & (1<<i)]
    if len(supp)==1:
        j=supp[0]
        return sum(((x>>i)&1)<<k for k,i in enumerate(i for i in range(n) if i!=j))
    if len(supp)==2:
        i,j=supp
        others=[a for a in range(n) if a not in (i,j)]
        z=sum(((x>>p)&1)<<k for k,p in enumerate(others))
        a=((x>>i)^(x>>j))&1
        return (a^ (z.bit_count()&1)) | (z<<1)
    raise ValueError(v)

def verify():
    tests=0;types={}
    for n in range(2,7):
        hh=all_short_subgroups(n)
        for h in hh:
            if len(h)==1: continue
            orbits, edges=orbit_graph(n,h)
            assert len(orbits)==(1<<n)//len(h)
            if len(h)==2:
                v=next(iter(h-{0}))
                assert weight(v) in (1,2)
                coords=[canon_coset_coord(next(iter(o)),v,n) for o in orbits]
                assert len(set(coords))==len(orbits)
                expected={(i,j) for i in range(len(orbits)) for j in range(i+1,len(orbits))
                          if weight(coords[i]^coords[j])==1}
                assert edges==expected,(n,v,edges,expected)
                assert len(edges)==(n-1)*(1<<(n-2))
                types['rank1_weight'+str(weight(v))]=types.get('rank1_weight'+str(weight(v)),0)+1
            elif len(h)==4:
                assert all(weight(v)<=2 for v in h)
                assert not edges,(n,h,edges)
                types['rank2']=types.get('rank2',0)+1
            else:
                raise AssertionError((n,h))
            tests+=1
        for v in range(1,1<<n):
            if weight(v)>=3:
                assert weight(v)>2
                # Every orbit of <v> contains a pair at distance > 2.
                assert all(weight(x^(x^v))>2 for x in range(1<<n))
        print('n=',n,'short_subgroups=',len(hh)-1)
    print('TRANSLATION_FIXED_RIPS2_VERIFIED',tests,'nontrivial_subgroups',types)

if __name__=='__main__':verify()
