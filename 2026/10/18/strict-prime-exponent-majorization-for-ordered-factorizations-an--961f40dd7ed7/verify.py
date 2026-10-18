"""Exact finite tests for exponent-transfer inequalities and sum-system transform."""
from functools import lru_cache
from itertools import product
from math import comb, factorial, prod


def c(a, j):
    return sum(
        (-1) ** (j - t) * comb(j, t)
        * prod(comb(e + t - 1, e) for e in a)
        for t in range(j + 1)
    )


@lru_cache(None)
def stirling(n, m):
    if n == m == 0:
        return 1
    if n < 0 or m < 0 or m > n:
        return 0
    return stirling(n - 1, m - 1) + m * stirling(n - 1, m)


def compositions(k, r):
    if r == 1:
        yield (k,)
    else:
        for v in range(1, k - r + 2):
            for rest in compositions(k - v, r - 1):
                yield (v,) + rest


def weak(k, r):
    if r == 1:
        yield (k,)
    else:
        for v in range(k + 1):
            for rest in weak(k - v, r - 1):
                yield (v,) + rest


def direct(a, j):
    # Independent enumeration of weak prime-exponent assignments into j slots.
    return sum(
        all(sum(row[t] for row in rows) > 0 for t in range(j))
        for rows in product(*(list(weak(e, j)) for e in a))
    )


def N(v, m):
    return factorial(m) * sum(stirling(j - 1, m - 1) * c(v, j) for j in range(m, sum(v) + 1))


balancing = factor_comparisons = sum_system_comparisons = 0
for k in range(2, 13):
    for r in range(2, k + 1):
        for a in compositions(k, r):
            original = [c(a, j) for j in range(1, k + 1)]
            assert original[0] == 1
            for u in range(r):
                for v in range(r):
                    if a[u] >= a[v] + 2:
                        b = list(a)
                        b[u] -= 1
                        b[v] += 1
                        updated = [c(b, j) for j in range(1, k + 1)]
                        assert updated[0] == original[0]
                        for j in range(2, k + 1):
                            assert updated[j - 1] > original[j - 1], (k, a, b, j)
                            factor_comparisons += 1
                        for m in range(2, k + 1):
                            assert N(b, m) > N(a, m), (k, a, b, m)
                            sum_system_comparisons += 1
                        balancing += 1

# Splitting any exponent is strictly increasing in every nontrivial length.
splits = 0
for k in range(2, 10):
    for r in range(1, k):
        for a in compositions(k, r):
            for i in range(r):
                for u in range(1, a[i]):
                    b = a[:i] + (u, a[i] - u) + a[i + 1 :]
                    for j in range(2, k + 1):
                        assert c(b, j) > c(a, j), (a, b, j)
                        splits += 1

# Inclusion-exclusion is checked against direct allocation enumeration.
independent = 0
for k in range(2, 7):
    for r in range(1, min(k, 4) + 1):
        for a in compositions(k, r):
            for j in range(1, k + 1):
                assert direct(a, j) == c(a, j), (a, j)
                independent += 1

assert N((2, 1), 2) == 14 and N((2, 1), 3) == 18
print(
    "VERIFY_OK",
    f"balancing_transfers={balancing}",
    f"strict_factor_comparisons={factor_comparisons}",
    f"strict_sum_system_comparisons={sum_system_comparisons}",
    f"strict_split_comparisons={splits}",
    f"direct_matrix_checks={independent}",
)
