"""Finite exact regression tests for a crosspolytope covering theorem.

The unbounded chromatic-number input is a published theorem, not proved by
these finite checks; the mathematical proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def l1(u, v):
    return sum(abs(a-b) for a, b in zip(u, v))


def check_witnesses(d):
    r = F(d-1, d)
    vertices = [tuple(s if i==j else 0 for i in range(d))
                for j in range(d) for s in (-1, 1)]
    facets = [tuple(F(s, d) for s in signs)
              for signs in product((-1,1), repeat=d)]
    assert all(l1(v, w)==2 for i,v in enumerate(vertices)
               for w in vertices[i+1:])
    assert all(l1(v, u)>=2*r for v in vertices for u in facets)
    assert all(l1(facets[i],facets[j]) == F(2 * sum(a!=b for a,b in zip(facets[i],facets[j])),d)
               for i in range(len(facets)) for j in range(i+1,len(facets)))
    for i, u in enumerate(facets):
        for v in facets[i+1:]:
            h = sum(a!=b for a,b in zip(u,v))
            if h>=d-1:
                assert l1(u,v)>=2*r
                # First two sign coordinates give a proper 4-coloring.
                assert u[:2]!=v[:2]
    # An odd-length zero-sum relation among the Hamming graph generators
    # confirms the graph is nonbipartite in every dimension tested.
    gen = [(1<<d)-1] + [((1<<d)-1) ^ (1<<i) for i in range(d)]
    cycle_gen = gen[1:] if d % 2 else gen
    assert len(cycle_gen) % 2
    total = 0
    for g in cycle_gen:
        total ^= g
    assert total == 0
    return len(vertices),len(facets)


def check_grid(d, den):
    r=F(d-1,d)
    centers=[tuple(F(s,d) if i==j else F(0) for i in range(d))
             for j in range(d) for s in (-1,1)]
    n=0
    for z in product(range(-den,den+1),repeat=d):
        if sum(map(abs,z))>den:
            continue
        x=tuple(F(k,den) for k in z)
        assert min(l1(x,c) for c in centers)<=r
        n+=1
    return n


if __name__ == '__main__':
    for d in range(3,9):
        nv,nf=check_witnesses(d)
        print(f'd={d}: exact vertex/facet tests: {nv} vertices, {nf} facet barycenters')
    for d,den in ((3,8),(4,6),(5,4)):
        print(f'd={d}, denominator={den}: grid points checked={check_grid(d,den)}')
    print('PASS: all finite exact regressions (not an infinite proof)')
