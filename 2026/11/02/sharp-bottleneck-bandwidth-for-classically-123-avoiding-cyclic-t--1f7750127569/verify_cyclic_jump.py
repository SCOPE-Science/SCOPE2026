"""Independent finite checks for a sharp classical-123/cyclic-jump threshold.
Run with Python 3.9+; no external packages.
"""
from itertools import permutations


def avoids_123(word):
    # A genuinely independent cubic test for small input sizes.
    n = len(word)
    return all(not (word[i] < word[j] < word[k])
               for i in range(n) for j in range(i + 1, n)
               for k in range(j + 1, n))


def cyclic_bandwidth(word):
    return max(abs(word[i] - word[(i + 1) % len(word)])
               for i in range(len(word)))


def make_witness(n, m):
    assert m >= 2 and 3 <= n <= 3 * m + 1
    if n <= m + 1:
        return tuple(range(n, 0, -1))
    a, b = n - m, max(1, n - 2 * m)
    return ((a,) + tuple(range(n, a, -1))
            + tuple(x for x in range(a - 1, 0, -1) if x != b)
            + (b,))


def predicted(n):
    return max(2, (n + 1) // 3)  # ceil((n-1)/3)


def exhaustive_small():
    for n in range(3, 10):
        minimum = n - 1
        witnesses = 0
        for pi in permutations(range(1, n + 1)):
            if avoids_123(pi):
                bandwidth = cyclic_bandwidth(pi)
                if bandwidth < minimum:
                    minimum = bandwidth
                    witnesses = 1
                elif bandwidth == minimum:
                    witnesses += 1
        assert minimum == predicted(n), (n, minimum, predicted(n))
        print('EXHAUSTIVE', 'n=', n, 'min_bandwidth=', minimum,
              'num_minimizers=', witnesses)


def all_extremal(m):
    n = 3 * m + 1
    a, b = 2 * m + 1, m + 1
    # Different enumerator than exhaustive_small: build words using an online
    # increasing-pair ceiling, exploring every path in the graph.
    count = 0
    first_two = None
    for start in range(1, n + 1):
        def visit(seq, used, minseen, ceiling):
            nonlocal count, first_two
            if len(seq) == n:
                if abs(seq[-1] - seq[0]) <= m:
                    assert (seq[0], seq[1], seq[-2], seq[-1]) == (a, n, 1, b)
                    count += 1
                    if first_two is None:
                        first_two = tuple(seq)
                return
            lo, hi = max(1, seq[-1] - m), min(n, seq[-1] + m)
            for nxt in range(lo, hi + 1):
                if used & (1 << nxt) or nxt > ceiling:
                    continue
                new_ceiling = min(ceiling, nxt) if nxt > minseen else ceiling
                visit(seq + [nxt], used | (1 << nxt), min(minseen, nxt), new_ceiling)
        visit([start], 1 << start, start, n + 1)
    print('BOUNDARY', 'm=', m, 'n=', n, 'count=', count, 'first_example=', first_two)
    assert count > 0


def construction_check():
    verified = 0
    for m in range(2, 41):
        for n in range(3, 3 * m + 2):
            pi = make_witness(n, m)
            assert sorted(pi) == list(range(1, n + 1)), (m, n)
            # Linear-time test for pattern avoidance in the constructed word.
            min_seen = n + 1
            least_possible_second = n + 1
            for x in pi:
                assert x <= least_possible_second, (m, n, pi)
                if x > min_seen:
                    least_possible_second = min(least_possible_second, x)
                min_seen = min(min_seen, x)
            assert cyclic_bandwidth(pi) <= m, (m, n, pi)
            verified += 1
    print('CONSTRUCTION_OK', verified, 'parameter_pairs')


if __name__ == '__main__':
    construction_check()
    exhaustive_small()
    for m in (2, 3, 4):
        all_extremal(m)
    print('VERIFY_OK sharp bandwidth, constructive witnesses, and rigid boundary')
