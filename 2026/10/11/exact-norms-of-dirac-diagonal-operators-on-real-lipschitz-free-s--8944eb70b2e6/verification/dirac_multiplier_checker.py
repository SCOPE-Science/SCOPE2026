#!/usr/bin/env python3
"""Exact-rational finite triangle tests for Dirac diagonal multipliers.

Reproduce with Python 3: python3 dirac_multiplier_checker.py
No external packages required. This checker validates the local hexagonal
support identity and projection/sign corollaries over a deterministic suite;
the arbitrary-metric and infinite-space claims require the analytic proof.
"""
from fractions import Fraction as F
from itertools import product


def vertices(a, b, c):
    # Each boundary is A*u+B*v=C; intersect every nonparallel pair.
    lines = [(F(1), F(0), a), (F(1), F(0), -a),
             (F(0), F(1), b), (F(0), F(1), -b),
             (F(1), F(-1), c), (F(1), F(-1), -c)]
    output = set()
    for i, (A, B, e) in enumerate(lines):
        for C, D, f in lines[i+1:]:
            det = A*D-B*C
            if not det:
                continue
            u, v = (e*D-B*f)/det, (A*f-e*C)/det
            if abs(u)<=a and abs(v)<=b and abs(u-v)<=c:
                output.add((u,v))
    return output


def direct_pair(a, b, c, z, w):
    return max(abs(z*u-w*v) for u,v in vertices(a,b,c))/c


def formula_pair(a, b, c, z, w):
    return max(abs(a*z-b*w), abs(a*(z-w)+c*w),
               abs(b*(z-w)-c*z))/c


def run():
    count = 0
    for ia in range(1,8):
        for ib in range(1,8):
            for ic in range(abs(ia-ib)+1, ia+ib+1):
                a,b,c = F(ia),F(ib),F(ic)
                verts = vertices(a,b,c)
                declared = {(a,b),(a,a-c),(b-c,b)}
                declared |= {(-u,-v) for u,v in declared}
                assert verts == declared, (a,b,c,verts,declared)
                for z,w in product((-3,-1,0,1,2), repeat=2):
                    assert direct_pair(a,b,c,F(z),F(w)) == formula_pair(a,b,c,F(z),F(w))
                    count+=1
                # Coordinate suppression at this pair with one active coordinate.
                assert formula_pair(a,b,c,F(1),F(0)) == a/c
                assert formula_pair(a,b,c,F(0),F(1)) == b/c
                # Sign diagonal with opposite signs.
                assert formula_pair(a,b,c,F(1),F(-1)) == (a+b)/c
    print(f"DIRAC_MULTIPLIER_LOCAL_EXACT_OK {count}")

if __name__=='__main__':
    run()
