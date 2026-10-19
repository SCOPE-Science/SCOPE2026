"""Direct finite tests for the one-repeat circular mesosome classification.

Requires only Python 3's standard library. Directly tests conjugacy, rather
than replacing it with Parikh-vector equality. Exhaustive for 2 <= q <= 7.
"""
from itertools import permutations
from math import factorial


def necklaces(q):
    """One representative per rotation: unique symbol 1 is placed first."""
    assert q >= 2
    return [(1,) + v for v in sorted(set(permutations((0, 0) + tuple(range(2, q)))))]


def direct_shortest_mesosome(period, max_half_length):
    n = len(period)
    # Enough repeated copies to include every queried pair of blocks.
    seq = period * (2 * max_half_length // n + 3)
    for half in range(2, max_half_length + 1):
        for start in range(n):
            left = seq[start:start + half]
            right = seq[start + half:start + 2 * half]
            if left == right:
                continue
            if any(right == left[shift:] + left[:shift]
                   for shift in range(1, half)):
                return 2 * half
    return None


def adjacency_of_duplicates(period):
    n = len(period)
    positions = [i for i, letter in enumerate(period) if letter == 0]
    assert len(positions) == 2
    return (positions[0] - positions[1]) % n in (1, n - 1)


def run():
    summary = []
    for q in range(2, 8):
        n = q + 1
        words = necklaces(q)
        assert len(words) == factorial(q) // 2
        adjacent = 0
        nonadjacent = 0
        for period in words:
            girth = direct_shortest_mesosome(period, 2 * n)
            if adjacency_of_duplicates(period):
                adjacent += 1
                assert girth == 2 * (n - 1), (q, period, girth)
            else:
                nonadjacent += 1
                assert girth is None, (q, period, girth)
        assert adjacent == factorial(q - 1)
        assert nonadjacent == (q - 2) * factorial(q - 1) // 2
        summary.append((q, len(words), adjacent, nonadjacent))
    for row in summary:
        print('q=%d necklaces=%d mesosome_forcing=%d mesosome_free=%d' % row)
    print('NEAR_PERMUTATION_MESOSOME_PASS')


if __name__ == '__main__':
    run()
