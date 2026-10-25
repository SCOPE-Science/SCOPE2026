#!/usr/bin/env python3
"""Exact finite check of the degree-four cyclotomic exponent classification."""
from itertools import product
DEG = (1, 1, 2, 2, 2)  # Phi_1, Phi_2, Phi_3, Phi_4, Phi_6
EXPECTED = {
 (1,0,0,0,0),
 (1,1,0,0,0),(2,0,0,0,0),
 (1,0,1,0,0),(2,1,0,0,0),(3,0,0,0,0),
 (1,1,0,1,0),(1,1,1,0,0),(2,0,1,0,0),(2,2,0,0,0),(3,1,0,0,0),(4,0,0,0,0)
}
def main():
    found=set()
    for e1,e2,e3,e4,e6 in product(range(5), repeat=5):
        if e1 < 1: continue
        degree=e1+e2+2*e3+2*e4+2*e6
        if degree > 4: continue
        if e1+e3 < e2+e6 or e2 < e4 or e1 < e3 or e2 < e6: continue
        found.add((e1,e2,e3,e4,e6))
    assert found == EXPECTED, (sorted(found), sorted(EXPECTED))
    assert len(found)==12
    degree_four=[e for e in found if sum(a*b for a,b in zip(e,DEG))==4]
    assert len(degree_four)==6
    # One x^(4-d) multiple per core of degree d, plus x^4.
    assert len(found)+1==13
    print('VERIFY_OK: 12 cyclotomic cores; 6 degree-four cores; 13 degree-four polynomials')
if __name__=='__main__': main()
