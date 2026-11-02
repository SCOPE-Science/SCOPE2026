"""Finite checks for the exact gap between split-source and joined-history parses.

Run with Python 3 standard library: python3 verify.py
"""
from functools import lru_cache
from itertools import product


def construct(m):
    alphabet = ''.join(chr(65 + j) for j in range(m))
    words = [alphabet]
    for j in range(2, m + 1):
        words.append(words[-1] + alphabet[j-1:] + words[-1])
    return alphabet, words


def allowed(reference, target, i, phrase, joined):
    if len(phrase) == 1:
        return True
    history = target[:i]
    if joined:
        return phrase in (reference + history)
    return phrase in reference or phrase in history


def greedy(reference, target, joined):
    i, pieces = 0, []
    while i < len(target):
        size = 1
        while i + size < len(target) and allowed(
                reference, target, i, target[i:i + size + 1], joined):
            size += 1
        pieces.append(target[i:i + size])
        i += size
    return pieces


def optimum(reference, target, joined):
    n = len(target)
    dp = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        possibilities = [1 + dp[i + k] for k in range(1, n-i+1)
                         if allowed(reference, target, i, target[i:i+k], joined)]
        dp[i] = min(possibilities)
    return dp[0]


def predicted_split_lengths(m, words):
    if m == 1:
        return [1]
    ans = [m, m-1, m]
    for j in range(3, m + 1):
        d = m-j+1 + len(words[j-3])
        ans += [d, d+1]
    return ans


def predicted_joined_lengths(m, words):
    return [m] + [(m-j+1)+len(words[j-2]) for j in range(2, m+1)]


def main():
    for m in range(1, 8):
        reference, words = construct(m)
        target = words[-1]
        split = greedy(reference, target, joined=False)
        joined = greedy(reference, target, joined=True)
        split_sizes = list(map(len, split))
        joined_sizes = list(map(len, joined))
        assert ''.join(split) == target == ''.join(joined)
        assert len(target) == (m-1)*2**m + 1
        assert split_sizes == predicted_split_lengths(m, words), (m, split_sizes)
        assert joined_sizes == predicted_joined_lengths(m, words), (m, joined_sizes)
        assert len(split) == 2*m-1 and len(joined) == m
        for j in range(3, m+1):
            previous = words[j-2]
            earlier = words[j-3]
            first = reference[j-1:] + earlier
            second = reference[j-2:] + earlier
            bridge = reference[-1] + reference[j-2]
            assert previous.count(bridge) == 1
            assert previous.count(first) == previous.count(second) == 1
            assert previous.endswith(first) and previous.endswith(second)
            assert (previous + first).count(second) == 1
        if m <= 5:
            assert optimum(reference, target, False) == 2*m-1
            assert optimum(reference, target, True) == m
        print('construct', m, 'length', len(target),
              'split', len(split), 'joined', len(joined), 'OK')

    count = 0
    for r in range(1, 4):
        for n in range(1, 7):
            for rr in product('01', repeat=r):
                R = ''.join(rr)
                for tt in product('01', repeat=n):
                    s = ''.join(tt)
                    a = optimum(R, s, joined=False)
                    p = optimum(R, s, joined=True)
                    assert p <= a <= 2*p-1, (R, s, p, a)
                    assert a == len(greedy(R, s, joined=False))
                    assert p == len(greedy(R, s, joined=True))
                    count += 1
    print('binary-exhaustive', count, 'paired optimum comparisons OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
