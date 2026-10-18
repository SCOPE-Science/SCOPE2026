"""Exact finite checks for intrinsic volumes of Cayley-tree graphical zonotopes.

Python 3 standard library only. Each algebraic radical is represented by a
squarefree positive integer and a rational coefficient.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import factorial, prod, isqrt


def radical(n):
    assert n > 0
    square = 1
    rem = n
    sf = 1
    p = 2
    while p * p <= rem:
        power = 0
        while rem % p == 0:
            rem //= p
            power += 1
        square *= p ** (power // 2)
        if power % 2:
            sf *= p
        p += 1
    return square, sf * rem


def compositions(n, r):
    if r == 1:
        if n >= 1:
            yield (n,)
        return
    for i in range(1, n-r+2):
        for tail in compositions(n-i, r-1):
            yield (i,) + tail


def assembly(n, r):
    assert 1 <= r <= n
    out = defaultdict(Fraction)
    for sizes in compositions(n, r):
        q = Fraction(factorial(n), factorial(r)) * Fraction(n, 1) ** (r-n)
        for s in sizes:
            q *= Fraction(s**(s-1), factorial(s))
        integer, sf = radical(prod(sizes))
        out[sf] += q * integer
    return dict(out)


def pruefer_tree(seq):
    n = len(seq) + 2
    degrees = [1] * n
    for v in seq:
        degrees[v] += 1
    edges = []
    for v in seq:
        u = next(i for i in range(n) if degrees[i] == 1)
        edges.append((min(u, v), max(u, v)))
        degrees[u] -= 1
        degrees[v] -= 1
    a,b = (i for i in range(n) if degrees[i] == 1)
    edges.append((a,b))
    return tuple(sorted(edges))


def forest_sizes(n, edges):
    parent = list(range(n))
    def root(u):
        while u != parent[u]:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    for u,v in edges:
        ru,rv = root(u),root(v)
        assert ru != rv
        parent[rv] = ru
    counts = defaultdict(int)
    for u in range(n):
        counts[root(u)] += 1
    return tuple(counts.values())


def det_integer(m):
    # Exact integer determinant via fractions, small matrices.
    if not m:
        return 1
    a = [[Fraction(x) for x in row] for row in m]
    det = Fraction(1)
    n = len(m)
    for j in range(n):
        piv = next((i for i in range(j,n) if a[i][j]),None)
        if piv is None:
            return 0
        if piv != j:
            a[j],a[piv] = a[piv],a[j]
            det = -det
        t = a[j][j]
        det *= t
        for i in range(j+1,n):
            rat = a[i][j] / t
            for h in range(j+1,n):
                a[i][h] -= rat*a[j][h]
            a[i][j] = 0
    assert det.denominator == 1
    return int(det)


def gram_det(n, edges):
    k = len(edges)
    cols = []
    for u,v in edges:
        c = [0]*n
        c[u] = 1
        c[v] = -1
        cols.append(c)
    m = [[sum(cols[i][j]*cols[h][j] for j in range(n)) for h in range(k)] for i in range(k)]
    return det_integer(m)


def brute(n,r, check_grams=False):
    accum = defaultdict(Fraction)
    tree_count = 0
    minor_count = 0
    for seq in product(range(n),repeat=n-2):
        edges = pruefer_tree(seq)
        tree_count += 1
        for f in combinations(edges, n-r):
            sizes = forest_sizes(n,f)
            sq = prod(sizes)
            if check_grams:
                assert gram_det(n,f) == sq, (n,r,edges,f,sizes)
            fac,sf=radical(sq)
            accum[sf] += fac
            minor_count += 1
    assert tree_count == n**(n-2)
    return {k:v/tree_count for k,v in accum.items()},minor_count


def main():
    grand_total=0
    for n in range(2,7):
        for r in range(1,n+1):
            if r == 1:
                # Full-dimensional volume is sqrt(n), identically for trees.
                got,_ = brute(n,r,check_grams=n<=6)
            else:
                got,count = brute(n,r,check_grams=n<=6)
                grand_total += count
            want = assembly(n,r)
            assert got == want, (n,r,got,want)
        print('exact Cayley ensemble and Gram checks:',n,'vertices',n**(n-2),'trees')
    # Every seven-vertex labeled tree contributes to the first new codimension.
    got,count = brute(7,3,check_grams=False)
    assert got == assembly(7,3)
    grand_total += count
    print("exact codimension-two check:",7,"vertices",7**5,"trees")
    # A diagnostic first nontrivial codimension-two value.
    assert assembly(5,3) == {1:Fraction(24,5),3:Fraction(18,5)}
    assert assembly(6,3) == {1:Fraction(80,9),6:Fraction(5),2:Fraction(10,9)}
    print('tested forest-subset observations:',grand_total)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
