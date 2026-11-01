#!/usr/bin/env python3
"""Independent finite checks for the crown dominance/neighborhood theorem.
No external packages are required. Run with Python 3.9 or newer.
"""
from itertools import combinations

def build(n):
    m = 2*n
    allmask = (1 << m) - 1
    # In the crown graph, a_i is adjacent to b_j exactly when i != j.
    crown_neigh = [sum(1 << (n+j) for j in range(n) if j != i)
                   for i in range(n)]
    crown_neigh += [sum(1 << j for j in range(n) if j != i)
                    for i in range(n)]
    # Open neighbors in the complement graph are complements of closed crown neighborhoods.
    complement_neigh = [allmask ^ (crown_neigh[v] | (1 << v))
                         for v in range(m)]
    neighborhood = {s for s in range(1, 1 << m)
                    if any((s & ~nb) == 0 for nb in complement_neigh)}
    dominance = {s for s in range(1, 1 << m)
                 if all((crown_neigh[v] & (allmask ^ s)) != 0
                        for v in range(m) if s & (1 << v))}
    # Exact combinatorial Alexander duality at the level of all subsets.
    assert all(((allmask ^ s) not in (dominance | {0})) == (s in (neighborhood | {0}))
               for s in range(1 << m))
    # Decompose the open-neighborhood complex as P union Q.
    A = (1 << n) - 1
    B = allmask ^ A
    P = {s for s in neighborhood if ((s & B).bit_count() == 0 and s != A)
         or any((s & ~((A ^ (1 << i)) | (1 << (n+i)))) == 0
                for i in range(n))}
    Q = {s for s in neighborhood if ((s & A).bit_count() == 0 and s != B)
         or any((s & ~((B ^ (1 << (n+i))) | (1 << i))) == 0
                for i in range(n))}
    assert P | Q == neighborhood
    intersection = P & Q
    crown_graph_faces = {1 << v for v in range(m)}
    crown_graph_faces |= {(1 << i) | (1 << (n+j)) for i in range(n)
                          for j in range(n) if i != j}
    assert intersection == crown_graph_faces
    assert len(crown_graph_faces) == 2*n+n*(n-1)
    return neighborhood, dominance, P, Q

def homology_mod_two(faces):
    by_dim = {}
    for s in faces:
        d = s.bit_count() - 1
        by_dim.setdefault(d, []).append(s)
    ranks = {}
    for d in range(1, max(by_dim)+1):
        lower = {s: j for j,s in enumerate(sorted(by_dim[d-1]))}
        pivots = {}
        for s in sorted(by_dim[d]):
            column = 0
            t=s
            while t:
                v=t & -t
                t-=v
                column ^= 1 << lower[s^v]
            while column:
                k=column.bit_length()-1
                if k in pivots:
                    column^=pivots[k]
                else:
                    pivots[k]=column
                    break
        ranks[d]=len(pivots)
    return {d:len(faces_d)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)
            for d, faces_d in sorted(by_dim.items())}

def expected_nb(n):
    b={2:n*n-3*n+1,n-2:2}
    if n==4:
        return {2:7}
    return b

def expected_dom(n):
    b={2*n-5:n*n-3*n+1,n-1:2}
    if n==4:
        return {3:7}
    return b

def positives(b):
    return {k:v for k,v in b.items() if v}

def main():
    for n in range(4,9):
        nb,dominance,P,Q=build(n)
        bn=positives(homology_mod_two(nb))
        assert bn==expected_nb(n),(n,bn)
        # Computing complete direct chains of the dual is more expensive:
        # use direct boundary matrices for n=4,5,6 only.
        bd=None
        if n<=6:
            bd=positives(homology_mod_two(dominance))
            assert bd==expected_dom(n),(n,bd)
        print(f'n={n} neighborhood_faces={len(nb)} P={len(P)} Q={len(Q)} '
              f'intersection={len(P&Q)} neighborhood_mod2={bn} '
              f'dominance_faces={len(dominance)} dominance_mod2={bd}',flush=True)
    print('CROWN_NEIGHBORHOOD_DOMINANCE_FINITE_CHECKS_PASS')

if __name__=='__main__':
    main()
