"""Independent finite checks for the pair-merger theorem of the cyclic Černý automata.

Uses reverse breadth-first search on the exact pair graph; it does not use
any claimed rank formula to determine shortest distances or path counts.
"""
from collections import deque
from math import comb


def image(pair, letter, n):
    if pair is None:
        return None
    if letter == 'a':
        q = sorted(((x + 1) % n for x in pair))
    elif letter == 'b':
        q = sorted((1 if x == 0 else x for x in pair))
    else:
        raise ValueError(letter)
    return None if q[0] == q[1] else tuple(q)


def analytical_pairs(n):
    ranks = {}
    spec = {}
    for d in range(1, n // 2 + 1):
        width = n if 2 * d < n else n // 2
        for j in range(width):
            pair = tuple(sorted(((-j) % n, (d - j) % n)))
            assert pair not in ranks
            ranks[pair] = n * (d - 1) + j + 1
            spec[pair] = (d, j)
    assert len(ranks) == comb(n, 2)
    return ranks, spec


def breadth_first_shortest_distances(n):
    pairs = [(x, y) for x in range(n) for y in range(x + 1, n)]
    preds = {p: [] for p in pairs}
    preds[None] = []
    for p in pairs:
        for letter in ('a', 'b'):
            q = image(p, letter, n)
            preds[q].append((p, letter))
    d = {None: 0}
    dq = deque([None])
    while dq:
        q = dq.popleft()
        for pred, letter in preds[q]:
            if pred not in d:
                d[pred] = d[q] + 1
                dq.append(pred)
    assert len(d) == len(pairs) + 1
    paths = {None: 1}
    for p in sorted(pairs, key=lambda q: d[q]):
        paths[p] = sum(paths[image(p, a, n)] for a in ('a', 'b')
                       if d[image(p, a, n)] == d[p] - 1)
    return d, paths


def check(n):
    ranks, specs = analytical_pairs(n)
    dist, shortest_path_count = breadth_first_shortest_distances(n)
    assert set(dist) == set(ranks) | {None}
    assert sorted(ranks.values()) == list(range(1, comb(n, 2) + 1))
    for pair, (d, j) in specs.items():
        rank = ranks[pair]
        assert dist[pair] == rank
        assert shortest_path_count[pair] == 1
        for a in ('a', 'b'):
            child = image(pair, a, n)
            assert ranks.get(child, 0) >= rank - 1
        forced_letter = 'b' if j == 0 else 'a'
        other_letter = 'a' if j == 0 else 'b'
        assert ranks.get(image(pair, forced_letter, n), 0) == rank - 1
        assert ranks.get(image(pair, other_letter, n), 0) != rank - 1
        word = 'a' * j + 'b' + ('a' * (n - 1) + 'b') * (d - 1)
        assert len(word) == rank
        q = pair
        for a in word:
            q = image(q, a, n)
        assert q is None
        assert word.count('b') == d
    return len(ranks)


def main():
    tested = 0
    for n in range(3, 41):
        tested += check(n)
    print(f'VERIFY_OK: n=3..40; {tested} pair instances; ' +
          'independent reverse BFS, distance spectrum, uniqueness, ' +
          'rank monotonicity and exact optimal words agree')


if __name__ == '__main__':
    main()
