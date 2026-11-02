#!/usr/bin/env python3
"""Standalone finite verifier for the three-level S5-confluence census.

No external packages or files are required. The symbolic proof is in RESULT.md;
finite checking is corroborative, not a replacement for it.
"""
from itertools import combinations
from math import comb


def partitions(n):
    """All set partitions of range(n), once each, via insertion recursion."""
    if n == 0:
        yield ()
        return
    for part in partitions(n - 1):
        for i in range(len(part)):
            next_part = list(part)
            next_part[i] = part[i] + (n - 1,)
            yield tuple(next_part)
        yield part + ((n - 1,),)


def bell(n):
    counts = [1]
    for m in range(n):
        counts.append(sum(comb(m, k) * counts[k] for k in range(m + 1)))
    return counts[n]


def valid_by_witnesses(a, b, c, parts):
    """Tests source's two quantified confluences literally, for every triple."""
    levels = (0,) * a + (1,) * b + (2,) * c
    n = len(levels)
    block_number = [None] * n
    for idx, part in enumerate(parts):
        for point in part:
            block_number[point] = idx
    for x in range(n):
        for y in range(n):
            if x != y and levels[x] >= levels[y]:
                continue
            for z in range(n):
                if block_number[y] == block_number[z]:
                    if not any(block_number[x] == block_number[w]
                               and (w == z or levels[w] < levels[z])
                               for w in range(n)):
                        return False
                if block_number[x] == block_number[z]:
                    if not any(block_number[y] == block_number[w]
                               and (z == w or levels[z] < levels[w])
                               for w in range(n)):
                        return False
    return True


def structural_type(a, b, c, parts):
    """Checks a different, exact combinatorial partition classification."""
    A = set(range(a))
    B = set(range(a, a + b))
    C = set(range(a + b, a + b + c))
    blocks = [set(p) for p in parts]
    if len(blocks) == 1:
        return 'universal'
    if all((s <= A or s <= B or s <= C) for s in blocks):
        return 'levelwise'
    if any(s == A | B for s in blocks) and all(s == A | B or s <= C for s in blocks):
        return 'lower_merged'
    if any(s == B | C for s in blocks) and all(s == B | C or s <= A for s in blocks):
        return 'upper_merged'
    if len(blocks) == 2:
        for s in blocks:
            if A <= s and s != A and s < A | B and s <= A | B:
                other = (A | B | C) - s
                if C <= other and other <= B | C and other != C:
                    return 'split'
    return None


def predicted(a, b, c):
    return bell(a) * bell(b) * bell(c) + bell(a) + bell(c) + (1 << b) - 1


def main():
    cases = 0
    examined = 0
    accepted = 0
    for n in range(3, 9):
        ps = tuple(partitions(n))
        assert len(ps) == bell(n)
        for a in range(1, n - 1):
            for b in range(1, n - a):
                c = n - a - b
                tally = dict(levelwise=0, lower_merged=0,
                             upper_merged=0, split=0, universal=0)
                for part in ps:
                    witness_result = valid_by_witnesses(a, b, c, part)
                    structure = structural_type(a, b, c, part)
                    assert witness_result == (structure is not None), (a, b, c, part, structure)
                    if witness_result:
                        tally[structure] += 1
                expected_types = {
                    'levelwise': bell(a) * bell(b) * bell(c),
                    'lower_merged': bell(c),
                    'upper_merged': bell(a),
                    'split': (1 << b) - 2,
                    'universal': 1,
                }
                assert tally == expected_types, (a, b, c, tally, expected_types)
                assert sum(tally.values()) == predicted(a, b, c)
                cases += 1
                examined += len(ps)
                accepted += sum(tally.values())
    print('CASES', cases)
    print('TOTAL_LABELLED_EQUIVALENCES_EXAMINED', examined)
    print('TOTAL_VALID', accepted)
    for a, b, c in [(1, 1, 1), (1, 2, 1), (2, 2, 2), (2, 3, 2), (3, 3, 3)]:
        print('FORMULA', a, b, c, predicted(a, b, c))
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
