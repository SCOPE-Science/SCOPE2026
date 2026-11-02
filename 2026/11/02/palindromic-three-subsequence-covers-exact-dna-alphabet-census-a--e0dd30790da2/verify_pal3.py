"""Exact minimal palindromic-three subsequence supersequence enumeration.

This script is self-contained and uses only the Python standard library.
"""
from functools import lru_cache
from itertools import combinations
from math import factorial


def count_by_masks(q):
    """Count length-3q words with three copies of each symbol and every aba."""
    full = (1 << q) - 1
    @lru_cache(maxsize=None)
    def finish(counts, interior):
        if all(c == 3 for c in counts):
            return 1
        total = 0
        for b in range(q):
            if counts[b] == 3:
                continue
            nxt = list(counts)
            nxt[b] += 1
            mask = list(interior)
            # b occurs strictly within the first-to-third span of a.
            for a in range(q):
                if a != b and 1 <= counts[a] <= 2:
                    mask[a] |= 1 << b
            # The third b ends the last opportunity to see other letters in its span.
            if nxt[b] == 3 and (mask[b] & (full ^ (1 << b))) != (full ^ (1 << b)):
                continue
            total += finish(tuple(nxt), tuple(mask))
        return total
    result = finish((0,) * q, (0,) * q)
    return result, finish.cache_info().currsize


def multiset_words(q):
    """Independent index-set enumeration: every word occurs exactly once."""
    def build(first, positions):
        if first == q - 1:
            yield (first,) * len(positions)
            return
        n = len(positions)
        for indices in combinations(range(n), 3):
            selected = set(indices)
            for remainder in build(first + 1, tuple(positions[i] for i in range(n) if i not in selected)):
                it = iter(remainder)
                yield tuple(first if i in selected else next(it) for i in range(n))
    yield from build(0, tuple(range(3*q)))


def qualifies(w, q):
    """Independent direct subsequence check by first/last occurrences."""
    for a in range(q):
        left = w.index(a)
        right = len(w) - 1 - w[::-1].index(a)
        # Every other letter must occur between the first and third a.
        if not (set(range(q)) - {a}).issubset(set(w[left + 1:right])):
            return False
    return True


def brute(q):
    accepted = seen = 0
    for word in multiset_words(q):
        seen += 1
        accepted += qualifies(word, q)
    return accepted, seen


def main():
    expected = {1: 1, 2: 14, 3: 690, 4: 80016, 5: 17825160}
    state_counts = {}
    for q, target in expected.items():
        value, nstates = count_by_masks(q)
        assert value == target, (q, value, target)
        state_counts[q] = nstates
        assert value % factorial(q) == 0
        assert value >= factorial(q) ** 3
    for q in (1, 2, 3, 4):
        actual, total = brute(q)
        assert actual == expected[q], (q, actual)
        assert total == factorial(3*q) // factorial(3)**q, (q, total)
    witness = tuple(i for _ in range(3) for i in range(4))
    assert qualifies(witness, 4)
    print('VERIFY_OK')
    print('counts', expected)
    print('dp_states', state_counts)
    print('brute_q_1_to_4', {q: factorial(3*q)//6**q for q in (1,2,3,4)})
    print('q4_unlabeled_orbits', expected[4] // factorial(4))
    print('q4_fully_universal_shortest_hosts', factorial(4)**3)


if __name__ == '__main__':
    main()
