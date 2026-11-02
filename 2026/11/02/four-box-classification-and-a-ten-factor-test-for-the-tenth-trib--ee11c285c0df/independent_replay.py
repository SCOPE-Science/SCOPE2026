#!/usr/bin/env python3
"""Independent factor-ID exhaustive check of Tribonacci attractors."""
from itertools import combinations, product

M = {'0': '01', '1': '02', '2': '0'}
A = (80, 82, 93, 95)
B = (148, 152, 172, 176)
C = (229, 231, 242, 244)
D = (273, 274, 280, 281, 317, 318, 324, 325)
E = (354, 356, 367, 369)
F = (422, 426, 446, 450)
EXPECTED = set().union(*(set(product(*block)) for block in
    ((A, B, D), (B, C, D), (B, D, E), ((229,), D, F))))


def word_at(stage):
    x = '0'
    for _ in range(stage):
        x = ''.join(M[ch] for ch in x)
    return x


def attractors(x):
    # Assign each distinct factor an integer ID independently of support sets.
    ids = {}
    for a in range(len(x)):
        for b in range(a + 1, len(x) + 1):
            factor = x[a:b]
            if factor not in ids:
                ids[factor] = len(ids)
    covered = [0] * len(x)
    for a in range(len(x)):
        for b in range(a + 1, len(x) + 1):
            bit = 1 << ids[x[a:b]]
            for i in range(a, b):
                covered[i] |= bit
    target = (1 << len(ids)) - 1
    answer = set()
    for i, j, k in combinations(range(len(x)), 3):
        if (covered[i] | covered[j] | covered[k]) == target:
            answer.add((i, j, k))
    return answer, len(ids)


def main():
    earlier, earlier_factors = attractors(word_at(9))
    assert len(earlier) == 224
    found, distinct = attractors(word_at(10))
    assert (len(found), distinct) == (416, 80559)
    assert found == EXPECTED
    print('previous_stage_length:', len(word_at(9)))
    print('previous_stage_attractors:', len(earlier))
    print('stage_ten_length:', len(word_at(10)))
    print('stage_ten_distinct_factors:', distinct)
    print('stage_ten_attractors:', len(found))
    print('box_set_equality: true')
    print('PASS')

if __name__ == '__main__':
    main()
