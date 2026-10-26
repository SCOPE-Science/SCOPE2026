"""Reproduce finite-field checks for commuting involution tuples in Heisenberg groups.

Independent from the proof's rank-fiber argument: enumerate actual group elements
with square one and test their pairwise commutators, then compare with a
separately implemented Gaussian-binomial formula.
"""
from itertools import product
from math import prod


def mul(a, b, q):
    if q == 2:
        return a & b
    if q == 4:
        out = 0
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 7
        return out
    raise ValueError('Only q=2 or q=4 are checked by direct enumeration')


def dot(x, y, q):
    z = 0
    for a, b in zip(x, y):
        z ^= mul(a, b, q)
    return z


def rank_columns(xrows, q):
    a = [list(row) for row in xrows]
    r, c = len(a), len(a[0])
    h = 0
    for col in range(c):
        good = next((i for i in range(h, r) if a[i][col]), None)
        if good is None:
            continue
        a[h], a[good] = a[good], a[h]
        pivot = a[h][col]
        inv = next(v for v in range(1, q) if mul(v, pivot, q) == 1)
        a[h] = [mul(inv, v, q) for v in a[h]]
        for i in range(r):
            if i != h and a[i][col]:
                scale = a[i][col]
                a[i] = [v ^ mul(scale, w, q) for v, w in zip(a[i], a[h])]
        h += 1
        if h == r:
            break
    return h


def qbinom(n, d, q):
    if d < 0 or d > n:
        return 0
    if d == 0:
        return 1
    num = prod(q**(n-i)-1 for i in range(d))
    den = prod(q**(d-i)-1 for i in range(d))
    assert num % den == 0
    return num // den


def formula(q, b, r):
    terms = {}
    for d in range(min(b, r)+1):
        surjections = prod(q**b-q**i for i in range(d))
        terms[d] = (q**r * qbinom(r, d, q) * surjections
                    * q**(r*(b-d)+d*(d-1)//2))
    return terms


def direct(q, b, r):
    vectors = list(product(range(q), repeat=b))
    involutions = [(x,y) for x in vectors for y in vectors if dot(x,y,q) == 0]
    out = {d:0 for d in range(min(b,r)+1)}
    for tup in product(involutions, repeat=r):
        if any(dot(tup[i][0], tup[j][1], q) != dot(tup[j][0], tup[i][1], q)
               for i in range(r) for j in range(i+1,r)):
            continue
        d = rank_columns([a for a,_ in tup],q)
        out[d] += q**r # independent central coordinates
    return out


def main():
    cases=[(2,1,1),(2,1,2),(2,1,3),(2,1,4),
           (2,2,1),(2,2,2),(2,2,3),(2,3,1),(2,3,2),
           (4,1,1),(4,1,2),(4,1,3),(4,2,1),(4,2,2)]
    for q,b,r in cases:
        want=formula(q,b,r)
        got=direct(q,b,r)
        assert got==want, (q,b,r,got,want)
        print('PASS',q,b,r,sum(got.values()),got)
    print('HEISENBERG_ELEMENTARY_2_HOMS_OK',len(cases),'cases')

if __name__=='__main__':
    main()
