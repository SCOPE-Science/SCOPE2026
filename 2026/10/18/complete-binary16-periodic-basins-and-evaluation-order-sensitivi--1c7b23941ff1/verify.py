#!/usr/bin/env python3
"""Exact exhaustive functional graphs for two binary16 quadratic iterations.

Only standard-library integer arithmetic is required for the proof certificate.
Every input is a finite binary16 value in [-2,2]; signed zeros are identified.
The alternative struct oracle uses native binary16 conversion independently.
"""
from bisect import bisect_left
from collections import Counter, deque
from fractions import Fraction
import struct

U = 1 << 24


def decode_half_word(word):
    """Decode a finite binary16 bit word to the integer value 2**24*x."""
    exponent = (word >> 10) & 31
    fraction = word & 1023
    if exponent == 31:
        return None
    magnitude = fraction if exponent == 0 else (1024 + fraction) << (exponent - 1)
    return -magnitude if word & 0x8000 else magnitude


all_encodings = {}
for word in range(1 << 16):
    value = decode_half_word(word)
    if value is not None:
        all_encodings[value] = word
all_encodings[0] = 0  # Two signed-zero words represent one numerical state.
STATES = sorted(value for value in all_encodings if abs(value) <= 2 * U)
SQUARE_STATES = sorted(value for value in all_encodings if 0 <= value <= 4 * U)
assert len(STATES) == 32769
assert len(SQUARE_STATES) == 17409
assert STATES[0] == -2 * U and STATES[-1] == 2 * U


