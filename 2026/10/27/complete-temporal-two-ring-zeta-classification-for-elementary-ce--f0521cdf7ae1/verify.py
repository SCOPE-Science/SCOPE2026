#!/usr/bin/env python3
"""Exact, dependency-free certificate for ECA temporal-two ring data.

Run in a directory with eca2_rules.csv and eca2_classes.csv.
The matrices and Newton identities are implemented over the integers.
"""
import ast
import csv
from fractions import Fraction
from collections import Counter


def bit(rule, left, middle, right):
    return (rule >> ((left << 2) | (middle << 1) | right)) & 1


def graph(rule, depth):
    """De Bruijn matrix of the fixed points of the depth-th iterate."""
    width = 2 * depth
    size = 1 << width
    M = [[0] * size for _ in range(size)]
    for v in range(size):
        u = [(v >> (width - 1 - j)) & 1 for j in range(width)]
        for nxt in (0, 1):
            word = u + [nxt]
            if depth == 1:
                output = bit(rule, *word)
            else:
                lower = [bit(rule, *word[i:i+3]) for i in range(3)]
                output = bit(rule, *lower)
            if output == word[depth]:
                w = ((v << 1) & (size - 1)) | nxt
                M[v][w] += 1
    return M


def multiply(A, B):
    n = len(A)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for k, ai in enumerate(A[i]):
            if ai:
                for j, bkj in enumerate(B[k]):
                    if bkj:
                        ans[i][j] += ai * bkj
    return ans


def characteristic_zeta_denominator(M):
    """Coefficients of det(I-zM), via exact Newton identities."""
    n = len(M)
    power = [row[:] for row in M]
    trace = []
    for j in range(1, n + 1):
        trace.append(sum(power[k][k] for k in range(n)))
        if j < n:
            power = multiply(power, M)
    coefficients = [1]
    for k in range(1, n + 1):
        numerator = -sum(coefficients[k-j] * trace[j-1]
                         for j in range(1, k+1))
        assert numerator % k == 0, (n, k, numerator)
        coefficients.append(numerator // k)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients


def evolve_once(rule, word):
    n = len(word)
    return tuple(bit(rule, word[(i-1) % n], word[i], word[(i+1) % n])
                 for i in range(n))


def direct_counts(rule, n):
    c1 = c2 = 0
    for number in range(1 << n):
        word = tuple((number >> i) & 1 for i in range(n))
        after = evolve_once(rule, word)
        if after == word:
            c1 += 1
        if evolve_once(rule, after) == word:
            c2 += 1
    return c1, c2


def traces(M, limit):
    power = [row[:] for row in M]
    output = []
    for j in range(limit):
        output.append(sum(power[i][i] for i in range(len(M))))
        if j + 1 < limit:
            power = multiply(power, M)
    return output



def polynomial_division(A, B):
    """Exact Q[z] division, ascending coefficient convention."""
    a = [Fraction(x) for x in A]
    b = [Fraction(x) for x in B]
    assert b and b[-1]
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        shift = len(a) - len(b)
        factor = a[-1] / b[-1]
        q[shift] = factor
        for i, coeff in enumerate(b):
            a[shift+i] -= factor * coeff
        while a and a[-1] == 0:
            a.pop()
    return q, a


def canonical_ratio(D, E):
    a, b = [Fraction(x) for x in D], [Fraction(x) for x in E]
    while b:
        _, remainder = polynomial_division(a, b)
        a, b = b, remainder
    gcd_poly = [u / a[0] for u in a]
    numerator, r = polynomial_division(D, gcd_poly)
    assert not r
    denominator, r = polynomial_division(E, gcd_poly)
    assert not r
    assert numerator[0] == denominator[0] == 1
    assert all(x.denominator == 1 for x in numerator + denominator)
    return tuple(int(x) for x in numerator), tuple(int(x) for x in denominator)


def main():
    with open('eca2_rules.csv', encoding='utf-8', newline='') as fh:
        rows = list(csv.DictReader(fh))
    with open('eca2_classes.csv', encoding='utf-8', newline='') as fh:
        classes = list(csv.DictReader(fh))
    assert len(rows) == 256
    assert sorted(int(row['rule']) for row in rows) == list(range(256))
    assert len(classes) == 51
    with open('eca2_ratio_classes.csv', encoding='utf-8', newline='') as fh:
        ratios = list(csv.DictReader(fh))
    assert len(ratios) == 25
    expected_ratios = {(tuple(ast.literal_eval(x['numerator_coefficients'])),
                        tuple(ast.literal_eval(x['denominator_coefficients']))): int(x['ratio_class_id'])
                       for x in ratios}
    assert len(expected_ratios) == 25
    known = {(tuple(ast.literal_eval(x['fixed_denominator_coefficients'])),
              tuple(ast.literal_eval(x['second_fixed_denominator_coefficients']))): int(x['class_id'])
             for x in classes}
    assert len(known) == 51
    pairs = set()
    second = set()
    exact2_ratios = set()
    witnesses = Counter()
    for row in rows:
        r = int(row['rule'])
        M1 = graph(r, 1)
        M2 = graph(r, 2)
        D = tuple(characteristic_zeta_denominator(M1))
        E = tuple(characteristic_zeta_denominator(M2))
        assert list(D) == ast.literal_eval(row['fixed_denominator_coefficients'])
        assert list(E) == ast.literal_eval(row['second_fixed_denominator_coefficients'])
        assert known[(D, E)] == int(row['class_id'])
        ratio = canonical_ratio(D, E)
        assert expected_ratios[ratio] == int(row['ratio_class_id'])
        exact2_ratios.add(ratio)
        pairs.add((D, E))
        second.add(E)
        t1 = traces(M1, 8)
        t2 = traces(M2, 8)
        for n in range(1, 9):
            assert (t1[n-1], t2[n-1]) == direct_counts(r, n), (r,n)
            assert t2[n-1] >= t1[n-1]
            assert (t2[n-1] - t1[n-1]) % 2 == 0
        first = next((n for n in range(1, 7) if t2[n-1] > t1[n-1]), None)
        if first is None:
            assert D == E, ('unseen long-cycle candidate', r)
        else:
            assert D != E
        claimed = int(row['first_two_cycle_ring']) if row['first_two_cycle_ring'] else None
        assert claimed == first
        witnesses[first] += 1
    assert len(pairs) == 51
    assert len(second) == 40
    assert len(exact2_ratios) == 25
    assert witnesses == {None:107, 1:64, 2:48, 3:6, 4:17, 5:2, 6:12}, witnesses
    for data in ratios:
        rules = ast.literal_eval(data['rules'])
        assert len(rules) == int(data['multiplicity'])
        for r in rules:
            assert int(rows[r]['ratio_class_id']) == int(data['ratio_class_id'])
    for data in classes:
        rlist = ast.literal_eval(data['rules'])
        assert len(rlist) == int(data['multiplicity'])
        for r in rlist:
            assert known[(tuple(ast.literal_eval(rows[r]['fixed_denominator_coefficients'])),
                          tuple(ast.literal_eval(rows[r]['second_fixed_denominator_coefficients'])))] == int(data['class_id'])
    print('VERIFY_OK rules=256 pair_types=51 second_fixed_zeta_types=40 exact_two_zeta_types=25 temporally_two_rules=149 max_witness_ring=6')


if __name__ == '__main__':
    main()
