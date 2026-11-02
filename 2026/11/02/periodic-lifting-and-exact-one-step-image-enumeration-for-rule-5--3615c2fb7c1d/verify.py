#!/usr/bin/env python3
"""Reproduce a finite-state certificate for the cyclic Rule 54 image theorem.
Python 3 standard library only; uses exact integer and Boolean arithmetic.
"""
from collections import deque

RULE = 54
FORBIDDEN = ("10110", "10101", "01101", "10111101")
STATES = sorted({p[:k] for p in FORBIDDEN for k in range(len(p))},
                key=lambda s: (len(s), s))
assert len(STATES) == 13


def aho_step(state, symbol):
    tail = state + symbol
    if any(p in tail for p in FORBIDDEN):
        return None
    return max((q for q in STATES if tail.endswith(q)), key=len)


def relation_letter(bit):
    result = []
    for prefix in range(4):
        targets = 0
        for right in range(2):
            triple = 2 * prefix + right
            if (RULE >> triple) & 1 == bit:
                targets |= 1 << (triple & 3)
        result.append(targets)
    return tuple(result)

T = [relation_letter(0), relation_letter(1)]
I = (1, 2, 4, 8)
assert T == [(1, 8, 0, 12), (2, 4, 3, 0)]


def mul(A, B):
    C = []
    for row in A:
        c = 0
        for j in range(4):
            if (row >> j) & 1:
                c |= B[j]
        C.append(c)
    return tuple(C)


def product(word):
    R = I
    for b in word:
        R = mul(R, T[int(b)])
    return R


def diagonal(R):
    return any((R[i] >> i) & 1 for i in range(4))


def certify_image_language():
    # Every forbidden word annihilates the entire predecessor relation.
    for p in FORBIDDEN:
        assert product(p) == (0, 0, 0, 0)

    # All possible cycles of the deterministic avoidance presentation are
    # handled: each visited triple contains a suffix state, a four-by-four
    # Boolean predecessor relation, and length capped at 2.  Because both
    # update maps are deterministic, breadth-first closure proves the claim
    # for cycles of arbitrary length, not just for bounded enumeration.
    visited_by_origin = []
    for origin in STATES:
        start = (origin, I, 0)
        seen = {start}
        queue = deque([start])
        while queue:
            state, rel, size = queue.popleft()
            for bit in "01":
                dest = aho_step(state, bit)
                if dest is None:
                    continue
                next_rel = mul(rel, T[int(bit)])
                next_size = min(2, size + 1)
                assert not (dest == origin and next_size == 2
                            and not diagonal(next_rel)), (
                                "nonliftable avoiding cycle", origin,
                                state, rel, bit)
                item = (dest, next_rel, next_size)
                if item not in seen:
                    seen.add(item)
                    queue.append(item)
        visited_by_origin.append(len(seen))
    assert visited_by_origin == [144, 131, 132, 119, 103, 112,
                                 84, 67, 67, 65, 119, 112, 67]
    # In the one-cell ring the local triple is constant and maps to zero.
    assert ((RULE >> 0) & 1) == ((RULE >> 7) & 1) == 0
    return visited_by_origin


def integer_matrix_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            a = A[i][k]
            if a:
                for j in range(n):
                    result[i][j] += a * B[k][j]
    return result


def exact_determinant_polynomial_and_traces():
    n = len(STATES)
    A = [[0] * n for _ in range(n)]
    for i, state in enumerate(STATES):
        for b in "01":
            dest = aho_step(state, b)
            if dest is not None:
                A[i][STATES.index(dest)] += 1
    current = [[int(i == j) for j in range(n)] for i in range(n)]
    traces = []
    for _ in range(n):
        current = integer_matrix_multiply(current, A)
        traces.append(sum(current[i][i] for i in range(n)))
    assert traces[:13] == [2, 2, 5, 14, 22, 41, 79, 150, 275,
                           512, 959, 1793, 3343]

    # Newton identities exactly determine det(I-zA), including its
    # possibly zero trailing coefficients: no sequence-guessing occurs.
    c = [1]
    for k in range(1, n+1):
        total = sum(c[k-j] * traces[j-1] for j in range(1, k+1))
        assert total % k == 0
        c.append(-total // k)
    assert c == [1, -2, 1, -1, -1, 1, -1] + [0] * 7
    return traces, c


def one_step_ring(word):
    n = len(word)
    return ''.join(str((RULE >> (4 * int(word[(i-1) % n])
                                 + 2 * int(word[i])
                                 + int(word[(i+1) % n]))) & 1)
                   for i in range(n))


def cyclic_avoids(word):
    n = len(word)
    return all(not any(''.join(word[(i+j) % n]
                                 for j in range(len(p))) == p
                           for i in range(n)) for p in FORBIDDEN)


def brute_force():
    expected = [1, 2, 5, 14, 22, 41, 79, 150,
                275, 512, 959, 1793, 3343, 6239, 11650, 21750]
    for n in range(1, 17):
        images = set()
        avoid = set()
        for x in range(1 << n):
            word = f'{x:0{n}b}'
            images.add(one_step_ring(word))
            if cyclic_avoids(word):
                avoid.add(word)
        assert len(images) == expected[n-1]
        if n == 1:
            assert images == {'0'} and avoid == {'0', '1'}
        else:
            assert images == avoid, n
    return expected


def main():
    visits = certify_image_language()
    traces, coefficients = exact_determinant_polynomial_and_traces()
    counts = brute_force()
    assert sum(visits) == 1322
    print('CERTIFICATE_VISITS', ','.join(map(str, visits)))
    print('AVOIDANCE_COUNTS', ','.join(map(str, traces)))
    print('IMAGE_COUNTS_N1_TO_N16', ','.join(map(str, counts)))
    print('DETERMINANT_COEFFICIENTS', ','.join(map(str, coefficients)))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
