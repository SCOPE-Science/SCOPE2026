#!/usr/bin/env python3
"""Independent finite checks for the one-step Černý reset-word spectrum.

Uses exact integer counts in the subset automaton and direct letter-by-letter
word actions. Finite computations support but do not establish the theorem.
"""
from collections import defaultdict, deque


def transitions(n):
    full = (1 << n) - 1
    result = {}
    for s in range(1, full + 1):
        a = ((s << 1) & full) | (s >> (n - 1))
        b = (s & ~(1 << (n - 1))) | (1 if s & (1 << (n - 1)) else 0)
        result[s] = (a, b)
    return result


def short_and_next(n):
    edges = transitions(n)
    full = (1 << n) - 1
    length = (n - 1)**2
    dp = {full: 1}
    shortest = None
    targets = None
    for t in range(length + 2):
        if t == length:
            shortest = sum(dp.get(1 << i, 0) for i in range(n))
        if t == length + 1:
            targets = [dp.get(1 << i, 0) for i in range(n)]
            break
        following = defaultdict(int)
        for subset, count in dp.items():
            for dest in edges[subset]:
                following[dest] += count
        dp = following
    return shortest, targets


def predicted(n):
    base = 'b' + ('a'*(n-1) + 'b')*(n-2)
    candidates = {'a' + base, base + 'a'}
    for index, letter in enumerate(base):
        if letter == 'b':
            candidates.add(base[:index] + 'b' + base[index:])
    block_start = 1
    for j in range(1, n-1):
        for i in range(1, n-1):
            if i != j:
                pos = block_start + i
                candidates.add(base[:pos] + 'b' + base[pos:])
        block_start += n
    assert block_start == 1 + n*(n-2)
    return candidates


def act(n, word):
    subset = (1 << n)-1
    edges = transitions(n)
    for letter in word:
        subset = edges[subset][letter == 'b']
    return subset


def enumerate_actual(n):
    edges = transitions(n)
    full = (1 << n)-1
    reverse = {s: [] for s in edges}
    for src, destinations in edges.items():
        for dst in destinations:
            reverse[dst].append(src)
    distances = {1 << i: 0 for i in range(n)}
    pending = deque(distances)
    while pending:
        subset = pending.popleft()
        for pre in reverse[subset]:
            if pre not in distances:
                distances[pre] = distances[subset]+1
                pending.append(pre)
    depth = (n-1)**2 + 1
    actual = set()

    def walk(subset, prefix, remaining):
        if remaining == 0:
            if subset.bit_count() == 1:
                actual.add(prefix)
            return
        for letter, out in zip('ab', edges[subset]):
            if distances.get(out, depth+1) <= remaining-1:
                walk(out, prefix+letter, remaining-1)
    walk(full, '', depth)
    return actual


def main():
    target_checks=0
    for n in range(2,14):
        expected = predicted(n)
        assert len(expected) == (n-2)**2+3
        assert all(len(w) == (n-1)**2+1 for w in expected)
        assert all(act(n,w).bit_count() == 1 for w in expected)
        shortest, targets = short_and_next(n)
        assert shortest == 1, (n,shortest)
        assert targets == [len(expected)-1,1]+[0]*(n-2), (n,targets)
        if n <= 8:
            actual = enumerate_actual(n)
            assert actual == expected, (n,actual ^ expected)
        target_checks += len(expected)
        print(f'n={n} shortest={shortest} next={sum(targets)} terminal0={targets[0]} terminal1={targets[1]}')
    print(f'VERIFY_OK n=2..13 exhaustive_reset_languages_n=2..8 checked_explicit_words={target_checks}')


if __name__ == '__main__':
    main()
