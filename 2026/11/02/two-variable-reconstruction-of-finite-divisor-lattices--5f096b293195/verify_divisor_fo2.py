#!/usr/bin/env python3
"""Finite checks of rank/incomparability observables for products of chains.

All claims for arbitrary factor tuples are proved symbolically in RESULT.md;
these bounded checks neither prove the infinite theorem nor test historical priority.
"""
from itertools import product
from math import prod
from collections import defaultdict


def partitions(s, maximum=None):
    if s == 0:
        yield ()
        return
    for first in range(min(maximum or s, s), 0, -1):
        for rest in partitions(s-first, first):
            yield (first,) + rest


def values(exponents):
    return list(product(*(range(e+1) for e in exponents)))


def leq(a,b):
    return all(x <= y for x,y in zip(a,b))


def invariant(exponents):
    V=values(exponents)
    S=sum(exponents)
    atoms=[x for x in V if sum(x)==1]
    ranks={v:sum(v) for v in V}
    marks={}
    for a in atoms:
        incomparables=[ranks[z] for z in V if not leq(a,z) and not leq(z,a)]
        marks[a]=(S-max(incomparables)) if incomparables else S
    if len(atoms)>=2:
        expected=sorted(exponents)
        observed=sorted(marks.values())
        assert observed==expected,(exponents,observed,expected)
    else:
        assert list(marks.values())==[S]
    recovered=[]
    for e in range(1,S+1):
        class_atoms=[a for a in atoms if marks[a]==e]
        minimal=min(ranks[v] for v in V if all(leq(a,v) for a in class_atoms))
        assert minimal==exponents.count(e),(exponents,e,minimal)
        recovered.extend([e]*minimal)
    assert tuple(sorted(recovered,reverse=True))==exponents
    return len(V)


def modal_signatures(objects):
    # Noncounting vertex-color refinement: every color is defined by an FO^2 unary formula.
    structures=[]
    for exps in objects:
        V=values(exps)
        bins=[]
        for x in V:
            below=[];above=[];incomp=[]
            for j,y in enumerate(V):
                if x==y:continue
                if leq(y,x):below.append(j)
                elif leq(x,y):above.append(j)
                else:incomp.append(j)
            bins.append((below,above,incomp))
        structures.append(bins)
    colors=[[0]*len(structure) for structure in structures]
    iterations=0
    while True:
        lookup={};new=[]
        for bins,old in zip(structures,colors):
            cur=[]
            for i,rels in enumerate(bins):
                key=(old[i],tuple(frozenset(old[j] for j in direction) for direction in rels))
                if key not in lookup:lookup[key]=len(lookup)
                cur.append(lookup[key])
            new.append(cur)
        iterations+=1
        if sum(len(set(row)) for row in new) == sum(len(set(row)) for row in colors) and len(lookup)==len(set(c for row in colors for c in row)):
            colors=new;break
        colors=new
        if iterations>30:raise AssertionError('Unexpectedly slow refinement')
    spectra=defaultdict(list)
    for exps,clr in zip(objects,colors): spectra[frozenset(clr)].append(exps)
    collision=[v for v in spectra.values() if len(v)>1]
    assert not collision,collision
    return iterations,len(lookup)


def main():
    samples=[p for s in range(1,11) for p in partitions(s) if prod(v+1 for v in p)<=120]
    tested=0
    for p in samples:
        invariant(p);tested+=1
    # Width-one logic has no nontrivial atomic data on reflexive orders.
    # Explicit collision of size and order-height, resolved by atom fingerprints.
    a=(5,1,1,1);b=(3,3,2)
    assert sum(a)==sum(b)==8
    assert prod(x+1 for x in a)==prod(x+1 for x in b)==48
    invariant(a);invariant(b)
    small=[p for p in samples if sum(p)<=8 and prod(v+1 for v in p)<=80]
    iterations,ncolors=modal_signatures(small)
    print('FINITE_CHECK_OK')
    print('distinct_exponent_multisets_tested=',tested)
    print('max_total_exponent=10, max_poset_cardinality=120')
    print('same_height_same_size_pair=(5,1,1,1) versus (3,3,2): S=8, size=48')
    print('modal_FO2_lower_bound_structures=',len(small))
    print('modal_refinement_rounds=',iterations)
    print('modal_final_vertex_colors=',ncolors)
    print('modal_spectra_distinct=PASS')
    print('atom_fingerprints_and_multiplicities=PASS')

if __name__=='__main__':main()
