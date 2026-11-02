"""Finite exact checks for the switching-hole entropy criterion.

This checks short schedules and rational-count identities. Universal
quantifiers and the asymptotic criterion are established in RESULT.md.
Execute with Python 3: python verify_switch.py
"""
from itertools import product
from math import ceil

M0 = ((0, 1), (1, 1))
M1 = ((1, 1), (1, 0))
I2 = ((1, 0), (0, 1))


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def count_matrix(schedule):
    p = I2
    for symbol in schedule:
        p = mm(p, (M0, M1)[symbol])
    return sum(sum(row) for row in p)


def count_direct(schedule):
    n = len(schedule)
    total = 0
    for seq in product((0, 1), repeat=n + 1):
        if all(not (seq[i] == seq[i + 1] == schedule[i])
               for i in range(n)):
            total += 1
    return total


def defect_count(schedule):
    return sum(a == b for a, b in zip(schedule, schedule[1:]))


def check():
    for n in range(1, 12):
        for schedule in product((0, 1), repeat=n):
            count = count_matrix(schedule)
            assert count == count_direct(schedule), (n, schedule)
            d = defect_count(schedule)
            k = d + 1
            assert count >= 2 ** (1 + ceil(d / 2)), (n, schedule, 'lower')
            # Rearranged exact-integer version of the AM--GM bound:
            assert count ** k * k ** (k * k) <= (2 ** k) * (n + k) ** (k * k), (n, schedule, 'upper')
            if d == 0:
                assert count == n + 2, (n, schedule, 'alternating')
    # An independent sample with sparse switching defects and a long horizon.
    # The finite computation is illustrative, not an asymptotic certificate.
    for n in (100, 250, 500):
        schedule = [i % 2 for i in range(n)]
        for j in range(1, int(n ** 0.5) + 1):
            if j * j < n:
                schedule[j * j] = schedule[j * j - 1]
        count = count_matrix(schedule)
        d = defect_count(schedule)
        k = d + 1
        assert count >= 2 ** (1 + ceil(d / 2))
        assert count ** k * k ** (k * k) <= (2 ** k) * (n + k) ** (k * k)
    # Transfer identities used by the proof.
    assert mm(M0, M1) == ((1, 0), (2, 1))
    assert mm(M1, M0) == ((1, 2), (0, 1))
    assert mm(M0, M0) == ((1, 1), (1, 2))
    assert mm(M1, M1) == ((2, 1), (1, 1))
    print('PASS: exhaustive finite word counts, matrix identities, and bounds')


if __name__ == '__main__':
    check()
