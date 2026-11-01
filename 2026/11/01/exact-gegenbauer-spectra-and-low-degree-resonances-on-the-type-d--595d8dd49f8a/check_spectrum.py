"""Exact rational cross-checks for harmonic sampling on type-D root directions."""
from fractions import Fraction as Q
from itertools import combinations, product


def gegenbauer_at(n, degree, t):
    lam = Q(n - 2, 2)
    c0, c1 = Q(1), 2 * lam * t
    if degree == 0:
        return c0
    if degree == 1:
        return c1
    for k in range(2, degree + 1):
        c0, c1 = c1, (2 * (k - 1 + lam) * t * c1 - (k - 2 + 2 * lam) * c0) / k
    return c1


def values(n, degree):
    den = gegenbauer_at(n, degree, Q(1))
    a = gegenbauer_at(n, degree, Q(0)) / den
    b = gegenbauer_at(n, degree, Q(1, 2)) / den
    if degree % 2:
        return [2 + 4 * (n - 2) * b, 2 - 4 * b]
    return [2 * (1 - a),
            2 * (1 + a) + 8 * (n - 2) * b + 2 * (n - 2) * (n - 3) * a,
            2 * (1 + a) + 4 * (n - 4) * b - 4 * (n - 3) * a,
            2 * (1 + 3 * a - 4 * b)]


def roots(n):
    return [(i, j, a, b) for i, j in combinations(range(n), 2)
            for a, b in product((-1, 1), repeat=2)]


def dot(r, s):
    i, j, a, b = r
    k, h, c, d = s
    return Q((a*c if i == k else 0) + (a*d if i == h else 0)
             + (b*c if j == k else 0) + (b*d if j == h else 0), 2)


def witnesses(n, deg, R):
    if deg % 2:
        def star(r):
            i, j, a, b = r
            return a if i == 0 else (b if j == 0 else 0)
        def contrast(r):
            i, j, a, b = r
            if i == 0 and j == 1: return a
            if i == 0 and j == 2: return -a
            return 0
        return [[star(r) for r in R], [contrast(r) for r in R]]
    def e(r): return (r[0], r[1])
    def prod(r):return r[2]*r[3] if e(r) == (0,1) else 0
    def all_edges(r): return 1
    def standard(r): return int(0 in e(r)) - int(1 in e(r))
    rectangle = {(0,1):1,(2,3):1,(0,2):-1,(1,3):-1}
    def second(r):return rectangle.get(e(r),0)
    return [[prod(r) for r in R], [all_edges(r) for r in R],
            [standard(r) for r in R], [second(r) for r in R]]


def check(n, deg):
    R = roots(n)
    v = values(n, deg)
    W = witnesses(n, deg, R)
    pol = {t: gegenbauer_at(n, deg, t) / gegenbauer_at(n, deg, Q(1))
           for t in (Q(-1), Q(-1,2), Q(0), Q(1,2), Q(1))}
    for i, row in enumerate(R):
        for k, witness in enumerate(W):
            lhs = sum(pol[dot(row, other)] * a for other, a in zip(R, witness) if a)
            assert lhs == v[k] * witness[i], (n, deg, i, k, lhs, v[k] * witness[i])
    half = n*(n-1)
    if deg % 2:
        multiplicities = [n, n*(n-2)]
    else:
        multiplicities = [n*(n-1)//2, 1, n-1, n*(n-3)//2]
    assert sum(multiplicities) == half
    assert sum(a*b for a,b in zip(multiplicities, v)) == 2*half
    return sum(k for k,s in zip(multiplicities,v) if s != 0)

if __name__ == '__main__':
    tested = 0
    for n in range(5, 10):
        for deg in range(0, 11):
            r = check(n, deg)
            tested += 1
            if deg <= 6:
                half = n*(n-1)
                expected = {0:1, 1:n, 2:n*(n+1)//2-1,
                            3:half, 4:half-(n-1 if n==8 else 0),
                            5:half, 6:half-(1 if n==16 else 0)}[deg]
                assert r == expected, (n,deg,r,expected)
    for n in range(5, 81):
        half = n*(n-1)
        for deg in range(0, 7):
            vv = values(n,deg)
            mm = [n,n*(n-2)] if deg%2 else [half//2,1,n-1,n*(n-3)//2]
            r = sum(k for k,s in zip(mm,vv) if s)
            exp = {0:1,1:n,2:n*(n+1)//2-1,3:half,
                   4:half-(n-1 if n==8 else 0),5:half,
                   6:half-(1 if n==16 else 0)}[deg]
            assert r==exp,(n,deg,r,exp)
    assert values(8,4)[2]==0
    assert values(16,6)[1]==0
    print('PASS: %d exact full-kernel eigenvector tests; %d low-degree rank comparisons; exceptional resonances verified' % (tested, 76*7))
