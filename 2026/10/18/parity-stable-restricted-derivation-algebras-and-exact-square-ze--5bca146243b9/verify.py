"""Reproducible finite-field checks of truncated-derivation rank distributions.

Run with Python 3; no external packages or data required. Finite checks
corroborate the separately stated symbolic theorem and do not prove all cases.
"""
from collections import Counter
from itertools import product


def multiply(a, b, q):
    if q == 2:
        return a & b
    if q == 4:  # F_2[w]/(w*w + w + 1), coefficients stored as bit pairs
        a0, a1, b0, b1 = a & 1, a >> 1, b & 1, b >> 1
        return (a0 * b0 ^ a1 * b1) | ((a0 * b1 ^ a1 * b0 ^ a1 * b1) << 1)
    raise ValueError("Only the explicitly tested fields F2 and F4 are implemented")


def matrix_of_derivation(f, q):
    n = len(f)
    out = [[0] * n for _ in range(n)]
    for j in range(1, n, 2):
        for i in range(n - j + 1):
            out[i + j - 1][j] = f[i]
    return out


def rank(mat, q):
    a = [row[:] for row in mat]
    nr, nc = len(a), len(a[0])
    inverses = {x: next(y for y in range(1, q) if multiply(x, y, q) == 1)
                for x in range(1, q)}
    r = 0
    for j in range(nc):
        pivot = next((i for i in range(r, nr) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = inverses[a[r][j]]
        a[r] = [multiply(inv, x, q) for x in a[r]]
        for i in range(nr):
            if i != r and a[i][j]:
                c = a[i][j]
                a[i] = [x ^ multiply(c, y, q) for x, y in zip(a[i], a[r])]
        r += 1
    return r


def square_zero(mat, q):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            v = 0
            for k in range(n):
                v ^= multiply(mat[i][k], mat[k][j], q)
            if v:
                return False
    return True


def lift(f):
    n = len(f)
    out = [0] * (n + 1)
    for i, c in enumerate(f):
        out[i if i % 2 else i + 2] = c
    return out


def theoretical(q, s):
    h = s // 2
    d = {0: 1}
    for r in range(1, s + 1):
        d[r] = (q * q - 1) * q ** (2 * r - 2) if r <= h else (q - 1) * q ** (s - 1)
    return Counter(d)


def check(q, s):
    even_counts = Counter()
    odd_counts = Counter()
    n = 2 * s
    for coefficients in product(range(q), repeat=n):
        f = list(coefficients)
        even = matrix_of_derivation(f, q)
        odd = matrix_of_derivation(lift(f), q)
        # The linear embedding J maps basis monomials t^j as specified.
        for j in range(n):
            jj = j if j % 2 else j + 2
            for i in range(n):
                ii = i if i % 2 else i + 2
                assert even[i][j] == odd[ii][jj]
        assert all(v == 0 for v in odd[0])
        assert all(odd[i][0] == 0 for i in range(n + 1))
        a, b = square_zero(even, q), square_zero(odd, q)
        assert a == b
        if a:
            even_counts[rank(even, q)] += 1
            odd_counts[rank(odd, q)] += 1
    assert even_counts == theoretical(q, s), (q, s, even_counts, theoretical(q, s))
    assert odd_counts == even_counts
    assert sum(even_counts.values()) == q ** s + (s // 2) * (q - 1) * q ** (s - 1)
    print(f"F_{q}, s={s}: {dict(sorted(even_counts.items()))}")


if __name__ == '__main__':
    for field_order, maximal_s in [(2, 4), (4, 3)]:
        for s in range(1, maximal_s + 1):
            check(field_order, s)
    print('VERIFY_OK_EVEN_ODD_DERIVATIONS')
