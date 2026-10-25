"""Exact finite checks supporting a theorem on temporal cumulative maximum envy.

No external libraries or input files are required. All arithmetic is integral.
The infinite-family theorem is proved analytically in RESULT.md.
"""
from functools import lru_cache
from itertools import product


def greedy_cost(seq):
    imbalance = total = 0
    for weight in seq:
        imbalance = abs(imbalance - weight)
        total += imbalance
    return total


def optimal_cost(seq):
    states = {0: 0}
    for weight in seq:
        update = {}
        for imbalance, cost in states.items():
            for nxt in (abs(imbalance - weight), imbalance + weight):
                candidate = cost + nxt
                update[nxt] = min(update.get(nxt, candidate), candidate)
        states = update
    return min(states.values())


def check_all_binary_words(max_len=12):
    count = 0
    for n in range(max_len + 1):
        for seq in product((1, 2), repeat=n):
            assert greedy_cost(seq) == optimal_cost(seq), seq
            count += 1
    return count


def check_suffix_invariants(max_len=10, max_d=30):
    count = 0
    for n in range(max_len + 1):
        for seq in product((1, 2), repeat=n):
            @lru_cache(maxsize=None)
            def f(i, d):
                if i == n:
                    return 0
                w = seq[i]
                return min(abs(d - w) + f(i + 1, abs(d - w)),
                           d + w + f(i + 1, d + w))
            for i in range(n + 1):
                assert f(i, 0) - 2 <= f(i, 2) <= f(i, 0), (seq, i)
                assert f(i, 4) >= f(i, 0), (seq, i)
                for d in range(1, max_d + 1):
                    assert f(i, d + 2) >= f(i, d), (seq, i, d)
            count += 1
    return count


def check_three_item_minimality(max_weight=9):
    count = 0
    for n in range(4):
        for seq in product(range(1, max_weight + 1), repeat=n):
            assert greedy_cost(seq) == optimal_cost(seq), seq
            count += 1
    return count


def check_witnesses(max_weight=20):
    for k in range(3, max_weight + 1):
        seq = (1, 1, k, 1)
        assert greedy_cost(seq) == 2 * k
        assert optimal_cost(seq) == 2 * k - 2
    return max_weight - 2


def main():
    a = check_all_binary_words()
    b = check_suffix_invariants()
    c = check_three_item_minimality()
    d = check_witnesses()
    print('PASS binary sequences lengths 0..12:', a)
    print('PASS full suffix-state invariant checks lengths 0..10:', b)
    print('PASS arbitrary-positive-integer words lengths 0..3, values 1..9:', c)
    print('PASS counterexample family k=3..20:', d)


if __name__ == '__main__':
    main()
