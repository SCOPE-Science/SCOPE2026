#!/usr/bin/env python3
"""Exact finite graph census for the strict 0-or-2-neighbor rule.
Requires only Python 3 standard library. Run: python3 verify.py
"""
from itertools import permutations
from math import factorial

E8 = ((0,1),(0,2),(0,4),(0,5),(1,2),(2,3),(2,5),(3,4))
E9 = ((0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(1,4),(3,4),(4,5))


def pairs(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def encode(n, es):
    idx = {edge:k for k,edge in enumerate(pairs(n))}
    return sum(1<<idx[tuple(sorted(edge))] for edge in es)


def adjacency(n, bits):
    nbr = [0]*n
    for k,(i,j) in enumerate(pairs(n)):
        if (bits>>k)&1:
            nbr[i] |= 1<<j
            nbr[j] |= 1<<i
    return nbr


def is_equilibrium(nbr, state):
    return all(((state>>i)&1) == int((nbr[i]&state).bit_count() in (0,2))
               for i in range(len(nbr)))


def has_equilibrium(n,bits):
    nbr=adjacency(n,bits)
    return any(is_equilibrium(nbr,s) for s in range(1<<n))


def independent_equilibrium_test(n,bits,state):
    # Edge-by-edge neighbor tally; does not use bitmask intersections.
    active=[(state>>i)&1 for i in range(n)]
    counts=[0]*n
    for k,(i,j) in enumerate(pairs(n)):
        if bits&(1<<k):
            counts[i]+=active[j]
            counts[j]+=active[i]
    return all(active[i]==int(counts[i] in (0,2)) for i in range(n))


def orbit(n,edge_list):
    result=set()
    for p in permutations(range(n)):
        result.add(encode(n,[(p[i],p[j]) for (i,j) in edge_list]))
    return result


def main():
    misses_by_n = {}
    for n in range(1,7):
        misses={mask for mask in range(1<<(n*(n-1)//2))
                if not has_equilibrium(n,mask)}
        misses_by_n[n]=misses
        print('n=%d graphs=%d no_equilibrium=%d' %
              (n,1<<(n*(n-1)//2),len(misses)))
        if n<6:
            assert not misses
    assert len(misses_by_n[6])==300
    orbit8=orbit(6,E8)
    orbit9=orbit(6,E9)
    assert len(orbit8)==180 and len(orbit9)==120
    assert not (orbit8 & orbit9)
    assert misses_by_n[6] == orbit8 | orbit9
    assert factorial(6)//len(orbit8)==4
    assert factorial(6)//len(orbit9)==6
    assert all(x.bit_count()==8 for x in orbit8)
    assert all(x.bit_count()==9 for x in orbit9)
    # Truly separate edge-based evaluation on every state of both witnesses,
    # plus selected graph labels from each orbit and from its complement.
    probes = {encode(6,E8),encode(6,E9)}
    probes.update(sorted(orbit8)[:20]); probes.update(sorted(orbit9)[:20])
    probes.update(range(0,1<<15,257))
    for g in probes:
        nbr=adjacency(6,g)
        for s in range(64):
            assert is_equilibrium(nbr,s)==independent_equilibrium_test(6,g,s)
    print('orbits=180+120, automorphisms=4,6, edges=8,9')
    print('independent edge-by-edge checks:',len(probes)*64)
    print('CERTIFICATE_OK')

if __name__=='__main__':
    main()
