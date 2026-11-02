#!/usr/bin/env python3
"""Check exact abelian-square factor spectra against literal enumeration.
No external dependencies. Run: python3 abelian_square_run_verifier.py.
"""
from itertools import product
from collections import Counter
from random import Random


def literal_spectrum(runs, copies):
    q = len(runs)
    word = ''.join(chr(65 + i) * size for i, size in enumerate(runs)) * copies
    n = len(word)
    prefix = [[0] * (n + 1) for _ in range(q)]
    for pos, c in enumerate(word, 1):
        for j in range(q):
            prefix[j][pos] = prefix[j][pos - 1]
        prefix[ord(c) - 65][pos] += 1
    spectrum = {}
    for half in range(1, n // 2 + 1):
        found = set()
        for start in range(n - 2 * half + 1):
            if all(prefix[j][start + half] - prefix[j][start] ==
                   prefix[j][start + 2 * half] - prefix[j][start + half]
                   for j in range(q)):
                found.add(word[start:start + 2 * half])
        spectrum[half] = len(found)
    return spectrum


def structural_spectrum(runs, copies):
    p = sum(runs)
    n = copies * p
    starts = []
    a = 0
    for size in runs:
        starts.append((a, a + size))
        a += size

    def monochrome(start, width):
        return any(lo <= start < hi and start + width <= hi
                   for lo, hi in starts)

    spectrum = {}
    for half in range(1, n // 2 + 1):
        if 2 * half < p:
            spectrum[half] = sum(size >= 2 * half for size in runs)
            continue
        limit = min(p - 1, n - 2 * half)
        residue = half % p
        if residue == 0:
            spectrum[half] = limit + 1
        elif 2 * residue <= p:
            spectrum[half] = sum(monochrome(s, 2 * residue)
                                 for s in range(limit + 1))
        else:
            delta = p - residue
            spectrum[half] = sum(monochrome((s - 2 * delta) % p, 2 * delta)
                                 for s in range(limit + 1))
    return spectrum


def closed_total(runs, copies):
    p = sum(runs)
    small = sum(x // 2 for x in runs)
    increment = p + 2 * sum(x * x // 4 for x in runs)
    if copies % 2:
        return small + (copies // 2) * increment
    return (small + ((copies - 2) // 2) * increment
            + 1 + runs[0] // 2 + runs[-1] // 2)


def check():
    cases = 0
    length_cases = 0
    distinct_sum = 0
    for q, cap, kmax in [(3, 4, 6), (4, 3, 5), (5, 2, 4)]:
        for runs in product(range(1, cap + 1), repeat=q):
            for k in range(1, kmax + 1):
                direct = literal_spectrum(runs, k)
                predicted = structural_spectrum(runs, k)
                assert direct == predicted, (runs, k, direct, predicted)
                assert sum(direct.values()) == closed_total(runs, k), (runs, k)
                cases += 1
                length_cases += len(direct)
                distinct_sum += sum(direct.values())
    rng = Random(20261026)
    for _ in range(80):
        q = rng.randint(3, 6)
        runs = tuple(rng.randint(1, 7) for _ in range(q))
        k = rng.randint(1, 6)
        direct = literal_spectrum(runs, k)
        predicted = structural_spectrum(runs, k)
        assert direct == predicted, (runs, k, direct, predicted)
        assert sum(direct.values()) == closed_total(runs, k), (runs, k)
        cases += 1
        length_cases += len(direct)
        distinct_sum += sum(direct.values())
    # Independently enumerate the circular adjacent-arc obstruction.
    cyclic_windows = 0
    for q, cap in [(3, 4), (4, 3)]:
        for runs in product(range(1, cap + 1), repeat=q):
            p = sum(runs)
            circular = ''.join(chr(65+i)*size for i,size in enumerate(runs))
            for width in range(1, (p // 2) + 1):
                for start in range(p):
                    first = ''.join(circular[(start+j)%p] for j in range(width))
                    second = ''.join(circular[(start+width+j)%p]
                                     for j in range(width))
                    joined = first + second
                    assert ((Counter(first) == Counter(second)) ==
                            (len(set(joined)) == 1)), (runs,width,start)
                    cyclic_windows += 1
    print('VERIFY_OK literal_cases=%d half_length_profiles=%d distinct_abelian_squares=%d circular_arc_tests=%d all_equal=TRUE' %
          (cases,length_cases,distinct_sum,cyclic_windows))

if __name__ == '__main__':
    check()
