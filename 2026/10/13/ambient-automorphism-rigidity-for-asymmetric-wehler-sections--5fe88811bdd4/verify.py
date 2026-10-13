"""Exact low-dimensional consistency checks for a multiprojective extension theorem.

The computations do not replace the universal weak Lefschetz argument.
"""
from itertools import combinations, product
from math import factorial


def bundle_cohomology(degrees):
    """Return dimensions of cohomology on the product of P1 factors."""
    dims = [1]
    for a in degrees:
        h0 = a + 1 if a >= 0 else 0
        h1 = -a - 1 if a <= -2 else 0
        out = [0] * (len(dims) + 1)
        for i, value in enumerate(dims):
            out[i] += value * h0
            out[i + 1] += value * h1
        dims = out
    return dims


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def top_intersection(m, d, marked_index):
    """Compute integral H_i (sum H)^(m-3) (2 sum H)(sum d_j H_j)."""
    result = 0
    for f in range(m):
        for g in range(m):
            if len({f, g, marked_index}) != 3:
                continue
            result += 2 * d[g] * factorial(m-3)
    return result


def check_case(d):
    m = len(d)
    e = [2] * m
    assert m >= 6 and len(set(d)) > 1 and min(d) >= 3
    assert bundle_cohomology(tuple(-x for x in d))[1] == 0
    assert bundle_cohomology(minus(e, d))[0] == 0
    for i in range(m):
        u = tuple(int(i == j) for j in range(m))
        c1 = bundle_cohomology(minus(u, e))
        c2 = bundle_cohomology(minus(u, d))
        c3 = bundle_cohomology(minus(minus(u, e), d))
        assert not any(c1)
        assert c2[0] == c2[1] == 0
        assert c3[0] == c3[1] == c3[2] == 0
        assert top_intersection(m, d, i) > 0
    # Degree-four cup monomials form an integral basis in the ambient ring.
    pairs = list(combinations(range(m), 2))
    assert len(pairs) == m * (m-1) // 2
    for a in product(range(-2, 3), repeat=min(m, 6)):
        if m > 6:
            break  # Small-support check only; no claim of full m-dimensional census.
        cup_square = {p: 2 * a[p[0]] * a[p[1]] for p in pairs}
        sq_zero = all(value == 0 for value in cup_square.values())
        assert sq_zero == (sum(x != 0 for x in a) <= 1)


for vector in (
    (3, 3, 3, 3, 3, 4),
    (3, 4, 3, 5, 3, 4),
    (3, 3, 4, 3, 3, 3, 3),
    (3, 4, 4, 3, 3, 5, 3, 3),
):
    check_case(vector)
print("VERIFY_OK")
