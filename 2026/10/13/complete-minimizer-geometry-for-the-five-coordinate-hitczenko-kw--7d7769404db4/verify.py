#!/usr/bin/env python3
"""Exact finite-grid regression checks for the five-coordinate minimizer theorem."""
from itertools import combinations_with_replacement


def ge_sqrt(d, q):
    """Return whether integer d is at least sqrt(q), exactly."""
    return d >= 0 and d * d >= q


def lt_sqrt(d, q):
    """Return whether integer d is strictly below sqrt(q), exactly."""
    return d < 0 or d * d < q


def positive_tail_count(b):
    q = sum(x * x for x in b)
    s = sum(b)
    n = 0
    for mask in range(32):
        w = sum(b[i] for i in range(5) if (mask >> i) & 1)
        d = s - 2 * w
        if ge_sqrt(d, q):
            n += 1
    return n


def predicts_equality(b):
    q = sum(x * x for x in b)
    s = sum(b)
    u, v, _ = sorted((b[2], b[3], b[0] + b[1]))
    tau_ge_u = ge_sqrt(s - 2 * u, q)
    tau_lt_v = lt_sqrt(s - 2 * v, q)
    return tau_ge_u and tau_lt_v


def main():
    checked = 0
    minimizers = 0
    minimum_count = 32
    for b in combinations_with_replacement(range(9), 5):
        if not any(b):
            continue
        checked += 1
        n = positive_tail_count(b)
        minimum_count = min(minimum_count, n)
        assert n >= 4, (b, n)
        pred = predicts_equality(b)
        assert pred == (n == 4), (b, n, pred)
        if n == 4:
            minimizers += 1
        else:
            assert n >= 5, (b, n)
    print(f"VERIFY_OK tuples={checked} minimizer_tuples={minimizers} min_positive_count={minimum_count}")


if __name__ == '__main__':
    main()
