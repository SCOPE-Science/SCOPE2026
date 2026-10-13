"""Exact checks for edge-open-packing enumerators of rectangular rook graphs.

Uses only the Python standard library; invoke: python3 eop_rook_verify.py
"""
from collections import Counter
from itertools import combinations
from functools import lru_cache
from math import factorial


def edges_of_rook(m, n):
    cells = [(i, j) for i in range(m) for j in range(n)]
    return [(a, b) for a, b in combinations(cells, 2)
            if a[0] == b[0] or a[1] == b[1]]


def brute_polynomial(m, n, cap=None):
    """Enumerate all edge subsets; test each pair using every third graph edge."""
    edges = edges_of_rook(m, n)
    forbidden = [0] * len(edges)
    for i, (a, b) in enumerate(edges):
        for j, (c, d) in enumerate(edges):
            if j <= i:
                continue
            for k, (u, v) in enumerate(edges):
                if k == i or k == j:
                    continue
                if ((u in (a, b) and v in (c, d)) or
                        (v in (a, b) and u in (c, d))):
                    forbidden[i] |= 1 << j
                    forbidden[j] |= 1 << i
                    break
    totals = Counter()
    if cap is None:
        choices = range(1 << len(edges))
        checked = 1 << len(edges)
    else:
        choices = (sum(1 << j for j in ids)
                   for k in range(cap + 1)
                   for ids in combinations(range(len(edges)), k))
        from math import comb
        checked = sum(comb(len(edges), k) for k in range(cap + 1))
    for subset in choices:
        good = True
        rem = subset
        while rem:
            bit = rem & -rem
            i = bit.bit_length() - 1
            rem ^= bit
            if forbidden[i] & rem:
                good = False
                break
        if good:
            totals[subset.bit_count()] += 1
    return totals, checked


def formula_polynomial(m, n):
    """Triple-coefficient formula from labeled edge-block decomposition."""
    mf, nf = factorial(m), factorial(n)
    out = Counter()
    for a in range(min(m, n // 2) + 1):
        for b in range(min(m // 2, n) + 1):
            for c in range(min(m // 2, n // 2) + 1):
                r = m - a - 2*b - 2*c
                s = n - 2*a - b - 2*c
                if r >= 0 and s >= 0:
                    d = (factorial(r)*factorial(s)*factorial(a)*
                         factorial(b)*factorial(c)*2**(a+b))
                    numerator = mf*nf
                    assert numerator % d == 0
                    out[a+b+2*c] += numerator // d
    return out



@lru_cache(maxsize=None)
def recurrence_polynomial(m, n):
    """Independent distinguished-row recurrence, with edge-degree shifts."""
    if m < 0 or n < 0:
        return Counter()
    if m == 0 or n == 0:
        return Counter({0: 1})
    p = m - 1
    out = Counter(recurrence_polynomial(p, n))
    terms = [(n*(n-1)//2, 1, p, n-2),
             (p*n, 1, p-1, n-1),
             (2*p*n*(n-1), 2, p-1, n-2)]
    for coefficient, shift, r, c in terms:
        if coefficient:
            for k, value in recurrence_polynomial(r, c).items():
                out[k+shift] += coefficient*value
    return out

def expected_degree(m, n):
    k = min(m, n)
    return k - int(m == n and k % 2 == 1)


def main():
    cases = [(0, 0), (0, 3), (1, 1), (1, 2), (1, 3),
             (2, 2), (2, 3), (2, 4), (3, 3)]
    evaluated = 0
    for m, n in cases:
        expected = formula_polynomial(m, n)
        observed, checked = brute_polynomial(m, n)
        assert dict(observed) == dict(expected), (m, n, observed, expected)
        evaluated += checked
        print(f'direct m={m}, n={n}: edge_subsets={checked}, polynomial={sorted(expected.items())}')
    bounded_total = 0
    for m, n in [(3, 4), (4, 4)]:
        expected = formula_polynomial(m, n)
        observed, checked = brute_polynomial(m, n, cap=expected_degree(m, n))
        assert dict(observed) == dict(expected), (m, n, observed, expected)
        bounded_total += checked
        print(f'bounded m={m}, n={n}: checked_through_degree={expected_degree(m,n)}, '
              f'candidate_subsets={checked}, polynomial={sorted(expected.items())}')
    parameter_pairs = 0
    for m in range(0, 15):
        for n in range(0, 15):
            counts = formula_polynomial(m, n)
            assert counts[0] == 1
            assert max(counts) == expected_degree(m, n), (m, n, counts)
            assert counts[1] == m*n*(m+n-2)//2 if m*n else counts[1] == 0
            assert counts == formula_polynomial(n, m), (m, n)
            assert counts == recurrence_polynomial(m, n), (m, n)
            parameter_pairs += 1
    print(f'EXACT_CHECKS_OK direct_subsets={evaluated} bounded_subsets={bounded_total} parameter_pairs={parameter_pairs}')


if __name__ == '__main__':
    main()
