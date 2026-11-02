#!/usr/bin/env python3
"""Reproduce the finite independent Parikh-vector checks described in RESULT.md."""
from collections import defaultdict

def stern(i):
    assert i >= 0
    if i < 2: return i
    if i % 2 == 0: return stern(i // 2)
    return stern(i // 2) + stern(i // 2 + 1)

def fibonacci(i):
    a, b = 0, 1
    for _ in range(i): a, b = b, a + b
    return a

def spectrum(word, alphabet_size):
    length = len(word)
    ans = [1]
    for ell in range(1, length + 1):
        counts = [0] * alphabet_size
        for v in word[:ell]: counts[v] += 1
        signatures = {tuple(counts)}
        for end in range(ell, length):
            counts[word[end - ell]] -= 1
            counts[word[end]] += 1
            signatures.add(tuple(counts))
        ans.append(len(signatures))
    return ans

def main():
    word = []
    for n in range(1, 10):
        word = word + [n - 1] + word
        obs = spectrum(word, n)
        exp = [stern(2 ** n - ell) for ell in range(2 ** n)]
        assert obs == exp, (n, next((i for i in range(len(obs)) if obs[i] != exp[i]), None))
        assert sum(obs[1:]) == (3 ** n - 1) // 2
        assert max(obs[1:]) == fibonacci(n + 1)
        J = (2 ** n - (-1) ** n) // 3
        assert obs[J] == fibonacci(n + 1)
        print('rank', n, 'length', len(word), 'spectrum OK; total', sum(obs[1:]), 'max', max(obs[1:]))
    print('ALL CHECKS PASS')

if __name__ == '__main__': main()
