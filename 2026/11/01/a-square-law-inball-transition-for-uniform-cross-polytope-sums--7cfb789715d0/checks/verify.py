#!/usr/bin/env python3
"""Finite checks for the uniform-subset crosspolytope sum inball formula.
Checks corroborate but do not establish the theorem for unbounded n.
"""
from itertools import combinations, product
from math import comb
from random import Random


def b(n,k,j):
    return comb(n,k) - (comb(n-j,k) if n-j>=k else 0)


def support_direct(n,k,u):
    return sum(max(abs(u[i]) for i in I) for I in combinations(range(n), k))


def support_sorted(n,k,u):
    a=sorted(map(abs,u))
    return sum(comb(i,k-1)*a[i] for i in range(k-1,n))


def support_hyperplanes(n,k,u):
    coords=sorted((abs(t),i) for i,t in enumerate(u))
    vals=[x for x,_ in coords]
    total=0
    last=0
    for i,(v,_) in enumerate(coords):
        total+=(v-last)*b(n,k,n-i)
        last=v
    return total


def run():
    rng=Random(20261030)
    support_count=0
    for n in range(3,9):
        for k in range(3,n+1):
            for z in range(240):
                u=tuple(rng.randrange(-8,9) for _ in range(n))
                a=support_direct(n,k,u)
                assert a==support_sorted(n,k,u)==support_hyperplanes(n,k,u),(n,k,u)
                support_count+=1
    inequality_count=0
    end_count=0
    for n in range(3,151):
        for k in range(3,n+1):
            b1=b(n,k,1)
            bn=comb(n,k)
            endpoint=min(b1*b1*n,bn*bn)  # squared r multiplied by n
            for j in range(1,n+1):
                inequality_count+=1
                assert n*b(n,k,j)**2>=j*endpoint,(n,k,j)
                if 1<j<n:
                    assert n*b(n,k,j)**2>j*endpoint,(n,k,j)
            if n<k*k:
                assert bn*bn<n*b1*b1
            elif n>k*k:
                assert bn*bn>n*b1*b1
            else:
                assert bn*bn==n*b1*b1
            end_count+=1
    print(f"PASS: {support_count} exact support comparisons; {inequality_count} exact squared-distance inequalities; {end_count} sharp endpoint classifications (3 <= k <= n <= 150).")

if __name__ == '__main__':
    run()
