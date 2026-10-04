#!/usr/bin/env python3
from fractions import Fraction


def wt(x):
    return x.bit_count()


def min_arc_quarters(residues):
    r = sorted(set(x % 4 for x in residues))
    if len(r) == 1:
        return 0
    gaps = []
    for a, b in zip(r, r[1:]):
        gaps.append(b - a)
    gaps.append(r[0] + 4 - r[-1])
    return 4 - max(gaps)


def phase_identity(n):
    # At t=n*pi/4, U has phase (-i)^d under exp(-iAt/n).
    # Multiplying row and column y/x by i^h gives Walsh sign (-1)^(x dot y).
    for x in range(1 << n):
        for y in range(1 << n):
            d = wt(x ^ y)
            dot = wt(x & y)
            lhs_exp = (wt(x) - d + wt(y)) % 4
            rhs_exp = (2 * dot) % 4
            if lhs_exp != rhs_exp:
                raise AssertionError((n, x, y, lhs_exp, rhs_exp))


def schedule_residues(n):
    # Work in quarter-turn time units pi/2; e^{-is} has exponent -s modulo 4.
    if n == 1:
        durations = [1]
        # Scalar-rotated target phases for h=0,1 are {-i,1}: accumulated times {1,0}.
        acc = {0: 1, 1: 0}
    elif n == 2:
        durations = [1, 1]
        # Scalar-rotated target {-1,-i,1}: accumulated times {2,1,0}.
        acc = {0: 2, 1: 1, 2: 0}
    else:
        durations = [2, 1]
        # Scalar-rotated target {-1,-i,1,i}: times {2,1,0,3}.
        acc = {0: 2, 1: 1, 2: 0, 3: 3}
    total = sum(durations)
    if any(s < 0 or s > total for s in acc.values()):
        raise AssertionError('bad accumulated time')
    # Every desired accumulated time must be a subset sum of layer durations.
    subs = {0}
    for d in durations:
        subs |= {x + d for x in list(subs)}
    if not set(acc.values()) <= subs:
        raise AssertionError((n, durations, acc, subs))
    return total


for n in range(1, 9):
    phase_identity(n)
    residues = list(range(n + 1))
    arc_q = min_arc_quarters(residues)
    expected_q = min(n, 3)
    if arc_q != expected_q:
        raise AssertionError((n, arc_q, expected_q))
    sched_q = schedule_residues(n)
    if sched_q != expected_q:
        raise AssertionError((n, sched_q, expected_q))
    # Runtime in units of pi: n/4 + two sides * (expected_q/2).
    runtime = Fraction(n, 4) + Fraction(expected_q, 1)
    if n == 1 and runtime != Fraction(5, 4):
        raise AssertionError(runtime)
    if n == 2 and runtime != Fraction(5, 2):
        raise AssertionError(runtime)
    if n >= 3 and runtime != Fraction(n, 4) + 3:
        raise AssertionError(runtime)

print('VERIFY_OK')
