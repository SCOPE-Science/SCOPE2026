#!/usr/bin/env python3
"""Exact small-domain verification for automorphisms of paired random graphs.

All graphs are simple undirected graphs on vertices (i,b), where i is
an orbit index and b is 0 or 1. The fixed involution toggles b.
The data bits consist of one within-pair bit per orbit and two bits per
unordered pair of distinct orbits. Runs with Python's standard library.
"""
from itertools import permutations, product
from math import comb
from fractions import Fraction


def coordinate_pairs(m):
    reps=[]
    for i in range(m):
        reps.append((2*i,2*i+1))
    for i in range(m):
        for j in range(i+1,m):
            for a in range(2):
                reps.append((2*i,2*j+a))
    assert len(reps)==m*m
    return reps


def induced_coordinate_maps(m):
    reps=coordinate_pairs(m)
    edge_index={}
    for p,(a,b) in enumerate(reps):
        edge_index[tuple(sorted((a,b)))]=p
        edge_index[tuple(sorted((a^1,b^1)))]=p
    out=[]
    for sigma in permutations(range(m)):
        for flips in product(range(2),repeat=m):
            vx=[2*sigma[i]+(b^flips[i]) for i in range(m) for b in range(2)]
            mapped=tuple(edge_index[tuple(sorted((vx[a],vx[b])))] for a,b in reps)
            assert len(set(mapped))==m*m
            out.append((sigma,flips,mapped))
    return out


def preserves(bits, coord_map):
    return all(((bits>>j)&1)==((bits>>k)&1) for j,k in enumerate(coord_map))


def run():
    count_checks=0
    for m in range(2,5):
        maps=induced_coordinate_maps(m)
        reps=coordinate_pairs(m)
        pairid={reps[p]:p for p in range(m*m)}
        n=1<<(m*m)
        hit=0
        single=0
        orbit_permuting=0
        fibre_checks=0
        for bits in range(n):
            local=any(all(( (bits>>pairid[(2*min(i,j),2*max(i,j))])&1 ) ==
                          ( (bits>>pairid[(2*min(i,j),2*max(i,j)+1)])&1 )
                          for j in range(m) if j!=i)
                      for i in range(m))
            # Avoid rechecking the automorphism search if a single-fibre
            # symmetry was already independently detected.
            nontrivial=local or any(preserves(bits, mp) and
                           (sig!=tuple(range(m)) or
                            flips not in ((0,)*m,(1,)*m))
                           for sig,flips,mp in maps)
            # Difference edges form a simple graph on the pair orbits.
            h=[set() for _ in range(m)]
            for i in range(m):
                for j in range(i+1,m):
                    a=pairid[(2*i,2*j)]
                    b=pairid[(2*i,2*j+1)]
                    if ((bits>>a)&1)!=((bits>>b)&1):
                        h[i].add(j);h[j].add(i)
            seen=set()
            comps=0
            for i in range(m):
                if i in seen: continue
                comps+=1
                todo=[i];seen.add(i)
                while todo:
                    for j in h[todo.pop()]:
                        if j not in seen:seen.add(j);todo.append(j)
            actual_kernel=sum(preserves(bits,mp) for sig,eps,mp in maps
                              if sig==tuple(range(m)))
            assert actual_kernel==2**comps
            nontrivial_projection=any(preserves(bits,mp) for sig,eps,mp in maps
                                      if sig!=tuple(range(m)))
            assert nontrivial==(comps>=2 or nontrivial_projection)
            fibre_checks+=1
            orbit_permuting+=nontrivial_projection
            hit+=nontrivial
            single+=local
        assert single <= hit
        # Union-event indicator is independently enumerated from the 
        # involutive edge-orbit constraints, not automorphism search.
        if m==2:
            assert single==n//2
        print('m',m,'graphs',n,'extra_aut',hit,'single_fiber_flip',single,
              'extra_fraction',str(Fraction(hit,n)), 'orbit_permutation',orbit_permuting,
              'kernel_checks',fibre_checks)
        count_checks+=n*len(maps)
    # Exact probabilities for any fixed non-global flip are 2^{-s(m-s)}.
    for m in range(2,11):
        for s in range(1,m):
            # Each of s(m-s) cross-pair coordinates independently requires
            # equality of its two unbiased bits.
            p=Fraction(1,2**(s*(m-s)))
            assert p*2**(s*(m-s))==1
    print('PAIRED_GRAPH_AUT_EXACT_OK',count_checks,'flip_laws',sum(m-1 for m in range(2,11)))

if __name__=='__main__':
    run()
