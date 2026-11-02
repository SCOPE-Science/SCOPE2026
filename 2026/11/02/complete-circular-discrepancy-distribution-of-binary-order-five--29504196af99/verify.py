#!/usr/bin/env python3
"""Exact full order-five binary de Bruijn discrepancy enumeration.

Two independent exhaustive constructions and two discrepancy algorithms are
compared. Python standard library only; no downloaded tables or inputs.
"""
from collections import Counter
from hashlib import sha256

EXPECTED = {5: 224, 6: 688, 7: 912, 8: 224}


def discrepancy_prefix(word):
    """Range of prefix sums (valid because every de Bruijn cycle is balanced)."""
    s = lo = hi = 0
    for b in word:
        s += 2 * b - 1
        lo = min(lo, s)
        hi = max(hi, s)
    assert s == 0
    return hi - lo


def discrepancy_substrings(word):
    """Independently scan every circular substring of all lengths 1..32."""
    assert len(word) == 32
    best = 0
    for start in range(32):
        balance = 0
        for length in range(1, 33):
            balance += 2 * word[(start + length - 1) % 32] - 1
            best = max(best, abs(balance))
    return best


def feedback_cycles():
    """All bijective 5-bit feedback maps, tested at their 00000 orbit."""
    for truth in range(1 << 16):
        state = 0
        visited = 0
        result = []
        for step in range(32):
            bit = 1 << state
            if visited & bit:
                break
            visited |= bit
            result.append((state >> 4) & 1)
            tail = state & 15
            output = ((state >> 4) ^ ((truth >> tail) & 1)) & 1
            state = ((state << 1) & 31) | output
        if len(result) == 32 and state == 0:
            assert visited == (1 << 32) - 1
            assert result[:5] == [0] * 5
            yield tuple(result)


def euler_cycles():
    """All Eulerian circuits of the binary 4-gram de Bruijn digraph.

    Each of its 32 distinct labeled edges is a five-bit word. Force the
    unique edge 00000 first; cyclic rotations are thereby identified.
    """
    path = [0]  # edge 00000 gives output symbol zero
    used_start = 1  # first edge 00000 has edge index zero

    def explore(vertex, used):
        if len(path) == 32:
            if vertex == 0:
                yield tuple(path)
            return
        for new_bit in (0, 1):
            edge = (vertex << 1) | new_bit
            flag = 1 << edge
            if used & flag:
                continue
            path.append(edge >> 4)
            yield from explore(edge & 15, used | flag)
            path.pop()

    yield from explore(0, used_start)


def main():
    one = list(feedback_cycles())
    two = list(euler_cycles())
    assert len(one) == len(set(one)) == 2048
    assert len(two) == len(set(two)) == 2048
    assert set(one) == set(two), "Independent exhaustive cycle sets differ"

    a = Counter(discrepancy_prefix(w) for w in one)
    b = Counter(discrepancy_substrings(w) for w in two)
    assert dict(a) == dict(b) == EXPECTED
    assert sum(EXPECTED.values()) == 2048
    assert sum(v * d for d, v in EXPECTED.items()) == 13424
    assert min(a) == 5 and max(a) == 8

    ordered = sorted(''.join(map(str, w)) for w in one)
    fingerprint = sha256(('\n'.join(ordered) + '\n').encode('ascii')).hexdigest()
    assert all(len(x) == 32 and x[:5] == '00000' for x in ordered)
    print('feedback_maps=65536 canonical_cycles=2048')
    print('euler_circuits=2048 exactly_matching_cycles=True')
    print('discrepancy_histogram=', dict(sorted(a.items())))
    print('mean_discrepancy=839/128')
    print('cycle_list_sha256=', fingerprint)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
