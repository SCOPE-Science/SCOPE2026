#!/usr/bin/env python3
"""Finite-field independent spot checks for commuting schemes of almost-abelian Lie algebras.

Run with Python 3; no external packages are required.
"""
from collections import Counter
from itertools import product


def rank_mod_p(rows, p):
    if not rows:
        return 0
    a = [[v % p for v in row] for row in rows]
    m, n = len(a), len(a[0])
    rr = 0
    for cc in range(n):
        pivot = next((i for i in range(rr, m) if a[i][cc]), None)
        if pivot is None:
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        inv = pow(a[rr][cc], -1, p)
        a[rr] = [(inv * x) % p for x in a[rr]]
        for i in range(rr + 1, m):
            if a[i][cc]:
                factor = a[i][cc]
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[rr])]
        rr += 1
        if rr == m:
            break
    return rr


def bracket(x, z, D, p):
    n = len(D)
    out = [0] * n
    for i in range(n):
        out[i] = sum(D[i][j] * (x[0] * z[j + 1] - z[0] * x[j + 1])
                     for j in range(n)) % p
    return tuple(out)


def joint_rank(xs, D, p):
    n = len(D)
    # Construct the actual joint bracket matrix on all n+1 domain generators.
    basis = [tuple(int(j == i) for j in range(n + 1)) for i in range(n + 1)]
    columns = [tuple(v for x in xs for v in bracket(x, b, D, p)) for b in basis]
    rows = list(zip(*columns))
    return rank_mod_p(rows, p)


def expected(p, n, r, s):
    k = n - r
    factor = p ** (k * s)
    vals = [(0, factor), (1, factor * (p ** (r*s) - 1)),
            (r, factor * (p**s - 1) * p**r),
            (r+1, factor * (p**s - 1) * (p**(r*s) - p**r))]
    c = Counter()
    for rank, num in vals:
        c[rank] += num
    return dict(c)


def census(p, D, s):
    n = len(D)
    elements = list(product(range(p), repeat=n + 1))
    tally = Counter()
    for xs in product(elements, repeat=s):
        tally[joint_rank(xs, D, p)] += 1
    pred = expected(p, n, rank_mod_p(D, p), s)
    assert dict(tally) == pred, (p, n, s, dict(tally), pred)
    # Independently count pairwise commuting tuples from the actual Lie bracket.
    pairwise = 0
    for xs in product(elements, repeat=s):
        if all(not any(bracket(xs[i], xs[j], D, p))
               for i in range(s) for j in range(i+1, s)):
            pairwise += 1
    r = rank_mod_p(D, p)
    k = n-r
    predicted_pairs = p**(n*s) + p**(k*s+r)*(p**s - 1)
    assert pairwise == predicted_pairs, (p,n,s,pairwise,predicted_pairs)
    print(f"F_{p}, dim={n+1}, r={r}, s={s}: adjoint_ranks={dict(sorted(tally.items()))}, commuting_tuples={pairwise}")


def main():
    D31 = [[0,1,0,0], [0,0,1,0], [0,0,0,0], [0,0,0,0]]
    D22 = [[0,1,0,0], [0,0,0,0], [0,0,0,1], [0,0,0,0]]
    D3 = [[0,1,0],[0,0,1],[0,0,0]]
    for p,D,s in ((2,D31,2),(2,D22,2),(2,D31,3),(2,D22,3),
                  (3,D31,2),(3,D22,2),(3,D3,2)):
        census(p,D,s)
    assert rank_mod_p(D31,2) == rank_mod_p(D22,2) == 2
    assert rank_mod_p([[sum(D31[i][j]*D31[j][k] for j in range(4)) for k in range(4)] for i in range(4)], 2) == 1
    assert rank_mod_p([[sum(D22[i][j]*D22[j][k] for j in range(4)) for k in range(4)] for i in range(4)], 2) == 0
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
