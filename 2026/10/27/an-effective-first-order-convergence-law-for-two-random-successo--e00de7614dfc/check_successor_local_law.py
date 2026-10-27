#!/usr/bin/env python3
"""Exact finite checks for small coloured cyclic patterns in two random directed Hamilton paths.

Each order is a permutation of 0,...,n-1, retaining consecutive arcs.
Checks exact ensemble means against path-block contraction identities; no asymptotic claim is certified by enumeration.
"""
from itertools import permutations
from fractions import Fraction
from math import factorial

def falling(n, k):
    if k > n: return 0
    v = 1
    for i in range(k): v *= n-i
    return v

def run():
    checks = 0
    structures = 0
    for n in range(2, 7):
        pp = list(permutations(range(n)))
        arrays = []
        for p in pp:
            suc = [-1] * n
            for i in range(n-1): suc[p[i]] = p[i+1]
            arrays.append(suc)
        totals = [0,0,0,0]
        for A in arrays:
            for B in arrays:
                structures += 1
                # H1: opposed 2-cycle, A(a,b), B(b,a).
                opp = sum(1 for a,b in enumerate(A) if b >= 0 and B[b] == a)
                # Same-oriented double arcs (a,b) in A and B.
                par = sum(1 for a,b in enumerate(A) if b >= 0 and B[a] == b)
                # Coherently directed 3-cycle of colour pattern A,B,B.
                tri = 0
                for a,b in enumerate(A):
                    if b < 0: continue
                    c = B[b]
                    if c >= 0 and len({a,b,c}) == 3 and B[c] == a:
                        tri += 1
                # Coherently directed four-cycle with cyclic pattern A,B,A,B.
                # Each such coloured cycle is found from its two A-starts.
                four_twice = 0
                for a,b in enumerate(A):
                    if b < 0: continue
                    c = B[b]
                    if c < 0: continue
                    d = A[c]
                    if d >= 0 and len({a,b,c,d}) == 4 and B[d] == a:
                        four_twice += 1
                assert four_twice % 2 == 0
                vals = (opp,par,tri,four_twice//2)
                for j,v in enumerate(vals): totals[j] += v
        expected = [
            Fraction(n-1,n),
            Fraction(n-1,n),
            Fraction(falling(n,3),falling(n,1)*falling(n,2)) if n>=3 else Fraction(0),
            Fraction(falling(n,4),2*falling(n,2)**2) if n>=4 else Fraction(0),
        ]
        means = [Fraction(total, factorial(n)**2) for total in totals]
        assert means == expected, (n,means,expected)
        checks += 4
        print('n',n,'mean opposed, parallel, ABB-triangle, ABAB-four:',*[str(x) for x in means])
    print('SUCCESSOR_LOCAL_EXACT_OK',structures,checks)

if __name__ == '__main__': run()
