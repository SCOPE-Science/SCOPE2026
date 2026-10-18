#!/usr/bin/env python3
"""Exact finite support and covariance-rank checks for dimer occupation on a path."""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def greedy(n, sequence):
    used = [0]*n
    for edge in sequence:
        if not used[edge] and not used[edge+1]:
            used[edge] = used[edge+1] = 1
    return tuple(used)


def rank(rows):
    if not rows:
        return 0
    a = [[Fraction(z) for z in row] for row in rows]
    pivots = 0
    ncol = len(a[0])
    for j in range(ncol):
        found = next((i for i in range(pivots,len(a)) if a[i][j]),None)
        if found is None:
            continue
        a[pivots],a[found] = a[found],a[pivots]
        v = a[pivots][j]
        a[pivots] = [z/v for z in a[pivots]]
        for i in range(pivots+1,len(a)):
            if a[i][j]:
                q = a[i][j]
                a[i] = [w-q*z for w,z in zip(a[i],a[pivots])]
        pivots+=1
        if pivots == len(a):
            break
    return pivots


def affine_rank(outcomes):
    first = next(iter(outcomes))
    return rank([tuple(x-y for x,y in zip(out,first)) for out in outcomes])


def jam_states(n):
    edges = n-1
    result = set()
    for mask in range(1 << edges):
        chosen = tuple(i for i in range(edges) if (mask >> i) & 1)
        if any(abs(i-j)==1 for i,j in combinations(chosen,2)):
            continue
        if any(all(abs(e-i)>1 for i in chosen) for e in range(edges)):
            continue
        used = [0]*n
        for i in chosen:
            used[i]=used[i+1]=1
        result.add(tuple(used))
    return result


def finite_time_law(n):
    # Every edge is early independently with probability 1/2. Conditional
    # on the early set, its chronological order is a uniform permutation.
    e=n-1
    masses={}
    for mask in range(1 << e):
        early=tuple(i for i in range(e) if (mask>>i)&1)
        weight=Fraction(1,2**e * factorial(len(early)))
        for order in permutations(early):
            x=greedy(n,order)
            masses[x]=masses.get(x,Fraction(0))+weight
    assert sum(masses.values()) == 1
    return masses


def covariance(law):
    n=len(next(iter(law)))
    means=[sum(p*x[i] for x,p in law.items()) for i in range(n)]
    return [[sum(p*(x[i]-means[i])*(x[j]-means[j]) for x,p in law.items()) for j in range(n)] for i in range(n)]


def verify():
    total=0
    for n in range(4,13):
        outcomes=jam_states(n)
        ar=affine_rank(outcomes)
        assert ar==n-3,(n,ar)
        total+=1
        for x in outcomes:
            assert x[1]==x[-2]==1
            assert sum((-1)**i*x[i] for i in range(n))==0
            total+=3
        if n<=7:
            # Independently compare support against every priority ordering.
            from_orders={greedy(n,perm) for perm in permutations(range(n-1))}
            assert outcomes == from_orders
            total+=1
    for n in range(4,8):
        law=finite_time_law(n)
        c=covariance(law)
        assert rank(c)==n-1
        total+=1
        for i in range(n):
            assert sum(c[i][j] * (-1)**j for j in range(n))==0
            total+=1
        assert (0,)*n in law
        for edge in range(n-1):
            v=tuple(int(i in (edge,edge+1)) for i in range(n))
            assert v in law
            total+=1
    print(f'PASS {total} exact assertions: jammed n=4..12, finite-time n=4..7, rational covariance ranks.')

if __name__=='__main__':
    verify()
