#!/usr/bin/env python3
"""Reproduce exact finite certificates for sparse synchronization codes.

Run next to certificates.json with Python 3.9+; standard library only.
No integer-programming package is needed to check either optimality bound.
"""
import itertools
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def word_list(n, weight):
    for pos in itertools.combinations(range(n), weight):
        s = ['0'] * n
        for i in pos:
            s[i] = '1'
        yield ''.join(s)


def rotations(s):
    return {s[k:] + s[:k] for k in range(len(s))}


def compatible(s, t):
    n = len(s)
    assert n == len(t)
    return all(s[:k] != t[-k:] and t[:k] != s[-k:]
               for k in range(1, n))


def is_code(code, n, weight):
    if len(code) != len(set(code)):
        return False
    if not all(len(s) == n and s.count('1') == weight and
               set(s) <= {'0', '1'} and compatible(s, s)
               for s in code):
        return False
    return all(compatible(s, t) for s, t in itertools.combinations(code, 2))


def primitive_necklaces(n, weight):
    classes = defaultdict(set)
    for s in word_list(n, weight):
        rot = rotations(s)
        if len(rot) == n:
            classes[min(rot)].add(s)
    assert all(len(v) == n for v in classes.values())
    return classes


def admissible_rotations(s):
    return sorted(t for t in rotations(s) if compatible(t, t))


def count_compatible_choices(domains):
    good = 0
    for choices in itertools.product(*domains):
        if all(compatible(a, b) for a, b in itertools.combinations(choices, 2)):
            good += 1
    return good


def main():
    data = json.loads((HERE / 'certificates.json').read_text(encoding='utf-8'))
    assert data['weight'] == 4
    expected = {4: 0, 5: 1, 6: 2, 7: 5, 8: 8,
                9: 14, 10: 20, 11: 30, 12: 39}
    upper = {4: 0, 5: 1, 6: 2, 7: 5, 8: 8,
             9: 14, 10: 20, 11: 30, 12: 40}
    for n in range(4, 13):
        code = data['maxima'][str(n)]
        assert len(code) == expected[n], (n, len(code))
        assert is_code(code, n, 4), ('invalid code', n)
        classes = primitive_necklaces(n, 4)
        assert len(classes) == upper[n], ('necklaces', n, len(classes))
        assert len({min(rotations(s)) for s in code}) == len(code)
        if n < 12:
            # Every codeword is primitive and at most one per rotation class.
            assert expected[n] == upper[n]
        else:
            assert len(classes) == 40
            assert len(code) == 39
            assert all(s in classes for s in data['six_necklace_obstruction'])
    six = data['six_necklace_obstruction']
    assert len(six) == len(set(six)) == 6
    domains = [admissible_rotations(s) for s in six]
    assert list(map(len, domains)) == [3, 4, 4, 3, 3, 3]
    # 3*4*4*3*3*3 = 1296 independent exact transversal trials.
    tested = 1
    for domain in domains:
        tested *= len(domain)
    assert tested == 1296
    assert count_compatible_choices(domains) == 0
    five_counts = [count_compatible_choices(domains[:i] + domains[i+1:])
                   for i in range(6)]
    assert five_counts == [3, 2, 2, 3, 3, 3], five_counts
    print('VERIFY_OK')
    print('weight-4 optimum sizes, lengths 4..12:',
          [expected[n] for n in range(4, 13)])
    print('primitive-necklace upper bounds, lengths 4..12:',
          [upper[n] for n in range(4, 13)])
    print('length-12 six-necklace obstruction: 1296 choices, zero feasible')
    print('five-of-six feasible-transversal counts:', five_counts)


if __name__ == '__main__':
    main()
