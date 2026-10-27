"""Standalone exact checks for the Heisenberg Nijenhuis classification.
Run with Python 3.9+; no external dependencies.  This is a finite
cross-check of the universal proof in RESULT.md, not a proof by search.
"""
from collections import Counter
from itertools import product
from random import Random


def rank(matrix, p):
    a = [[entry % p for entry in row] for row in matrix]
    n = len(a)
    m = len(a[0]) if n else 0
    r = 0
    for col in range(m):
        pivot = next((i for i in range(r, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [inv * x % p for x in a[r]]
        for i in range(n):
            if i != r and a[i][col]:
                c = a[i][col]
                a[i] = [(x-c*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r


def omega(v, w, n, p):
    return sum(v[i]*w[n+i]-v[n+i]*w[i] for i in range(n)) % p


def bracket(v, w, n, p):
    return [0]*(2*n) + [omega(v, w, n, p)]


def mv(A, v, p):
    return [sum(a*b for a, b in zip(row, v)) % p for row in A]


def torsion_zero(N, n, p):
    d = 2*n+1
    base = [[int(i == j) for i in range(d)] for j in range(d)]
    for i in range(d):
        for j in range(i+1, d):
            x, y = base[i], base[j]
            nx, ny = mv(N, x, p), mv(N, y, p)
            b = bracket(x, y, n, p)
            b1 = bracket(nx, y, n, p)
            b2 = bracket(x, ny, n, p)
            nb = mv(N, b, p)
            rhs = mv(N, [(a+b-c) % p for a, b, c in zip(b1, b2, nb)], p)
            if bracket(nx, ny, n, p) != rhs:
                return False
    return True


def criterion(N, n, p):
    d = 2*n
    if any(N[i][d] % p for i in range(d)):
        return False
    c = N[d][d]
    B = [[(N[i][j] - (c if i == j else 0)) % p for j in range(d)] for i in range(d)]
    cols = [[B[i][j] for i in range(d)] for j in range(d)]
    return all(omega(v, w, n, p) == 0 for v in cols for w in cols)


def isotropic_count(n, r, q):
    numerator = 1
    denominator = 1
    for j in range(r):
        numerator *= q**(2*n-j)-q**j
        denominator *= q**r-q**j
    assert numerator % denominator == 0
    return numerator//denominator


def surjection_count(n, r, q):
    value = 1
    for j in range(r):
        value *= q**(2*n)-q**j
    return value


def predicted(n, q):
    counts = Counter()
    for r in range(n+1):
        b = isotropic_count(n, r, q)*surjection_count(n, r, q)
        counts[(r, r)] = q*b*q**r
        counts[(r, r+1)] = q*b*(q**(2*n)-q**r)
    return counts


def exhaustive_three_dimensional(p):
    tally = Counter()
    for entries in product(range(p), repeat=9):
        N = [list(entries[3*i:3*i+3]) for i in range(3)]
        fact = torsion_zero(N, 1, p)
        crit = criterion(N, 1, p)
        assert fact == crit, (p, N, fact, crit)
        if fact:
            c = N[2][2]
            B = [[(N[i][j]-(c if i==j else 0)) % p for j in range(2)] for i in range(2)]
            centered = [[(N[i][j]-(c if i==j else 0)) % p for j in range(3)] for i in range(3)]
            tally[(rank(B, p), rank(centered, p))] += 1
    assert tally == predicted(1, p), (p, tally, predicted(1, p))
    return sum(tally.values())


def exhaustive_five_dimensional_binary():
    # Enumerates all possible 4-by-4 B, not all 2^25 endomorphisms.
    p, n, d = 2, 2, 4
    tally = Counter()
    satisfying = []
    for entries in product(range(p), repeat=d*d):
        B = [list(entries[d*i:d*i+d]) for i in range(d)]
        cols = [[B[i][j] for i in range(d)] for j in range(d)]
        if all(omega(v,w,n,p)==0 for v in cols for w in cols):
            tally[rank(B,p)] += 1
            satisfying.append(B)
    expected = {r:isotropic_count(n,r,p)*surjection_count(n,r,p) for r in range(n+1)}
    assert dict(tally) == expected, (tally, expected)
    assert dict(tally) == {0:1, 1:225, 2:3150}
    return satisfying


def random_checks():
    rng = Random(20261022)
    binary = exhaustive_five_dimensional_binary()
    for p in (2, 3, 5):
        n, d = 2, 4
        for trial in range(1200):
            N = [[rng.randrange(p) for _ in range(d+1)] for _ in range(d+1)]
            assert torsion_zero(N,n,p) == criterion(N,n,p)
        for trial in range(600):
            c = rng.randrange(p)
            if p == 2:
                B = binary[rng.randrange(len(binary))]
            else:
                # A rank-at-most-one B always has isotropic image.
                u = [rng.randrange(p) for _ in range(d)]
                v = [rng.randrange(p) for _ in range(d)]
                B = [[u[i]*v[j] % p for j in range(d)] for i in range(d)]
            ell = [rng.randrange(p) for _ in range(d)]
            N = [[(B[i][j]+(c if i==j else 0)) % p for j in range(d)] + [0] for i in range(d)]
            N.append(ell+[c])
            assert criterion(N,n,p)
            assert torsion_zero(N,n,p)
    assert sum(predicted(2,2).values()) == 108032


if __name__ == '__main__':
    print('h3 exhaustive F2:', exhaustive_three_dimensional(2))
    print('h3 exhaustive F3:', exhaustive_three_dimensional(3))
    random_checks()
    print('h5 F2 isotropic ranks:', {r:isotropic_count(2,r,2)*surjection_count(2,r,2) for r in range(3)})
    print('HEISENBERG_NIJENHUIS_OK')
