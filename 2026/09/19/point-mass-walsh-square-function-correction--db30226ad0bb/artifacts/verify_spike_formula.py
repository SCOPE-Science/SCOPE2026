"""Verify the exact singleton higher-Walsh square-function formula on small cubes."""

from itertools import combinations, product
from math import comb


def iterated_difference(f, x, J):
    """Compute D_J f from the defining finite differences, D_j=(I-flip_j)/2."""
    total = 0.0
    k = len(J)
    for mask in range(1 << k):
        y = list(x)
        flips = 0
        for a, j in enumerate(J):
            if (mask >> a) & 1:
                y[j] *= -1
                flips += 1
        total += (-1.0 if flips % 2 else 1.0) * f(tuple(y))
    return total / (2**k)


def brute_ratio(n, k, p):
    points = list(product((-1, 1), repeat=n))
    apex = (1,) * n

    def f(x):
        return 1.0 if x == apex else 0.0

    values = []
    for x in points:
        sq = 0.0
        for J in combinations(range(n), k):
            value = iterated_difference(f, x, J)
            sq += value * value
        values.append(sq**0.5)

    norm = (sum(v**p for v in values) / (2**n)) ** (1.0 / p)
    fnorm = (2.0 ** (-n)) ** (1.0 / p)
    return norm / fnorm


def closed_ratio(n, k, p):
    total = sum(
        comb(n, r) * comb(n - r, k - r) ** (p / 2.0)
        for r in range(k + 1)
    )
    return (2.0 ** (-k * p) * total) ** (1.0 / p)


def main():
    for n in range(2, 7):
        for k in range(1, min(3, n) + 1):
            for p in (1.2, 1.5, 2.0, 3.0):
                lhs = brute_ratio(n, k, p)
                rhs = closed_ratio(n, k, p)
                assert abs(lhs - rhs) < 1e-10, (n, k, p, lhs, rhs)

    # Lemma 6.3 of arXiv:2609.09040v1 would give, for n=2,k=1,p=3/2,
    # ratio >= n^(1/p).  The exact ratio is strictly smaller.
    n, k, p = 2, 1, 1.5
    exact = brute_ratio(n, k, p)
    claimed = n ** (1.0 / p)
    assert exact < claimed

    print("exact formula checks passed")
    print(f"counterexample: exact={exact:.12f}, claimed lower bound={claimed:.12f}")


if __name__ == "__main__":
    main()
