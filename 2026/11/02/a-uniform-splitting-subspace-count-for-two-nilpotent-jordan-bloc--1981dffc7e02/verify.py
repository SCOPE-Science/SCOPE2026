"""Finite tests for the two-block nilpotent splitting-space theorem.

Run with: python verify.py
Uses only the Python standard library. Finite checks support, but do not
replace, the proof for arbitrary prime powers and unbounded block length.
"""
from itertools import product


def rank(rows, p, n):
    pivots = {}
    for row in rows:
        x = [int(t) % p for t in row]
        for j in range(n):
            if x[j] == 0:
                continue
            if j in pivots:
                c = x[j]
                x = [(a - c*b) % p for a, b in zip(x, pivots[j])]
            else:
                k = pow(x[j], -1, p)
                pivots[j] = [(k*a) % p for a in x]
                break
    return len(pivots)


def shift(v, length_a, length_b):
    a, b = v[:length_a], v[length_a:]
    return (0,) + a[:-1] + ((0,) + b[:-1] if length_b else ())


def splitting(u, v, d, r, p):
    a, b = d+r, d-r
    columns = []
    for _ in range(d):
        columns.extend((u, v))
        u, v = shift(u, a, b), shift(v, a, b)
    return rank(columns, p, 2*d) == 2*d


def count_normalized(d, r, p):
    a, b = d+r, d-r
    n = 2*d
    count = 0
    for up in product(range(p), repeat=n-2):
        u = (1,) + up[:a-1] + (0,) + up[a-1:]
        for vp in product(range(p), repeat=n-2):
            v = (0,) + vp[:a-1] + (1,) + vp[a-1:]
            count += splitting(u, v, d, r, p)
    return count


def det_nonzero(matrix, p):
    return rank(matrix, p, len(matrix)) == len(matrix)


def count_nonsingular_hankel(r, p):
    count = 0
    for coeff in product(range(p), repeat=2*r-1):
        h = [[coeff[i+j] for j in range(r)] for i in range(r)]
        count += det_nonzero(h, p)
    return count


def independent_grassmann_count(d, r):
    """Enumerate ALL 2-subspaces over F2, not just normalized complements."""
    n = 2*d
    representatives = set()
    vecs = list(product((0, 1), repeat=n))
    for u in vecs[1:]:
        for v in vecs[1:]:
            if u == v:
                continue
            vectors = tuple(sorted({tuple(x^y for x,y in zip(u,v)), u, v}))
            representatives.add(vectors)
    count = 0
    for subspace in representatives:
        u,v = subspace[:2]
        count += splitting(u,v,d,r,2)
    expected_total = ((2**n - 1)*(2**n-2))//6
    assert len(representatives) == expected_total, (len(representatives),expected_total)
    return count


def main():
    cases = [(3,0,2),(3,1,2),(3,2,2),(3,2,3),
             (4,0,2),(4,1,2),(4,2,2),(4,3,2)]
    for d,r,p in cases:
        actual = count_normalized(d,r,p)
        expected = p**(4*d-4) if r == 0 else (p-1)*p**(4*d-5)
        assert actual == expected, (d,r,p,actual,expected)
        print('SPLIT_OK',d,r,p,actual)
    for r in range(1,5):
        for p in (2,3):
            actual = count_nonsingular_hankel(r,p)
            expected = (p-1)*p**(2*r-2)
            assert actual == expected, (r,p,actual,expected)
            print('HANKEL_OK',r,p,actual)
    for r in (0,1,2):
        actual = independent_grassmann_count(3,r)
        expected = 2**8 if r==0 else 2**7
        assert actual == expected,(r,actual,expected)
        print('GRASSMANN_OK',3,r,2,actual)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
