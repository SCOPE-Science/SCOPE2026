#!/usr/bin/env python3
"""Finite independent checks supporting the 2/5-density theorem.

Reconstructs arithmetic Pythagorean pairs without using the four-ratio
classification, then separately reconstructs its predicted exponent graph.
It also checks a finite translational five-cycle certificate.
"""
from itertools import product, combinations
from math import gcd, isqrt

DIRECTIONS = ((2,-1,0),(2,1,-1),(3,-1,-1),(3,-2,1))
CYCLE = (405,540,720,1350,1800)
EXP_CYCLE = ((0,4,1),(2,3,1),(4,2,1),(1,3,2),(3,2,2))

def compute_box(a_size,b_size,c_size):
    vectors = list(product(range(a_size),range(b_size),range(c_size)))
    values = {v:2**v[0]*3**v[1]*5**v[2] for v in vectors}
    direct = set()
    for u,v in combinations(vectors,2):
        h2=values[u]**2+values[v]**2
        h=isqrt(h2)
        if h*h==h2: direct.add(frozenset((u,v)))
    predicted = set()
    for u in vectors:
        for d in DIRECTIONS:
            v=tuple(u[j]+d[j] for j in range(3))
            if v in values:predicted.add(frozenset((u,v)))
    assert direct==predicted,(a_size,b_size,c_size,len(direct),len(predicted),next(iter(direct^predicted)))
    independent={v for v in vectors if v[0]%5 in (0,1)}
    assert not any(e<=independent for e in direct)
    expected=(2*(a_size//5)+min(a_size%5,2))*b_size*c_size
    assert len(independent)==expected
    if a_size>=2:
        limit=(2*(a_size+3)*(b_size+2)*(c_size+1))//5
        assert expected<=limit
        periods=(a_size+3,b_size+2,c_size+1)
        xs={v for v in independent}
        torus_support=xs
        assert all(frozenset((v,tuple((v[j]+d[j])%periods[j] for j in range(3)))) not in
                   {frozenset((z,w)) for z in torus_support for w in torus_support if z!=w}
                   for v in torus_support for d in DIRECTIONS)
    return len(direct)

def main():
    hypotenuses=(675,900,1530,2250,1845)
    for j,u in enumerate(CYCLE):
        v=CYCLE[(j+1)%5]
        assert u*u+v*v==hypotenuses[j]**2
        assert 2**EXP_CYCLE[j][0]*3**EXP_CYCLE[j][1]*5**EXP_CYCLE[j][2]==u
    count=0
    for A in range(1,7):
        for B in range(1,6):
            for C in range(1,5):
                compute_box(A,B,C)
                count+=1
    print(f'VERIFY_OK rectangular_boxes={count} five_cycle_edges=5 classification_agrees=YES')

if __name__=='__main__':main()
