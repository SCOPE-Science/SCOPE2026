#!/usr/bin/env python3
"""Exact finite checks for parallel chip-firing on an open path.

Runs three independently constructed enumerators: direct two-step simulation,
cut-side chip intervals, and the bivariate recurrence. No external modules.
"""
from collections import Counter
from itertools import product
from math import comb


def direct(n):
    degrees = [1] + [2] * (n - 2) + [1]
    polynomial = Counter()
    tested = 0
    for x in product(*[range(2*d) for d in degrees]):
        tested += 1
        firing = [int(x[v] >= degrees[v]) for v in range(n)]
        y = tuple(x[v] - degrees[v]*firing[v] + (firing[v-1] if v else 0) + (firing[v+1] if v<n-1 else 0) for v in range(n))
        firing2 = [int(y[v] >= degrees[v]) for v in range(n)]
        z = tuple(y[v] - degrees[v]*firing2[v] + (firing2[v-1] if v else 0) + (firing2[v+1] if v<n-1 else 0) for v in range(n))
        if x == z and x != y:
            polynomial[sum(x)] += 1
    assert all(v%2 == 0 for v in polynomial.values())
    return Counter({a:b//2 for a,b in polynomial.items()}),tested


def cuts(n):
    mass = Counter()
    for edges in product((0,1), repeat=n-1):
        c = [edges[0]] + [edges[i-1]+edges[i] for i in range(1,n-1)] + [edges[-1]]
        if min(c)==0:
            continue
        states = Counter({2*(n-1)-sum(edges):1})
        for count in c:
            nextstates = Counter()
            for deg, coeff in states.items():
                for off in range(count):
                    nextstates[deg+off] += coeff
            states = nextstates
        mass.update(states)
    return mass


def recurrence(nmax):
    p={2:Counter({1:1}),3:Counter({2:1,3:1})}
    for n in range(4,nmax+1):
        d=Counter()
        for k,c in p[n-1].items():
            d[k+1]+=c;d[k+2]+=c
        for k,c in p[n-2].items():
            d[k+3]+=c
        p[n]=d
    return p


def binomial(n):
    d=Counter()
    for j in range((n-2)//2+1):
        for h in range(n-1-2*j):
            d[n-1+j+h]+=comb(n-2-j,j)*comb(n-2-2*j,h)
    return d


if __name__=='__main__':
    p=recurrence(40)
    total=0
    for n in range(2,11):
        d,examined=direct(n);total+=examined
        assert d==cuts(n)==p[n]==binomial(n),(n,d,cuts(n),p[n])
        print(f'n={n:2d} states_tested={examined:7d} orbit_count={sum(d.values()):6d} support=[{min(d)},{max(d)}] coefficients={dict(sorted(d.items()))}')
    for n in range(11,41):
        assert p[n]==cuts(n) if n<=12 else p[n]==binomial(n)
    pell=[0,1]
    for n in range(2,41):
        pell.append(2*pell[-1]+pell[-2])
    for n in range(2,41):
        assert sum(p[n].values())==pell[n-1]
        assert all(p[n][k]==p[n][3*n-4-k] for k in p[n])
        assert sum(k*v for k,v in p[n].items())*2==(3*n-4)*sum(p[n].values())
    print(f'EXHAUSTIVE_DIRECT_STATES={total}')
    print('CROSS_CHECK_BIVARIATE_RECURRENCE_CUTS_BINOMIAL_AND_PELL_OK')
    print('SYMMETRY_EXACT_MEAN_OK')
