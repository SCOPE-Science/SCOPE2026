#!/usr/bin/env python3
from collections import Counter, defaultdict


def closed_masks(n):
    return [sum(1 << u for u in ((v - 1) % n, v, (v + 1) % n)) for v in range(n)]


def maximum_sequences(n):
    masks = closed_masks(n)
    all_mask = (1 << n) - 1
    best_len = -1
    best = []

    def dfs(seq, used, dominated):
        nonlocal best_len, best
        if dominated == all_mask:
            k = len(seq)
            if k > best_len:
                best_len = k
                best = [tuple(seq)]
            elif k == best_len:
                best.append(tuple(seq))
            return
        for v in range(n):
            if (used >> v) & 1:
                continue
            new = masks[v] & ~dominated
            if new:
                dfs(seq + [v], used | (1 << v), dominated | masks[v])

    dfs([], 0, 0)
    return best_len, best


def cyclic_distance(n, a, b):
    d = (a - b) % n
    return min(d, n - d)


def check(n):
    gamma, seqs = maximum_sequences(n)
    expected_gamma = 1 if n == 3 else n - 2
    assert gamma == expected_gamma, (n, gamma, expected_gamma)
    if n == 3:
        assert len(seqs) == 3
        return len(seqs), len({frozenset(s) for s in seqs})

    expected_count = 3 * n * (2 ** (n - 4))
    assert len(seqs) == expected_count, (n, len(seqs), expected_count)

    set_mult = Counter(frozenset(s) for s in seqs)
    by_dist = defaultdict(list)
    for S, mult in set_mult.items():
        omitted = sorted(set(range(n)) - set(S))
        assert len(omitted) == 2
        d = cyclic_distance(n, omitted[0], omitted[1])
        assert d in (1, 2), (n, omitted, d)
        by_dist[d].append(mult)

    if n == 4:
        assert len(set_mult) == 6
        assert len(by_dist[1]) == 4 and set(by_dist[1]) == {2}
        assert len(by_dist[2]) == 2 and set(by_dist[2]) == {2}
    else:
        assert len(set_mult) == 2 * n
        assert len(by_dist[1]) == n and set(by_dist[1]) == {2 ** (n - 3)}
        assert len(by_dist[2]) == n and set(by_dist[2]) == {2 ** (n - 4)}
    return len(seqs), len(set_mult)


def main():
    total_sequences = 0
    total_sets = 0
    for n in range(3, 11):
        a, b = check(n)
        total_sequences += a
        total_sets += b
    print(f"VERIFY_OK n_range=3..10 maximum_sequence_checks={total_sequences} maximum_set_checks={total_sets} formula=3*n*2^(n-4)_for_n>=4")


if __name__ == '__main__':
    main()
