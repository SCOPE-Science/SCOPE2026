"""Independent finite checks of the total Roman {2} enumerator on crown graphs.

Run with Python 3.8 or later: python3 verify.py
Standard library only. Graph feasibility is tested from adjacency, independently
of the support classification used in the mathematical proof.
"""
from itertools import product
from collections import Counter
from math import comb


def admissible(labels, n):
    """Check the original graph definition directly on Cr_n."""
    neighbors = [[] for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                neighbors[i].append(n + j)
                neighbors[n + j].append(i)
    for u, value in enumerate(labels):
        if value == 0:
            if sum(labels[v] for v in neighbors[u]) < 2:
                return False
        elif not any(labels[v] > 0 for v in neighbors[u]):
            return False
    return True


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def scale(a, c):
    return [c * x for x in a]


def mult(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power(a, n):
    out = [1]
    for _ in range(n):
        out = mult(out, a)
    return out


def shift(a, k):
    return [0] * k + a


def predicted(n):
    t = [1, 1, 1]
    robust = add(power(t, n), scale([1, n, n + comb(n, 2), n * (n - 1)], -1))
    one = add(mult([0, 1, 1], power(t, n - 1)),
              scale([0, 1, n, 2 * (n - 1)], -1))
    two = add(mult([0, 0, 1, 2, 1], power(t, n - 2)),
              scale([0, 0, 1, 2], -1))
    ans = mult(robust, robust)
    ans = add(ans, scale(shift(two, 2), n * (n - 1)))
    ans = add(ans, scale(shift(one, 3), 2 * n * (n - 1)))
    ans = add(ans, shift([comb(n, 2), 2 * n * (n - 1), n * n * (n - 1)], 4))
    return ans


def total_formula(n):
    # Closed total from the exact polynomial, kept in integer arithmetic.
    numerator = (9 * n**4 - 14 * n**3 + 39 * n**2 - 2 * n + 4)
    assert numerator % 4 == 0
    return 9**n - (11*n*n + 25*n + 18) * 3**(n-2) + numerator // 4


def main():
    total = 0
    for n in range(3, 7):
        observed = Counter()
        for labels in product((0, 1, 2), repeat=2*n):
            total += 1
            if admissible(labels, n):
                observed[sum(labels)] += 1
        p = predicted(n)
        for k in range(max(len(p), 4*n + 1)):
            assert observed[k] == (p[k] if k < len(p) else 0), (n, k, observed[k])
        assert min(observed) == 4
        assert observed[4] == comb(n, 2)
        assert observed[5] == n*n*(n-1)
        assert sum(observed.values()) == total_formula(n)
        print(f"n={n}: checked {3**(2*n)} ternary labelings; "
              f"valid={sum(observed.values())}; minimum=4; "
              f"number of minima={observed[4]}; all coefficients match")
    for n in range(7, 61):
        p = predicted(n)
        assert all(c >= 0 for c in p)
        assert p[4] == comb(n, 2)
        assert p[5] == n*n*(n-1)
        assert sum(p) == total_formula(n)
        assert p[2*n*2] == 1
    print(f"PASS: exhaustive {total} labelings for n=3..6; "
          "exact polynomial consistency for n=7..60")

if __name__ == '__main__':
    main()
