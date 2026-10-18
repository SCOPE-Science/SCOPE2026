#!/usr/bin/env python3
"""Exact finite checks for induced two-path/triangle covariance in G(n,m) and G(n,p)."""
from fractions import Fraction
from itertools import combinations
from math import comb, prod


def falling(a, k):
    if k > a:
        return 0
    return prod(a - i for i in range(k))


def fixed_cov_counts(n, m):
    N = comb(n, 2)
    if not (0 <= m <= N):
        raise ValueError("edge count outside range")
    q = lambda j: Fraction(falling(m, j), falling(N, j))
    H, W = comb(n, 3), n * comb(n - 1, 2)
    cov_tw = H * ((W - 6 * (n - 3) - 3) * (q(5) - q(3) * q(2))
                  + 6 * (n - 3) * (q(4) - q(3) * q(2))
                  + 3 * (q(3) - q(3) * q(2)))
    var_t = H * ((H - 1 - 3 * (n - 3)) * (q(6) - q(3)**2)
                 + 3 * (n - 3) * (q(5) - q(3)**2)
                 + q(3) - q(3)**2)
    return cov_tw - 3 * var_t


def fixed_cov_factored(n, m):
    N = comb(n, 2)
    B = m * (n*n - 3*n - 8) + n**3 - 2*n*n - 3*n + 4
    denom = (n + 1)**2 * (n + 2) * (n*n - n - 10) * (n*n - n - 8) * (n*n - n - 4)**2
    return Fraction(-64*m*(m-1)*(m-2)*(N-m)*(N-m-1)*B, denom)


def bernoulli_cov(n, p):
    return 3 * comb(n, 3) * p**4 * (1-p) * (2*(n-3) - (3*n-8)*p)


def enumerate_statistics(n):
    ed = list(combinations(range(n), 2))
    ed_index = {e: i for i, e in enumerate(ed)}
    triad = [tuple(ed_index[tuple(sorted(e))] for e in combinations(vertices, 2))
             for vertices in combinations(range(n), 3)]
    out = [[0, 0, 0, 0] for _ in range(len(ed)+1)]
    for graph in range(1 << len(ed)):
        m = graph.bit_count()
        triangles = opens = 0
        for a, b, c in triad:
            num = ((graph >> a) & 1) + ((graph >> b) & 1) + ((graph >> c) & 1)
            triangles += (num == 3)
            opens += (num == 2)
        row = out[m]
        row[0] += 1
        row[1] += triangles
        row[2] += opens
        row[3] += triangles * opens
    return out


def checks():
    tested = 0
    allgraphs = 0
    for n in (4, 5, 6):
        N = comb(n, 2)
        rows = enumerate_statistics(n)
        allgraphs += 1 << N
        for m, (cnt, sumt, sumo, sumto) in enumerate(rows):
            assert cnt == comb(N, m)
            empirical = Fraction(sumto, cnt) - Fraction(sumt*sumo, cnt*cnt)
            assert empirical == fixed_cov_counts(n, m)
            assert empirical == fixed_cov_factored(n, m)
            assert (empirical < 0) == (3 <= m <= N-2)
            tested += 4
        for p in (Fraction(1, 4), Fraction(2, 5), Fraction(1, 2), Fraction(3, 4)):
            weights = [p**m*(1-p)**(N-m) for m in range(N+1)]
            Et = sum(row[1]*weights[m] for m, row in enumerate(rows))
            Eo = sum(row[2]*weights[m] for m, row in enumerate(rows))
            Eto = sum(row[3]*weights[m] for m, row in enumerate(rows))
            assert Eto - Et*Eo == bernoulli_cov(n, p)
            tested += 1
    for n in range(4, 61):
        N = comb(n, 2)
        for m in (0, 1, 2, 3, 4, N//4, N//2, 3*N//4, N-2, N-1, N):
            if not 0 <= m <= N:
                continue
            assert fixed_cov_counts(n, m) == fixed_cov_factored(n, m)
            tested += 1
    print(f"PASS; exact checks={tested}; exhaustively enumerated simple graphs={allgraphs}")

if __name__ == '__main__':
    checks()
