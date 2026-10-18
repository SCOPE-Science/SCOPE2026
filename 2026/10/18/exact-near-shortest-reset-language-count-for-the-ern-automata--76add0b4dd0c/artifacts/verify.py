#!/usr/bin/env python3
"""Reproduce the finite checks for the near-minimum reset-language theorem.

No packages beyond the Python standard library are required.
"""
from collections import Counter


def image(mask, letter, n):
    out = 0
    for state in range(n):
        if (mask >> state) & 1:
            target = (state + 1) % n if letter == 'a' else (0 if state == n - 1 else state)
            out |= 1 << target
    return out


def reset_target(word, n):
    state_mask = (1 << n) - 1
    for c in word:
        state_mask = image(state_mask, c, n)
    if state_mask.bit_count() != 1:
        return None
    return state_mask.bit_length() - 1


def predicted_words(n):
    u = 'b' + ('a' * (n - 1) + 'b') * (n - 2)
    assert len(u) == (n - 1) ** 2
    ans = {'a' + u, u + 'a', u + 'b'}
    for i in range(1, n - 1):
        run_start = 1 + (i - 1) * n
        assert u[run_start:run_start + n - 1] == 'a' * (n - 1)
        for j in range(n - 1):
            if j == i:
                continue
            insert = run_start + j
            ans.add(u[:insert] + 'b' + u[insert:])
    return u, ans


def count_reset_words_by_forward_dp(n):
    sz = 1 << n
    transitions = ([image(mask, 'a', n) for mask in range(sz)],
                   [image(mask, 'b', n) for mask in range(sz)])
    L = (n - 1) ** 2
    dp = {(1 << n) - 1: 1}
    observed = {}
    for length in range(L + 2):
        reset_count = sum(cnt for mask, cnt in dp.items() if mask.bit_count() == 1)
        if length < L:
            assert reset_count == 0, (n, length, reset_count)
        else:
            observed[length] = reset_count
        if length == L + 1:
            break
        next_dp = Counter()
        for mask, cnt in dp.items():
            next_dp[transitions[0][mask]] += cnt
            next_dp[transitions[1][mask]] += cnt
        dp = next_dp
    return observed[L], observed[L + 1]


def test_preimage_nonproductive_steps(n):
    # Direct inverse-set reconstruction, independent of the closed count.
    Q = set(range(n))
    for k in range(2, n):
        for j in range(n - 1):
            arc_start = (n - 1 - j) % n
            S = {(arc_start + h) % n for h in range(k)}
            invb = {i for i in Q if ((0 if i == n - 1 else i) in S)}
            if j == k - 1:
                assert len(invb) == len(S) - 1
            else:
                assert invb == S


def main():
    checked = 0
    for n in range(3, 14):
        L = (n - 1) ** 2
        u, predicted = predicted_words(n)
        assert reset_target(u, n) == 0
        assert len(predicted) == (n - 2) ** 2 + 3, n
        for w in predicted:
            assert len(w) == L + 1
            assert reset_target(w, n) is not None, (n, w)
        shortest, near_shortest = count_reset_words_by_forward_dp(n)
        assert shortest == 1, (n, shortest)
        assert near_shortest == len(predicted), (n, near_shortest, len(predicted))
        test_preimage_nonproductive_steps(n)
        checked += 1
        print('n=%d L=%d shortest=%d near=%d' % (n, L, shortest, near_shortest))
    # Independently exhaust all binary strings through the near-minimum length
    # for n=3,4,5, rather than relying solely on a subset-state DP.
    for n in (3, 4, 5):
        L = (n - 1) ** 2
        u, predicted = predicted_words(n)
        observed = set()
        for value in range(1 << (L + 1)):
            w = format(value, '0%db' % (L + 1)).replace('0', 'a').replace('1', 'b')
            if reset_target(w, n) is not None:
                observed.add(w)
        assert observed == predicted, (n, len(observed), len(predicted))
    print('CERNY_NEAR_RESET_PASS n=3..13 count_checks=%d exhaustive_n=3,4,5' % checked)


if __name__ == '__main__':
    main()
