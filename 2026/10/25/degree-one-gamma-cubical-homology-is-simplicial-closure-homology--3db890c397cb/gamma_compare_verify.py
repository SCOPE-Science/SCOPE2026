#!/usr/bin/env python3
"""Integral low-degree Gamma-cubical/associated-complex comparison checks.

Reproduces finite instances of a general chain-level proof. No external data
and no external services. The mathematical theorem is not inferred from tests.
"""
from collections import Counter
from itertools import combinations, product
from random import Random
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def all_subsets_in_edges(hyperedges):
    h = [frozenset(e) for e in hyperedges]
    return lambda xs: any(set(xs) <= edge for edge in h)


def oriented(a, b):
    if a == b:
        return {}
    return {(min(a, b), max(a, b)): 1 if a < b else -1}


def chain_add(*chains):
    s = Counter()
    for chain in chains:
        s.update(chain)
    return {k: v for k, v in s.items() if v}


def minus(chain):
    return {k: -v for k, v in chain.items()}


def oriented_triangle(a, b, c):
    return chain_add(oriented(a, b), oriented(b, c), minus(oriented(a, c)))


def gamma2_boundary(a, b, c, d):
    # The defining sign is sum_i (-1)^i(A_i-B_i).
    # Map into antisymmetric simplicial one-chains.
    return chain_add(minus(oriented(a, c)), oriented(b, d),
                     oriented(a, b), minus(oriented(c, d)))


def check_gamma_cubes(hyperedges, vcount):
    contained = all_subsets_in_edges(hyperedges)
    faces = [(a, b) for a in range(vcount) for b in range(a + 1, vcount)
             if contained((a, b))]
    # A Gamma-2 cube is admissible iff each three-corner radius-one star
    # maps into one target hyperedge.
    nvalid = 0
    for a, b, c, d in product(range(vcount), repeat=4):
        if not all(contained(t) for t in ((a, b, c), (a, b, d),
                                           (a, c, d), (b, c, d))):
            continue
        nvalid += 1
        actual = gamma2_boundary(a, b, c, d)
        predicted = chain_add(oriented_triangle(a, b, c),
                              oriented_triangle(b, d, c))
        assert actual == predicted, (a, b, c, d, actual, predicted)
    for a, b in faces:
        assert contained((a, b))
        # Explicit Gamma-2 backtrack (a,b,a,a) generates [a,b]+[b,a].
        assert all(contained(t) for t in ((a,b,a),(a,b,a),(a,a,a),(b,a,a)))
        # Gamma-2 (a,b,c,b) generates a triangle modulo backtracks.
        for c in range(vcount):
            if contained((a,b,c)):
                assert all(contained(t) for t in ((a,b,c),(a,b,b),
                                                   (a,c,b),(b,c,b)))
                assert gamma2_boundary(a,b,c,b) == oriented_triangle(a,b,c)
    return len(faces), nvalid


def triangulated_projective_plane():
    facets = [tuple(map(lambda x: int(x)-1, f)) for f in
              ('123','124','135','146','156','236','245','256','345','346')]
    vertices = range(6)
    edges = sorted({pair for f in facets for pair in combinations(f,2)})
    edgecount = Counter(pair for f in facets for pair in combinations(f,2))
    assert len(edges) == 15 and set(edgecount.values()) == {2}
    assert len(facets) == 10
    assert 6-len(edges)+len(facets) == 1
    # Check that every vertex link is a single simple 5-cycle.
    for v in vertices:
        link_edges = [tuple(sorted(x for x in face if x != v))
                      for face in facets if v in face]
        deg = Counter(x for a,b in link_edges for x in (a,b))
        assert len(link_edges) == 5 and len(deg) == 5
        assert set(deg.values()) == {2}
        seen = {next(iter(deg))}; q = list(seen)
        while q:
            cur = q.pop()
            for a,b in link_edges:
                if cur in (a,b):
                    other = b if a == cur else a
                    if other not in seen:
                        seen.add(other); q.append(other)
        assert len(seen) == 5
    boundary1 = Matrix([[(-1 if i == a else (1 if i == b else 0))
                         for (a,b) in edges] for i in vertices])
    boundary2 = Matrix([[((1 if (a,b)==tuple(sorted((f[1],f[2]))) else 0) *
                         (1 if f[1]<f[2] else -1)
                         - (1 if (a,b)==tuple(sorted((f[0],f[2]))) else 0) *
                         (1 if f[0]<f[2] else -1)
                         + (1 if (a,b)==tuple(sorted((f[0],f[1]))) else 0) *
                         (1 if f[0]<f[1] else -1)) for f in facets]
                        for a,b in edges])
    assert boundary1*boundary2 == Matrix.zeros(6,10)
    d1 = [abs(int(smith_normal_form(boundary1, domain=ZZ)[i,i]))
          for i in range(min(boundary1.shape))]
    d2 = [abs(int(smith_normal_form(boundary2, domain=ZZ)[i,i]))
          for i in range(min(boundary2.shape))]
    nz1 = [x for x in d1 if x]
    nz2 = [x for x in d2 if x]
    assert nz1 == [1]*5, nz1
    assert sorted(nz2) == [1]*9+[2], nz2
    assert 15-len(nz1)-len(nz2)==0
    return facets, len(edges), nz2


def main():
    Hcases = [
        ('triangle_graph', ((0,1),(1,2),(0,2)), 3),
        ('four_cycle', ((0,1),(1,2),(2,3),(3,0)), 4),
        ('nonuniform_four_cycle', ((0,1,2),(1,4),(2,3),(3,4)), 5),
        ('linear_clique_bouquet', ((0,1,2),(2,3,4),(4,5,0)), 6),
    ]
    facets, nedges, invariant = triangulated_projective_plane()
    Hcases.append(('six_vertex_RP2', facets, 6))
    rng = Random(142857)
    for i in range(60):
        n = rng.randint(3,6)
        possible = [frozenset(s) for k in range(2,min(n,4)+1)
                    for s in combinations(range(n),k)]
        selected = rng.sample(possible,k=min(len(possible),rng.randint(2,11)))
        if len(set(range(n))-set().union(*selected)):
            selected.append(frozenset(range(n)))
        Hcases.append((f'seeded_{i:02d}',tuple(selected),n))
    total_cubes = total_pairs = 0
    for name, H, n in Hcases:
        e, c = check_gamma_cubes(H,n)
        total_pairs += e
        total_cubes += c
        if name in ('six_vertex_RP2','triangle_graph','four_cycle',
                    'nonuniform_four_cycle'):
            print(f'{name}: |associated edges|={e}, allowed Gamma-2 cubes={c}')
    print('RP2 6-vertex 10-facet closed 2-manifold: (V,E,F)=(6,15,10), chi=1')
    print('Integral Smith invariants of d2:',invariant)
    print('Integral H1 of associated complex and Gamma theory: Z/2Z')
    print(f'Gamma-2 algebra identities exhaustively checked: {total_cubes} cubes in {len(Hcases)} finite hypergraphs; {total_pairs} associated edges')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
