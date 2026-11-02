"""Self-contained integer/string certificate for de Bruijn MCS spectra, orders 1--5.
Run: python3 verify.py
"""
from collections import Counter
from hashlib import sha256

EXPECTED = {
    1: {2: 1},
    2: {4: 1},
    3: {8: 2},
    4: {19: 4, 20: 10, 21: 2},
    5: {
        40: 8, 41: 16, 42: 112, 43: 204, 44: 252,
        45: 304, 46: 308, 47: 264, 48: 176, 49: 124,
        50: 108, 51: 84, 52: 52, 53: 28, 54: 8,
    },
}
EXPECTED_WORDS = {1: 1, 2: 1, 3: 2, 4: 16, 5: 2048}


def all_linearizations(order):
    """All canonical 0**order-rooted Euler circuits, once each."""
    size = 1 << order
    mask = size - 1
    symbols = ['0'] * order

    def dfs(last_vertex, used_edges):
        if used_edges.bit_count() == size:
            word = ''.join(symbols)
            cycle = word[:size]
            # Independently test the circular de Bruijn condition.
            wrap = cycle + cycle[:order - 1]
            if len({wrap[p:p + order] for p in range(size)}) == size:
                assert word == wrap
                yield word
            return
        for bit in (0, 1):
            edge = ((last_vertex << 1) & mask) | bit
            if not (used_edges & (1 << edge)):
                symbols.append(str(bit))
                yield from dfs(edge, used_edges | (1 << edge))
                symbols.pop()

    yield from dfs(0, 1)  # Edge 00...0 has already been used.


def closed_direct(factor):
    if len(factor) == 1:
        return True
    for length in range(len(factor) - 1, 0, -1):
        border = factor[:length]
        if factor.endswith(border):
            # find() checks overlapping occurrences as well.
            if factor.find(border, 1) == len(factor) - length:
                return True
    return False


def mcs_direct(text):
    """Definition-only checker: all intervals, borders and two extensions."""
    n = len(text)
    closed = [[False] * n for _ in range(n)]
    for i in range(n):
        for e in range(i, n):
            closed[i][e] = closed_direct(text[i:e + 1])
    return {
        (i, e) for i in range(n) for e in range(i, n)
        if closed[i][e]
        and (i == 0 or not closed[i - 1][e])
        and (e == n - 1 or not closed[i][e + 1])
    }


def mcs_via_lcp(text):
    """Independent next-occurrence / record-LCP characterization."""
    n = len(text)
    lcp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if text[i] == text[j]:
                lcp[i][j] = 1 + lcp[i + 1][j + 1]
    answer = set()
    for i in range(n):
        if (i == 0 or text[i] != text[i - 1]) and (
            i == n - 1 or text[i] != text[i + 1]
        ):
            answer.add((i, i))
        previous_maximum = 0
        for j in range(i + 1, n):
            length = lcp[i][j]
            if length > previous_maximum:
                if i == 0 or text[i - 1] != text[j - 1]:
                    answer.add((i, j + length - 1))
                previous_maximum = length
    return answer


def verify():
    for order in range(1, 6):
        histogram = Counter()
        examples = {}
        seen = set()
        checksum = sha256()
        for word in all_linearizations(order):
            assert word.startswith('0' * order)
            assert len(word) == (1 << order) + order - 1
            assert word not in seen
            seen.add(word)
            checksum.update((word + '\n').encode('ascii'))
            a = mcs_direct(word)
            b = mcs_via_lcp(word)
            assert a == b, (order, word, a ^ b)
            count = len(a)
            histogram[count] += 1
            examples.setdefault(count, word)
        assert len(seen) == EXPECTED_WORDS[order], order
        assert dict(histogram) == EXPECTED[order], (order, histogram)
        smallest = min(histogram)
        largest = max(histogram)
        print('order', order, 'words', len(seen), 'min', smallest,
              'max', largest, 'histogram', dict(sorted(histogram.items())))
        print('enumeration_sha256', checksum.hexdigest())
        print('min_example', examples[smallest])
        print('max_example', examples[largest])
    print('DEBRUIJN_MCS_CENSUS_VERIFY_OK')

if __name__ == '__main__':
    verify()
