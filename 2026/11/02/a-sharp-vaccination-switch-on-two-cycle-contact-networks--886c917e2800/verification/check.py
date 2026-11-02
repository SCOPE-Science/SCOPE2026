#!/usr/bin/env python3
"""Independent finite-state checks for optimal single-vertex vaccination on double-cycle graphs."""
from fractions import Fraction
from itertools import combinations
from math import comb


def graph(r):
    assert r >= 3
    # Two cycles on 0,...,r-1 and r,...,2*r-1; portal vertices 0 and r.
    # An additional bridge vertex 2*r connects the portals.
    edges = [tuple(sorted((i, (i + 1) % r))) for i in range(r)]
    edges += [tuple(sorted((r+i, r+(i+1)%r))) for i in range(r)]
    edges += [(0,2*r), (r,2*r)]
    assert len(set(edges)) == 2*r+2
    return sorted(set(edges)), 2*r+1


def closed_form(r, q):
    # Expected unordered pair connections on post-vaccination residual graph.
    cycle = r * sum((q**k for k in range(1,r)), Fraction(0)) - Fraction(r*(r-1),2)*q**r
    path = sum(((r-1-k)*q**k for k in range(1,r-1)), Fraction(0))
    rooted = 1 + 2 * sum((q**k for k in range(1,r)), Fraction(0)) - (r-1)*q**r
    center = 2*cycle
    portal = path + cycle + q*rooted
    delta = portal-center
    poly = -q-sum(((k-1)*q**k for k in range(2,r)), Fraction(0)) + (Fraction(r*(r-1),2)+2)*q**r - (r-1)*q**(r+1)
    assert delta == poly
    return center, portal, poly


def brute_exact(r, q, vaccinated):
    edges, n = graph(r)
    active = [v for v in range(n) if v != vaccinated]
    edges = [e for e in edges if vaccinated not in e]
    out = Fraction(0)
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        size = [1]*n
        def find(v):
            while v != parent[v]:
                v = parent[v]
            return v
        k = mask.bit_count()
        for j,(a,b) in enumerate(edges):
            if mask & (1 << j):
                aa,bb = find(a),find(b)
                if aa != bb:
                    if size[aa] < size[bb]: aa,bb=bb,aa
                    parent[bb]=aa
                    size[aa]+=size[bb]
        sizes = {}
        for v in active:
            x=find(v)
            sizes[x]=sizes.get(x,0)+1
        pairs=sum(comb(z,2) for z in sizes.values())
        out+=pairs*q**k*(1-q)**(len(edges)-k)
    return out


def threshold(r):
    def poly(x):
        return -x-sum((k-1)*x**k for k in range(2,r)) + (r*(r-1)/2+2)*x**r - (r-1)*x**(r+1)
    lo,hi=0.0,1.0
    for _ in range(55):
        mid=(lo+hi)/2
        if poly(mid)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def main():
    checks=0
    for r in (3,4,5):
        for q in (Fraction(1,3), Fraction(1,2),Fraction(3,4),Fraction(1)):
            cen,port,_=closed_form(r,q)
            assert brute_exact(r,q,2*r)==cen; checks+=1
            assert brute_exact(r,q,0)==port;checks+=1
            assert brute_exact(r,q,r)==port;checks+=1
            for v in (1,r+1):
                assert brute_exact(r,q,v)>port;checks+=1
            for v in range(2*r+1):
                if v not in (0,r,2*r):
                    assert brute_exact(r,q,v)>port;checks+=1
    assert closed_form(3,Fraction(1))[2]==1
    for r in range(3,51):
        p=threshold(r)
        assert 0<p<1
        v1=(-p*.99-sum((k-1)*(p*.99)**k for k in range(2,r))+(r*(r-1)/2+2)*(p*.99)**r-(r-1)*(p*.99)**(r+1))
        v2=(-(1+p)/2-sum((k-1)*((1+p)/2)**k for k in range(2,r))+(r*(r-1)/2+2)*((1+p)/2)**r-(r-1)*((1+p)/2)**(r+1))
        assert v1<0<v2
        checks+=2
    for r in (100,200,400):
        p=threshold(r)
        coefficient = (1-p)*r**3
        assert 5.7<coefficient<6.4, (r,coefficient)
        checks+=1
    print('PASS:',checks,'exact finite-state and algebraic tests plus asymptotic numerical checks')
    print('Root examples:',[(r,round(threshold(r),12)) for r in (3,4,5,10,20,50)])

if __name__=='__main__':main()
