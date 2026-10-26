#!/usr/bin/env python3
"""Reproduce exact two-deletion circular trace counts by independent encodings.
No external dependencies.  All deletion pairs are enumerated, no sampling.
"""
from itertools import combinations


def minimal_rotation(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def run_signature(word):
    n = len(word)
    edges = [i for i in range(n) if word[i] != word[i-1]]
    if not edges:
        return ((word[0], n),)
    runs = []
    for index, start in enumerate(edges):
        nxt = edges[(index + 1) % len(edges)]
        runs.append((word[start], (nxt - start) % n))
    return min(tuple(runs[i:] + runs[:i]) for i in range(len(runs)))


def profile(a, k, rotate=0):
    w = '0'*a + '10'*(k-1) + '1'
    w = w[rotate:] + w[:rotate]
    text = [set(), set(), set()]
    signatures = [set(), set(), set()]
    count = 0
    for i, j in combinations(range(len(w)), 2):
        v = w[:i] + w[i+1:j] + w[j+1:]
        t = (w[i] == '1') + (w[j] == '1')
        text[t].add(minimal_rotation(v))
        signatures[t].add(run_signature(v))
        count += 1
    assert tuple(map(len,text)) == tuple(map(len,signatures))
    # Strong check: no two distinct words share a run-signature.
    for p in range(3):
        bijection = {run_signature(v): v for v in text[p]}
        assert len(bijection) == len(text[p])
        assert set(bijection) == signatures[p]
    assert count == len(w)*(len(w)-1)//2
    return tuple(map(len, text))


def expected(a, k):
    # The three entries index the number of deleted ones (0,1,2).
    q0 = 1 + k*(k-1)//2
    q1 = 1 + (k-2)**2 + (k-2 if a >= 4 else (k-1)//2)
    q2 = (k-1)*(k-2)//2 - (0 if a >= 4 else (k-3)//2)
    return (q0, q1, q2)


def main():
    cases = 0
    for a in range(3, 9):
        for k in range(3, 23):
            observed = profile(a, k)
            predicted = expected(a, k)
            assert observed == predicted, (a, k, observed, predicted)
            total = sum(observed)
            target = (2*k*k - 6*k + 8) if a == 3 else (2*k*k - 5*k + 5)
            assert total == target
            # Rotating the source cannot change circular-output support.
            if k <= 9:
                assert profile(a,k,rotate=(a+k)%len('0'*a+'10'*(k-1)+'1')) == observed
            cases += 1
    print('CIRCULAR_TWO_DELETION_PASS cases=%d a=3..8 k=3..22 independent=word-rotations,run-cycles source_rotations=checked' % cases)
    for k in range(3, 9):
        print('k=%d a=3:%s a=4:%s' % (k, profile(3,k), profile(4,k)))


if __name__ == '__main__':
    main()
