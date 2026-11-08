#!/usr/bin/env python3
"""Independently check the two-hole reaching-distance theorem.

Standard Cerny automaton: a maps n-1 to 0 and fixes the other states;
b rotates states by one. All image sets are bitmasks. Requires stdlib only.
"""
from collections import Counter, deque
from itertools import combinations


def predicted(n, u, v):
    assert 3 <= n and 0 <= u < v < n
    if v == n - 1:
        return n + 2 if u == 0 else u + 3
    return n + u + 3 if v == u + 1 else v + 3


def normal_witness(n, u, v):
    candidates = []
    for newest, other in ((u, v), (v, u)):
        t = (newest + 1) % n
        k = (other - newest) % n
        if k >= 2:
            candidates.append('a' + 'b' * k + 'a' + 'b' * t)
    assert candidates
    return min(candidates, key=lambda w: (len(w), w))


def action(n, image, symbol):
    if symbol == 'a':
        return (image & ~(1 << (n - 1))) | (1 if image & (1 << (n - 1)) else 0)
    assert symbol == 'b'
    full = (1 << n) - 1
    return ((image << 1) & full) | (image >> (n - 1))


def exhaustive_distances(n):
    full = (1 << n) - 1
    distances = {full: 0}
    queue = deque([full])
    while queue:
        state = queue.popleft()
        for symbol in 'ab':
            nxt = action(n, state, symbol)
            if nxt not in distances:
                distances[nxt] = distances[state] + 1
                queue.append(nxt)
    return distances


def f(n, holes):
    holes = set(holes)
    if not holes:
        return 0
    if len(holes) == 1:
        return 1 + ((next(iter(holes)) + 1) % n)
    assert len(holes) == 2
    u, v = sorted(holes)
    return predicted(n, u, v)


def check_lipschitz(n):
    states = [frozenset()] + [frozenset([u]) for u in range(n)]
    states += [frozenset([u, v]) for u, v in combinations(range(n), 2)]
    for holes in states:
        rotated = {(x + 1) % n for x in holes}
        assert f(n, rotated) <= f(n, holes) + 1, ('b', n, holes)
        if n - 1 in holes:
            new = set(holes)
        elif 0 in holes:
            new = (set(holes) - {0}) | {n - 1}
        else:
            new = set(holes) | {n - 1}
        if len(new) <= 2:
            assert f(n, new) <= f(n, holes) + 1, ('a', n, holes)


def main():
    bfs_states = pairs = 0
    for n in range(3, 16):
        distances = exhaustive_distances(n)
        full = (1 << n) - 1
        assert len(distances) == full
        histogram = Counter()
        for u, v in combinations(range(n), 2):
            target = full ^ (1 << u) ^ (1 << v)
            expected = predicted(n, u, v)
            assert distances[target] == expected, (n, u, v, distances[target], expected)
            word = normal_witness(n, u, v)
            current = full
            for symbol in word:
                current = action(n, current, symbol)
            assert current == target and len(word) == expected
            histogram[expected] += 1
            pairs += 1
        expected_hist = {length: length - 3 for length in range(4, n + 2)}
        expected_hist.update({length: 1 for length in range(n + 2, 2 * n + 1)})
        assert dict(histogram) == expected_hist, (n, histogram, expected_hist)
        bfs_states += len(distances)
    print(f'BFS_PASS n=3..15, total_visited_subset_states={bfs_states}, target_pairs={pairs}')
    for n in range(3, 141):
        check_lipschitz(n)
    print('POTENTIAL_TRANSITION_PASS n=3..140, all hole sets of sizes 0, 1, 2')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
