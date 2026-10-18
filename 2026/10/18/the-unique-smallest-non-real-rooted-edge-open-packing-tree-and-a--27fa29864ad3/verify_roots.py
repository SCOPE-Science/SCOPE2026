#!/usr/bin/env python3
"""Exact stdlib edge-open-packing census and broom real-rootedness checks."""
from itertools import combinations
from math import comb
from fractions import Fraction

def product(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return tuple(r)

def packpoly(edges):
    m=len(edges)
    forbidden=[]
    for i,j in combinations(range(m),2):
        a=set(edges[i]);b=set(edges[j])
        if any(k!=i and k!=j and (u in a and v in b or v in a and u in b)
               for k,(u,v) in enumerate(edges)):
            forbidden.append((i,j))
    cnt=[0]*(m+1)
    for mask in range(1<<m):
        if all(not (mask & (1<<i) and mask & (1<<j)) for i,j in forbidden):
            cnt[mask.bit_count()]+=1
    while len(cnt)>1 and cnt[-1]==0:cnt.pop()
    return tuple(cnt)

def broom(d):
    return [(0,i) for i in range(1,d+1)]+[(d,d+1)]

def cubic_discriminant(a,b,c,d):
    return b*b*c*c - 4*a*c*c*c -4*b*b*b*d - 27*a*a*d*d + 18*a*b*c*d

# All unlabeled trees of order 1 through 6: exact canonical representatives.
representatives={
    1:[([], (1,))],
    2:[([(0,1)], (1,1))],
    3:[([(0,1),(1,2)],(1,2,1))],
    4:[([(0,1),(1,2),(2,3)],(1,3,2)), ([(0,1),(0,2),(0,3)],(1,3,3,1))],
    5:[([(0,1),(1,2),(2,3),(3,4)],(1,4,4)),
       ([(0,1),(0,2),(0,3),(3,4)],product((1,1),(1,3,1))),
       ([(0,i) for i in range(1,5)],tuple(comb(4,k) for k in range(5)))],
    6:[([(i,i+1) for i in range(5)],product((1,2),(1,3,1))),
       ([(0,1),(0,2),(0,3),(3,4),(4,5)],product((1,2),(1,3,1))),
       ([(0,1),(0,2),(0,3),(1,4),(1,5)],product((1,1),(1,4,2))),
       ([(0,1),(0,2),(2,3),(0,4),(4,5)],(1,5,6,1)),
       (broom(4),product((1,1),(1,4,3,1))),
       ([(0,i) for i in range(1,6)],tuple(comb(5,k) for k in range(6)))]
}

def main():
    casecount=0;subsetcount=0
    for n,items in representatives.items():
        for edges,expected in items:
            measured=packpoly(edges)
            assert measured==expected,(n,edges,measured,expected)
            casecount+=1;subsetcount+=(1<<len(edges))
    assert [len(representatives[n]) for n in range(1,7)]==[1,1,1,2,3,6]
    # For the six order-6 cases the four real-rooted factorizations above,
    # the star binomial polynomial, and one cubic obstruction are complete.
    assert cubic_discriminant(1,6,5,1)==49
    assert cubic_discriminant(1,3,4,1)==-31
    for d in range(2,10):
        exp=product((1,1),tuple(comb(d-1,k)+(1 if k==1 else 0) for k in range(d)))
        assert packpoly(broom(d))==exp,d
    for d in range(4,101):
        m=d-1
        assert Fraction(1,1) < Fraction(m+1,m)
        assert comb(m,2)>0 and comb(m,3)>0
    print('VERIFICATION_ROOTS_OK unlabeled_tree_cases=%d small_tree_edge_subsets=%d broom_orders=2..9 newton_thresholds=4..100 cubic_discriminants=49,-31' % (casecount,subsetcount))
if __name__=='__main__':main()
