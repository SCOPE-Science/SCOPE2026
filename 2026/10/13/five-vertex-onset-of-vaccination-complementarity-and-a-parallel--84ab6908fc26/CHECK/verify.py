"""Exact checks for node-immunization complementarity in independent bond transmission.
Requires only Python 3 standard library. The mathematical theorem is proved separately.
"""
from itertools import combinations
from fractions import Fraction
from math import comb


def comps(n, edges, blocked=frozenset()):
    active = set(range(n)) - set(blocked)
    components = []
    while active:
        start = min(active)
        active.remove(start)
        frontier = [start]
        comp = {start}
        while frontier:
            u = frontier.pop()
            for v in range(n):
                if v in active and ((min(u, v), max(u, v)) in edges):
                    active.remove(v)
                    comp.add(v)
                    frontier.append(v)
        components.append(comp)
    return components


def burden(n, edges, S):
    return sum(len(c) ** 2 for c in comps(n, edges, S))


def gap(n, edges, S, a, b):
    S = frozenset(S)
    return (burden(n, edges, S) + burden(n, edges, S | {a, b})
            - burden(n, edges, S | {a}) - burden(n, edges, S | {b}))


def structural_gap(n, edges, S, a, b):
    # The general two-vaccine formula, independent of transmission.
    H = set(range(n)) - set(S)
    whole = next(c for c in comps(n, edges, S) if a in c)
    if b not in whole:
        return 0
    pieces = [c for c in comps(n, edges, set(S) | {a, b}) if c <= whole]
    a_only = [c for c in pieces if any((min(a, x), max(a, x)) in edges for x in c)
              and not any((min(b, x), max(b, x)) in edges for x in c)]
    b_only = [c for c in pieces if any((min(b, x), max(b, x)) in edges for x in c)
              and not any((min(a, x), max(a, x)) in edges for x in c)]
    both = [c for c in pieces if any((min(a, x), max(a, x)) in edges for x in c)
            and any((min(b, x), max(b, x)) in edges for x in c)]
    A = sum(map(len, a_only))
    B = sum(map(len, b_only))
    Q = sum(len(c) * len(d) for c, d in combinations(both, 2))
    return 2 * ((A + 1) * (B + 1) - Q)


def edges_of(n, bits):
    possible = list(combinations(range(n), 2))
    return frozenset(e for j, e in enumerate(possible) if bits & (1 << j))


def exact_graph_checks():
    checked = 0
    for n in range(2, 6):
        possible = list(combinations(range(n), 2))
        for bits in range(1 << len(possible)):
            E = edges_of(n, bits)
            for a, b in possible:
                rest = [x for x in range(n) if x not in (a, b)]
                for t in range(len(rest)+1):
                    for subset in combinations(rest, t):
                        lhs = gap(n, E, subset, a, b)
                        assert lhs == structural_gap(n, E, subset, a, b), (n, E, subset, a, b)
                        if n <= 4:
                            assert lhs >= 0, (n, E, subset, a, b)
                        checked += 1
    return checked


def poly_coefficient_certificate():
    # Five-cycle in cyclic labeling, vaccinate nonadjacent nodes 0 and 2.
    edges = [(0,1),(1,2),(2,3),(3,4),(0,4)]
    coeff = [0] * 6
    for mask in range(32):
        live = frozenset(e for i,e in enumerate(edges) if mask & (1 << i))
        k = mask.bit_count()
        d = gap(5, live, (), 0, 2)
        for j in range(6-k):
            coeff[k+j] += d * (-1)**j * comb(5-k, j)
    assert coeff == [0,0,2,6,10,-20], coeff
    return coeff


def rational_checks():
    def h(p): return 1 + 3*p + 5*p*p - 10*p*p*p
    assert h(Fraction(93,100)) > 0 and h(Fraction(94,100)) < 0
    p = Fraction(19,20)
    assert h(p) == Fraction(-169,800)
    gap_exact = 2*p*p*h(p)
    assert gap_exact == Fraction(-61009,160000), gap_exact
    return str(gap_exact)


def main():
    checks = exact_graph_checks()
    coefficients = poly_coefficient_certificate()
    g = rational_checks()
    print('VERIFY_OK', 'structural_and_small_graph_cases='+str(checks),
          'C5_coefficients='+str(coefficients), 'C5_gap_at_19_over_20='+g)


if __name__ == '__main__':
    main()
