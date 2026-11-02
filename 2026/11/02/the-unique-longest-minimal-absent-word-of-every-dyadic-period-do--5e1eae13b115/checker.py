"""Independent finite checks for extremal minimal absent words of period-doubling prefixes.

Run: python checker.py
No third-party dependencies. Finite tests do not replace the induction proof.
"""

from collections import defaultdict


def iterate(k):
    word = "0"
    for _ in range(k):
        word = "".join("01" if c == "0" else "00" for c in word)
    return word


def factors_by_length(word):
    n = len(word)
    return [set()] + [set(word[i:i + ell] for i in range(n - ell + 1))
                      for ell in range(1, n + 1)]


def maws(word):
    """List every minimal absent binary contiguous factor, via all proper borders."""
    n = len(word)
    present = factors_by_length(word)
    ans = {a for a in '01' if a not in present[1]}
    for length in range(2, n + 2):
        middles = present[length - 2] if length > 2 else {''}
        prefixes = present[length - 1]
        complete = present[length] if length <= n else set()
        for q in middles:
            for a in '01':
                if a + q not in prefixes:
                    continue
                for b in '01':
                    candidate = a + q + b
                    if q + b in prefixes and candidate not in complete:
                        ans.add(candidate)
    return ans


def occurrences(word, target):
    return [i for i in range(len(word) - len(target) + 1)
            if word[i:i + len(target)] == target]


def check():
    for k in range(3, 10):
        w = iterate(k)
        h = len(w) // 2
        q = w[:h - 1]
        c = w[h - 1]
        predicted = c + q + c
        assert w[:h - 1] == w[h:2 * h - 1]
        assert w[h - 1] != w[-1]
        assert occurrences(w, q) == [0, h]
        assert len({w[i:i + h] for i in range(len(w) - h + 1)}) == h + 1
        observed = maws(w)
        extremal = {v for v in observed if len(v) == max(map(len, observed))}
        assert extremal == {predicted}, (k, max(map(len, observed)), extremal)
        assert len(predicted) == h + 1
        print('level', k, 'length', len(w), 'MAWs', len(observed),
              'maximal', len(predicted), 'count', len(extremal))
    print('All finite checks passed; infinite proof is separate.')


if __name__ == '__main__':
    check()
