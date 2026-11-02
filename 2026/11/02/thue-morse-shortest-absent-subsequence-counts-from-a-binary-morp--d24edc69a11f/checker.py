#!/usr/bin/env python3
"""Self-contained verification of shortest-absent-subsequence transfer counts.

Run: python3 checker.py
"""
from itertools import product
from math import log, exp


def morphism(word):
    return ''.join('01' if symbol == '0' else '10' for symbol in word)


def distinct_including_empty(word):
    # Independent ordinary distinct-subsequence recurrence.
    total = 1
    last = {}
    for symbol in word:
        previous_total = total
        total = 2 * total - last.get(symbol, 0)
        last[symbol] = previous_total
    return total


def direct_absent_count(word, length):
    # Count target words absent as subsequences, by the literal greedy matcher.
    n = len(word)
    nxt = [[n + 1, n + 1] for _ in range(n + 1)]
    for pos in range(n - 1, -1, -1):
        nxt[pos] = nxt[pos + 1].copy()
        nxt[pos][int(word[pos])] = pos + 1
    counts = [0] * (n + 2)
    counts[0] = 1
    for _ in range(length):
        updated = [0] * (n + 2)
        for pos, multiplicity in enumerate(counts):
            if multiplicity:
                if pos == n + 1:
                    updated[n + 1] += 2 * multiplicity
                else:
                    updated[nxt[pos][0]] += multiplicity
                    updated[nxt[pos][1]] += multiplicity
        counts = updated
    return counts[n + 1]


def combinatorial_count(v):
    a, b = 1, 1
    for bit in v:
        if bit == '0':
            a += b
        else:
            b += a
    return a + b


def direct_avoidance_count(v):
    m = len(v)
    return sum(1 for x in product('01', repeat=m + 1)
               if all(''.join(x[i:i + 2]) != ('01' if v[i] == '0' else '10')
                      for i in range(m)))


def matmul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def matword(word):
    out = ((1, 0), (0, 1))
    for bit in word:
        out = matmul(((1, 1), (0, 1)) if bit == '0' else ((1, 0), (1, 1)), out)
    return out


def verify():
    tested = 0
    for m in range(1, 9):
        for bits in product('01', repeat=m):
            v = ''.join(bits)
            predicted = combinatorial_count(v)
            assert predicted == distinct_including_empty(v) + 1
            assert predicted == direct_absent_count(morphism(v), m + 1)
            assert predicted == direct_avoidance_count(v)
            assert direct_absent_count(morphism(v), m) == 0
            tested += 1
    print('All binary sources of lengths 1..8:', tested, 'passed four independent checks')

    tm = '0'
    a, t, tn = 2, 1, 1
    transfer = ((1, 1), (0, 1))
    for k in range(0, 9):
        B = matword(tm)
        assert transfer == B
        assert a == B[0][0] + B[1][1]
        assert t == B[0][1] + B[1][0]
        predicted = a + t
        assert predicted == distinct_including_empty(tm) + 1
        assert predicted == direct_absent_count(morphism(tm), len(tm) + 1)
        assert direct_absent_count(morphism(tm), len(tm)) == 0
        print('k', k, 'Thue-Morse length', len(tm), 'SAS', predicted)
        a, t = t*t + 2, a*t
        transfer = matmul(((0, 1), (1, 0)), B)
        transfer = matmul(transfer, transfer)
        tm = morphism(tm)

    values = [1, 2]
    for _ in range(8):
        values.append(values[-1]*(values[-2]*values[-2]+2))
    constant = log(2)/3 + sum(2**(-j-1)*log1p_two_square(x)/3
                              for j, x in enumerate(values))
    print('Growth base approximation:', exp(constant))


def log1p_two_square(x):
    from math import log1p
    return log1p(2/(x*x))


if __name__ == '__main__':
    verify()
