"""Finite checks for generalized-support extremizers of even-cycle edge codes.

Run: python3 verify.py
Only Python's standard library is needed. This is independent finite evidence,
not a replacement for the all-parameter argument in RESULT.md.
"""
from itertools import combinations, product
from math import factorial, prod
from fractions import Fraction


def rrefs(n, d, q):
    """All reduced-row-echelon d-dimensional subspaces of F_q^n, q prime."""
    for piv in combinations(range(n), d):
        free = [(i, j) for i in range(d) for j in range(piv[i] + 1, n)
                if j not in piv]
        for vals in product(range(q), repeat=len(free)):
            matrix = [[int(j == piv[i]) for j in range(n)] for i in range(d)]
            for (i, j), value in zip(free, vals):
                matrix[i][j] = value
            yield piv, matrix


def count_direct(q, k, piv, rows, columns):
    d = len(piv)
    return sum(all(sum(rows[i][j] * col[piv[i]] for i in range(d)) % q
                   == col[j] for j in range(2 * k)) for col in columns)


def count_partition_number(k, d):
    """Independent rational evaluation of the balanced-partition formula."""
    def compositions(n, m):
        if m == 1:
            if n >= 1:
                yield (n,)
        else:
            for first in range(1, n - m + 2):
                for rest in compositions(n - first, m - 1):
                    yield (first,) + rest

    factor = Fraction(factorial(k) ** 2, factorial(d))
    s = sum((Fraction(1, prod(factorial(a) ** 2 for a in part))
             for part in compositions(k, d)), Fraction())
    answer = factor * s
    assert answer.denominator == 1
    return int(answer)


def count_residue_partitions(k, d, Q):
    """Independently enumerate partitions balanced modulo Q."""
    n = 2 * k
    count = 0
    for labels in product(range(d), repeat=n):
        if set(labels) != set(range(d)):
            continue
        if [labels.index(i) for i in range(d)] != sorted(labels.index(i) for i in range(d)):
            continue
        if all((sum(labels[i] == j for i in range(0, n, 2)) -
                sum(labels[i] == j for i in range(1, n, 2))) % Q == 0
               for j in range(d)):
            count += 1
    return count


def check_direct(q, k, d):
    n = 2 * k
    columns = [tuple(x[i] * x[(i + 1) % n] % q for i in range(n))
               for x in product(range(1, q), repeat=n)]
    max_zero = -1
    ties = 0
    total = 0
    for piv, rows in rrefs(n, d, q):
        total += 1
        count = count_direct(q, k, piv, rows, columns)
        if count > max_zero:
            max_zero, ties = count, 1
        elif count == max_zero:
            ties += 1
    expected = (q - 1) ** (d + 1)
    assert max_zero == expected, (q, k, d, max_zero, expected)
    expect_ties = (q - 1) ** (2 * k - d - 1) * count_residue_partitions(k, d, q - 1)
    assert ties == expect_ties, (q, k, d, ties, expect_ties)
    if q >= k + 2:
        assert count_residue_partitions(k, d, q - 1) == count_partition_number(k, d)
    print('DIRECT', q, k, d, total, max_zero, ties, flush=True)


def check_image(q, k, d):
    """Independent hypersurface image enumeration, not vertex torus enumeration."""
    n = 2 * k
    torus_d = list(product(range(1, q), repeat=d))
    maximum = -1
    ties = 0
    total = 0
    for piv, rows in rrefs(n, d, q):
        total += 1
        count = 0
        for t in torus_d:
            edge = [sum(t[i] * rows[i][j] for i in range(d)) % q
                    for j in range(n)]
            if 0 in edge:
                continue
            if prod(edge[::2]) % q == prod(edge[1::2]) % q:
                count += 1
        if count > maximum:
            maximum, ties = count, 1
        elif count == maximum:
            ties += 1
    assert maximum == (q - 1) ** d
    expect_ties = (q - 1) ** (2 * k - d - 1) * count_residue_partitions(k, d, q - 1)
    assert ties == expect_ties, (q, k, d, ties, expect_ties)
    print('IMAGE', q, k, d, total, maximum, ties, flush=True)


def check_balanced_construction(q=5, k=3, d=3):
    """Generate every predicted extremizer for the final dimension case.

    This construction census is NOT an exhaustive search through other planes.
    """
    n = 2 * k
    seen = set()
    good = 0
    for tags in product(range(d), repeat=n):
        if set(tags) != set(range(d)):
            continue
        first = [tags.index(j) for j in range(d)]
        if first != sorted(first):
            continue  # one canonical labeling for every partition
        if any(sum(tags[i] == j for i in range(0, n, 2)) !=
               sum(tags[i] == j for i in range(1, n, 2))
               for j in range(d)):
            continue
        floating = [i for i in range(n) if i not in first]
        for values in product(range(1, q), repeat=len(floating)):
            c = [1] * n
            for i, value in zip(floating, values):
                c[i] = value
            if prod(c[::2]) % q != prod(c[1::2]) % q:
                continue
            rows = [[c[j] if tags[j] == a else 0 for j in range(n)]
                    for a in range(d)]
            key = tuple(sorted(tuple(row) for row in rows))
            assert key not in seen
            seen.add(key)
            count = 0
            for t in product(range(1, q), repeat=d):
                edge = [sum(t[i] * rows[i][j] for i in range(d)) % q
                        for j in range(n)]
                if prod(edge[::2]) % q == prod(edge[1::2]) % q:
                    count += 1
            assert count == (q - 1) ** d
            good += 1
    predicted = (q - 1) ** (2 * k - d - 1) * count_partition_number(k, d)
    assert good == predicted == 96
    print('CONSTRUCTED', q, k, d, good, flush=True)


if __name__ == '__main__':
    for qq, kk, dd in [(3, 2, 1), (3, 2, 2), (5, 2, 1), (5, 2, 2),
                       (3, 3, 1), (3, 3, 2), (3, 3, 3)]:
        check_direct(qq, kk, dd)
    for dd in (1, 2):
        check_image(5, 3, dd)
    check_balanced_construction()
    print('VERIFY_OK')
