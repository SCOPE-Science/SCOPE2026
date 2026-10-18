"""Independent exact finite tests for the clique-corona random-greedy law.
Uses direct vertex-order enumeration, not the proposed Bernoulli reduction.
Python 3 standard library only. Run: python verify_corona_greedy.py
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def edges_for_case(r, case):
    all_edges = list(combinations(range(r), 2))
    return [e for j, e in enumerate(all_edges) if (case >> j) & 1]


def predicted(r, s, edges):
    full = (1 << r) - 1
    total = Counter()
    for b in range(1 << r):
        vs = [v for v in range(r) if (b >> v) & 1]
        hist = Counter()
        for order in permutations(vs):
            I = 0
            for v in order:
                if all(not (((I >> u) & 1) and (min(u,v), max(u,v)) in edges) for u in range(r) if u != v):
                    I |= 1 << v
            hist[I] += 1
        for I, c in hist.items():
            total[I] += Fraction(s ** (r-len(vs))*c, (s+1)**r*factorial(len(vs)))
    return total


def brute(r, s, edges):
    n = r * (s+1)
    neighborhood = [0] * n
    for u,v in edges:
        neighborhood[u] |= 1 << v
        neighborhood[v] |= 1 << u
    for v in range(r):
        block = [v] + [r+v*s+j for j in range(s)]
        for u,w in combinations(block,2):
            neighborhood[u] |= 1 << w
            neighborhood[w] |= 1 << u
    observed = Counter()
    for order in permutations(range(n)):
        chosen = 0
        for v in order:
            if not (neighborhood[v] & chosen):
                chosen |= 1 << v
        observed[chosen & ((1 << r)-1)] += 1
    return {I: Fraction(count, factorial(n)) for I,count in observed.items()}


def independent(r, edges, b):
    return all(not ((b >> u)&1 and (b >> v)&1) for u,v in edges)


def check_case(r,s,mask):
    E = edges_for_case(r,mask)
    predicted_law = predicted(r,s,E)
    direct_law = brute(r,s,E)
    assert {I:p for I,p in predicted_law.items() if p} == direct_law,(r,s,mask,predicted_law,direct_law)
    assert sum(direct_law.values()) == 1
    Z = sum(Fraction(1,s**I.bit_count()) for I in range(1<<r) if independent(r,E,I))
    assert direct_law.get(0,0) == Fraction(s,s+1)**r
    if E:
        assert Fraction(1,Z)>direct_law[0]
    else:
        assert all(p == Fraction(1,s**I.bit_count())/Z for I,p in direct_law.items())
    return factorial(r*(s+1))


def main():
    cases = [(r,1,mask) for r in (1,2,3) for mask in range(1 << (r*(r-1)//2))]
    cases += [(4,1,k) for k in (0,1,3,7,11,19,37,63)]
    cases += [(2,2,k) for k in (0,1)]
    cases += [(3,2,k) for k in (0,1,7)]
    total=0
    for r,s,k in cases:
        total+=check_case(r,s,k)
    print(f"PASS: {len(cases)} base-graph/clique-size cases; {total:,} complete vertex orderings; exact Fraction comparisons.")

if __name__=='__main__':
    main()
