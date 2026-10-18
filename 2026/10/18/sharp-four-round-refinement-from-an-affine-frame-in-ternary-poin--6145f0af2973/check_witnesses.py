#!/usr/bin/env python3
"""Independent finite checks of the explicit 2-round singleton witness geometry.

The code does not use graph colour refinement and tests the proposed
incidence-separating set directly. It is not an infinite-dimensional proof.
"""
from itertools import combinations, product
from collections import Counter


def hyperplanes(d):
    for a in product(range(3),repeat=d):
        if all(x == 0 for x in a):
            continue
        if a[next(i for i,t in enumerate(a) if t)] != 1:
            continue
        for b in range(3):
            yield a,b


def witness_points(d):
    zero = (0,)*d
    base = [tuple(int(k==i) for k in range(d)) for i in range(d)]
    opposite = [tuple(2*int(k==i) for k in range(d)) for i in range(d)]
    pairs = [tuple(2*int(k==i or k==j) for k in range(d)) for i,j in combinations(range(d),2)]
    return [zero]+base+opposite+pairs


def main():
    for d in range(2,10):
        w = witness_points(d)
        seen = set()
        num=0
        for a,b in hyperplanes(d):
            # A signature is *only* incidences with points proved individually colored by round 2.
            sig = tuple(int(sum(t*u for t,u in zip(a,p))%3==b) for p in w)
            assert sig not in seen, (d,a,b)
            seen.add(sig)
            num+=1
        assert num==3*(3**d-1)//2
        assert len(w)==1+2*d+d*(d-1)//2
        print(f'dimension={d} witnessed_points={len(w)} hyperplane_signatures={num} all_distinct=True')
    # Verify the exact local signature collision for the three nonmarked points
    # (1,1),(1,2),(2,1), uniformly across every possible first-round normal class.
    for d in range(2,16):
        for active in (0,1,2):
            # b=0 normal class: 0,1,2 active coordinates among the first two.
            def zero_count(u,v):
                vals=[]
                for a0 in ((1,2) if active>=1 else (0,)):
                    for a1 in ((1,2) if active==2 else (0,)):
                        if (a0*u+a1*v)%3==0: vals.append((a0,a1))
                return len(vals)
            if active==0:
                expected=1
            elif active==1:
                expected=0
            else:
                expected=2
            assert all(zero_count(u,v)==expected for u,v in ((1,1),(1,2),(2,1)))
        for ti,tj in product((False,True),repeat=2):
            counts=[]
            for u,v in ((1,1),(1,2),(2,1)):
                counts.append(sum((a0*u+a1*v)%3==1 for a0 in ((1,) if ti else (0,2)) for a1 in ((1,) if tj else (0,2))))
            assert len(set(counts))==1, (d,ti,tj,counts)
    print('PASS independent witness signatures and local second-round collision identities')

if __name__=='__main__':
    main()
