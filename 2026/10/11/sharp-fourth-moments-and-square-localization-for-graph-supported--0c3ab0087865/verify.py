"""Exact-rational finite checks of fourth moments on edge-disjoint-square graphs.

This script tests sample instances, not the unrestricted graph theorem.
Run with Python 3 standard library: python verify_edge_cactus.py
"""
from fractions import Fraction
from itertools import combinations, product


def canonical_edges(edges):
    return tuple(sorted(tuple(sorted(e)) for e in edges))


def squares(edges):
    graph = canonical_edges(edges)
    vs = sorted(set(v for e in graph for v in e))
    adjacent = set(graph)
    result = set()
    for subset in combinations(vs, 4):
        for order in __import__('itertools').permutations(subset[1:]):
            cyc = (subset[0],) + order
            ee = frozenset(tuple(sorted((cyc[i], cyc[(i + 1) % 4]))) for i in range(4))
            if len(ee) == 4 and ee.issubset(adjacent):
                result.add(ee)
    return tuple(result)


def moment_by_enumeration(edges, coeffs):
    vs = sorted(set(v for e in edges for v in e))
    n = len(vs)
    ind = {v: i for i, v in enumerate(vs)}
    return sum((sum(a * signs[ind[u]] * signs[ind[v]]
                    for (u, v), a in zip(edges, coeffs)))**4
               for signs in product((-1, 1), repeat=n)) / Fraction(2**n)


def moment_identity(edges, coeffs):
    S = sum((a*a for a in coeffs), Fraction())
    aa = {tuple(sorted(edge)): a for edge, a in zip(edges, coeffs)}
    return 3*S*S - 2*sum((a**4 for a in coeffs), Fraction()) + 24*sum((__import__('math').prod(aa[e] for e in cyc) for cyc in squares(edges)), Fraction())


def test(edges):
    edges = canonical_edges(edges)
    c4 = squares(edges)
    incidence = [sum(e in c for c in c4) for e in edges]
    assert max(incidence, default=0) <= 1, (edges, c4)
    examples = ([Fraction(k) for k in range(1, len(edges) + 1)],
                [Fraction((-1)**k*(k+2), k+1) for k in range(len(edges))],
                [Fraction(1) for _ in edges])
    for coeffs in examples:
        S = sum((a*a for a in coeffs), Fraction())
        exact = moment_by_enumeration(edges, coeffs)
        symbolic = moment_identity(edges, coeffs)
        assert exact == symbolic, (edges, coeffs, exact, symbolic)
        if c4:
            assert symbolic <= 4*S*S
            if symbolic * 2 > 7 * S*S:
                delta = (4*S*S-symbolic)/(S*S)
                masses = [sum(a*a for edge, a in zip(edges, coeffs) if edge in C) / S
                          for C in c4]
                t = max(masses)
                assert t > Fraction(1,2)
                assert 2*t*(1-t) <= delta
        else:
            assert symbolic * len(edges) <= (3*len(edges)-2)*S*S
    return len(examples)


def main():
    C4 = [(0,1),(1,2),(2,3),(3,0)]
    C5 = [(i,(i+1)%5) for i in range(5)]
    two = C4 + [(u+4,v+4) for u,v in C4]
    fig8 = C4 + [(0,4),(4,5),(5,6),(6,0)]
    tail = C4 + [(3,4),(4,5)]
    diamond = [(0,1),(1,2),(2,3),(3,0),(0,2)]
    tests = sum(test(e) for e in (C4, C5, two, fig8, tail, diamond, [(0,1)], [(0,1),(1,2)]))
    for a, b in ((Fraction(3), Fraction(4)), (Fraction(2), Fraction(3))):
        edges = canonical_edges(two)
        # Rational edge magnitudes give an exact two-square stability witness.
        coeffs = [a if max(e)<4 else b for e in edges]
        S = sum(t*t for t in coeffs)
        masses = [Fraction(4*a*a,S),Fraction(4*b*b,S)]
        m4 = moment_by_enumeration(edges, coeffs)/S**2
        assert m4 == 4-2*masses[0]*masses[1]
    print('EDGE_DISJOINT_SQUARE_MOMENT_EXACT_OK', tests)

if __name__ == '__main__':
    main()
