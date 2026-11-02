"""Direct finite checks for singleton two-rainbow domination of rook graphs.

Use: python3 verify.py (Python standard library only).
The infinite theorem requires the mathematical lower-bound proof.
"""
from itertools import combinations, product


def feasible(m, n, matrix):
    assert len(matrix) == m and all(len(row) == n for row in matrix)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                assert matrix[i][j] in (1, 2)
                continue
            colors = {matrix[i][jj] for jj in range(n) if jj != j}
            colors.update(matrix[ii][j] for ii in range(m) if ii != i)
            if 1 not in colors or 2 not in colors:
                return False
    return True


def construction(m, n):
    assert 2 <= m <= n
    grid = [[0] * n for _ in range(m)]
    if n >= m + 2:
        for i in range(m):
            grid[i][0], grid[i][1] = 1, 2
    elif m <= 3:
        for j in range(n - 1):
            grid[0][j] = 1
        for i in range(1, m):
            grid[i][n - 1] = 2
    else:
        p = n - m + 1
        for j in range(p):
            grid[0][j] = 1
        grid[1][p] = 2
        d = m - 2
        for k in range(d):
            grid[k + 2][p + 1 + k] = 1
            grid[k + 2][p + 1 + (k + 1) % d] = 2
    return grid


def finite_exhaustion(m, n, expected):
    """Enumerate every assignment with fewer nonzero cells than expected."""
    sites = list(product(range(m), range(n)))
    tested = 0
    for w in range(expected):
        for support in combinations(sites, w):
            for labels in product((1, 2), repeat=w):
                arr = [[0] * n for _ in range(m)]
                for (i, j), v in zip(support, labels):
                    arr[i][j] = v
                tested += 1
                if feasible(m, n, arr):
                    raise AssertionError((m, n, w, arr))
    return tested


def lower_bound_palette_check(m, n):
    """Check the proof's disjoint-support inequalities for all row/column palettes."""
    for a in range(m + 1):
        for b in range(m - a + 1):
            c = m - a - b
            for p in range(n + 1):
                for q in range(n - p + 1):
                    r = n - p - q
                    if a and p:
                        x = a * p + max(c, r)
                    else:
                        x = max(a + c, p + r)
                    if b and q:
                        y = b * q + max(c, r)
                    else:
                        y = max(b + c, q + r)
                    # These bounds are only applied with nonempty row/column palettes.
                    if not (a + c and b + c and p + r and q + r):
                        continue
                    assert x + y >= min(2 * m, m + n - 2), (m, n, a, b, c, p, q, r, x, y)


def main():
    checks = 0
    for m in range(2, 21):
        for n in range(m, m + 6):
            arr = construction(m, n)
            target = min(2 * m, m + n - 2)
            assert feasible(m, n, arr), (m, n, arr)
            assert sum(bool(v) for row in arr for v in row) == target
            checks += 1
    print('CONSTRUCTIVE_CROSSCHECK_OK', checks)
    total = 0
    for m, n in [(2, 2), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5), (4, 4)]:
        target = min(2 * m, m + n - 2)
        k = finite_exhaustion(m, n, target)
        total += k
        print('EXHAUSTIVE_NO_SMALLER_OK', m, n, k)
    print('EXHAUSTIVE_TOTAL', total)
    palette_checks = 0
    for m in range(2, 13):
        for n in range(m, m + 4):
            lower_bound_palette_check(m, n)
            palette_checks += 1
    print('PALETTE_INEQUALITY_CROSSCHECK_OK', palette_checks)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
