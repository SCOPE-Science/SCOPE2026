#!/usr/bin/env python3
"""Exact depth-four separators for disjointness graphs of triples.

Uses integer orbit partitions rather than an exponential list of graph-tuples.
All tuples include repeated selected vertices. No floating point or randomness.
"""
from itertools import combinations, product
from functools import lru_cache

K = 3


def atomic(cell, t):
    """Complete equality/adjacency table of t selected 3-sets."""
    val=[]
    for i in range(t):
        for j in range(i+1,t):
            meet=sum(cell[m] for m in range(1<<t) if (m>>i)&1 and (m>>j)&1)
            val.append((int(meet==K), int(meet==0)))
    return tuple(val)


def triple_cells(n):
    """All S_n-orbits of ordered triples of 3-subsets of [n]."""
    for a,b,c,d,e,f in product(range(4),repeat=6):
        g=3-a-c-e
        if not 0<=g<=3 or b+c+f+g!=3 or d+e+f+g!=3:
            continue
        u=a+b+c+d+e+f+g
        if u<=n:
            yield (n-u,a,b,c,d,e,f,g)


@lru_cache(None)
def allocations(c,needed=K):
    """Every possible count split of a new 3-set across old Venn cells."""
    if not c:
        return ((),) if needed==0 else ()
    return tuple((v,)+tail for v in range(min(c[0],needed)+1)
                 for tail in allocations(c[1:],needed-v))


def triple_profile(c):
    """Atomic triple type + all atomic four-tuple types from one extension."""
    extensions=set()
    for select in allocations(c):
        cells4=tuple(c[m]-select[m] for m in range(8)) + tuple(select[m] for m in range(8))
        extensions.add(atomic(cells4,4))
    return atomic(c,3),frozenset(extensions)


def spectrum(n):
    return frozenset(triple_profile(c) for c in triple_cells(n))


def explicit_spectrum(n):
    """Independent graph-based confirmation for the three smallest orders."""
    vertices=list(combinations(range(n),3))
    q=len(vertices)
    edges=[[int(not set(a).intersection(b)) for b in vertices] for a in vertices]
    out=set()
    for i in range(q):
        for j in range(q):
            for k in range(q):
                a=((int(i==j),edges[i][j]),
                   (int(i==k),edges[i][k]),
                   (int(j==k),edges[j][k]))
                b=frozenset(
                    ((int(i==j),edges[i][j]),(int(i==k),edges[i][k]),
                     (int(i==w),edges[i][w]),(int(j==k),edges[j][k]),
                     (int(j==w),edges[j][w]),(int(k==w),edges[k][w]))
                    for w in range(q))
                out.add((a,b))
    return frozenset(out)


def main():
    ns=range(6,13)
    spectra={n:spectrum(n) for n in ns}
    for n in ns:
        print('SPECTRUM',n,len(spectra[n]),'TRIPLE_ORBITS',len(set(triple_cells(n))))
    for n in ns:
        differences=[len(spectra[n]-spectra[m]) if m!=n else 0 for m in ns]
        print('EXCLUSIVE',n,*differences)
    assert all(spectra[n]!=spectra[m] for n in ns for m in ns if n!=m)
    for n in (6,7,8):
        assert spectra[n]==explicit_spectrum(n),f'independent enumeration disagrees at n={n}'
        print('DIRECT_GRAPH_AGREEMENT',n,len(spectra[n]))
    assert spectrum(12)==spectrum(13)
    print('ORBIT_CERTIFICATE_OK')
    print('STABILIZATION_BOUND_12_FROM_FOUR_MOVE_UNION_ARGUMENT')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
