#!/usr/bin/env python3
"""Finite consistency checks for the complete-bipartite graph-state SLD formula."""
from itertools import product
from math import comb


def zero_sum_count(p, t):
    return ((p - 1) ** t + (p - 1) * ((-1) ** t)) // p


def nonzero_sum_count(p, t):
    return (p - 1) ** t - zero_sum_count(p, t)


def poly_z(p, r):
    out = [0] * (r + 1)
    for t in range(r + 1):
        out[t] = comb(r, t) * zero_sum_count(p, t)
    return out


def poly_n(p, r):
    out = [0] * (r + 1)
    for t in range(r + 1):
        out[t] = comb(r, t) * nonzero_sum_count(p, t)
    return out


def add_shifted(dst, src, shift, scale=1):
    for i, value in enumerate(src):
        dst[i + shift] += scale * value


def conv(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def formula_counts(p, m, n):
    out = [0] * (m + n + 1)
    zz = conv(poly_z(p, m), poly_z(p, n))
    add_shifted(out, zz, 0)
    add_shifted(out, poly_n(p, n), m, p ** (m - 1))
    add_shifted(out, poly_n(p, m), n, p ** (n - 1))
    out[m + n] += (p - 1) ** 2 * p ** (m + n - 2)
    return out


def brute_counts(p, m, n):
    out = [0] * (m + n + 1)
    for r in product(range(p), repeat=m + n):
        ra, rb = r[:m], r[m:]
        sa, sb = sum(ra) % p, sum(rb) % p
        weight = sum(1 for x in ra if x != 0 or sb != 0)
        weight += sum(1 for x in rb if x != 0 or sa != 0)
        out[weight] += 1
    return out


def run():
    cases = [(2, 2, 2), (2, 2, 3), (2, 3, 2), (2, 2, 4),
             (3, 2, 2), (3, 2, 3), (3, 3, 2)]
    for p, m, n in cases:
        expected = formula_counts(p, m, n)
        actual = brute_counts(p, m, n)
        assert expected == actual, (p, m, n, expected, actual)
        assert expected[0] == 1
        assert sum(expected) == p ** (m + n)
        print(f"PASS p={p} m={m} n={n}: total={sum(expected)}; coefficients match")
    print("PASS all finite consistency checks; these checks are not the general proof")


if __name__ == "__main__":
    run()
