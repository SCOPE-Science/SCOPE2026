#!/usr/bin/env python3
"""Self-contained finite-field checks for exterior-multiplication Jordan spectra.

Runs Gaussian recurrences, exhausts all cubic alternating forms in six variables
 over F_2, and checks wedge-multiplication matrices over F_2 and F_4.
"""
from collections import Counter
from itertools import combinations
from math import comb
from random import Random


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    numer = 1
    denom = 1
    for j in range(1, k + 1):
        numer *= q ** (n - k + j) - 1
        denom *= q ** j - 1
    assert numer % denom == 0
    return numer // denom


def full_support_counts(n, q):
    f = [0] * (n + 1)
    f[0] = 1
    for m in range(1, n + 1):
        f[m] = q ** comb(m, 3) - sum(gaussian(m, j, q) * f[j] for j in range(m))
    return f


def formula(n, q):
    f = full_support_counts(n, q)
    counts = {0: 1}
    for r in range(1, n + 1):
        count = gaussian(n, r, q) * f[r]
        if count:
            counts[2 + 2 * r] = count
    assert sum(counts.values()) == q ** comb(n, 3)
    return counts


def exhaustive_six_binary():
    n = 6
    triples = list(combinations(range(n), 3))
    pairs = list(combinations(range(n), 2))
    pair_pos = {pair: i for i, pair in enumerate(pairs)}
    updates = []
    for a, b, c in triples:
        updates.append(((a, 1 << pair_pos[(b, c)]),
                        (b, 1 << pair_pos[(a, c)]),
                        (c, 1 << pair_pos[(a, b)])))
    rows = [0] * n
    counts = Counter()
    for i in range(1 << len(triples)):
        if i:
            j = (i & -i).bit_length() - 1
            for row, bit in updates[j]:
                rows[row] ^= bit
        basis = [0] * 15
        rank = 0
        for row in rows:
            v = row
            while v:
                k = v.bit_length() - 1
                if basis[k]:
                    v ^= basis[k]
                else:
                    basis[k] = v
                    rank += 1
                    break
        counts[0 if i == 0 else 2 + 2 * rank] += 1
    return dict(counts)


def gf_mul(a, b, q):
    if q == 2:
        return a & b
    assert q == 4
    # F4 = F2[z]/(z*z+z+1), polynomial basis encoding.
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return result


def field_rank(columns, q):
    bases = {}
    nrows = len(columns[0]) if columns else 0
    rank = 0
    for col in columns:
        v = col[:]
        while any(v):
            pivot = next(j for j in range(nrows) if v[j])
            if pivot in bases:
                w = bases[pivot]
                coeff = v[pivot]
                for j in range(pivot, nrows):
                    v[j] ^= gf_mul(coeff, w[j], q)
            else:
                c = v[pivot]
                inv = next(z for z in range(1, q) if gf_mul(c, z, q) == 1)
                for j in range(pivot, nrows):
                    v[j] = gf_mul(v[j], inv, q)
                bases[pivot] = v
                rank += 1
                break
    return rank


def direct_rank_and_radical(n, q, coeffs):
    full = (1 << n) - 1
    triples = list(combinations(range(n), 3))
    pair_indices = list(combinations(range(n), 2))
    map_u = {}
    for triple, scalar in zip(triples, coeffs):
        t = sum(1 << i for i in triple)
        map_u[full ^ t] = scalar
    contraction_cols = []
    for i in range(n):
        contraction_cols.append([
            coeffs[triples.index(tuple(sorted((i, j, k))))]
            if i != j and i != k else 0 for j, k in pair_indices
        ])
    support_rank = field_rank(contraction_cols, q)
    columns = []
    for subset in range(1 << n):
        if subset.bit_count() > 3:
            continue
        vector = [0] * (1 << n)
        for monomial, scalar in map_u.items():
            if not subset & monomial:
                vector[subset | monomial] ^= scalar
        columns.append(vector)
    direct_rank = field_rank(columns, q)
    return direct_rank, support_rank


def main():
    for q in (2, 4, 8):
        for n in range(6, 12):
            counts = formula(n, q)
            f = full_support_counts(n, q)
            assert all(v >= 0 for v in f)
            assert f[1] == f[2] == f[4] == 0 and f[3] > 0
            assert all(f[r] > 0 for r in range(5, n + 1))
        print('Gaussian inversion and support spectra checked for q=', q, 'n=6..11')
    expected = formula(6, 2)
    observed = exhaustive_six_binary()
    assert observed == expected, (observed, expected)
    print('Full GF(2) six-variable cubic census:', dict(sorted(observed.items())))
    rng = Random(214006)
    for q in (2, 4):
        for n in (6, 7):
            for trial in range(90):
                form = [rng.randrange(q) for _ in range(comb(n, 3))]
                if not any(form):
                    continue
                actual, contraction = direct_rank_and_radical(n, q, form)
                assert actual == 2 + 2 * contraction, (q, n, actual, contraction)
            print('Direct wedge matrices passed 90 GF(%d) tests for n=%d' % (q, n))
    print('All checks PASS')


if __name__ == '__main__':
    main()
