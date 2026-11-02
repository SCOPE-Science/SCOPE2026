"""Exact independent tests of triangle/open-wedge covariance in random graphs.

Run: python check.py
Standard library only; exhaustive checks are finite diagnostics, not a proof of
universal identities. The analytic proof is given in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def moments_by_edge_count(n):
    edges = list(combinations(range(n), 2))
    triples = list(combinations(range(n), 3))
    groups = [[0, 0, 0, 0] for _ in range(len(edges) + 1)]
    for edge_mask in range(1 << len(edges)):
        edge_set = {edge for j, edge in enumerate(edges) if (edge_mask >> j) & 1}
        t = s = 0
        for v in triples:
            edge_count = sum((v[i], v[j]) in edge_set
                             for i, j in ((0, 1), (0, 2), (1, 2)))
            t += (edge_count == 3)
            s += (edge_count == 2)
        m = edge_mask.bit_count()
        groups[m][0] += 1
        groups[m][1] += t
        groups[m][2] += s
        groups[m][3] += t * s
    return groups


def fixed_cov(n, m):
    N = comb(n, 2)
    q = m * (n * n - 3 * n - 8) + (n - 1) * (n * n - n - 4)
    return Fraction(-4 * m * (m - 1) * (m - 2) * (N - m) * (N - m - 1) * q,
                    (n + 1)**2 * (n + 2) * (N - 5) * (N - 4) * (N - 2)**2)


def independent_cov(n, p):
    return 3 * comb(n, 3) * p**4 * (1 - p) * ((n - 3) * (2 - 3*p) - p)


def falling_ratio(m, N, k):
    if m < k:
        return Fraction(0)
    out = Fraction(1)
    for i in range(k):
        out *= Fraction(m - i, N - i)
    return out


def overlap_cov(n, m):
    N = comb(n, 2)
    A = comb(n, 3)
    B = 3 * A
    f = {k: falling_ratio(m, N, k) for k in range(2, 7)}
    p2, p3, p4, p5, p6 = (f[i] for i in range(2, 7))
    ctw = A * (3*(p3-p3*p2) + 6*(n-3)*(p4-p3*p2)
               + (B-3-6*(n-3))*(p5-p3*p2))
    var_t = A * ((p3-p3*p3) + 3*(n-3)*(p5-p3*p3)
                 + (A-1-3*(n-3))*(p6-p3*p3))
    return ctw - 3*var_t


def main():
    checks = 0
    for n in range(4, 7):
        N = comb(n, 2)
        groups = moments_by_edge_count(n)
        assert sum(group[0] for group in groups) == 2**N
        for m, (count, sum_t, sum_s, sum_ts) in enumerate(groups):
            assert count == comb(N, m)
            direct = Fraction(sum_ts, count) - Fraction(sum_t*sum_s, count*count)
            assert direct == overlap_cov(n, m) == fixed_cov(n, m), (n, m)
            assert (direct < 0) == (3 <= m <= N-2), (n, m)
            checks += 4
        for p in (Fraction(1, 4), Fraction(1, 3), Fraction(1, 2),
                  Fraction(2, 3), Fraction(4, 5)):
            st = ss = sts = Fraction(0)
            for m, (count, sum_t, sum_s, sum_ts) in enumerate(groups):
                weight = p**m * (1-p)**(N-m)
                st += sum_t*weight
                ss += sum_s*weight
                sts += sum_ts*weight
            assert sts-st*ss == independent_cov(n, p), (n, p)
            checks += 1
    for n in range(4, 31):
        N = comb(n, 2)
        for m in range(N + 1):
            assert overlap_cov(n, m) == fixed_cov(n, m), (n, m)
            assert (fixed_cov(n, m) < 0) == (3 <= m <= N-2), (n, m)
            checks += 2
    print(f"PASS: {checks} exact comparisons; n=4..6 exhaustive; n=4..30 symbolic-ratio grid.")


if __name__ == '__main__':
    main()
