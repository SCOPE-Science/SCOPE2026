#!/usr/bin/env python3
"""Independent closed-neighborhood enumeration of double dominating sets.

Usage: python3 verify_double_subdivision.py
Only Python standard library is needed.
"""
from math import comb


def add(a, b):
    result = [0] * max(len(a), len(b))
    for i, v in enumerate(a): result[i] += v
    for i, v in enumerate(b): result[i] += v
    return result


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return c


def power(a, n):
    c = [1]
    for _ in range(n): c = multiply(c, a)
    return c


def shift(a, n):
    return [0]*n+a


def binomial_poly(n):
    return [comb(n, k) for k in range(n+1)]


def predicted(p, q):
    # Edge-cover polynomial by inclusion-exclusion over uncovered vertices.
    e = [0]*(p*q+1)
    for i in range(p+1):
        for j in range(q+1):
            w = (-1)**(i+j)*comb(p, i)*comb(q, j)
            for k, x in enumerate(binomial_poly((p-i)*(q-j))):
                e[k] += w*x
    ans = shift(e, p+q)
    # Omitted original vertices on the first bipartition side.
    row = binomial_poly(q)
    row[0] = 0
    for u in range(1, p+1):
        a = shift(power(row, p-u), p+q-u+u*q)
        ans = add(ans, [comb(p,u)*v for v in a])
    # Omitted original vertices on the second side.
    column = binomial_poly(p)
    column[0] = 0
    for v in range(1, q+1):
        b = shift(power(column, q-v), p+q-v+v*p)
        ans = add(ans, [comb(q,v)*x for x in b])
    return ans


def oracle(p, q):
    count = p+q+p*q
    closed = [(1<<v) for v in range(count)]
    for i in range(p):
        for j in range(q):
            w = p+q+i*q+j
            a, b = i, p+j
            for u in (a,b):
                closed[u] |= 1<<w
                closed[w] |= 1<<u
    counts=[0]*(count+1)
    for mask in range(1<<count):
        if all((mask & neighborhood).bit_count()>=2 for neighborhood in closed):
            counts[mask.bit_count()]+=1
    return counts


def onto(q, p):
    return sum((-1)**i*comb(p,i)*(p-i)**q for i in range(p+1))


def minimal_multiplicity(p, q):
    assert 2<=p<=q
    if p>=3: return onto(q,p)
    if q==2: return 12
    return 3**q+2*q-2


def main():
    cases=[(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)]
    total=0
    for p,q in cases:
        actual=oracle(p,q)
        expected=predicted(p,q)
        if actual != expected:
            raise AssertionError((p,q,actual,expected))
        d=min(k for k,x in enumerate(actual) if x)
        if d!=p+2*q or actual[d]!=minimal_multiplicity(p,q):
            raise AssertionError(('minima',p,q,d,actual[d]))
        print(f'p={p} q={q} n={p+q+p*q} total={sum(actual)} min={d} minima={actual[d]} MATCH')
        total+=1<<(p+q+p*q)
    for p in range(2,10):
        for q in range(p,12):
            f=predicted(p,q)
            d=min(k for k,x in enumerate(f) if x)
            if d!=p+2*q or f[d]!=minimal_multiplicity(p,q) or any(x<0 for x in f):
                raise AssertionError(('symbolic',p,q,d))
    print(f'ALL PASS; brute_force_subsets={total}; brute_force_instances={len(cases)}; symbolic_pairs={sum(12-p for p in range(2,10))}')


if __name__ == '__main__': main()
