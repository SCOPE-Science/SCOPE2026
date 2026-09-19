#!/usr/bin/env python3
from itertools import product
from fractions import Fraction


def mat_rank(flat, rows, cols, q):
    a = [list(flat[i*cols:(i+1)*cols]) for i in range(rows)]
    rank = 0
    for c in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][c] % q), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][c] % q, -1, q)
        a[rank] = [(x * inv) % q for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][c] % q:
                f = a[i][c] % q
                a[i] = [(x - f*y) % q for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def matmul(U, V, k, r, n, q):
    out = []
    for i in range(k):
        for j in range(n):
            out.append(sum(U[i*r+h] * V[h*n+j] for h in range(r)) % q)
    return tuple(out)


def p_full(a, b, q):
    p = Fraction(1, 1)
    for j in range(a):
        p *= Fraction(q**b - q**j, q**b)
    return p


def check_case(q, k, r, n):
    hist = {}
    total = q ** (k*r + r*n)
    for U in product(range(q), repeat=k*r):
        for V in product(range(q), repeat=r*n):
            M = matmul(U, V, k, r, n, q)
            hist[M] = hist.get(M, 0) + 1

    Q = Fraction(1, q**(k*n))
    tv = Fraction(0, 1)
    deficient_min_ratio = None
    full_ratios = set()
    for M in product(range(q), repeat=k*n):
        P = Fraction(hist.get(tuple(M), 0), total)
        d = mat_rank(M, k, n, q)
        tv += abs(P - Q)
        ratio = P / Q
        if d < k:
            deficient_min_ratio = ratio if deficient_min_ratio is None else min(deficient_min_ratio, ratio)
        else:
            full_ratios.add(ratio)
    tv /= 2

    expected = p_full(k, n, q) * (1 - p_full(k, r, q))
    assert tv == expected, (q, k, r, n, tv, expected)
    assert deficient_min_ratio is None or deficient_min_ratio >= 1
    assert full_ratios == {p_full(k, r, q)}
    return total, tv


def main():
    cases = [
        (2, 1, 1, 2),
        (2, 2, 2, 3),
        (2, 2, 3, 4),
        (3, 1, 1, 2),
        (3, 2, 2, 3),
        (5, 1, 1, 2),
    ]
    total_pairs = 0
    for case in cases:
        pairs, tv = check_case(*case)
        total_pairs += pairs
        print(f"q,k,r,n={case}: pairs={pairs}, TV={tv}")
    print(f"PASS: {len(cases)} cases, {total_pairs} factor pairs checked")


if __name__ == '__main__':
    main()
