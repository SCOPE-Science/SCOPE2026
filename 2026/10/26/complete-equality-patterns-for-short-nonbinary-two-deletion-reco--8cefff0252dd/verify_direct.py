"""Independent direct-word verifier for short q-ary deletion intersections.

Run: python3 verify_direct.py
Enumerates labeled words, rather than canonical equality partitions.
"""
from collections import Counter
from itertools import combinations, product

EXPECTED = {
    3: (3, {3: 1}),
    4: (4, {2: 1, 3: 4, 4: 1}),
    5: (6, {3: 1}),
    6: (6, {2: 2, 3: 8, 4: 2}),
}


def falling(q, s):
    a = 1
    for i in range(s):
        a *= max(0, q - i)
    return a


def deletion_outputs(word, deleted):
    n = len(word)
    return frozenset(tuple(word[i] for i in range(n) if i not in omitted)
                     for omitted in (set(c) for c in combinations(range(n), deleted)))


def direct(q, n):
    words = list(product(range(q), repeat=n))
    one = [deletion_outputs(w, 1) for w in words]
    two = [deletion_outputs(w, 2) for w in words]
    highest = -1
    total = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if not one[i].isdisjoint(one[j]):
                continue
            k = len(two[i] & two[j])
            if k > highest:
                highest = k
                total = 0
            if k == highest:
                total += 1
    return highest, total


def main():
    trials = [(q, n) for q in (2, 3, 4) for n in (3, 4, 5, 6)]
    trials += [(5, n) for n in (3, 4, 5)]
    trials += [(6, n) for n in (3, 4)]
    for q, n in trials:
        expected_max, by_support = EXPECTED[n]
        present = sum(count * falling(q, s) for s, count in by_support.items())
        if present == 0:
            continue
        predicted = present // 2
        observed = direct(q, n)
        assert observed == (expected_max, predicted), (q, n, observed, predicted)
        print('q=', q, 'n=', n, 'max=', observed[0],
              'unordered_extremal_pairs=', observed[1])
    print('DIRECT_VERIFY_OK')


if __name__ == '__main__':
    main()
