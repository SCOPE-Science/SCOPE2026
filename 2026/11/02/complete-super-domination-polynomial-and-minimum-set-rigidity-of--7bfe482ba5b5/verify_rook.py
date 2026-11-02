"""Standalone exact super-domination verifier for labeled rook graphs.

No external packages needed: python3 verify_rook.py
The finite checks corroborate, but do not replace, the general proof.
"""
from functools import lru_cache
from itertools import combinations
from math import comb


def add(*polys):
    out = [0] * max(map(len, polys))
    for poly in polys:
        for i, a in enumerate(poly):
            out[i] += a
    return tuple(out)


def scale(poly, amount, shift=0):
    return (0,) * shift + tuple(amount * a for a in poly)


@lru_cache(None)
def forests(rows, cols):
    """Counts all labeled bipartite star forests with the given part sizes."""
    if rows == 0:
        return (1,)
    options = [forests(rows - 1, cols)]  # distinguished row isolated
    for leaves in range(1, cols + 1):
        options.append(scale(forests(rows - 1, cols - leaves),
                             comb(cols, leaves), leaves))
    if cols:
        for leaves in range(2, rows + 1):
            options.append(scale(forests(rows - leaves, cols - 1),
                                 cols * comb(rows - 1, leaves - 1), leaves))
    return add(*options)


def isolated_both(rows, cols):
    options = []
    for a in range(1, rows + 1):
        for b in range(1, cols + 1):
            options.append(scale(forests(rows - a, cols - b),
                          (-1) ** (a + b) * comb(rows, a) * comb(cols, b)))
    return add(*options)


def onto(codomain, domain):
    return sum((-1) ** j * comb(codomain, j) * (codomain - j) ** domain
               for j in range(codomain + 1))


def formula(rows, cols):
    polynomial = list(isolated_both(rows, cols))
    polynomial.extend([0] * max(0, max(rows, cols) + 1 - len(polynomial)))
    polynomial[rows] += cols ** rows - onto(cols, rows)
    polynomial[cols] += rows ** cols - onto(rows, cols)
    return tuple(polynomial)


def neighborhoods(rows, cols):
    size = rows * cols
    return [sum(1 << (i * cols + j)
                for i in range(rows) for j in range(cols)
                if (i == a) != (j == b))
            for a in range(rows) for b in range(cols)]


def direct_super_dominating(omitted, neighbors, universe):
    # Explicitly inspect selected vertices and their omitted neighbors.
    witnesses = 0
    for vertex, vicinity in enumerate(neighbors):
        if (omitted >> vertex) & 1:
            continue
        outside = vicinity & omitted
        if outside and (outside & (outside - 1)) == 0:
            witnesses |= outside
        if witnesses == omitted:
            return True
    return witnesses == omitted


def brute_counts(rows, cols):
    size = rows * cols
    neighbors = neighborhoods(rows, cols)
    out = [0] * (size + 1)
    for omitted in range(1 << size):
        if direct_super_dominating(omitted, neighbors, (1 << size) - 1):
            out[omitted.bit_count()] += 1
    return tuple(out)


def check_optimal_five_board():
    m = n = 5
    neighbors = neighborhoods(m, n)
    chosen = set()
    for rcenter in range(m):
        for rempty in range(m):
            if rempty == rcenter:
                continue
            for ccenter in range(n):
                for cempty in range(n):
                    if cempty == ccenter:
                        continue
                    omitted = frozenset(
                        {(rcenter, j) for j in range(n) if j not in (ccenter, cempty)} |
                        {(i, ccenter) for i in range(m) if i not in (rcenter, rempty)}
                    )
                    assert len(omitted) == m + n - 4
                    chosen.add(sum(1 << (i * n + j) for i, j in omitted))
    assert len(chosen) == m * (m - 1) * n * (n - 1) == 400
    total = 0
    for vertices in combinations(range(m * n), m + n - 4):
        mask = sum(1 << v for v in vertices)
        if direct_super_dominating(mask, neighbors, (1 << (m*n))-1):
            total += 1
            assert mask in chosen
    assert total == len(chosen)
    assert formula(m, n)[m + n - 4] == total
    print("5x5 size-six omitted subsets: exactly 400, all two-star templates")


def run():
    tested = ((2, 2), (2, 3), (2, 4), (3, 3),
              (3, 4), (3, 5), (4, 4))
    for m, n in tested:
        lhs, rhs = brute_counts(m, n), formula(m, n)
        assert lhs[:len(rhs)] == rhs and all(x == 0 for x in lhs[len(rhs):]), (m, n)
        print(f"{m}x{n}: {sum(lhs)} valid complements, coefficient match")
    for m, n in ((5, 5), (5, 6), (6, 6), (5, 8), (8, 5)):
        poly = formula(m, n)
        assert max(i for i, c in enumerate(poly) if c) == m+n-4
        assert poly[m+n-4] == m*(m-1)*n*(n-1)
    check_optimal_five_board()
    print("VERIFY_OK")


if __name__ == "__main__":
    run()
