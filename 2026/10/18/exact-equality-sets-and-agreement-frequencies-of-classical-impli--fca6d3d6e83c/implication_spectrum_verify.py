#!/usr/bin/env python3
"""Independent finite truth-table tests for the implication-only equation theorem.

Both term-function closure and equality-set families are exhaustively checked
through arity three. This does not certify the infinitary universal claim.
"""
from itertools import product


def check(n):
    points = list(product((0, 1), repeat=n))
    variables = tuple(tuple(p[i] for p in points) for i in range(n))
    term_values = set(variables)
    rounds = 0
    while True:
        rounds += 1
        next_values = term_values | {
            tuple(int((not a) or b) for a, b in zip(f, g))
            for f in term_values for g in term_values
        }
        if next_values == term_values:
            break
        term_values = next_values

    expected_terms = {
        table for table in product((0, 1), repeat=len(points))
        if any(all(table[j] == 1 for j, p in enumerate(points) if p[i] == 1)
               for i in range(n))
    }
    assert term_values == expected_terms, (n, 'term closure differs')

    equality_sets = {
        tuple(int(a == b) for a, b in zip(f, g))
        for f in term_values for g in term_values
    }
    if n == 1:
        expected_sets = {
            tuple(int(p[0] == 1 or p[0] == 0 and val) for p in points)
            for val in (0, 1)
        }
    else:
        expected_sets = {
            table for table in product((0, 1), repeat=len(points))
            if any(all(table[j] == 1 for j, p in enumerate(points)
                       if p[i] == 1 and p[h] == 1)
                   for i in range(n) for h in range(i + 1, n))
        }
    assert equality_sets == expected_sets, (n, 'equation set classification differs')
    numerators = {sum(s) for s in equality_sets}
    expected_numerators = (set(range(2**(n-2), 2**n+1)) if n >= 2
                           else {1, 2})
    assert numerators == expected_numerators
    return (n, rounds, len(term_values), len(equality_sets),
            min(numerators), max(numerators))


if __name__ == '__main__':
    for n in range(1, 4):
        arity, rounds, terms, equality_sets, minimum, maximum = check(n)
        print(f'arity={arity} closure_rounds={rounds} distinct_terms={terms} '
              f'equality_sets={equality_sets} numerator_range=[{minimum},{maximum}]')
    print('IMPLICATION_SPECTRUM_VERIFY_OK')
