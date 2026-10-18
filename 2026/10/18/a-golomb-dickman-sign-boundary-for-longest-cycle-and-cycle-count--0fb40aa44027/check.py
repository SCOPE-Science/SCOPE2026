"""Reproduce finite checks for largest-cycle / cycle-count covariance.
Uses standard-library exact rational arithmetic only.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations


def stats(perm):
    n = len(perm)
    visited = [False] * n
    counts = [0] * (n + 1)
    largest = 0
    for v in range(n):
        if not visited[v]:
            w = v
            s = 0
            while not visited[w]:
                visited[w] = True
                s += 1
                w = perm[w]
            counts[s] += 1
            largest = max(largest, s)
    return largest, counts


def exhaustive(n):
    total = 0
    max_sum = 0
    c_sum = [0] * (n + 1)
    product_sum = [0] * (n + 1)
    for pi in permutations(range(n)):
        M, C = stats(pi)
        total += 1
        max_sum += M
        for r in range(1, n + 1):
            c_sum[r] += C[r]
            product_sum[r] += C[r] * M
    mean_M = F(max_sum, total)
    return mean_M, [F(product_sum[r], total) - mean_M * F(c_sum[r], total) for r in range(n + 1)]


def exact_cdfs(max_n):
    """P(M_n<=k), by a recursion based on the uniform cycle of label 1."""
    out = [[F(0) for k in range(max_n + 1)] for n in range(max_n + 1)]
    for k in range(max_n + 1):
        out[0][k] = F(1)
        for n in range(1, max_n + 1):
            out[n][k] = sum((out[n-j][k] for j in range(1, min(n, k) + 1)), F(0)) / n
    return out


def main():
    nmax = 35
    cdf = exact_cdfs(nmax)
    means = [sum((F(1)-cdf[n][k] for k in range(n)), F(0)) for n in range(nmax + 1)]
    assert means[0] == 0
    for n in range(2, nmax+1):
        for r in range(1, n+1):
            mm = n-r
            conditional_max = r + sum((F(1)-cdf[mm][k] for k in range(r,mm)), F(0))
            cov = (conditional_max - means[n])/r
            assert (cov > 0) == (r > means[n])
            assert (cov < 0) == (r < means[n])
            assert (cov == 0) == (r == means[n])
            if r <= n//2:
                assert cov < 0
            if 2*r>n:
                assert cov == (F(r)-means[n])/r
    for n in range(2, 9):
        brute_mean, brute_cov = exhaustive(n)
        assert brute_mean == means[n]
        for r in range(1, n+1):
            mm = n-r
            cond = r + sum((F(1)-cdf[mm][k] for k in range(r,mm)), F(0))
            assert brute_cov[r] == (cond-means[n])/r
    for n in (3, 5, 8, 12, 20, 35):
        print('n', n, 'E[M_n]', means[n], 'cut', int(means[n]),
              'C_-', 'r<=',int(means[n]),'C_+','r>=',int(means[n])+1)
    print('PASS: exact recurrence n<=35; exhaustive permutation enumeration n<=8.')

if __name__ == '__main__':
    main()
