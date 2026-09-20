#!/usr/bin/env python3
"""Exhaustive check of the H_2(q) formula for q=2,3 over prime fields."""
from itertools import combinations, product


def qbinom(n, k, q):
    if k < 0 or k > n:
        return 0
    k = min(k, n-k)
    num = den = 1
    for i in range(1, k+1):
        num *= q**(n-k+i) - 1
        den *= q**i - 1
    return num // den


def isotropic_count(m, r, q):
    if r < 0 or r > m:
        return 0
    out = qbinom(m, r, q)
    for i in range(r):
        out *= q**(m-i) + 1
    return out


def disjoint_count(M, a, b, q):
    return sum(
        (-1)**j * q**(j*(j-1)//2) * qbinom(a, j, q)
        * isotropic_count(M-j, b-j, q)
        for j in range(min(a, b)+1)
    )


def pair_count(m, r, s, t, q):
    return (
        isotropic_count(m, t, q)
        * isotropic_count(m-t, r-t, q)
        * disjoint_count(m-t, r-t, s-t, q)
    )


def orthogonal_pair_count(m, r, s, t, q):
    d = r+s-t
    if d > m:
        return 0
    return (
        isotropic_count(m, d, q)
        * qbinom(d, t, q)
        * qbinom(d-t, r-t, q)
        * q**((r-t)*(s-t))
    )


def formula_counts(m, q):
    center = sum(qbinom(2*m, k, q) for k in range(2*m+1))
    graphs = sum(q**r * isotropic_count(m, r, q) for r in range(m+1))
    total = center + graphs
    bad = sum(
        (pair_count(m, r, s, t, q) - orthogonal_pair_count(m, r, s, t, q))
        * q**(r+s-t)
        for r in range(m+1)
        for s in range(m+1)
        for t in range(min(r, s)+1)
    )
    return total, total*total-bad, bad


def rank_mod(rows, p):
    a = [list(map(lambda x: x % p, row)) for row in rows if any(x % p for x in row)]
    if not a:
        return 0
    ncol = len(a[0])
    r = 0
    for c in range(ncol):
        pivot = next((i for i in range(r, len(a)) if a[i][c] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(inv*x) % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] % p:
                f = a[i][c] % p
                a[i] = [(x-f*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def contains(basis, v, p):
    return rank_mod(basis + [v], p) == rank_mod(basis, p)


def all_subspaces(n, p):
    out = []
    cols = range(n)
    for k in range(n+1):
        for pivots in combinations(cols, k):
            free_cols = [j for j in cols if j not in pivots]
            positions = [(i, j) for i, pv in enumerate(pivots) for j in free_cols if j > pv]
            for vals in product(range(p), repeat=len(positions)):
                rows = [[0]*n for _ in range(k)]
                for i, pv in enumerate(pivots):
                    rows[i][pv] = 1
                for (i, j), val in zip(positions, vals):
                    rows[i][j] = val
                out.append(tuple(tuple(row) for row in rows))
    return out


def bracket_h2(a, b, p):
    z = (a[0]*b[1] - a[1]*b[0] + a[2]*b[3] - a[3]*b[2]) % p
    return (0, 0, 0, 0, z)


def is_subalgebra(basis, p):
    for a in basis:
        for b in basis:
            if not contains(list(basis), bracket_h2(a, b, p), p):
                return False
    return True


def permute(A, B, p):
    nonzero_bracket = any(bracket_h2(a, b, p)[4] for a in A for b in B)
    if not nonzero_bracket:
        return True
    z = (0, 0, 0, 0, 1)
    return contains(list(A) + list(B), z, p)


def exhaustive(p):
    spaces = all_subspaces(5, p)
    subs = [U for U in spaces if is_subalgebra(U, p)]
    good = sum(1 for A in subs for B in subs if permute(A, B, p))
    bad = len(subs)**2 - good
    return len(spaces), len(subs), good, bad


def main():
    for p in (2, 3):
        all_count, total, good, bad = exhaustive(p)
        f_total, f_good, f_bad = formula_counts(2, p)
        assert (total, good, bad) == (f_total, f_good, f_bad)
        print(
            f"q={p}: vector_subspaces={all_count}, lie_subalgebras={total}, "
            f"permutable_ordered_pairs={good}, nonpermutable_ordered_pairs={bad}"
        )
    print("all checks passed")


if __name__ == "__main__":
    main()
