#!/usr/bin/env python3
"""Independent finite checks of even-dihedral quandle-algebra idempotent geometry.

Run: python3 verify.py (Python 3 standard library; SymPy optional for determinants).
"""
from collections import Counter, defaultdict
from itertools import product
from math import gcd


def orbit_partition(m):
    unused = set(range(1,m))
    orbits = []
    while unused:
        x = min(unused)
        todo = [x]
        orbit = set()
        while todo:
            t = todo.pop()
            if t in orbit:
                continue
            orbit.add(t)
            todo.extend(((-t)%m, (2*t)%m))
        assert orbit <= unused
        unused -= orbit
        orbits.append(sorted(orbit))
    return orbits


def determinant_int(a):
    # Integer-preserving fraction-free elimination (Bareiss), exact for all sizes.
    n = len(a)
    if not n:
        return 1
    a = [list(row) for row in a]
    sign = 1
    divisor = 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k+1,n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k],a[pivot] = a[pivot],a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value = a[i][j]*pivot-a[i][k]*a[k][j]
                assert value % divisor == 0
                a[i][j] = value//divisor
            a[i][k] = 0
        divisor = pivot
    return sign*a[-1][-1]


def orbit_determinant(m, orbit):
    ix = {v:i for i,v in enumerate(orbit)}
    h = len(orbit)
    matrix = [[int(i==j) for j in range(h)] for i in range(h)]
    for v in orbit:
        i = ix[v]
        matrix[i][ix[(-v)%m]] -= 1
        matrix[i][ix[(2*v)%m]] -= 1
    return abs(determinant_int(matrix))


def closed_delta(d):
    assert d % 2 == 1 and d>1
    t = 1
    m = 0
    while True:
        m += 1
        t = (2*t) % d
        if t == 1:
            break
    return (2**(m//2)+1) if (m%2==0 and pow(2,m//2,d) == d-1) else (2**m-1)


def component_poly(m):
    assert m>=1 and m%2==1
    a = [1,1]  # augmentation 0 or 1; for the latter, one free Fourier coordinate
    orbits = orbit_partition(m)
    for orb in orbits:
        d = m//gcd(m,orb[0])
        delta = closed_delta(d)
        assert delta == orbit_determinant(m,orb),(m,orb,delta)
        h = len(orb)//2
        assert 2*h == len(orb)
        b = [0]*(len(a)+h)
        for i,v in enumerate(a):
            b[i] += v
            b[i+h] += v*delta
        a=b
    assert sum(a)>0
    return a


def quandle_product(a,b,q):
    n=len(a)
    c=[0]*n
    for i,ai in enumerate(a):
        if not ai:continue
        for j,bj in enumerate(b):
            c[(2*j-i)%n]=(c[(2*j-i)%n]+ai*bj)%q
    return tuple(c)


def primitive_root_order(n,q):
    for z in range(2,q):
        if pow(z,n,q)!=1:continue
        if all(pow(z,k,q)!=1 for k in range(1,n)):
            return z
    raise ValueError('no primitive root')


def field_fiber_census(n,q):
    assert n%2==0 and (n//2)%2==1 and (q-1)%n==0
    z=primitive_root_order(n,q)
    m=n//2
    buckets=defaultdict(int)
    for a in product(range(q),repeat=n):
        if quandle_product(a,a,q)!=a:
            continue
        even_fourier=tuple(sum(a[x]*pow(z,2*j*x,q) for x in range(n))%q for j in range(m))
        buckets[even_fourier]+=1
    observed=Counter(buckets.values())
    expected=Counter()
    for dim,multiplicity in enumerate(component_poly(m)):
        if multiplicity:
            expected[q**dim]+=multiplicity
    assert observed==expected,(n,q,observed,expected)
    return len(buckets),sum(buckets.values()),dict(sorted(observed.items()))


def run():
    for m in (1,3,5,7,9,11,13,15,21,25,31):
        p=component_poly(m)
        assert len(p)-1==(m+1)//2,(m,p)
        assert p[0]==1
        print('m',m,'component dimensions',p,'components',sum(p))
    for n,q in ((2,5),(6,7)):
        components,total,hist=field_fiber_census(n,q)
        print('DIRECT',n,q,'components',components,'field idempotents',total,'fiber histogram',hist)
    print('VERIFY_OK odd-order orbit determinants and two complete finite-field quandle-algebra censuses')

if __name__=='__main__':
    run()