def nearest_half(numerator, denominator, admissible_values):
    """Round exact dyadic result (numerator/denominator)/U to binary16.

    ``admissible_values`` comprises the complete binary16 choices in the
    exact output range. Both numerator and denominator are integers.
    """
    # ceil(numerator / denominator), also correct for negative numerators.
    upper_bound = -(-numerator // denominator)
    position = bisect_left(admissible_values, upper_bound)
    if position == 0:
        return admissible_values[0]
    if position == len(admissible_values):
        return admissible_values[-1]
    low, high = admissible_values[position - 1], admissible_values[position]
    left = numerator - low * denominator
    right = high * denominator - numerator
    assert left >= 0 and right >= 0
    if left < right:
        return low
    if right < left:
        return high
    # Even least significant significand bit is equivalent to even raw word.
    assert (all_encodings[low] & 1) != (all_encodings[high] & 1)
    return low if (all_encodings[low] & 1) == 0 else high


def one_final_round(k):
    # x=k/U, 2-x**2=(2*U**2-k**2)/U**2.
    return nearest_half(2 * U * U - k * k, U, STATES)


def two_separate_rounds(k):
    rounded_square = nearest_half(k * k, U, SQUARE_STATES)
    return nearest_half((2 * U - rounded_square) * U, U, STATES)


def graph_certificate(successors):
    """Cycle and full-basin census via exact indegree peeling."""
    n = len(successors)
    indegree = [0] * n
    for destination in successors:
        indegree[destination] += 1
    queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
    peeled = []
    while queue:
        v = queue.popleft()
        peeled.append(v)
        w = successors[v]
        indegree[w] -= 1
        if indegree[w] == 0:
            queue.append(w)

    cycle_id = [-1] * n
    depth = [-1] * n
    cycles = []
    for start in range(n):
        if indegree[start] == 0 or cycle_id[start] != -1:
            continue
        cycle = []
        v = start
        while cycle_id[v] == -1:
            cycle_id[v] = len(cycles)
            depth[v] = 0
            cycle.append(v)
            v = successors[v]
        assert v == start
        cycles.append(cycle)
    for v in reversed(peeled):
        w = successors[v]
        assert cycle_id[w] >= 0
        cycle_id[v] = cycle_id[w]
        depth[v] = depth[w] + 1
    assert all(c >= 0 for c in cycle_id)
    assert all(d >= 0 for d in depth)
    assert len(peeled) + sum(map(len, cycles)) == n
    basin = Counter(cycle_id)
    assert sum(basin.values()) == n
    assert all(successors[v] in cycle for cycle in cycles for v in cycle)

    # A second direct path walker checks the preperiod and cycle length for
    # every starting state without relying on the peeling traversal.
    for start in range(n):
        v = start
        for _ in range(depth[start]):
            v = successors[v]
        assert depth[v] == 0 and cycle_id[v] == cycle_id[start]
    return cycles, cycle_id, depth, basin


def uniform_stored_mean(cycles, ids, allowed=lambda x: True):
    subset = [i for i, x in enumerate(STATES) if allowed(x)]
    counts = Counter(ids[i] for i in subset)
    return sum((Fraction(sum(STATES[v] for v in cycle), len(cycle) * U) * counts[j]
                for j, cycle in enumerate(cycles)), Fraction(0)) / len(subset)


def output_certificate(fn):
    lookup = {v: i for i, v in enumerate(STATES)}
    successors = [lookup[fn(v)] for v in STATES]
    cycles, ids, depth, basin = graph_certificate(successors)
    table = sorted((min(all_encodings[STATES[v]] for v in cyc),
                    min(STATES[v] for v in cyc), len(cyc), basin[j])
                   for j, cyc in enumerate(cycles))
    # Sort by minimum numerical value rather than bit encoding.
    table = sorted((min(STATES[v] for v in cyc), len(cyc), basin[j])
                   for j, cyc in enumerate(cycles))
    return successors, cycles, ids, depth, table, uniform_stored_mean(cycles, ids), uniform_stored_mean(
        cycles, ids, lambda x: 0 <= x <= U)


def independent_struct_oracle(x, two_rounds):
    """Distinct half conversion path; all expressions fit exactly in float64."""
    real = x / U
    if two_rounds:
        squared = struct.unpack('<e', struct.pack('<e', real * real))[0]
        answer = struct.unpack('<e', struct.pack('<e', 2.0 - squared))[0]
    else:
        answer = struct.unpack('<e', struct.pack('<e', 2.0 - real * real))[0]
    return int(answer * U)


def main():
    one = output_certificate(one_final_round)
    two = output_certificate(two_separate_rounds)
    expected_one = [
        (-33554432, 1, 20785),
        (-33423360, 94, 11706),
        (-32063488, 6, 168),
        (-28229632, 5, 60),
        (-27541504, 5, 48),
        (16777216, 1, 2),
    ]
    expected_two = [
        (-33554432, 1, 20341),
        (-33292288, 44, 12156),
        (-31293440, 4, 62),
        (-29229056, 8, 208),
        (16777216, 1, 2),
    ]
    assert one[4] == expected_one, (one[4], expected_one)
    assert two[4] == expected_two, (two[4], expected_two)
    assert one[5] == Fraction(-145830929641, 126168514560)
    assert two[5] == Fraction(-861146119, 738220032)
    assert one[6] == Fraction(-217681579937, 177430609920)
    assert two[6] == Fraction(-215011427, 173026304)
    assert max(one[3]) == 59 and one[3].count(59) == 2
    assert max(two[3]) == 69 and two[3].count(69) == 2
    assert len(set(one[0])) == 2049
    assert len(set(two[0])) == 1946
    assert sum(a != b for a, b in zip(one[0], two[0])) == 1842
    for fn, two_rounds in [(one_final_round, False), (two_separate_rounds, True)]:
        for x in STATES:
            assert fn(x) == independent_struct_oracle(x, two_rounds)
    for label, cert in [('single', one), ('separate', two)]:
        print(label, 'cycles:', [
            (hex(all_encodings[low]), period, basin)
            for low, period, basin in cert[4]
        ])
        print(label, 'uniform-stored long-run mean:', cert[5])
        print(label, '[0,1]-stored long-run mean:', cert[6])
        print(label, 'longest transient:', max(cert[3]))
    print('OK: 32769 states, all transitions and basins checked exactly;')
    print('OK: both 32769-transition maps independently match binary16 conversion;')
    print('OK: 1842 evaluation-order discrepancies, rational averages and cycle data.')


if __name__ == '__main__':
    main()
