"""Independent exhaustive checks for square-zero derivations on truncated polynomials.

Run: python research11_sqzero_verifier.py
Uses direct matrices for derivations, rather than the coefficient criterion of the proof.
"""
from collections import Counter
from itertools import product


def mul(a, b, q, poly):
    if q == 2:
        return a & b
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= poly
    return out


def field_tables(q, poly):
    assert q in (2, 4, 8)
    times = [[mul(x, y, q, poly) for y in range(q)] for x in range(q)]
    inv = [None] * q
    for x in range(1, q):
        for y in range(1, q):
            if times[x][y] == 1:
                inv[x] = y
    assert all(x is not None for x in inv[1:])
    return times, inv


def matrix_rank(mat, q, table, inv):
    a = [list(row) for row in mat]
    rows, cols = len(a), len(a[0])
    r = 0
    for col in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scalar = inv[a[r][col]]
        a[r] = [table[scalar][x] for x in a[r]]
        for i in range(rows):
            if i != r and a[i][col]:
                v = a[i][col]
                a[i] = [x ^ table[v][y] for x, y in zip(a[i], a[r])]
        r += 1
        if r == rows:
            break
    return r


def histogram_formula(M, q):
    h = Counter({0: 1})
    for r in range(1, M + 1):
        h[r] += (q - 1) * q ** (r - 1)
    for j in range((M + 1) // 2, M):
        bcount = (q - 1) * q ** (M - j - 1)
        h[M-j] += bcount * q ** (M-j)
        for alpha in range(M-j, j):
            h[M-alpha] += bcount * (q - 1) * q ** (M-alpha-1)
    assert sum(h.values()) == q**M + (M//2) * (q-1) * q**(M-1)
    return h


def enumerate_derivations(M, q, poly):
    n = 2*M
    table, inv = field_tables(q, poly)
    histogram = Counter()
    for f in product(range(q), repeat=n):
        # D(x^j) = (j mod 2) x^(j-1) f (truncated)
        mat = [[0]*n for _ in range(n)]
        for j in range(1, n, 2):
            for k in range(n-j+1):
                mat[k+j-1][j] = f[k]
        # Independent square-zero test by direct matrix composition.
        square_zero = True
        for i in range(n):
            for j in range(n):
                s = 0
                for k in range(n):
                    s ^= table[mat[i][k]][mat[k][j]]
                if s:
                    square_zero = False
                    break
            if not square_zero:
                break
        if square_zero:
            histogram[matrix_rank(mat, q, table, inv)] += 1
    return histogram


def main():
    configs = [(2,1,0b11), (2,2,0b11), (2,3,0b11), (2,4,0b11),
               (2,5,0b11), (2,6,0b11), (4,1,0b111), (4,2,0b111),
               (4,3,0b111), (8,1,0b1011), (8,2,0b1011)]
    for q, M, poly in configs:
        counted = enumerate_derivations(M,q,poly)
        predicted = histogram_formula(M,q)
        assert counted == predicted, (q,M,counted,predicted)
        print(f'FIELD={q} LENGTH={2*M} TOTAL={sum(counted.values())} RANKS={dict(sorted(counted.items()))}')
    for q in (2, 4, 8):
        for M in range(1, 80):
            assert sum(histogram_formula(M,q).values()) == q**M+(M//2)*(q-1)*q**(M-1)
    print('VERIFY_OK: 11 exhaustive matrix cases and 237 symbolic total-count checks')

if __name__ == '__main__':
    main()
