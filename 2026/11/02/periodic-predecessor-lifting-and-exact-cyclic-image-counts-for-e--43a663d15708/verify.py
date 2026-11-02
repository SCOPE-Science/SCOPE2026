#!/usr/bin/env python3
"""Independent exact finite tests for cyclic Rule 126 reachability and counts."""
from itertools import product


def rule126_output(word, n):
    """Direct Wolfram-table evaluation, without using boundary differences."""
    result = 0
    for i in range(n):
        a = (word >> ((i - 1) % n)) & 1
        b = (word >> i) & 1
        c = (word >> ((i + 1) % n)) & 1
        if not (a == b == c):
            result |= 1 << i
    return result


def runs_between_zeros(word, n):
    """Return positive one-run lengths or None for constant words."""
    b = tuple((word >> i) & 1 for i in range(n))
    if all(b) or not any(b):
        return None
    starts = [i for i in range(n) if b[i] == 1 and b[(i - 1) % n] == 0]
    lengths = []
    for i in starts:
        length, j = 0, i
        while b[j] == 1:
            length += 1
            j = (j + 1) % n
        lengths.append(length)
    return lengths


def reachable_by_gap_criterion(word, n):
    if word == 0:
        return True
    if word == (1 << n) - 1:
        return n > 1
    runs = runs_between_zeros(word, n)
    if 1 in runs:
        return False
    if any(length >= 4 for length in runs):
        return True
    return sum(length == 2 for length in runs) % 2 == 0


def all_cyclic_010_free(word, n):
    for i in range(n):
        if (((word >> (i % n)) & 1) == 0 and
            ((word >> ((i + 1) % n)) & 1) == 1 and
            ((word >> ((i + 2) % n)) & 1) == 0):
            return False
    return True


def recurrence_counts(max_n):
    # tau_n: trace of the three nonzero eigenvalues of the 010 avoidance graph.
    tau = [3, 2, 2]
    for n in range(3, max_n + 1):
        tau.append(2 * tau[n - 1] - tau[n - 2] + tau[n - 3])
    lucas = [2, 1]
    for n in range(2, max_n + 1):
        lucas.append(lucas[n - 1] + lucas[n - 2])
    reachable, short, signed = [0] * (max_n + 1), [0] * (max_n + 1), [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        epsilon = (2, 0, -2, 0)[n % 4]
        short[n] = lucas[n] + epsilon - 1
        signed[n] = 3 * (-1 if (n // 3) % 2 else 1) if n % 3 == 0 else 0
        assert (short[n] - signed[n]) % 2 == 0
        reachable[n] = tau[n] - (short[n] - signed[n]) // 2 - (n == 1)
    return tau, lucas, short, signed, reachable


def matrix_010_count(n):
    states = ((0, 0), (0, 1), (1, 0), (1, 1))
    M = [[0] * 4 for _ in range(4)]
    for i, (a, b) in enumerate(states):
        for c in (0, 1):
            if (a, b, c) != (0, 1, 0):
                M[i][states.index((b, c))] += 1
    P = [[int(i == j) for j in range(4)] for i in range(4)]
    for _ in range(n):
        P = [[sum(P[i][k] * M[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    return sum(P[i][i] for i in range(4))


def construct_period_at_most_twice(word, n):
    """Return (period, predecessor) with period n or 2*n, for 010-free y."""
    assert all_cyclic_010_free(word, n)
    if word == 0:
        d = [0] * n
    elif word == (1 << n) - 1:
        d = [1] * n
        if n >= 3 and (n % 2):
            d[0] = 0
    else:
        b = [(word >> i) & 1 for i in range(n)]
        d = [0] * n
        runs = []
        for i in range(n):
            if b[i] and not b[(i - 1) % n]:
                length, j = 0, i
                while b[j]:
                    length += 1
                    j = (j + 1) % n
                runs.append((i, length))
                for s in range(length - 1):
                    d[(i + s) % n] = 1
        assert all(length >= 2 for _, length in runs)
        if sum(d) % 2:
            for i, length in runs:
                if length >= 4:
                    d[(i + 1) % n] = 0  # interior edge, flanked by two ones
                    break
    multiple = 1 if sum(d) % 2 == 0 else 2
    D = d * multiple
    assert sum(D) % 2 == 0
    x = [0] * len(D)
    for i in range(len(D) - 1):
        x[i + 1] = x[i] ^ D[i]
    assert (x[-1] ^ x[0]) == D[-1]
    value = sum(bit << i for i, bit in enumerate(x))
    expected = sum(word << (n * j) for j in range(multiple))
    assert rule126_output(value, n * multiple) == expected
    return n * multiple, value


def verify():
    tau, lucas, short, signed, counts = recurrence_counts(120)
    assert counts[1:20] == [1, 2, 2, 6, 12, 23, 37, 66, 119, 217, 387, 693, 1237, 2207, 3927, 6986, 12412, 22028, 39047]
    for n in range(1, 121):
        assert tau[n] == matrix_010_count(n), ('matrix', n)
    for n in range(1, 19):
        exact_image = {rule126_output(x, n) for x in range(1 << n)}
        predicted_image = {y for y in range(1 << n) if reachable_by_gap_criterion(y, n)}
        assert exact_image == predicted_image, ('criterion', n)
        assert len(exact_image) == counts[n], ('closed counts', n)
        if n <= 15:
            avoid_010 = sum(all_cyclic_010_free(y, n) for y in range(1 << n))
            assert avoid_010 == tau[n], ('010-free', n)
            candidate_short = [(y, runs_between_zeros(y, n)) for y in range(1 << n)]
            candidate_short = [(y, runs) for y, runs in candidate_short
                               if runs is not None and all(t in (2, 3) for t in runs)]
            assert len(candidate_short) == short[n], ('short-run count', n)
            signed_actual = sum(-1 if (sum(t == 2 for t in r) % 2) else 1 for _, r in candidate_short)
            assert signed_actual == signed[n], ('short-run sign', n)
    # Explicit periodic-lifting construction: every locally admissible image
    # lifts at length n or exactly double length, including n=1.
    for n in range(1, 14):
        for y in range(1 << n):
            if all_cyclic_010_free(y, n):
                p, x = construct_period_at_most_twice(y, n)
                assert p == (n if reachable_by_gap_criterion(y, n) else 2 * n)
    # Certificate of an infinite obstruction family: y=(011)^odd_m has
    # odd many 2-runs, no 010, and no same-period predecessor.
    for m in (1, 3, 5, 7, 9):
        n = 3 * m
        y = sum((1 << (3 * j + 1)) | (1 << (3 * j + 2)) for j in range(m))
        assert all_cyclic_010_free(y, n)
        assert not reachable_by_gap_criterion(y, n)
    print('VERIFY_OK')
    print('brute_force_rings=1..18; transfer_matrix=1..120; short_run_sign=1..15; explicit_lifts=1..13')
    print('image_counts_n1_to19=', ','.join(map(str, counts[1:20])))


if __name__ == '__main__':
    verify()
