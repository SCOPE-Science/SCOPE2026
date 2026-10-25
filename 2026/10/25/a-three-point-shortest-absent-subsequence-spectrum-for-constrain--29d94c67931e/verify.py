"""Exhaustive reproducibility checker for a cyclic binary scattered-subsequence theorem.
Uses both a direct subset enumerator and a next-occurrence dynamic program.
No external packages or input files are required.
"""
from collections import Counter
from itertools import product


def occurs(pattern, word):
    position = 0
    for letter in pattern:
        while position < len(word) and word[position] != letter:
            position += 1
        if position == len(word):
            return False
        position += 1
    return True


def shortest_absent_dp(word):
    n = len(word)
    nxt = [[n, n] for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        nxt[i] = nxt[i + 1].copy()
        nxt[i][int(word[i])] = i
    distance = [0] * (n + 1)
    count = [0] * (n + 1)
    for i in range(n, -1, -1):
        choices = [1 if j == n else 1 + distance[j + 1] for j in nxt[i]]
        distance[i] = min(choices)
        count[i] = sum((1 if j == n else count[j + 1])
                       for j, length in zip(nxt[i], choices) if length == distance[i])
    return distance[0], count[0]


def all_shortest_absent(word, length):
    return {''.join(v) for v in product('01', repeat=length)
            if not occurs(''.join(v), word)}


def run():
    tested_sequences = 0
    tested_rotations = 0
    for r in range(2, 9):
        subtotal = 0
        for gaps in product((1, 2), repeat=r):
            if any(gaps[i] == gaps[(i + 1) % r] == 1 for i in range(r)):
                continue
            d, s = gaps.count(2), gaps.count(1)
            word = ''.join('1' + '0' * g for g in gaps)
            observed = Counter()
            for cut in range(len(word)):
                rotation = word[cut:] + word[:cut]
                length, number = shortest_absent_dp(rotation)
                assert length == r + 1, (r, gaps, cut, length)
                missing = all_shortest_absent(rotation, r + 1)
                assert number == len(missing), (r, gaps, cut, number, missing)
                possible = {'1' * (r+1), '0' + '1' * r, '1' * r + '0',
                            '00' + '1' * (r-1), '1' * (r-1) + '00'}
                assert missing <= possible, (r, gaps, cut, missing - possible)
                observed[number] += 1
                tested_rotations += 1
            assert observed == Counter({1:d, 2:2*d, 3:2*s}), (r, gaps, observed)
            tested_sequences += 1
            subtotal += 1
        print('ones', r, 'verified labeled gap-tuples', subtotal)
    assert sorted({shortest_absent_dp(('1010100')[j:]+('1010100')[:j])[1]
                   for j in range(7)}) == [1,2,3,4]
    print('PASS', 'tuples=', tested_sequences, 'marked_rotations=', tested_rotations)


if __name__ == '__main__':
    run()
