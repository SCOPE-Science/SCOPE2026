#!/usr/bin/env python3
"""Exact rational certificate verifier for four-block Van der Laan rigidity."""
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import json


def vector(*terms):
    v = [0] * 8
    for index, scalar in terms:
        v[index] += scalar
    return v


def equations_and_inequalities(perm):
    # perm is a rank tuple of 1,2,3,4 in temporal order.
    p = [i - 1 for i in perm]
    equations = []
    for start in range(5):
        order = sorted(range(start, start + 4),
                       key=lambda index: (index // 4, p[index % 4]))
        equations.append(vector((order[-1], +1),
                                (order[0], -1), (order[1], -1)))
    inequalities = []
    for block in range(2):
        positions = [4 * block + p.index(rank) for rank in range(4)]
        for rank in range(3):
            inequalities.append(vector((positions[rank], +1),
                                        (positions[rank + 1], -1)))
    inequalities.append(vector((p.index(3), +1),
                               (4 + p.index(0), -1)))
    for index in range(8):
        inequalities.append(vector((index, -1)))
    assert len(equations) == 5 and len(inequalities) == 15
    return equations, inequalities


def verify_certificates():
    certificates = json.loads(Path(__file__).with_name('certificates.json').read_text('utf-8'))
    expected = {p for p in permutations((1, 2, 3, 4)) if p != (1, 2, 3, 4)}
    assert {tuple(c['perm']) for c in certificates} == expected
    assert len(certificates) == 23
    for cert in certificates:
        equations, inequalities = equations_and_inequalities(cert['perm'])
        reconstruction = [Fraction(0)] * 8
        assert len({int(i) for i, _ in cert['ineq']}) == len(cert['ineq'])
        assert len({int(i) for i, _ in cert['eq']}) == len(cert['eq'])
        for index, weight in cert['ineq']:
            index, weight = int(index), Fraction(weight)
            assert 0 <= index < 15 and weight >= 0
            for coordinate in range(8):
                reconstruction[coordinate] += weight * inequalities[index][coordinate]
        for index, weight in cert['eq']:
            index, weight = int(index), Fraction(weight)
            assert 0 <= index < 5
            for coordinate in range(8):
                reconstruction[coordinate] += weight * equations[index][coordinate]
        assert reconstruction == [1, 1, 1, 1, 0, 0, 0, 0], (cert['perm'], reconstruction)
    return len(certificates)


def verify_identity_examples():
    # First three values generate a globally nondecreasing Padovan-type solution.
    count = 0
    for a in range(5):
        for b in range(a, 6):
            for c in range(b, a + b + 1):
                seq = [a, b, c]
                for _ in range(97):
                    seq.append(seq[-2] + seq[-3])
                assert all(x <= y for x, y in zip(seq, seq[1:]))
                assert all(max(seq[i:i + 4]) == sum(sorted(seq[i:i + 4])[:2])
                           for i in range(len(seq) - 3))
                count += 1
    assert count > 0
    return count


if __name__ == '__main__':
    n = verify_certificates()
    examples = verify_identity_examples()
    print(f'EXACT_CERTIFICATES_OK={n}; INDEPENDENT_CONSTRUCTIONS_OK={examples}')
