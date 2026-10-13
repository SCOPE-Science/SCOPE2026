from itertools import combinations
from math import comb
from collections import Counter


def vertices(n):
    return [('a', i) for i in range(n)] + [('b', i) for i in range(n)]


def adjacent(u, v):
    return u[0] != v[0] and u[1] != v[1]


def is_super_dominating(n, D):
    V = vertices(n)
    D = set(D)
    T = [v for v in V if v not in D]
    for t in T:
        ok = False
        for d in D:
            if adjacent(d, t):
                outside_neighbors = {w for w in T if adjacent(d, w)}
                if outside_neighbors == {t}:
                    ok = True
                    break
        if not ok:
            return False
    return True


def criterion(n, D):
    D = set(D)
    I = {i for i in range(n) if ('a', i) not in D}
    J = {i for i in range(n) if ('b', i) not in D}
    if n == 3:
        return len(I) + len(J) <= 2
    if len(I) > 2 or len(J) > 2:
        return False
    if (len(I) == 2 or len(J) == 2) and (I & J):
        return False
    return True


def predicted_bivariate(n):
    c = Counter()
    if n == 3:
        c[(3, 3)] += 1
        c[(2, 3)] += 3
        c[(3, 2)] += 3
        c[(2, 2)] += 9
        c[(1, 3)] += 3
        c[(3, 1)] += 3
        return c
    c[(n, n)] += 1
    c[(n-1, n)] += n
    c[(n, n-1)] += n
    c[(n-1, n-1)] += n*n
    c[(n-2, n)] += comb(n, 2)
    c[(n, n-2)] += comb(n, 2)
    c[(n-2, n-1)] += comb(n, 2)*(n-2)
    c[(n-1, n-2)] += comb(n, 2)*(n-2)
    c[(n-2, n-2)] += comb(n, 2)*comb(n-2, 2)
    return c

subset_checks = 0
classification_checks = 0
coefficient_checks = 0
minimum_checks = 0
for n in range(3, 9):
    V = vertices(n)
    actual = Counter()
    for mask in range(1 << (2*n)):
        D = {V[k] for k in range(2*n) if mask & (1 << k)}
        a = is_super_dominating(n, D)
        b = criterion(n, D)
        subset_checks += 1
        classification_checks += 1
        assert a == b, (n, mask, a, b)
        if a:
            actual[(sum(1 for v in D if v[0]=='a'), sum(1 for v in D if v[0]=='b'))] += 1
    pred = predicted_bivariate(n)
    keys = set(actual) | set(pred)
    for key in keys:
        coefficient_checks += 1
        assert actual[key] == pred[key], (n, key, actual[key], pred[key])
    min_size = min(i+j for i,j in actual)
    min_count = sum(v for (i,j),v in actual.items() if i+j == min_size)
    if n == 3:
        assert min_size == 4 and min_count == 15
    else:
        assert min_size == 2*n-4
        assert min_count == comb(n,2)*comb(n-2,2)
    minimum_checks += 1

print(f"VERIFY_OK n_range=3..8 subset_checks={subset_checks} classification_checks={classification_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=16")
