"""Exact finite-field consistency tests for the critical locus of e_3."""
from itertools import product, combinations
from math import comb


def gradients(point, p):
    n = len(point)
    return tuple(sum(point[j] * point[k]
                     for j in range(n) for k in range(j + 1, n)
                     if j != i and k != i) % p
                 for i in range(n))


def predicted(point, p):
    n = len(point)
    values = set(point)
    if n % p != 2:
        return len(values) == 1 and 0 in values or (
            len([a for a in values if a]) <= 1
            and (sum(v != 0 for v in point) % p == 1 or not any(point)))
    if len(values) == 1:
        return True
    if len(values) != 2:
        return False
    a, b = tuple(values)
    return point.count(a) % p == 1 and point.count(b) % p == 1


def expected_count(n, p):
    if n % p == 2:
        return sum(comb(n, m) for m in range(1, n)
                   if m % p == 1 and (n - m) % p == 1) // 2
    return sum(comb(n, m) for m in range(1, n + 1) if m % p == 1)


def actual_linear_components(n, p):
    allowed = [m for m in range(1, n + 1) if m % p == 1]
    if n % p != 2:
        return {tuple(1 if i in s else 0 for i in range(n))
                for m in allowed for s in combinations(range(n), m)}
    components = set()
    for m in allowed:
        if n - m == 0 or (n - m) % p != 1:
            continue
        for s in combinations(range(n), m):
            mask = tuple(int(i in s) for i in range(n))
            comp = tuple(1 - q for q in mask)
            components.add(min(mask, comp))
    return components


def rank_mod(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    r = 0
    for j in range(cols):
        t = next((i for i in range(r, rows) if a[i][j]), None)
        if t is None:
            continue
        a[t], a[r] = a[r], a[t]
        v = pow(a[r][j], -1, p)
        a[r] = [(x * v) % p for x in a[r]]
        for i in range(rows):
            if i != r:
                q = a[i][j]
                a[i] = [(x - q * y) % p for x, y in zip(a[i], a[r])]
        r += 1
    return r


def hessian(point, p):
    n = len(point)
    return [[0 if i == j else sum(point[k] for k in range(n)
                                 if k != i and k != j) % p
             for j in range(n)] for i in range(n)]


def check(n, p):
    for x in product(range(p), repeat=n):
        assert (not any(gradients(x, p))) == predicted(x, p), (n, p, x)
    comps = actual_linear_components(n, p)
    assert len(comps) == expected_count(n, p)
    dimension = 2 if n % p == 2 else 1
    for mask in comps:
        point = tuple((1 if i else 2) if dimension == 2 else i
                      for i in mask)
        assert not any(gradients(point, p)), (n, p, mask, point)
        assert rank_mod(hessian(point, p), p) == n - dimension, (n, p, mask)
    print(f'field={p}, variables={n}, components={len(comps)}, dimension={dimension}: PASS')


if __name__ == '__main__':
    for p, n in [(3, 3), (3, 4), (3, 5), (3, 6), (3, 8),
                 (5, 3), (5, 5), (5, 6), (5, 7), (7, 3), (7, 5)]:
        check(n, p)
    print('VERIFY_OK')
