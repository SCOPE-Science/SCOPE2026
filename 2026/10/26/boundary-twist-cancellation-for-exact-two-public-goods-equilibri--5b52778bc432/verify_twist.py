#!/usr/bin/env python3
"""Independent exhaustive check of exact-two-neighbor equilibria on two cubic strip graph families.

Requires only the Python standard library. A profile is a labeled 0/1 string.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def graph(n, twisted):
    assert n >= 3
    edges = set()
    for j in range(n):
        edges.add(tuple(sorted((j, n+j))))
        if twisted:
            edges.add(tuple(sorted((j, (j+1) % (2*n)))))
            edges.add(tuple(sorted((n+j, (n+j+1) % (2*n)))))
        else:
            edges.add(tuple(sorted((j, (j+1) % n))))
            edges.add(tuple(sorted((n+j, n+(j+1) % n))))
    # For the twisted strip, close the two horizontal paths crosswise.
    if twisted:
        edges.add((0, 2*n-1))
        edges.add((n-1, n))
    neighbors = [[] for _ in range(2*n)]
    for u,v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    assert all(len(a)==3 for a in neighbors), (n, twisted, neighbors)
    return neighbors


def direct(n, twisted):
    a=graph(n,twisted)
    c=Counter()
    for mask in range(1<<(2*n)):
        if all(((mask>>i)&1)==(sum((mask>>j)&1 for j in a[i])==2) for i in range(2*n)):
            c[mask.bit_count()]+=1
    return dict(c)


def bulk(n):
    return {4*j: (n*comb(n-3*j,j))//(n-3*j) for j in range(n//4+1)}


def formula(n, twisted):
    c=Counter(bulk(n))
    if twisted:
        if n%4==2: c[3*n//2]+=4
    else:
        c[n]+=2
        if n%4==0:c[3*n//2]+=4
    return dict(c)


def run():
    cases=0; profiles=0
    for n in range(3,10):
        for twisted in (False,True):
            observed=direct(n,twisted)
            predicted=formula(n,twisted)
            assert observed==predicted,(n,twisted,observed,predicted)
            cases+=1
            profiles+=1<<(2*n)
            print(('Mobius' if twisted else 'Prism'),n,sorted(observed.items()))
    assert cases==14
    print('PASS',cases,'graph instances;',profiles,'labeled binary profiles checked.')

if __name__=='__main__':run()
