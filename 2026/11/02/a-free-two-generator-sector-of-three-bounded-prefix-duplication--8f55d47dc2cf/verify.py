#!/usr/bin/env python3
"""Independent finite checks for a bounded-prefix-duplication normal form."""
from collections import defaultdict
from itertools import product
from math import comb

BLOCKS = ("01", "010")


def all_derivations(seed, limit, bound=3):
    """Count all distinct step sequences reaching words of length <= limit."""
    by_length = [defaultdict(int) for _ in range(limit + 1)]
    by_length[len(seed)][seed] = 1
    for length in range(len(seed), limit + 1):
        for word, count in list(by_length[length].items()):
            for size in range(1, min(length, bound) + 1):
                target = word[:size] + word
                if len(target) <= limit:
                    by_length[len(target)][target] += count
    result = {}
    for layer in by_length:
        result.update(layer)
    return result


def expected_sector(seed, limit):
    words = {seed: 0}
    todo = [(seed, 0)]
    while todo:
        word, steps = todo.pop()
        for b in BLOCKS:
            w = b + word
            if len(w) <= limit:
                assert w not in words, (seed, word, w)
                words[w] = steps + 1
                todo.append((w, steps + 1))
    return words


def suffix_shortest_counts(seed, target):
    """Unrelated backward dynamic program on positions in target."""
    if not target.endswith(seed):
        return None
    m = len(target) - len(seed)
    dp = {m: (0, 1)}
    for i in range(m, 0, -1):
        if i not in dp:
            continue
        dist, num = dp[i]
        for size in (1, 2, 3):
            if i < size or target[i-size:i] != target[i:i+size]:
                continue
            previous = dp.get(i-size)
            if previous is None or dist + 1 < previous[0]:
                dp[i-size] = (dist+1, num)
            elif dist + 1 == previous[0]:
                dp[i-size] = (dist+1, previous[1]+num)
    return dp.get(0)


def test_general():
    seeds = ("010", "0100", "01001", "01010", "010010")
    tested = 0
    for seed in seeds:
        limit = len(seed) + 19
        observed = all_derivations(seed, limit)
        expected = expected_sector(seed, limit)
        actual_sector = {w: c for w, c in observed.items() if w.startswith('01')}
        assert set(actual_sector) == set(expected), seed
        for word, steps in expected.items():
            assert observed[word] == 1, (seed, word, observed[word])
            assert steps == word.count('1') - seed.count('1')
            assert suffix_shortest_counts(seed, word) == (steps, 1)
        for delta in range(limit-len(seed)+1):
            for steps in range(delta+1):
                count = sum((len(w)-len(seed)==delta and v==steps)
                            for w,v in expected.items())
                want = comb(steps,delta-2*steps) if 0 <= delta-2*steps <= steps else 0
                assert count == want, (seed,delta,steps,count,want)
        tested += len(expected)
    return tested


def test_fibonacci():
    f = ['0', '01']
    for _ in range(2, 17):
        f.append(f[-1] + f[-2])
    pairs = 0
    for i in range(2, 16):
        for j in range(i, 17, 2):
            seed, target = f[i], f[j]
            assert target.endswith(seed)
            assert seed.startswith('010') and target.startswith('010')
            assert '11' not in target and '000' not in target
            assert suffix_shortest_counts(seed, target) == (
                target.count('1') - seed.count('1'), 1), (i,j)
            pairs += 1
    return pairs


def test_boundary():
    seed = '010'
    via_four = '0101' + ('01' + seed)
    via_three = '01' + '01' + '01' + seed
    assert via_four == via_three == '010101010'
    assert all_derivations(seed, 9, 4)[via_four] >= 2
    assert all_derivations(seed, 9, 3)[via_four] == 1
    rare = '0100' + '010' + seed
    assert rare == '0100010010' and rare.startswith('01') and '000' in rare
    assert rare not in all_derivations(seed, len(rare), 3)
    assert rare in all_derivations(seed, len(rare), 4)
    return 2


if __name__ == '__main__':
    n = test_general()
    p = test_fibonacci()
    b = test_boundary()
    print('PASS general-sector targets:',n)
    print('PASS Fibonacci suffix pairs:',p)
    print('PASS sharp-bound examples:',b)
    print('PASS independent forward and reverse dynamic checks')
