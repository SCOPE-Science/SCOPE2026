#!/usr/bin/env python3
"""Exhaustive exact six-request all-symbol recovery test for RM(1,4).

Reconstructs legal singleton/triple supports from scratch; finds and
independently validates a disjoint recovery witness for each multiset.
"""
from itertools import combinations, combinations_with_replacement
from functools import lru_cache
from math import comb

N = 16
DIM = 4

def generator_column(x):
    assert 0 <= x < N
    return (1 << DIM) | x


def candidate_supports(target):
    choices = [(target,)]
    for triple in combinations(range(N), 3):
        if triple[0] ^ triple[1] ^ triple[2] == target:
            choices.append(triple)
    assert len(choices) == 36
    return tuple((sum(1 << c for c in group), group) for group in choices)

CANDIDATES = tuple(candidate_supports(i) for i in range(N))


def solve(requests):
    names = tuple(sorted(set(requests)))
    counts = tuple(requests.count(x) for x in names)
    pools = [CANDIDATES[x] for x in names]

    @lru_cache(maxsize=None)
    def dfs(needs, occupied):
        if not any(needs):
            return ()
        # Choose a remaining request with the fewest currently usable groups.
        pos = min((i for i, c in enumerate(needs) if c),
                  key=lambda i: sum((mask & occupied) == 0 for mask, _ in pools[i]))
        for mask, group in pools[pos]:
            if mask & occupied:
                continue
            new = list(needs)
            new[pos] -= 1
            suffix = dfs(tuple(new), occupied | mask)
            if suffix is not None:
                return ((names[pos], group),) + suffix
        return None

    return dfs(counts, 0)


def check_witness(requests, witness):
    assert witness is not None and len(witness) == 6
    used = 0
    actual_targets = []
    for target, group in witness:
        assert len(group) in (1, 3)
        assert len(group) == len(set(group))
        assert all(0 <= i < N for i in group)
        support = sum(1 << i for i in group)
        assert not (support & used)
        used |= support
        value = 0
        for i in group:
            value ^= generator_column(i)
        assert value == generator_column(target)
        actual_targets.append(target)
    assert sorted(actual_targets) == list(requests)


def check_upper_bound():
    # All 16 generator columns are distinct, with leading entry 1.
    # A non-singleton recovery group has odd size at least three.
    # Seven demands of the same coordinate would therefore consume
    # at least 1 + 6*3 = 19 distinct coordinates.
    assert len({generator_column(x) for x in range(N)}) == N
    for target in range(N):
        assert not any(generator_column(a) ^ generator_column(b) ==
                       generator_column(target)
                       for a, b in combinations(range(N), 2))
    assert 1 + 6 * 3 > N


def main():
    check_upper_bound()
    count = 0
    support_size_hist = {}
    for requests in combinations_with_replacement(range(N), 6):
        witness = solve(requests)
        check_witness(requests, witness)
        size = sum(len(group) for _, group in witness)
        support_size_hist[size] = support_size_hist.get(size, 0) + 1
        count += 1
    assert count == comb(N+6-1, 6) == 54264
    assert sum(support_size_hist.values()) == count
    print('CHECKED_REQUEST_MULTISETS', count)
    print('RECOVERY_SUPPORT_TOTAL_HISTOGRAM', sorted(support_size_hist.items()))
    print('UPPER_BOUND', 6)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
