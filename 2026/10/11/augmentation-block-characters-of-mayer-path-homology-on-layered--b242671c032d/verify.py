"""Finite exact checks for Mayer-path homology of layered transitive digraphs.

Only Python's standard library is required. Computations are in small finite
fields containing the requisite primitive root of unity. The universal
all-parameter statements are established by the accompanying mathematical proof,
not by these finite tests.
"""
from itertools import combinations, product
from math import prod


def rank_mod(rows, p):
    if not rows:
        return 0
    a = [[v % p for v in row] for row in rows]
    m, n = len(a), len(a[0])
    pivot_count = 0
    for j in range(n):
        t = next((i for i in range(pivot_count, m) if a[i][j]), None)
        if t is None:
            continue
        a[pivot_count], a[t] = a[t], a[pivot_count]
        q = pow(a[pivot_count][j], -1, p)
        a[pivot_count] = [v * q % p for v in a[pivot_count]]
        for i in range(m):
            if i != pivot_count and a[i][j]:
                q = a[i][j]
                a[i] = [(x-q*y) % p for x, y in zip(a[i], a[pivot_count])]
        pivot_count += 1
        if pivot_count == m:
            break
    return pivot_count


def chain_bases(sizes):
    return [
        [tuple(t) for I in combinations(range(len(sizes)), k+1)
         for t in product(*(tuple((i, j) for j in range(sizes[i])) for i in I))]
        for k in range(len(sizes))
    ]


def universal_bases(r, fixed):
    fixed = set(fixed)
    return [[I for I in combinations(range(r), k+1) if fixed.issubset(I)]
            for k in range(r)]


def boundary_matrices(bases, z, p, fixed=()):
    fixed = set(fixed)
    ans = []
    for k in range(len(bases)):
        mat = [[0 for _ in bases[k]] for _ in bases[k-1]] if k else []
        if k:
            lookup = {v: t for t, v in enumerate(bases[k-1])}
            for j, word in enumerate(bases[k]):
                for i, v in enumerate(word):
                    layer = v[0] if isinstance(v, tuple) else v
                    if layer in fixed:
                        continue
                    rem = word[:i] + word[i+1:]
                    if rem in lookup:
                        row = lookup[rem]
                        mat[row][j] = (mat[row][j] + pow(z, i, p)) % p
        ans.append(mat)
    return ans


def matrix_mul(a, b, p):
    if not a:
        return []
    if not b:
        return [[] for _ in a]
    return [[sum(x*y for x, y in zip(row, col)) % p
             for col in zip(*b)] for row in a]


def boundary_power(bases, ds, start, power, p):
    if start < power:
        return []
    mat = ds[start]
    for offset in range(1, power):
        mat = matrix_mul(ds[start-offset], mat, p)
    return mat


def dims(bases, ds, n, q, p):
    answer = []
    for k in range(len(bases)):
        outgoing = (rank_mod(boundary_power(bases, ds, k, q, p), p)
                    if k >= q else 0)
        incoming = (rank_mod(boundary_power(bases, ds, k+n-q, n-q, p), p)
                    if k+n-q < len(bases) else 0)
        answer.append(len(bases[k])-outgoing-incoming)
    return answer


def run():
    tests = {
        (2, 7, 6): [(1, 1, 1), (2, 2, 2), (1, 2, 2, 1)],
        (3, 7, 2): [(1, 1, 1), (1, 2, 1), (2, 2, 2), (2, 3, 2),
                    (3, 3, 3), (1, 1, 1, 1), (1, 2, 2, 2),
                    (2, 1, 2, 3), (1, 2, 1, 2, 1)],
        (4, 5, 2): [(1, 1, 1, 1), (2, 1, 2, 1), (2, 2, 2, 2),
                    (1, 2, 1, 1, 1)],
        (5, 11, 3): [(1, 1, 1, 1, 1), (2, 1, 1, 2, 1)],
    }
    comparisons = 0
    for (n, p, z), cases in tests.items():
        assert pow(z, n, p) == 1
        assert all(pow(z, t, p) != 1 for t in range(1, n))
        for sizes in cases:
            r = len(sizes)
            original = chain_bases(sizes)
            ds = boundary_matrices(original, z, p)
            for k in range(n, r):
                assert rank_mod(boundary_power(original, ds, k, n, p), p) == 0
            for q in range(1, n):
                actual = dims(original, ds, n, q, p)
                expected = [0] * r
                by_size = {}
                for mask in range(1 << r):
                    fixed = tuple(i for i in range(r) if (mask >> i) & 1)
                    bases = universal_bases(r, fixed)
                    u_ds = boundary_matrices(bases, z, p, fixed)
                    coeff = tuple(dims(bases, u_ds, n, q, p))
                    if len(fixed) in by_size:
                        assert by_size[len(fixed)] == coeff
                    else:
                        by_size[len(fixed)] = coeff
                    multiplicity = prod(sizes[i]-1 for i in fixed)
                    expected = [x + multiplicity*y for x, y in zip(expected, coeff)]
                assert actual == expected, (n, q, sizes, actual, expected)
                if r == 3 and n == 3:
                    a, b, c = sizes
                    V, E, F = a+b+c, a*b+a*c+b*c, a*b*c
                    if q == 1:
                        explicit = [2, E-V, (a-1)*(b-1)*(c-1)]
                    else:
                        explicit = [0, V-1, F-V+2]
                    assert actual == explicit, (n, q, sizes, actual, explicit)
                comparisons += 1
    print(f"VERIFY_OK: {comparisons} complete direct-vs-universal Mayer homology comparisons "
          "with canonical block and low-dimensional checks")


if __name__ == '__main__':
    run()
