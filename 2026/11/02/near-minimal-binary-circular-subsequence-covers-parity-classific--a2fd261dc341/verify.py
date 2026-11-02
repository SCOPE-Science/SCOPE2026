#!/usr/bin/env python3
"""Verify near-minimal binary circular-subsequence universality counts.

Independent greedy-arch, direct-subsequence and cyclic-edge formulations are
compared at finite sizes; the general theorem relies on the accompanying proof.
"""
from itertools import combinations


def arches(seq):
    count = 0
    seen = 0
    for b in seq:
        seen |= 1 << b
        if seen == 3:
            count += 1
            seen = 0
    return count


def circular_universal_greedy(w, k):
    n = len(w)
    return any(arches(w[j:] + w[:j]) >= k for j in range(n))


def transition_matching_formula(w):
    n = len(w)
    k = (n - 1) // 2
    bad = [j for j in range(n) if w[j] == w[(j + 1) % n]]
    if not bad:
        return False
    even_gap_count = sum((((bad[(i + 1) % len(bad)] - bad[i] - 1) % n) % 2 == 0) for i in range(len(bad)))
    return even_gap_count == 1


def direct_circular(w, k):
    n = len(w)
    goal = 1 << k
    for j in range(n):
        v = w[j:] + w[:j]
        subwords = set(tuple(v[i] for i in positions) for positions in combinations(range(n), k))
        if len(subwords) == goal:
            return True
    return False


def canonical_necklace(w):
    return min(w[j:] + w[:j] for j in range(len(w)))


def reverse_necklace(w):
    return canonical_necklace(w[::-1])


def validate():
    direct_cases = greedy_cases = 0
    for k in range(1, 9):
        n = 2 * k + 1
        accepted = []
        for mask in range(1 << n):
            word = tuple(mask >> i & 1 for i in range(n))
            criterion = transition_matching_formula(word)
            via_greedy = circular_universal_greedy(word, k)
            assert criterion == via_greedy, ('edge-vs-greedy', k, word)
            greedy_cases += 1
            if k <= 4:
                actual = direct_circular(word, k)
                assert criterion == actual, ('edge-vs-direct', k, word)
                direct_cases += 1
            if criterion:
                accepted.append(word)
                assert sum(word) in (k, k+1)
                assert len({word[j:] + word[:j] for j in range(n)}) == n
        assert len(accepted) == n * (1 << k), ('labeled', k, len(accepted))
        reflected = sum(all(w[j] == w[(-j) % n] for j in range(n)) for w in accepted)
        assert reflected == (1 << (k//2+1)), ('reflection', k, reflected)
        necklaces = {canonical_necklace(w) for w in accepted}
        assert len(necklaces) == (1 << k), ('necklaces', k)
        bracelets = {min(x, reverse_necklace(x)) for x in necklaces}
        assert len(bracelets) == ((1 << (k - 1)) + (1 << (k // 2))), ('bracelets', k)
        print('k={} n={} labeled={} necklaces={} bracelets={} reflection_fixed={}'.format(
            k, n, len(accepted), len(necklaces), len(bracelets), reflected))
    print('VERIFY_OK greedy_cases={} direct_cases={} k_range=1..8'.format(greedy_cases, direct_cases))


if __name__ == '__main__':
    validate()
