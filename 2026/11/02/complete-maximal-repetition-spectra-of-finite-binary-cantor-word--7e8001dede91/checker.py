"""Independent finite checks for Cantor-word maximal-repetition spectra.

Run using Python 3: python checker.py
Uses no third-party packages and does not assume a numerical theorem to detect runs.
"""
from collections import Counter


def cantor(level):
    w = '1'
    for _ in range(level):
        w = ''.join('101' if x == '1' else '000' for x in w)
    return w


def least_period(w):
    pi = [0] * len(w)
    for i in range(1, len(w)):
        j = pi[i - 1]
        while j and w[i] != w[j]:
            j = pi[j - 1]
        if w[i] == w[j]:
            j += 1
        pi[i] = j
    return len(w) - pi[-1]


def independently_enumerate_runs(w):
    n = len(w)
    ans = set()
    for p in range(1, n // 2 + 1):
        i = 0
        while i + p < n:
            if w[i] != w[i + p]:
                i += 1
                continue
            left = i
            while i + p < n and w[i] == w[i + p]:
                i += 1
            right = i + p
            if right - left >= 2 * p and least_period(w[left:right]) == p:
                ans.add((left, right, p))
    return ans


def construct_runs(level):
    w = cantor(level)
    ans = set()
    # Every maximal zero block with length at least two.
    i = 0
    while i < len(w):
        if w[i] == '0':
            j = i + 1
            while j < len(w) and w[j] == '0':
                j += 1
            if j - i >= 2:
                ans.add((i, j, 1))
            i = j
        else:
            i += 1
    # All positive-symbol runs: lifts of a zero-padded '101' image block.
    for j in range(level - 1):
        ancestor = cantor(level - j - 1)
        scale = 3**j
        base_length = 3 ** (level - j)
        for t, symbol in enumerate(ancestor):
            if symbol == '1':
                a = max(0, 3*t - 1)
                b = min(base_length, 3*t + 4)
                ans.add((a*scale, b*scale, 2*scale))
    return ans


def expected_distribution(level):
    period_and_length = Counter()
    for e in range(1, level):
        period_and_length[(1, 3**e)] += 2 ** (level - e - 1)
    for j in range(level - 1):
        scale = 3**j
        period_and_length[(2*scale, 4*scale)] += 2
        period_and_length[(2*scale, 5*scale)] += 2 ** (level - j - 1) - 2
    return +period_and_length


def main():
    for k in range(1, 7):
        w = cantor(k)
        brute = independently_enumerate_runs(w)
        predicted = construct_runs(k)
        if brute != predicted:
            raise AssertionError((k, 'set mismatch', sorted(brute-predicted)[:10], sorted(predicted-brute)[:10]))
        histogram = Counter((p, b-a) for a,b,p in brute)
        assert histogram == expected_distribution(k), (k,histogram,expected_distribution(k))
        expected_n = 0 if k == 1 else 3*2**(k-1)-3
        expected_length = 0 if k == 1 else 4*3**k-13*2**(k-1)+1
        assert len(brute) == expected_n
        assert sum(b-a for a,b,p in brute) == expected_length
        print('k={} length={} runs={} total_run_length={} profiles={}'.format(k,len(w),len(brute),sum(b-a for a,b,p in brute),sorted(histogram.items())))
    print('PASS: independent enumeration equals all predicted run triples, period/length spectra, and totals at levels 1..6')

if __name__ == '__main__':
    main()
