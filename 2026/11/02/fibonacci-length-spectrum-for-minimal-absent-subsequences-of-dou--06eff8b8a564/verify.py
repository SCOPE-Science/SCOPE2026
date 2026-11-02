#!/usr/bin/env python3
"""Exact finite checks for minimal absent subsequences of binary doubled runs."""
from collections import Counter
from itertools import product


def word(r):
    return ''.join(str(i % 2) * 2 for i in range(r))


def is_subseq(candidate, source):
    pos = 0
    for letter in candidate:
        found = source.find(letter, pos)
        if found == -1:
            return False
        pos = found + 1
    return True


def greedy_cost(candidate):
    if not candidate:
        return 0
    runs = []
    for letter in candidate:
        if runs and runs[-1][0] == letter:
            runs[-1][1] += 1
        else:
            runs.append([letter, 1])
    return len(candidate) - sum(length % 2 == 0 for _, length in runs) + (candidate[0] == '1')


def direct_minimal(candidate, source):
    return (not is_subseq(candidate, source)
            and all(is_subseq(candidate[:i] + candidate[i+1:], source)
                    for i in range(len(candidate))))


def structural_minimal(candidate, r):
    if not candidate:
        return False
    runs = []
    for letter in candidate:
        if runs and runs[-1][0] == letter:
            runs[-1][1] += 1
        else:
            runs.append([letter, 1])
    if any(length % 2 == 0 for _, length in runs):
        return False
    if candidate[0] == '0' and runs[0][1] == 1:
        return False
    phi = greedy_cost(candidate)
    return phi == r+1 or (phi == r+2 and runs[-1][1] >= 3)


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def expected(r):
    return ({r: fibonacci(r), r+1: 2*fibonacci(r-1), r+2: fibonacci(r-2)}
            if r >= 2 else {1:1, 2:0, 3:1})


def allbinary(length):
    for bits in product('01', repeat=length):
        yield ''.join(bits)


def main():
    inspected = 0
    for r in range(1, 9):
        source = word(r)
        counts = Counter()
        # Every MAS has length at most |source|+1, by minimality.
        for length in range(1, 2*r+2):
            for candidate in allbinary(length):
                real = direct_minimal(candidate, source)
                structural = structural_minimal(candidate, r)
                assert real == structural, (r, candidate, real, structural)
                if real:
                    counts[length] += 1
                inspected += 1
        assert dict(counts) == {k:v for k,v in expected(r).items() if v}, (r, counts)
        assert sum(counts.values()) == fibonacci(r+2)
        print(f'r={r:2d} |source|={2*r:2d}  MAS_lengths={dict(sorted(counts.items()))}  total={sum(counts.values())}')
    for r in range(1, 13):
        source = word(r)
        # Independent direct embedding decisions for bounded candidate lengths.
        for length in range(0, min(2*r+1, 12)+1):
            for candidate in allbinary(length):
                assert is_subseq(candidate, source) == (greedy_cost(candidate) <= r), (r, candidate)
                inspected += 1
    print(f'PASS: {inspected:,} exact word-level comparisons; all Fibonacci identities and all three length layers verified')

if __name__ == '__main__':
    main()
