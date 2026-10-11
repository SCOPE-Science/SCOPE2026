"""Exact integer validation of rank-slab polytope Laplacian formulas.

Run: python3 verify_slab_spectra.py
No non-standard dependencies. Finite enumeration supplements the general proof.
"""
from itertools import combinations
from math import comb, prod


def mul(f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i+j] += x*y
    return out


def sub(f, g):
    out = [0] * max(len(f), len(g))
    for i, x in enumerate(f):
        out[i] += x
    for i, x in enumerate(g):
        out[i] -= x
    return out


def evaluate(f, t):
    out = 0
    for c in reversed(f):
        out = t*out + c
    return out


def blocks(d, a, b):
    data = {}
    for j in range(d//2 + 1):
        low, high = max(a, j), min(b, d-j)
        if low > high:
            continue
        previous, current = [1], []
        for r in range(low, high+1):
            diag = ((d-r) if r < b else 0) + (r if r > a else 0)
            diag += j*(d+1-j) * int(r == a or r == b)
            new = mul([-diag, 1], previous)
            if r > low:
                c2 = (r-j)*(d-j-r+1)
                new = sub(new, [c2*x for x in current])
            current, previous = previous, new
        data[j] = (comb(d,j) - (comb(d,j-1) if j > 0 else 0), previous)
    return data


def determinant(mat):
    """Fraction-free Bareiss determinant for integral square matrices."""
    size = len(mat)
    if not size:
        return 1
    a = [list(row) for row in mat]
    sgn, denom = 1, 1
    for k in range(size-1):
        if a[k][k] == 0:
            p = next((i for i in range(k+1, size) if a[i][k] != 0), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sgn = -sgn
        p = a[k][k]
        for i in range(k+1, size):
            for j in range(k+1, size):
                numerator = a[i][j]*p - a[i][k]*a[k][j]
                assert numerator % denom == 0
                a[i][j] = numerator // denom
            a[i][k] = 0
        denom = p
    return sgn * a[-1][-1]


def graph_laplacian(d, a, b):
    vertices = [sum(1<<i for i in xs)
                for r in range(a, b+1) for xs in combinations(range(d), r)]
    n = len(vertices)
    lap = [[0]*n for _ in range(n)]
    for i, x in enumerate(vertices):
        for k in range(i+1, n):
            y = vertices[k]
            p, q = x.bit_count(), y.bit_count()
            edge = (abs(p-q) == 1 and (x & y).bit_count() == min(p, q))
            edge |= (p == q and p in (a,b) and (x^y).bit_count() == 2)
            if edge:
                lap[i][i] += 1
                lap[k][k] += 1
                lap[i][k] -= 1
                lap[k][i] -= 1
    return lap


def certified_trees(d, a, b, data):
    numerator = prod(d-r for r in range(a, b))
    denominator = comb(d, b)
    for j, (mult, polynomial) in data.items():
        if j:
            det = (-1)**(len(polynomial)-1)*polynomial[0]
            assert det > 0
            numerator *= det**mult
    assert numerator % denominator == 0
    return numerator // denominator


def run():
    pairs, checks, spectra, max_size = 0, 0, 0, 0
    for d in range(2, 11):
        for a in range(d):
            for b in range(a+1, d+1):
                data = blocks(d,a,b)
                n = sum(comb(d,r) for r in range(a,b+1))
                assert sum((len(q)-1)*m for m,q in data.values()) == n
                assert data[0][1][0] == 0
                if 1 in data:
                    e = int(a == 0) + int(b == d)
                    left = mul([0,1], data[1][1])
                    for _ in range(e):
                        left = mul([-2*d,1],left)
                    right = mul([-2*d,1],data[0][1])
                    assert left == right, (d,a,b,'spectral pairing')
                    spectra += 1
                pairs += 1
                if d <= 5:
                    lap = graph_laplacian(d,a,b)
                    exact = determinant([row[:-1] for row in lap[:-1]])
                    assert exact == certified_trees(d,a,b,data), (d,a,b,exact)
                    max_size = max(max_size,n)
                    checks += 1
                    if d <= 4:
                        for t in (-1,0,1,3,2*d+1):
                            direct = determinant([[(t if i == k else 0)-v for k,v in enumerate(row)] for i,row in enumerate(lap)])
                            predicted = prod(evaluate(q,t)**m for m,q in data.values())
                            assert direct == predicted, (d,a,b,t)
    print('VERIFY_OK rank-slab spectral blocks and tree counts',
          'intervals=',pairs,'paired=',spectra,
          'matrix_tree=',checks,'max_vertices=',max_size,
          'full_characteristic_test_d<=4=True')


if __name__ == '__main__':
    run()
