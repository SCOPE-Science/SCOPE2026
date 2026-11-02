#!/usr/bin/env python3
"""Independent finite tests for the total-domination enumerator of K_m x K_n.

Only standard-library integer arithmetic is used.  Finite checks corroborate,
not replace, the symbolic case classification and proof in RESULT.md.
"""
from math import comb


def prod(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def sum_into(dst, src, factor=1):
    for i, a in enumerate(src):
        dst[i] += factor * a


def binomial(d):
    return [comb(d, j) for j in range(d + 1)]


def E(d):
    # d * ((1+z)^(d-1) - 1 - (d-1)*z)
    out = [0] * d
    for j in range(2, d):
        out[j] = d * comb(d - 1, j)
    return out


def formula(m, n):
    N = m * n
    fail = [0] * (N + 1)
    fail[0] = 1
    sum_into(fail, binomial(n), m)
    fail[0] -= m
    sum_into(fail, binomial(m), n)
    fail[0] -= n
    fail[1] -= m * n
    fail[2] += 2 * comb(m, 2) * comb(n, 2)
    fail[3] += 4 * comb(m, 2) * comb(n, 2)
    sum_into(fail, prod([0, 1, 1], E(n)), 2 * comb(m, 2))
    sum_into(fail, prod([0, 1, 1], E(m)), 2 * comb(n, 2))
    sum_into(fail, prod([1, 1], prod(E(m), E(n))))
    return [comb(N, j) - fail[j] for j in range(N + 1)]


def direct_adj_count(m, n):
    # Directly apply open-neighborhood total domination, without use of
    # row-column cross criterion or the formula's supporting case analysis.
    N = m * n
    neighborhoods = []
    for i in range(m):
        for j in range(n):
            mask = 0
            for a in range(m):
                for b in range(n):
                    if i != a and j != b:
                        mask |= 1 << (a * n + b)
            neighborhoods.append(mask)
    counts = [0] * (N + 1)
    for mask in range(1 << N):
        good = True
        for nbrs in neighborhoods:
            if mask & nbrs == 0:
                good = False
                break
        if good:
            counts[mask.bit_count()] += 1
    return counts


def structural_non_dom(m, n, mask):
    # Independent test of characterization: support fits in a row + column.
    active = [(a, b) for a in range(m) for b in range(n)
              if (mask >> (a * n + b)) & 1]
    return any(all(a == i or b == j for a, b in active)
               for i in range(m) for j in range(n))


def check():
    tests = [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
             (3, 3), (3, 4), (3, 5), (4, 4), (4, 5)]
    checked = 0
    for m, n in tests:
        actual = direct_adj_count(m, n)
        expected = formula(m, n)
        assert actual == expected, (m, n, expected, actual)
        checked += 1 << (m * n)
        assert all(a >= 0 for a in expected)
        assert sum(expected) + sum(comb(m*n, j)-expected[j]
                                   for j in range(m*n+1)) == 2 ** (m*n)
        if min(m, n) == 2:
            k = max(m, n)
            q = binomial(k)
            q[0] = q[1] = 0
            assert expected == prod(q, q)
            assert expected[4] == comb(k, 2)**2
        else:
            assert expected[3] == 6 * comb(m, 3) * comb(n, 3)
        assert expected[-1] == 1
        assert all(expected[i] == comb(m*n, i)
                   for i in range(m+n, m*n+1))
        assert expected == formula(n, m)
    # Check cross characterization independently against open neighborhoods.
    for m, n in [(2, 3), (3, 3), (3, 4)]:
        neighborhoods = [sum((1 << (a*n+b)) for a in range(m) for b in range(n)
                             if a != i and b != j)
                         for i in range(m) for j in range(n)]
        for s in range(1 << (m*n)):
            fail_direct = any(s & neighbors == 0 for neighbors in neighborhoods)
            assert fail_direct == structural_non_dom(m, n, s)
    # Distinct arithmetical checks beyond brute-force range.
    for m in range(2, 27):
        for n in range(2, 27):
            coeffs = formula(m, n)
            assert len(coeffs) == m*n + 1
            assert all(x >= 0 for x in coeffs)
            assert coeffs[-1] == 1
            assert coeffs == formula(n, m)
            assert not any(coeffs[:3])
            low = 4 if min(m,n) == 2 else 3
            assert not any(coeffs[:low])
            assert coeffs[low] == (comb(max(m, n),2)**2 if low==4
                                  else 6*comb(m,3)*comb(n,3))
            assert all(coeffs[i] == comb(m*n,i) for i in range(m+n, m*n+1))
    print('DIRECT_SUBSETS_CHECKED', checked)
    print('DIRECT_GRAPHS_CHECKED', len(tests))
    print('EXACT_ARITHMETIC_PAIRS', 25*25)
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
