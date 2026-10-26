#!/usr/bin/env python3
"""Exact integer checks of ordinary and total domination polynomials of crown graphs."""
from math import comb


def polynomial(n):
    """Independent coefficient implementation of the closed generating polynomial."""
    a = [0] * (n + 1)
    for j in range(2, n + 1):
        a[j] = comb(n, j)
    out = [0] * (2 * n + 1)
    for i in range(n + 1):
        for j in range(n + 1):
            out[i + j] += a[i] * a[j]
    for j in range(n):
        out[j + 2] += 2 * n * comb(n - 1, j)
    out[2] -= n
    out[n] += 2
    return out


def total_polynomial(n):
    a = [0] * (n + 1)
    for j in range(2, n + 1):
        a[j] = comb(n, j)
    return [sum(a[i] * a[k - i] for i in range(n + 1) if 0 <= k - i <= n)
            for k in range(2 * n + 1)]


def exhaustive(n):
    """Directly test closed-neighborhood intersections for every labelled set."""
    width = 2 * n
    closed = []
    for i in range(n):
        closed.append((1 << i) | sum(1 << (n + j) for j in range(n) if j != i))
    for j in range(n):
        closed.append((1 << (n + j)) | sum(1 << i for i in range(n) if i != j))
    ordinary = [0] * (width + 1)
    total = [0] * (width + 1)
    for subset in range(1 << width):
        if all(subset & mask for mask in closed):
            ordinary[subset.bit_count()] += 1
        if all(subset & (mask & ~(1 << v)) for v, mask in enumerate(closed)):
            total[subset.bit_count()] += 1
    return ordinary, total


def strict_log_concave_on_support(c):
    indices = [i for i, v in enumerate(c) if v]
    return all(c[k] * c[k] >= c[k-1] * c[k+1]
               for k in range(indices[0] + 1, indices[-1]))


def main():
    checked = 0
    for n in range(2, 8):
        direct_d, direct_t = exhaustive(n)
        assert direct_d == polynomial(n), (n, direct_d, polynomial(n))
        assert direct_t == total_polynomial(n), (n, direct_t, total_polynomial(n))
        checked += 1 << (2*n)
    for n in range(2, 13):
        d = polynomial(n)
        t = total_polynomial(n)
        assert strict_log_concave_on_support(d), n
        assert strict_log_concave_on_support(t), n
    for n in range(13, 61):
        d = polynomial(n)
        assert d[2] == n and d[3] == 2*n*(n-1)
        assert d[4] == comb(n, 2)**2 + 2*n*comb(n-1, 2)
        defect = d[3]**2 - d[2]*d[4]
        assert defect == -n*n*(n-1)*(n*n-13*n+8)//4 and defect < 0
    for n in range(4, 61):
        d = polynomial(n)
        assert all(d[k] < d[k+1] for k in range(2, n))
        assert all(d[k] > d[k+1] for k in range(n, 2*n))
        assert d[n] == comb(2*n,n)-2*n
        assert all(d[k] == comb(2*n, k) for k in range(n+1,2*n+1))
    print(f'VERIFY_OK direct_subsets={checked} brute_orders=6 finite_logconcave_orders=11 failure_orders=48 strict_modes=57')
    for n in (4, 12, 13):
        d = polynomial(n)
        print('BOUNDARY',n,'d2_d3_d4',d[2:5],'delta3',d[3]**2-d[2]*d[4])


if __name__ == '__main__':
    main()
