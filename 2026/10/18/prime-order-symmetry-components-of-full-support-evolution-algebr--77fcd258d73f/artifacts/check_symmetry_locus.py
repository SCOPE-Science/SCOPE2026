#!/usr/bin/env python3
"""Finite tests for the prime-order symmetry strata of dense evolution algebras.

Run: python3 artifacts/check_symmetry_locus.py
Uses only the Python standard library. Counts labelled normalized matrices,
not full algebra isomorphism classes. All computations are over prime fields.
"""
from itertools import permutations, product
from math import factorial


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def order(g):
    e = tuple(range(len(g)))
    a = e
    for k in range(1, factorial(len(g))+1):
        a = compose(g,a)
        if a == e:
            return k
    raise AssertionError('order bound')


def orbit_partition(g, pairs):
    unvisited = set(pairs)
    groups = []
    while unvisited:
        t = min(unvisited)
        group = []
        u = t
        while u in unvisited:
            unvisited.remove(u)
            group.append(u)
            u = (g[u[0]],g[u[1]])
        assert u == t
        groups.append(tuple(group))
    return tuple(groups)


def rank_mod(a, p):
    z = [row[:] for row in a]
    n = len(z)
    rank = 0
    for j in range(n):
        k = next((k for k in range(rank,n) if z[k][j] % p),None)
        if k is None: continue
        z[rank],z[k] = z[k],z[rank]
        t = pow(z[rank][j], -1, p)
        z[rank] = [(t*v)%p for v in z[rank]]
        for i in range(rank+1,n):
            f = z[i][j]
            if f:
                z[i] = [(a-f*b)%p for a,b in zip(z[i],z[rank])]
        rank += 1
    return rank


def count_fixed(n,p,g):
    pairs = tuple((i,j) for i in range(n) for j in range(n) if i!=j)
    orbits = orbit_partition(g,pairs)
    valid=0
    for x in product(range(1,p),repeat=len(orbits)):
        a = [[int(i==j) for j in range(n)] for i in range(n)]
        for o,v in zip(orbits,x):
            for i,j in o:
                a[i][j]=v
        if rank_mod(a,p)==n:valid+=1
    return len(orbits),valid


def brute_total(n,p):
    pairs = tuple((i,j) for i in range(n) for j in range(n) if i!=j)
    perm = tuple(permutations(range(n)))
    total=nontriv=0
    for values in product(range(1,p),repeat=len(pairs)):
        a = [[int(i==j) for j in range(n)] for i in range(n)]
        for (i,j),v in zip(pairs,values):a[i][j]=v
        if rank_mod(a,p)<n:continue
        total+=1
        if any(g!=tuple(range(n)) and all(a[i][j]==a[g[i]][g[j]] for i,j in pairs) for g in perm):
            nontriv+=1
    return total,nontriv


def check_orbit_closure(n):
    perm=tuple(permutations(range(n)))
    pairs=tuple((i,j) for i in range(n) for j in range(n) if i!=j)
    nprime=0
    for g in perm:
        o=order(g)
        if o<2 or any(o%a==0 for a in range(2,o)):
            continue
        orbits=orbit_partition(g,pairs)
        want={tuple(range(n))}
        a=tuple(range(n))
        for k in range(1,o):
            a=compose(g,a);want.add(a)
        closure=set()
        for h in perm:
            if all(set((h[i],h[j]) for i,j in orbit)==set(orbit) for orbit in orbits):
                closure.add(h)
        assert closure==want,(n,g,o,closure,want)
        r=(n-sum(g[i]==i for i in range(n)))//o
        c=r*(o-1)*(2*n-o*r-1)
        assert len(pairs)-len(orbits)==c,(n,g,c)
        nprime+=1
    return nprime


def main():
    for n in (4,5,6):
        print('ORBIT_CLOSURE',n,check_orbit_closure(n))
    for n,p in ((4,2),(4,3)):
        total,nontriv=brute_total(n,p)
        print('WHOLE_OPEN_LOCUS',n,p,total,nontriv)
        assert 0<=nontriv<=total
    for n,p,g in ((4,3,(1,0,2,3)),(4,5,(1,0,2,3)),
                  (4,3,(1,0,3,2)),(4,3,(1,2,0,3)),
                  (5,3,(1,0,2,3,4)),(5,3,(1,0,3,2,4)),
                  (5,3,(1,2,0,3,4))):
        orbits,valid=count_fixed(n,p,g)
        ordg=order(g)
        r=(n-sum(i==g[i] for i in range(n)))//ordg
        expected=n*(n-1)-r*(ordg-1)*(2*n-ordg*r-1)
        assert orbits==expected
        assert 0<=valid<=(p-1)**orbits
        print('FIXED_LOCI',n,p,ordg,r,orbits,valid)
    print('ALL_PRIME_ORDER_SYMMETRY_CHECKS_PASSED')

if __name__=='__main__':main()
