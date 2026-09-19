#!/usr/bin/env python3
"""Exact integer checks for the cylindrical multiset-basis constructions."""

from __future__ import annotations

import argparse
from collections import defaultdict


def cycle_distance(n: int, x: int, y: int) -> int:
    d = abs(x - y)
    return min(d, n - d)


def gap_data(n: int, landmarks: tuple[int, int, int], x: int):
    vals = sorted(cycle_distance(n, x, w) for w in landmarks)
    return (vals[1] - vals[0], vals[2] - vals[1]), vals[0], tuple(vals)


def repeated_gap_groups(n: int, landmarks: tuple[int, int, int]):
    groups = defaultdict(list)
    for x in range(n):
        delta, height, _ = gap_data(n, landmarks, x)
        groups[delta].append((x, height))
    return {delta: items for delta, items in groups.items() if len(items) > 1}


def is_q_separated(n: int, landmarks: tuple[int, int, int], q: int) -> bool:
    for items in repeated_gap_groups(n, landmarks).values():
        heights = sorted(height for _, height in items)
        if any(b - a < q for a, b in zip(heights, heights[1:])):
            return False
    return True


def tail_arcs(q: int, r: int) -> tuple[int, int, int]:
    if q % 2 == 0:
        table = (
            (q + 2, 2 * q - 1, 3 * q + 2),
            (q + 1, 2 * q + 2, 3 * q + 1),
            (q + 2, 2 * q + 1, 3 * q + 2),
            (q + 1, 2 * q + 2, 3 * q + 3),
            (q + 2, 2 * q + 3, 3 * q + 2),
            (q + 1, 2 * q + 4, 3 * q + 3),
        )
    else:
        table = (
            (q + 1, 2 * q + 1, 3 * q + 1),
            (q, 2 * q + 2, 3 * q + 2),
            (q + 1, 2 * q + 1, 3 * q + 3),
            (q + 2, 2 * q + 2, 3 * q + 2),
            (q + 3, 2 * q + 1, 3 * q + 3),
            (q + 2, 2 * q + 2, 3 * q + 4),
        )
    return table[r]


def tail_landmarks(q: int, r: int):
    a, b, c = tail_arcs(q, r)
    n = a + b + c
    assert n == 6 * q + 3 + r
    return n, (0, a, a + b)


def expected_tail_pairs(q: int, r: int):
    if q % 2 == 0:
        table = {
            0: ((q, 4*q + 3), (q + 1, 4*q + 2), (q + 2, 4*q + 1)),
            1: ((q + 1, 4*q + 3),),
            2: ((q + 1, 4*q + 4), (q + 2, 4*q + 3)),
            3: ((q + 1, 4*q + 4),),
            4: ((q + 2, 4*q + 5),),
            5: ((q + 2, 4*q + 6),),
        }
    else:
        table = {
            0: ((q + 1, 4*q + 2),),
            1: ((q + 1, 4*q + 3),),
            2: ((q + 1, 4*q + 3),),
            3: ((q + 1, 4*q + 5), (q + 2, 4*q + 4)),
            4: ((q + 1, 4*q + 6), (q + 2, 4*q + 5), (q + 3, 4*q + 4)),
            5: ((q + 1, 4*q + 6), (q + 2, 4*q + 5)),
        }
    return sorted(tuple(sorted(pair)) for pair in table[r])


def actual_repeated_pairs(n: int, landmarks: tuple[int, int, int]):
    groups = repeated_gap_groups(n, landmarks)
    if any(len(items) != 2 for items in groups.values()):
        return None
    return sorted(tuple(sorted((items[0][0], items[1][0]))) for items in groups.values())


def boundary_landmarks(q: int, family: str):
    if family == "even-minus-one":
        assert q % 2 == 0
        return 6*q - 1, (0, q, 3*q - 1)
    if family == "even-plus-two":
        assert q % 2 == 0
        return 6*q + 2, (0, q + 1, 3*q + 1)
    if family == "odd-zero":
        assert q % 2 == 1
        return 6*q, (0, q, 3*q)
    if family == "odd-plus-one":
        assert q % 2 == 1
        return 6*q + 1, (0, q + 1, 3*q)
    raise ValueError(family)


def expected_boundary_pairs(q: int, family: str):
    if family == "even-minus-one":
        return [(q, 4*q - 1)]
    if family == "even-plus-two":
        return sorted(((q, 4*q + 2), (q + 1, 4*q + 1)))
    if family == "odd-zero":
        return [(q, 4*q)]
    if family == "odd-plus-one":
        return sorted(((q, 4*q + 1), (q + 1, 4*q)))
    raise ValueError(family)


def cylinder_code(m: int, n: int, landmarks: tuple[int, int, int], vertex):
    i, x = vertex
    return tuple(sorted(i + cycle_distance(n, x, w) for w in landmarks))


def resolves_cylinder(m: int, n: int, landmarks: tuple[int, int, int]) -> bool:
    seen = set()
    for i in range(m):
        for x in range(n):
            code = cylinder_code(m, n, landmarks, (i, x))
            if code in seen:
                return False
            seen.add(code)
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--q-max", type=int, default=500)
    parser.add_argument("--m-max", type=int, default=30)
    args = parser.parse_args()
    if args.q_max < 2 or args.m_max < 2:
        raise SystemExit("bounds must be at least 2")

    tail_checks = 0
    for q in range(2, args.q_max + 1):
        for r in range(6):
            n, landmarks = tail_landmarks(q, r)
            assert is_q_separated(n, landmarks, q)
            assert actual_repeated_pairs(n, landmarks) == expected_tail_pairs(q, r)
            tail_checks += 1

    boundary_checks = 0
    for q in range(2, args.q_max + 1):
        families = ("even-minus-one", "even-plus-two") if q % 2 == 0 else ("odd-zero", "odd-plus-one")
        for family in families:
            n, landmarks = boundary_landmarks(q, family)
            assert is_q_separated(n, landmarks, q)
            assert actual_repeated_pairs(n, landmarks) == expected_boundary_pairs(q, family)
            boundary_checks += 1

    cylinder_checks = 0
    for m in range(2, args.m_max + 1):
        special = ("even-minus-one", "even-plus-two") if m % 2 == 0 else ("odd-zero", "odd-plus-one")
        for family in special:
            n, landmarks = boundary_landmarks(m, family)
            assert resolves_cylinder(m, n, landmarks)
            cylinder_checks += 1
        for n in range(6*m + 3, 6*m + 15):
            q = (n - 3) // 6
            r = n - (6*q + 3)
            n2, landmarks = tail_landmarks(q, r)
            assert n2 == n and q >= m
            assert resolves_cylinder(m, n, landmarks)
            cylinder_checks += 1

    print("PASS")
    print(f"tail cycle constructions checked: {tail_checks}")
    print(f"boundary cycle constructions checked: {boundary_checks}")
    print(f"direct cylindrical resolving-set checks: {cylinder_checks}")
    print(f"q range: 2..{args.q_max}")
    print(f"m range for direct cylinder checks: 2..{args.m_max}")


if __name__ == "__main__":
    main()
