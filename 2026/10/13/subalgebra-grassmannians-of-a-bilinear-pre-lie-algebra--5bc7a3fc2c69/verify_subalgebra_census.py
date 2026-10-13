"""Independent finite-field checks for the bilinear pre-Lie subalgebra census.

Run with Python 3: python3 verify_subalgebra_census.py
The exhaustive part uses prime fields; the general theorem is proved algebraically.
"""
from collections import Counter
from itertools import combinations, product
from math import prod


def rank(rows, q):
    a = [list(row) for row in rows]
    if not a:
        return 0
    piv = 0
    for c in range(len(a[0])):
        k = next((i for i in range(piv, len(a)) if a[i][c] % q), None)
        if k is None:
            continue
        a[piv], a[k] = a[k], a[piv]
        inv = pow(a[piv][c], -1, q)
        a[piv] = [(inv * x) % q for x in a[piv]]
        for i in range(len(a)):
            if i != piv and a[i][c]:
                factor = a[i][c]
                a[i] = [(x - factor * y) % q for x, y in zip(a[i], a[piv])]
        piv += 1
        if piv == len(a):
            break
    return piv


def spaces(n, q):
    """All RREF spanning matrices of subspaces of F_q^n; q prime."""
    for r in range(n + 1):
        for pivots in combinations(range(n), r):
            free = [(i, j) for i, p in enumerate(pivots)
                    for j in range(p + 1, n) if j not in pivots]
            for vals in product(range(q), repeat=len(free)):
                rows = [[0] * n for _ in range(r)]
                for i, p in enumerate(pivots):
                    rows[i][p] = 1
                for (i, j), value in zip(free, vals):
                    rows[i][j] = value
                yield rows


def multiplication(x, y, diagonal, q):
    a, b = x[0], y[0]
    c = 2 * a * b + sum(t * v * w for t, v, w
                            in zip(diagonal, x[1:], y[1:]))
    return [c % q] + [(a * v) % q for v in y[1:]]


def bilinear(x, y, diagonal, q):
    return (x[0] * y[0] + sum(t * v * w for t, v, w
                              in zip(diagonal, x[1:], y[1:]))) % q


def exhaustive(diagonal, q):
    n = len(diagonal)
    out = Counter()
    e = [1] + [0] * n
    for rows in spaces(n + 1, q):
        r = len(rows)
        closed = all(rank(rows + [multiplication(x, y, diagonal, q)], q) == r
                     for x in rows for y in rows)
        contains_e = rank(rows + [e], q) == r
        isotropic = all(bilinear(x, y, diagonal, q) == 0
                        for x in rows for y in rows)
        assert closed == (contains_e or isotropic)
        if closed:
            out[r] += 1
    return out


def chi(x, q):
    x %= q
    return 0 if x == 0 else (1 if pow(x, (q - 1) // 2, q) == 1 else -1)


def gaussian(n, r, q):
    return (prod(q ** (n - i) - 1 for i in range(r)) //
            prod(q ** (r - i) - 1 for i in range(r)))


def predicted(diagonal, q):
    n = len(diagonal)
    dimension = n + 1
    determinant = prod(diagonal) % q
    eta = chi((-1) ** (dimension // 2) * determinant, q) if dimension % 2 == 0 else None
    out = Counter()
    count = 1
    for r in range(dimension // 2 + 1):
        out[r] += count
        d = dimension - 2 * r
        if r < dimension // 2:
            zeros = q ** (d - 1) if d % 2 else (
                q ** (d - 1) + (q - 1) * eta * q ** ((d - 2) // 2))
            num = count * (zeros - 1)
            den = q ** (r + 1) - 1
            assert num % den == 0
            count = num // den
    for k in range(n + 1):
        out[k + 1] += gaussian(n, k, q)
    return out


def main():
    examples = [
        (3, [1]), (3, [2]),
        (3, [1, 1]), (3, [1, 2]),
        (3, [1, 1, 1]), (3, [1, 1, 2]),
        (3, [1, 1, 1, 1]), (3, [1, 1, 1, 2]),
        (5, [1, 1]), (5, [1, 2]),
        (5, [1, 1, 1]), (5, [1, 1, 2]),
    ]
    for q, diag in examples:
        obtained = exhaustive(diag, q)
        expected = predicted(diag, q)
        assert obtained == expected, (q, diag, obtained, expected)
        print(f"GF({q}), diagonal={diag}: "
              f"{dict(sorted(obtained.items()))}")
    assert predicted([1, 1, 1, 1], 3) == predicted([1, 1, 1, 2], 3)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
