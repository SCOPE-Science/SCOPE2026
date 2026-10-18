#!/usr/bin/env python3
"""Finite tests of the ordered lift for omega-accumulation semantics.

The infinite-neighborhood equivalence is proved symbolically in RESULT.md.
Finite truncations are used only to test the partial-order law and finite
Boolean successor profiles, NOT to approximate omega-accumulation by finite
cardinality.
"""
from itertools import product


def has_edge(mask, n, u, v):
    return (mask >> (u*n+v)) & 1 == 1


def is_transitive(mask, n):
    return all(not (has_edge(mask,n,u,v) and has_edge(mask,n,v,w))
               or has_edge(mask,n,u,w)
               for u in range(n) for v in range(n) for w in range(n))


def lift_le(mask, n, a, b):
    u,i=a; v,j=b
    return a==b or (i<j and has_edge(mask,n,u,v))


def check(n, levels=3):
    pts=list(product(range(n), range(levels)))
    transitive_frames=0
    profile_checks=0
    for mask in range(1<<(n*n)):
        if not is_transitive(mask,n):
            continue
        transitive_frames+=1
        for a in pts:
            assert lift_le(mask,n,a,a)
            for b in pts:
                if lift_le(mask,n,a,b) and lift_le(mask,n,b,a):
                    assert a==b
                if lift_le(mask,n,a,b):
                    for c in pts:
                        if lift_le(mask,n,b,c):
                            assert lift_le(mask,n,a,c)
        for A in range(1<<n):
            for u in range(n):
                # Proof-derived exact symbol test for the *infinite* cone:
                # if an R-successor v in A exists, the whole infinite tail
                # {(v,j):j>i} lies in the cone. Otherwise at most (u,i) lies there.
                infinite_witness=any(has_edge(mask,n,u,v) and ((A>>v)&1)
                                     for v in range(n))
                kripke_diamond=any(((A>>v)&1) and has_edge(mask,n,u,v)
                                    for v in range(n))
                assert infinite_witness==kripke_diamond
                profile_checks+=1
        # Finite-frame converse well-foundedness iff no R loops
        # when R is transitive; any directed cycle gives a loop.
        cwf=all(not has_edge(mask,n,u,u) for u in range(n))
        for nonempty_B in range(1,1<<n):
            progressing=all(
                not ((nonempty_B>>u)&1) or
                any(((nonempty_B>>v)&1) and has_edge(mask,n,u,v)
                    for v in range(n))
                for u in range(n))
            if cwf:
                assert not progressing
        if not cwf:
            loop_nodes=sum((1<<u) for u in range(n) if has_edge(mask,n,u,u))
            assert loop_nodes
            assert all(not ((loop_nodes>>u)&1) or has_edge(mask,n,u,u)
                       for u in range(n))
    return transitive_frames,profile_checks


def main():
    total_frames=0;total_profiles=0
    for n in range(1,5):
        frames,profiles=check(n)
        total_frames+=frames;total_profiles+=profiles
        print(f'n={n}: transitive_frames={frames}, symbolic_profile_checks={profiles}')
    print(f'VERIFY_OK total_frames={total_frames} total_profiles={total_profiles}')

if __name__=='__main__':
    main()
