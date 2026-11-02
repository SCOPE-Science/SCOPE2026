"""Exhaustive order-five de Bruijn circular subsequence-universality census.

Requires Python 3.9 or later; no third-party dependencies.
"""
from collections import Counter


def feedback_cycles():
    """Yield (truth table, uniquely zero-rooted 32-letter circular word)."""
    for table in range(1 << 16):
        state, visited, bits = 0, 0, []
        for _ in range(32):
            if (visited >> state) & 1:
                break
            visited |= 1 << state
            bits.append(str(state >> 4))
            suffix = state & 15
            next_bit = (state >> 4) ^ ((table >> suffix) & 1)
            state = (suffix << 1) | next_bit
        if state == 0 and visited == (1 << 32) - 1:
            yield table, ''.join(bits)


def euler_cycles():
    """Independent edge-exhaustion construction in the 16-vertex graph."""
    cycles = set()
    for priority in range(1 << 16):
        used = [0] * 16
        edges = []

        def traverse(vertex):
            while used[vertex] != 2:
                bit = (priority >> vertex) & 1
                bit ^= used[vertex]
                used[vertex] += 1
                edge = 2 * vertex + bit
                traverse(edge & 15)
                edges.append(edge)

        traverse(0)
        assert len(edges) == 32
        word = ''.join(str(edge & 1) for edge in reversed(edges))
        doubled = word + word
        start = doubled.find('00000')
        assert 0 <= start < 32
        cycles.add(doubled[start:start + 32])
    return cycles


def greedy_index(word):
    seen = 0
    arches = 0
    for symbol in word:
        seen |= 1 << int(symbol)
        if seen == 3:
            arches += 1
            seen = 0
    return arches


def counted_index(word):
    """Independent distinct-subsequence DP via earliest matching positions."""
    n = len(word)
    after = [[n + 1, n + 1] for _ in range(n + 2)]
    for start in range(n - 1, -1, -1):
        after[start] = after[start + 1].copy()
        after[start][int(word[start])] = start + 1
    counts = [1] * (n + 2)
    length = 0
    while length <= n:
        counts = [sum(counts[after[pos][letter]]
                      for letter in (0, 1) if after[pos][letter] <= n)
                  for pos in range(n + 2)]
        if counts[0] != (1 << (length + 1)):
            return length
        length += 1
    raise AssertionError('No missing subsequence beyond word length')


def main():
    cycles = dict(feedback_cycles())
    assert len(cycles) == 2048
    assert len(set(cycles.values())) == 2048
    assert set(cycles.values()) == euler_cycles()

    tally = Counter()
    feedback_tally = Counter()
    for table, word in cycles.items():
        assert word.startswith('00000')
        assert len({(word + word)[start:start+5] for start in range(32)}) == 32
        indices = []
        doubled = word + word
        for start in range(32):
            rotated = doubled[start:start + 32]
            i = greedy_index(rotated)
            assert i == counted_index(rotated)
            indices.append(i)
        maximum = max(indices)
        minimum = min(indices)
        winners = indices.count(maximum)
        alternating = any(doubled[start:start+6] in ('010101', '101010')
                          for start in range(32))
        bit5, bit10 = (table >> 5) & 1, (table >> 10) & 1
        assert alternating == (bit5 != bit10)
        assert not (bit5 and bit10)
        profile = (minimum, maximum, winners)
        tally[(profile, alternating)] += 1
        feedback_tally[(bit5, bit10, profile)] += 1

    assert tally == Counter({((9, 10, 28), False): 512,
                            ((10, 11, 23), True): 1536}), tally
    assert feedback_tally == Counter({
        (0, 0, (9, 10, 28)): 512,
        (1, 0, (10, 11, 23)): 768,
        (0, 1, (10, 11, 23)): 768,
    }), feedback_tally
    print('FEEDBACK_TABLE', sorted(feedback_tally.items()))
    print('CIRCULAR_PROFILE', sorted(tally.items()))
    print('UNIQUE_CYCLES', len(cycles))
    print('CHECKS_PASSED')


if __name__ == '__main__':
    main()
