#!/usr/bin/env python3
"""Direct finite-field checks for graph-realization square-zero loci.
Run python3 verify.py. Uses only the Python standard library.
"""
from itertools import product
from math import comb


def verify(n, edges, q):
    """Brute force all elements of a graph algebra over a prime field."""
    e = tuple(sorted(tuple(sorted(edge)) for edge in edges))
    assert all(0 <= i < j < n for i, j in e)
    m = len(e)
    dim = 1+n+m
    # Basis: 1, x_0,...,x_{n-1}, z_e for each edge.
    multiplication = {}
    for i in range(dim):
        multiplication[0,i] = i
        multiplication[i,0] = i
    for z,(i,j) in enumerate(e):
        multiplication[1+i,1+j] = 1+n+z
    for a in range(dim):
        for b in range(dim):
            for c in range(dim):
                ab = multiplication.get((a,b))
                bc = multiplication.get((b,c))
                left = multiplication.get((ab,c)) if ab is not None else None
                right = multiplication.get((a,bc)) if bc is not None else None
                assert left == right, (n,e,a,b,c,left,right)
    count = 0
    for v in product(range(q), repeat=dim):
        square=[0]*dim
        for (a,b),out in multiplication.items():
            square[out] = (square[out] + v[a]*v[b])%q
        if not any(square):
            count += 1
    independent = sum(1 for choices in product(range(q),repeat=n)
                      if all(choices[i]*choices[j] == 0 for i,j in e))
    expected = q**m * independent
    assert count == expected, (n,e,q,count,expected)
    return count


def run():
    tally=0
    # Every graph on at most four labeled vertices over F_2.
    for n in range(5):
        possible=[(i,j) for i in range(n) for j in range(i+1,n)]
        for mask in range(1<<len(possible)):
            edges=[edge for k,edge in enumerate(possible) if mask>>k & 1]
            verify(n,edges,2)
            tally += 1
    # Selected configurations over odd-characteristic fields.
    samples=[(2,[(0,1)]), (3,[(0,1),(1,2)]),
             (3,[(0,1),(0,2),(1,2)]),
             (4,[(0,1),(1,2),(2,3)]),
             (4,[(0,1),(1,2),(2,3),(0,3)]),
             (4,[(i,j) for i in range(4) for j in range(i+1,4)])]
    for n,e in samples:
        verify(n,e,3)
        tally+=1
    # Independent-set polys and component dimensions for P_3.
    n=3; e={(0,1),(1,2)}
    sets=[frozenset(i for i in range(n) if (mask>>i)&1)
          for mask in range(1<<n)
          if all(not (mask>>i & 1 and mask>>j & 1) for i,j in e)]
    maxi=[s for s in sets if not any(s<t for t in sets)]
    assert sorted(map(len,maxi))==[1,2]
    assert sum(1 for s in sets if len(s)==1)==3
    assert sum(1 for s in sets if len(s)==2)==1
    print('VERIFY_OK', 'graph_instances', tally, 'P3_components',sorted(map(len,maxi)))

if __name__=='__main__':run()
