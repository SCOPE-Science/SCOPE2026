#!/usr/bin/env python3
"""Finite checks for the explicit S_{f,2f+1} formula."""


def greedy(f, count):
    seq = [f, 2 * f + 1]
    pair_sums = {seq[0] + seq[1]}
    while len(seq) < count:
        x = seq[-1] + 1
        while x in pair_sums:
            x += 1
        for a in seq:
            pair_sums.add(a + x)
        seq.append(x)
    return seq


def predicted_member(f, x):
    if x == f or 2 * f + 1 <= x <= 3 * f:
        return True
    if x < 4 * f + 1:
        return False
    m = 5 * f + 1
    r = x % m
    return (
        r in (f - 1, f, 4 * f + 1, 4 * f + 2)
        or 2 * f + 2 <= r <= 3 * f - 1
    )


def predicted_period(f):
    return [1, 2 * f - 2, 1, f + 2] + [1] * (f - 3) + [f + 2]


def check(f, count=300):
    seq = greedy(f, count)
    got = set(seq)
    for x in range(f, seq[-1] + 1):
        assert (x in got) == predicted_member(f, x), (f, x)

    diffs = [b - a for a, b in zip(seq, seq[1:])]
    pre = f + 1
    period = predicted_period(f)
    for i in range(pre, len(diffs)):
        assert diffs[i] == period[(i - pre) % len(period)], (f, i)


if __name__ == "__main__":
    for f in range(5, 81):
        check(f)
    print("PASS: f=5..80, first 300 sequence terms per parameter")
