"""Direct finite-field enumeration for a free two-step nilpotent Lie algebra.

Run: python3 verify.py
"""
from itertools import combinations, product
from math import comb


def gaussian(n, k, q):
    if not 0 <= k <= n:
        return 0
    a = 1
    b = 1
    for i in range(k):
        a *= q ** (n - i) - 1
        b *= q ** (k - i) - 1
    return a // b


def predicted(n, q):
    central = comb(n, 2)
    f = []
    for k in range(n):
        m = central - comb(k, 2)
        f.append(sum(gaussian(m, j, q) * q ** (k * (m - j)) for j in range(m + 1)))
    result = {0: f[0] - 1}
    for k in range(1, n):
        deg = sum(gaussian(k, k + ell - n, q) * q ** ((n - k) * (n - ell)) * f[ell]
                  for ell in range(n - k, n))
        assert deg not in result, (n, q, k, deg)
        result[deg] = gaussian(n, k, q) * f[k]
    return result


def rref_subspaces(dim, q):
    for r in range(dim + 1):
        for pivots in combinations(range(dim), r):
            free = [(i, j) for i, p in enumerate(pivots)
                    for j in range(p + 1, dim) if j not in pivots]
            for values in product(range(q), repeat=len(free)):
                rows = [[0] * dim for _ in range(r)]
                for i, p in enumerate(pivots):
                    rows[i][p] = 1
                for (i, j), a in zip(free, values):
                    rows[i][j] = a
                yield tuple(tuple(row) for row in rows)


def rank(vectors, q):
    if not vectors:
        return 0
    rows = [list(v) for v in vectors]
    cols = len(rows[0])
    pivot = 0
    for j in range(cols):
        idx = next((i for i in range(pivot, len(rows)) if rows[i][j] % q), None)
        if idx is None:
            continue
        rows[pivot], rows[idx] = rows[idx], rows[pivot]
        inv = pow(rows[pivot][j], -1, q)
        rows[pivot] = [(inv * x) % q for x in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot and rows[i][j]:
                a = rows[i][j]
                rows[i] = [(x - a * y) % q for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def bracket(x, y, n, q):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return (0,) * n + tuple((x[i] * y[j] - x[j] * y[i]) % q for i, j in pairs)


def is_subalgebra(basis, n, q):
    k = len(basis)
    for i in range(k):
        for j in range(i + 1, k):
            if rank(basis + (bracket(basis[i], basis[j], n, q),), q) > k:
                return False
    return True


def independent_spectrum(n, q):
    dim = n + comb(n, 2)
    subs = [rows for rows in rref_subspaces(dim, q)
            if 0 < len(rows) < dim and is_subalgebra(rows, n, q)]
    degree = [0] * len(subs)
    for i, s in enumerate(subs):
        for j in range(i + 1, len(subs)):
            t = subs[j]
            cross = tuple(bracket(x, y, n, q) for x in s for y in t)
            if rank(s + t + cross, q) == dim:
                degree[i] += 1
                degree[j] += 1
    result = {}
    for value in degree:
        result[value] = result.get(value, 0) + 1
    return result


def main():
    assert gaussian(4, 2, 2) == 35
    for n, q in [(2, 2), (2, 3), (3, 2)]:
        predicted_spectrum = predicted(n, q)
        enumerated = independent_spectrum(n, q)
        assert enumerated == predicted_spectrum, (n, q, predicted_spectrum, enumerated)
        print(f"n={n}, q={q}: {sum(enumerated.values())} vertices; degrees {sorted(enumerated.items())}")
    assert predicted(3, 3) == {0: 27, 1062: 2392, 3072: 1534}
    assert predicted(3, 2) == {0: 15, 116: 357, 378: 203}
    for n in range(3, 8):
        for q in [2, 3, 5]:
            assert len(predicted(n, q)) == n
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
