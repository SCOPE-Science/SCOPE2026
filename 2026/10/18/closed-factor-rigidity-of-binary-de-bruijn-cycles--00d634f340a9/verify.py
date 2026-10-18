#!/usr/bin/env python3
"""Exact circular closed-factor spectrum of binary order-five de Bruijn cycles.

Two complete independent Euler-cycle generators and two independent closed-word
predicates. No external libraries, services, or datasets are needed.
"""
from collections import Counter
from fractions import Fraction

ORDER = 5
N = 1 << ORDER
EXPECTED = {93: 360, 94: 888, 95: 600, 96: 200}


def switch_cycles():
    """Bijections between incoming and outgoing edges at every 4-bit vertex."""
    for switch in range(1 << 16):
        edge = 0
        used = 0
        bits = 0
        for _ in range(N):
            if (used >> edge) & 1:
                break
            used |= 1 << edge
            bits = (bits << 1) | (edge >> 4)
            vertex = edge & 15
            output_bit = (edge >> 4) ^ ((switch >> vertex) & 1)
            edge = ((vertex << 1) & 31) | output_bit
        if used.bit_count() == N and edge == 0:
            yield format(bits, '032b')


def euler_cycles():
    """Enumerate edge-simple closed trails, fixing the unique 00000 edge."""
    walk = [0]
    seen = set()
    def visit(vertex, used):
        if len(walk) == N:
            if vertex == 0:
                word = ''.join(str(e >> 4) for e in walk)
                assert word[:5] == '00000'
                seen.add(word)
            return
        for bit in (0, 1):
            edge = 2 * vertex + bit
            if not (used >> edge) & 1:
                walk.append(edge)
                visit(edge & 15, used | (1 << edge))
                walk.pop()
    visit(0, 1)
    return seen


def closed_by_shortest_return(word):
    """Directly test the defining prefix/suffix word that occurs twice."""
    n = len(word)
    if n == 1:
        return True
    for b in range(1, n):
        pref = word[:b]
        if word[-b:] != pref:
            continue
        occurrences = 0
        for start in range(n - b + 1):
            if word.startswith(pref, start):
                occurrences += 1
                if occurrences >= 3:
                    break
        if occurrences == 2:
            return True
    return False


def closed_by_longest_border(word):
    """Count using longest-border criterion and the de Bruijn order-5 cap."""
    n = len(word)
    if n == 1:
        return True
    for b in range(min(n - 1, ORDER - 1), 0, -1):
        if word[:b] == word[-b:]:
            return word.find(word[:b], 1) == n-b
    return False


def circular_closed_count(cycle, predicate):
    wrapped = cycle * 2
    total = 0
    for length in range(1, N + 1):
        if length <= ORDER:
            factors = {wrapped[i:i+length] for i in range(N)}
        else:
            factors = (wrapped[i:i+length] for i in range(N))
        total += sum(predicate(factor) for factor in factors)
    return total


def circular_closed_by_first_returns(cycle):
    """Enumerate complete first returns rather than testing arbitrary factors."""
    wrapped = cycle * 3
    answers = set(cycle)
    for border_len in range(1, ORDER):
        for start in range(N):
            head = wrapped[start:start+border_len]
            for distance in range(1, N):
                if wrapped[start+distance:start+distance+border_len] == head:
                    if distance + border_len <= N:
                        answers.add(wrapped[start:start+distance+border_len])
                    break
    return len(answers)


def main():
    switch_set = set(switch_cycles())
    euler_set = euler_cycles()
    assert len(switch_set) == len(euler_set) == 2048
    assert switch_set == euler_set
    fast_distribution = Counter()
    slow_distribution = Counter()
    return_distribution = Counter()
    factor_predicate_cases = 0
    for word in sorted(switch_set):
        wrapped = word * 2
        assert len({wrapped[i:i+5] for i in range(N)}) == N
        for length in range(1, N + 1):
            for start in range(N):
                factor = wrapped[start:start+length]
                assert closed_by_longest_border(factor) == closed_by_shortest_return(factor)
                factor_predicate_cases += 1
        fast_distribution[circular_closed_count(word, closed_by_longest_border)] += 1
        slow_distribution[circular_closed_count(word, closed_by_shortest_return)] += 1
        return_distribution[circular_closed_by_first_returns(word)] += 1
    assert factor_predicate_cases == 2048 * 32 * 32
    assert dict(fast_distribution) == dict(slow_distribution) == dict(return_distribution) == EXPECTED, (fast_distribution, slow_distribution, return_distribution)
    mean = sum(Fraction(v*k, 2048) for k, v in EXPECTED.items())
    var = sum(Fraction(v, 2048) * (k-mean)**2 for k, v in EXPECTED.items())
    assert mean == Fraction(1509,16) and var == Fraction(195,256)
    print('VERIFY_OK order5_cycles=2048 local_pairing_assignments=65536 '
          'independent_euler_enumeration=2048 identical_complete_sets=2048 '
          'independent_closed_predicates=2 independent_first_return_enumeration=2048 circular_nonempty_closed_factor_spectrum='
          '93:360,94:888,95:600,96:200 mean=1509/16 variance=195/256')


if __name__ == '__main__':
    main()
