#!/usr/bin/env python3
"""Finite checks for the rank-two fluted extension-amalgamation lemma.

Structures have a unary predicate P and a binary predicate R. The theorem's
proof works for any finite relational signature; this check exercises one
nontrivial mixed-arity signature. No finite check certifies the universal claim.
"""
from itertools import product
from random import Random


def descriptors(P,R):
    n=len(P)
    return [(P[i], frozenset((P[j],R[i][j]) for j in range(n))) for i in range(n)]

def compatible(A,B):
    da,db=descriptors(*A),descriptors(*B)
    return all(any(p==q and support<=target for q,target in db)
               for p,support in da)

def extension(A,B):
    """Construct C extending A with its entire set of rank-two row types equal B's."""
    Pa,Ra=A; Pb,Rb=B; na,nb=len(Pa),len(Pb)
    da,db=descriptors(*A),descriptors(*B)
    if not compatible(A,B):
        raise ValueError('incompatible row supports')
    # Four binary/unary y-types are possible, so four B copies suffice.
    copies=4
    N=na+nb*copies
    P=Pa+Pb*copies
    R=[[0]*N for _ in range(N)]
    for i in range(na):
        for j in range(na):R[i][j]=Ra[i][j]
    for c in range(copies):
        for i in range(nb):
            for j in range(nb):R[na+c*nb+i][na+c*nb+j]=Rb[i][j]
    choose={t:next(i for i,v in enumerate(Pb) if v==t) for t in set(Pb)}
    # For each old source, first fill allowable types, then force every desired
    # type on an unused fresh copy of a target bearing its prescribed unary bit.
    for i in range(na):
        u,S=da[i]
        target=next(profile for v,profile in db if v==u and S<=profile)
        by_label={label:next(edge for v,edge in target if v==label)
                  for label in set(Pb)}
        for c in range(copies):
            for j in range(nb):R[i][na+c*nb+j]=by_label[Pb[j]]
        for c,(v,edge) in enumerate(sorted(target)):
            j=choose[v]
            R[i][na+c*nb+j]=edge
    # Each new row already realizes its entire B-support inside its own copy;
    # all newly introduced targets are assigned a type it already realizes.
    for c in range(copies):
        for j in range(nb):
            i=na+c*nb+j
            support=db[j][1]
            by_label={v:next(edge for z,edge in support if z==v)
                      for v in set(Pb)}
            for z in range(N):
                if z<na or not(na+c*nb<=z<na+(c+1)*nb):
                    R[i][z]=by_label[P[z]]
    return P,R

def all_structures(n):
    for bits in product((0,1),repeat=n+n*n):
        P=list(bits[:n]); R=[list(bits[n+i*n:n+(i+1)*n]) for i in range(n)]
        yield P,R

def check_pair(A,B):
    C=extension(A,B)
    Pa,Ra=A;Pc,Rc=C; na=len(Pa)
    assert Pa==Pc[:na]
    assert all(Ra[i][j]==Rc[i][j] for i in range(na) for j in range(na))
    assert set(descriptors(*B))==set(descriptors(*C))
    return True

def main():
    rng=Random(212729)
    structures=[s for n in (1,2) for s in all_structures(n)]
    checked=0
    for A in structures:
        for B in structures:
            if compatible(A,B):
                check_pair(A,B)
                checked+=1
    sampled=[s for s in all_structures(3)]
    for _ in range(6000):
        A=rng.choice(sampled);B=rng.choice(sampled)
        if compatible(A,B):
            check_pair(A,B);checked+=1
    print('PASS: extension-amalgamation lemma:',checked,'compatible ordered pairs')
    print('Exhaustive source and target sizes 1,2, plus 6000 fixed-seed trials on 3-world structures.')
    # A simple rank-2 formula whose truth is a function of the row-profile set.
    def modal_example(S):
        P,R=S
        return any(P[i] and all(R[i][j] or P[j] for j in range(len(P))) for i in range(len(P)))
    for _ in range(300):
        A=rng.choice(sampled);B=rng.choice(sampled)
        if compatible(A,B):
            # This particular formula is not extension preserved, and need not
            # transfer. But equality of rank-two descriptor sets implies it
            # agrees between B and its constructed C.
            C=extension(A,B)
            assert modal_example(B)==modal_example(C)
    print('PASS: representative nested rank-two fluted sentence invariance.')
if __name__=='__main__':main()
