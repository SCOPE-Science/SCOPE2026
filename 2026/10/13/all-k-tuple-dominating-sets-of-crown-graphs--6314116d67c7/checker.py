from itertools import combinations
from math import comb

def subsets_indices(n):
    for mask in range(1 << n):
        yield {i for i in range(n) if (mask >> i) & 1}

def direct(n, k, P, Q):
    for i in range(n):
        ca = (1 if i in P else 0) + sum(1 for j in Q if j != i)
        cb = (1 if i in Q else 0) + sum(1 for j in P if j != i)
        if ca < k or cb < k:
            return False
    return True

def criterion(n, k, P, Q):
    p, q = len(P), len(Q)
    if k == 1:
        if p == n and q == 0:
            return True
        if q == n and p == 0:
            return True
    if p < k or q < k:
        return False
    if p == k and not P.issubset(Q):
        return False
    if q == k and not Q.issubset(P):
        return False
    return True

def formula_bivariate(n, k):
    out = {}
    # interior
    for p in range(k + 1, n + 1):
        for q in range(k + 1, n + 1):
            out[p, q] = out.get((p, q), 0) + comb(n, p) * comb(n, q)
    # boundary p=k, P subseteq Q
    for q in range(k, n + 1):
        out[k, q] = out.get((k, q), 0) + comb(n, k) * comb(n - k, q - k)
    # boundary q=k, Q subseteq P
    for p in range(k, n + 1):
        out[p, k] = out.get((p, k), 0) + comb(n, k) * comb(n - k, p - k)
    # diagonal counted twice
    out[k, k] -= comb(n, k)
    if k == 1:
        out[n, 0] = out.get((n, 0), 0) + 1
        out[0, n] = out.get((0, n), 0) + 1
    return {a:b for a,b in out.items() if b}

def formula_univariate(n, k):
    b = formula_bivariate(n, k)
    out = {}
    for (p, q), c in b.items():
        out[p + q] = out.get(p + q, 0) + c
    return out

subset_checks = 0
criterion_checks = 0
bivariate_checks = 0
coefficient_checks = 0
minimum_checks = 0
k_values = 0

for n in range(3, 9):
    subs = list(subsets_indices(n))
    for k in range(1, n + 1):
        k_values += 1
        observed_bi = {}
        observed_uni = {}
        min_size = None
        min_count = 0
        for P in subs:
            for Q in subs:
                subset_checks += 1
                a = direct(n, k, P, Q)
                b = criterion(n, k, P, Q)
                criterion_checks += 1
                if a != b:
                    raise AssertionError(("criterion", n, k, P, Q, a, b))
                if a:
                    key = (len(P), len(Q))
                    observed_bi[key] = observed_bi.get(key, 0) + 1
                    observed_uni[len(P)+len(Q)] = observed_uni.get(len(P)+len(Q), 0) + 1
                    bivariate_checks += 1
                    s = len(P) + len(Q)
                    if min_size is None or s < min_size:
                        min_size, min_count = s, 1
                    elif s == min_size:
                        min_count += 1
        expected_bi = formula_bivariate(n, k)
        expected_uni = formula_univariate(n, k)
        keys = set(observed_bi) | set(expected_bi)
        for key in keys:
            coefficient_checks += 1
            if observed_bi.get(key, 0) != expected_bi.get(key, 0):
                raise AssertionError(("bivariate", n, k, key, observed_bi.get(key, 0), expected_bi.get(key, 0)))
        if observed_uni != expected_uni:
            raise AssertionError(("univariate", n, k, observed_uni, expected_uni))
        minimum_checks += 1
        if min_size != 2 * k or min_count != comb(n, k):
            raise AssertionError(("minimum", n, k, min_size, min_count, 2*k, comb(n,k)))

print(
    "VERIFY_OK n_range=3..8 k_values=%d subset_checks=%d criterion_checks=%d "
    "bivariate_checks=%d coefficient_checks=%d minimum_checks=%d max_order=16"
    % (k_values, subset_checks, criterion_checks, bivariate_checks, coefficient_checks, minimum_checks)
)
