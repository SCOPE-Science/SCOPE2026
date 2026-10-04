#!/usr/bin/env python3
"""Independent finite replay for the closed-form one-braid optimizer.

This script re-enumerates the integer program from Theorem 1 of
Heiney--Kipe--Pezzimenti--Pontes--Ta and compares it with the stated closed form.
Finite enumeration is a consistency check; the general result is proved algebraically.
"""
from math import ceil, gcd


def feasible(p, q, h, v):
    return (
        isinstance(h, int) and isinstance(v, int)
        and h >= 0 and v >= 0 and h >= v
        and q - 2 * (h + v + p) + 4 >= 0
        and h + 3 * v <= q - 3 * p + 4
        and 3 * h + v <= q - p + 4
    )


def brute_optimum(p, q):
    best_n = None
    best_pairs = []
    # The second inequality in the source system gives h+v <= (q-2p+4)/2.
    s_cap = (q - 2 * p + 4) // 2
    if s_cap < 0:
        return None, []
    for h in range(s_cap + 1):
        for v in range(min(h, s_cap - h) + 1):
            if feasible(p, q, h, v):
                n = q - h - v
                if best_n is None or n < best_n:
                    best_n = n
                    best_pairs = [(h, v)]
                elif n == best_n:
                    best_pairs.append((h, v))
    return best_n, best_pairs


def closed_form(p, q):
    if q < 3 * p - 4:
        return None
    if q <= 4 * p - 4:
        return 3 * p - 4
    return p - 2 + ceil(q / 2) + (1 if q % 4 == 2 else 0)


def witness(p, q):
    if q < 3 * p - 4:
        return None
    if q <= 4 * p - 4:
        return q - 3 * p + 4, 0
    if q % 4 == 0:
        return q // 4 + 1, q // 4 - p + 1
    if q % 4 == 1:
        return (q + 3) // 4, (q - 4 * p + 3) // 4
    if q % 4 == 2:
        return (q + 2) // 4, (q - 4 * p + 2) // 4
    return (q + 1) // 4, (q - 4 * p + 5) // 4


def main():
    checked = 0
    for p in range(2, 31):
        for q in range(p + 1, 151):
            brute_n, pairs = brute_optimum(p, q)
            formula_n = closed_form(p, q)
            assert brute_n == formula_n, (p, q, brute_n, formula_n, pairs)
            w = witness(p, q)
            if formula_n is not None:
                assert feasible(p, q, *w), ("bad witness", p, q, w)
                assert q - sum(w) == formula_n, ("nonoptimal witness", p, q, w)
            checked += 1

    # Reproduce every p=3 entry in Table 1 of the source paper.
    table1 = {
        7: ((2, 0), 5), 8: ((3, 0), 5), 10: ((3, 0), 7),
        11: ((4, 0), 7), 13: ((4, 1), 8), 14: ((5, 0), 9),
        16: ((5, 2), 9), 17: ((5, 2), 10),
    }
    for q, (pair, n) in table1.items():
        assert feasible(3, q, *pair)
        assert q - sum(pair) == n == closed_form(3, q)

    # Check the p=2 corollary on coprime inputs and p=4 formulas on sample ranges.
    for q in range(3, 101, 2):
        assert closed_form(2, q) == (q + 1) // 2
    for q in range(9, 100):
        if gcd(4, q) == 1:
            expected = 8 if q == 9 else 3 + (q - 1) // 2
            assert closed_form(4, q) == expected

    print(f"VERIFY_OK exhaustive_pairs={checked}; p<=30; q<=150; source_tables_and_corollaries_match")


if __name__ == "__main__":
    main()
