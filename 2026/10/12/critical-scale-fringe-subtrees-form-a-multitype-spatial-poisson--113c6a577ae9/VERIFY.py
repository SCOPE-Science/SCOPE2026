#!/usr/bin/env python3
"""Independent exact checks of fringe-subtree rank events in uniform BSTs."""
from itertools import permutations
from collections import Counter
from fractions import Fraction
from math import factorial


def bst_intervals(order, n):
    class Node:
        __slots__ = ('v','l','r')
        def __init__(self,v): self.v,self.l,self.r=v,None,None
    root = None
    for value in order:
        if root is None:
            root=Node(value)
            continue
        cur=root
        while True:
            side='l' if value<cur.v else 'r'
            nxt=getattr(cur,side)
            if nxt is None:
                setattr(cur,side,Node(value));break
            cur=nxt
    intervals=set()
    def visit(node):
        if node is None: return (n+1,0,0)
        lmin,lmax,lsize=visit(node.l)
        rmin,rmax,rsize=visit(node.r)
        low=min(node.v,lmin,rmin)
        high=max(node.v,lmax,rmax)
        size=lsize+rsize+1
        assert high-low+1==size
        intervals.add((low,size))
        return (low,high,size)
    visit(root)
    return intervals


def indicators_by_order(order):
    n=len(order)
    timestamp=[-1]*(n+2)
    for rank,key in enumerate(order):timestamp[key]=rank
    return {(i,k):int(max(timestamp[i-1],timestamp[i+k]) < min(timestamp[i:i+k]))
            for k in range(1,n) for i in range(1,n-k+2)}


def finite_bst_checks():
    cases=0
    for n in range(2,8):
        frequencies=Counter()
        for order in permutations(range(1,n+1)):
            actual=bst_intervals(order,n)
            tests=indicators_by_order(order)
            assert all(bool(z)==((i,k) in actual) for (i,k),z in tests.items())
            for k in range(1,n):
                frequencies[k]+=sum(tests[i,k] for i in range(1,n-k+2))
            cases+=1
        for k in range(1,n):
            mean=Fraction(frequencies[k],factorial(n))
            assert mean==Fraction(2*(n+1),(k+1)*(k+2)), (n,k,mean)
    return cases


def poly_mul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def h_poly(k):
    # h_k(t) = (1-t)^k (t + (1-t)/(k+1)).
    # polynomials in t as exact fractions.
    from math import comb
    a=[Fraction(comb(k,i)*(-1)**i) for i in range(k+1)]
    b=[Fraction(1,k+1),Fraction(k,k+1)]
    return poly_mul(a,b)


def integr_h(k,l):
    c=poly_mul(h_poly(k),h_poly(l))
    return sum((x/Fraction(i+1) for i,x in enumerate(c)),Fraction(0))


def local_pair_checks():
    n=9
    cases=0
    singles=Counter();pairs=Counter()
    candidates=[(2,5),(2,2),(3,2),(5,2),(5,3),(4,3),(7,2)]
    pairs_to_check=[((2,5),(2,2)), # nested aligned left
                    ((2,5),(3,2)), # nested strict interior
                    ((2,5),(5,2)), # nested aligned right
                    ((2,2),(4,3)), # touching, disallowed
                    ((2,2),(5,3)), # one separating key 4
                    ((2,2),(7,2))] # neighborhoods [1..4] and [6..9] disjoint
    for order in permutations(range(1,n+1)):
        rank=[-1]*(n+2)
        for t,v in enumerate(order):rank[v]=t
        active={pair:max(rank[pair[0]-1],rank[pair[0]+pair[1]]) < min(rank[pair[0]:pair[0]+pair[1]]) for pair in candidates}
        for c in candidates:singles[c]+=active[c]
        for a,b in pairs_to_check:pairs[(a,b)]+=active[a] and active[b]
        cases+=1
    for i,k in candidates:
        p=Fraction(singles[i,k],cases)
        assert p==Fraction(2,(k+1)*(k+2)), ((i,k),p)
    outer=(2,5)
    p_outer=Fraction(2,6*7)
    assert Fraction(pairs[(outer,(2,2))],cases)==p_outer*Fraction(1,3)
    assert Fraction(pairs[(outer,(3,2))],cases)==p_outer*Fraction(2,3*4)
    assert Fraction(pairs[(outer,(5,2))],cases)==p_outer*Fraction(1,3)
    assert pairs[((2,2),(4,3))]==0
    assert Fraction(pairs[((2,2),(5,3))],cases)==integr_h(2,3)
    assert Fraction(pairs[((2,2),(7,2))],cases)==Fraction(2,3*4)**2
    return cases,len(pairs_to_check)


if __name__=='__main__':
    x=finite_bst_checks()
    y,z=local_pair_checks()
    print(f'VERIFY_OK: {x} BST permutations; {y} local timestamp permutations; {z} exact pair identities')
