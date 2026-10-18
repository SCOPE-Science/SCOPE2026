"""Independent exact checks of dyadic Thue--Morse shortest-absent-subsequence counts.

Uses (i) a direct greedy membership test for all query words at small
lengths, and (ii) standard distinct-subsequence dynamic programming.
The recurrence tested here is stated explicitly and separately below.
"""
from itertools import product


def word(m):
    return [i.bit_count() & 1 for i in range(1 << m)]


def recurrence(max_m):
    s, t = 1, 2
    out = {}
    for m in range(1, max_m + 1):
        out[m] = t + s
        s, t = s * t, s * s + 2
    return out


def contains_subsequence(w, v):
    j = 0
    for x in w:
        if j < len(v) and x == v[j]:
            j += 1
    return j == len(v)


def brute(m):
    w = word(m)
    k = 1 << (m - 1)
    return sum(not contains_subsequence(w, v)
               for v in product((0, 1), repeat=k + 1))


def dp_count(m):
    # Count distinct subsequences of all lengths through k, by updating
    # the last-occurrence correction for each letter.
    w = word(m)
    k = (1 << (m - 1)) + 1
    d = [0] * (k + 1)
    d[0] = 1
    prev0 = [0] * (k + 1)
    prev1 = [0] * (k + 1)
    for bit in w:
        last = prev0 if bit == 0 else prev1
        old = d[:]
        for j in range(1, k + 1):
            d[j] += old[j - 1] - last[j]
            last[j] = old[j - 1]
    return (1 << k) - d[k]



def direct_matrix_count(m):
    # Multiply explicit 2x2 transition matrices in source order.
    a, b, c, d = 1, 0, 0, 1
    for bit in word(m - 1):
        if bit == 0:  # forbid 01
            a, b, c, d = a + b, b, c + d, d
        else:  # forbid 10
            a, b, c, d = a, a + b, c, c + d
    return a + b + c + d


def main():
    predicted = recurrence(9)
    for m in range(1, 10):
        actual = direct_matrix_count(m)
        assert actual == predicted[m], (m, actual, predicted[m])
        print('matrix', m, actual)
    for m in range(1, 6):
        actual = brute(m)
        assert actual == predicted[m], (m, actual, predicted[m])
        print('brute', m, actual)
    for m in range(1, 10):
        actual = dp_count(m)
        assert actual == predicted[m], (m, actual, predicted[m])
        print('distinct-DP', m, actual)
    print('ALL CHECKS PASS')


if __name__ == '__main__':
    main()
