#!/usr/bin/env python3
"""Exact integer certificate for low-weight Roman functions of cycle prisms."""
from collections import Counter, defaultdict
from itertools import product

ALPHABET = tuple((a, b) for a in range(3) for b in range(3))
STATES = tuple((a, b) for a in range(9) for b in range(9))
INDEX = {s: i for i, s in enumerate(STATES)}
H = (
    (-1, -1, -1, -1, -1, -1, -1, -1, -2),
    ( 0,  0,  0,  0,  0,  0, -1, -1, -1),
    ( 0,  0,  0,  0,  0,  0,  0,  0,  0),
    ( 0,  0, -1,  0,  0, -1,  0,  0, -1),
    ( 0,  0,  0,  0,  0,  0,  0,  0,  0),
    ( 0,  0,  0,  0,  0,  0,  0,  0,  0),
    ( 0,  0,  0,  0,  0,  0,  0,  0,  0),
    ( 0,  0,  0,  0,  0,  0,  0,  0,  0),
    ( 0,  0,  0,  0,  0,  0,  0,  0,  0),
)

def admissible(left, middle, right):
    a, b = ALPHABET[left], ALPHABET[middle]
    c = ALPHABET[right]
    return ((b[0] != 0 or 2 in (a[0], b[1], c[0])) and
            (b[1] != 0 or 2 in (a[1], b[0], c[1])))

def build_matrices():
    mat = [[defaultdict(int) for _ in range(81)] for _ in range(2)]
    hist = Counter()
    for (a, b) in STATES:
        i = INDEX[a, b]
        for c in range(9):
            if not admissible(a, b, c):
                continue
            j = INDEX[b, c]
            cost = sum(ALPHABET[b]) - 1 + H[a][b] - H[b][c]
            assert cost >= 0, (a, b, c, cost)
            hist[cost] += 1
            if cost <= 1:
                mat[cost][i][j] += 1
    assert sum(hist.values()) == 601 and hist[0] == 104 and hist[1] == 299
    return [{j: int(v) for j, v in row.items()} for row in mat[0]], [
        {j: int(v) for j, v in row.items()} for row in mat[1]]

def matmul(x, y):
    ret = []
    for row in x:
        acc = defaultdict(int)
        for k, a in row.items():
            for j, b in y[k].items():
                acc[j] += a*b
        ret.append({j: v for j, v in acc.items() if v})
    return ret

def trace(x):
    return sum(row.get(i, 0) for i, row in enumerate(x))

def direct_polynomial(n):
    # Independent vertex-neighborhood implementation (not using the local transfer).
    neighbors = [[] for _ in range(2*n)]
    for i in range(n):
        for r in range(2):
            v = r*n+i
            neighbors[v] = [r*n+(i-1)%n, r*n+(i+1)%n, (1-r)*n+i]
    result = Counter()
    for f in product(range(3), repeat=2*n):
        if all(f[v] or any(f[u] == 2 for u in neighbors[v]) for v in range(2*n)):
            result[sum(f)] += 1
    return result

def transfer_polynomial(n):
    result = Counter()
    for cols in product(range(9), repeat=n):
        if all(admissible(cols[(i-1)%n], cols[i], cols[(i+1)%n]) for i in range(n)):
            result[sum(sum(ALPHABET[c]) for c in cols)] += 1
    return result

def claimed(n):
    if n == 3:
        return n+1, 15
    if n % 4 == 0:
        return n, 4
    return n+1, 2*n if n % 4 == 2 else 4*n

def main():
    b0, b1 = build_matrices()
    eye = [{i: 1} for i in range(81)]
    p = [eye]
    for _ in range(7):
        p.append(matmul(p[-1], b0))
    assert p[3] == p[7]  # Exact entrywise identity, implies 4-periodicity from exponent 3.
    zero_traces = [trace(p[n]) for n in range(3, 7)]
    first_ratios = [trace(matmul(b1, p[n-1])) for n in range(3, 8)]
    assert zero_traces == [0, 4, 0, 0]
    assert first_ratios == [5, 6, 4, 2, 4]
    for n in range(3, 7):
        brute = direct_polynomial(n)
        trans = transfer_polynomial(n)
        assert brute == trans, (n, brute, trans)
        k, multiplicity = claimed(n)
        assert min(brute) == k and brute[k] == multiplicity
        if n == 4:
            assert brute[n+1] == 6*n
    for n in range(3, 101):
        if n == 3:
            a0 = trace(p[3]); a1 = n*first_ratios[0]
        else:
            a0 = zero_traces[(n-3)%4]
            a1 = n*first_ratios[1+(n-4)%4]
        k, m = claimed(n)
        assert (a0 if k==n else a1) == m
        assert (a0 == 0) == (k==n+1)
        if n >= 4 and n%4==0:
            assert a1 == 6*n
    print('VERIFY_OK states=81 edges=601 potential_nonnegative=yes')
    print('VERIFY_OK matrix_identity=B0^3=B0^7 zero_traces_3..6=',zero_traces)
    print('VERIFY_OK first_ratios_3..7=',first_ratios)
    print('VERIFY_OK independent_full_polynomial_bruteforce_n=3..6 assignments=',sum(3**(2*n) for n in range(3,7)))
    print('VERIFY_OK coefficient_laws_n=3..100 exact_identity_used=yes')

if __name__ == '__main__':
    main()
