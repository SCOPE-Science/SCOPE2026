"""Exact integer checks for shared-embedding bilinear sign witnesses."""
import sys


def score(x, b, y):
    return sum(x[i] * b[i][j] * y[j] for i in range(len(x)) for j in range(len(y)))


def witnesses(n):
    if n == 1:
        return [(1,)], [[1]], [[-1]]
    if n == 2:
        return [(1, 0), (0, 1)], [[1, -1], [-1, 1]], [[-1, 1], [-1, -1]]
    h = [(1, i, i * i) for i in range(1, n + 1)]
    eq = [[1, 0, -2], [0, 4, 0], [-2, 0, 0]]
    lt = [[-1, 2, 0], [-2, 0, 0], [0, 0, 0]]
    return h, eq, lt


def verify(n):
    h, eq, lt = witnesses(n)
    for i in range(n):
        for j in range(n):
            a = score(h[i], eq, h[j])
            b = score(h[i], lt, h[j])
            assert (a > 0) == (i == j) and a != 0, (n, i, j, a)
            assert (b > 0) == (i < j) and b != 0, (n, i, j, b)
    return len(h[0]), n * n


def separate_three():
    h = [(1, 0), (-1, 2), (-1, -2)]
    b = [[1, 0], [0, 1]]
    for i in range(3):
        for j in range(3):
            s = score(h[i], b, h[j])
            assert s != 0 and (s > 0) == (i == j)
    h = [(1, i) for i in range(1, 4)]
    b = [[-1, 2], [-2, 0]]
    for i in range(3):
        for j in range(3):
            s = score(h[i], b, h[j])
            assert s != 0 and (s > 0) == (i < j)


def main():
    maxn = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    assert maxn >= 3
    separate_three()
    cases = 0
    for n in range(1, maxn + 1):
        dimension, tested = verify(n)
        assert dimension == min(n, 3)
        cases += tested
    print(f"VERIFY_OK max_domain={maxn} domain_sizes={maxn} pairs={cases} standalone_3point_relation_checks=18")


if __name__ == "__main__":
    main()
