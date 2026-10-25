"""Exact finite-dimensional examples for cross-polytope rainbow pushability.

Run: python verify_crosspolytope.py
This is supplementary arithmetic verification, not a proof of the all-d theorem.
"""
from fractions import Fraction
from itertools import product


def pair(d, j):
    out = {(k, s): Fraction(0) for k in range(d) for s in (-1, 1)}
    out[j, -1] = Fraction(1, 2)
    out[j, 1] = Fraction(1, 2)
    return out


def mixed(d):
    out = {(k, s): Fraction(k + 1, d * (d + 1)) for k in range(d) for s in (-1, 1)}
    assert sum(out.values()) == 1
    return out


def balanced(rows, d):
    return all(sum(row[j, 1] - row[j, -1] for row in rows) == 0 for j in range(d))


def common_facet_probability(rows, d):
    """Enumerate all random signed-axis outcomes exactly, counting each once."""
    active = [[(vertex, mass) for vertex, mass in row.items() if mass] for row in rows]
    total = Fraction(0)
    for outcome in product(*active):
        signs = {}
        mass = Fraction(1)
        valid = True
        for (axis, sign), prob in outcome:
            mass *= prob
            if axis in signs and signs[axis] != sign:
                valid = False
                break
            signs[axis] = sign
        if valid:
            total += mass
    return total


def run():
    cases = 0
    for d in range(2, 6):
        for r in range(1, min(d + 3, 7)):
            rows = [pair(d, j) for j in range(min(r, d))]
            if r > d:
                rows += [mixed(d) for _ in range(r - d)]
            assert len(rows) == r and balanced(rows, d)
            expected = min(Fraction(1), Fraction(2 ** d, 2 ** r))
            found = common_facet_probability(rows, d)
            assert found == expected, (d, r, found, expected)
            cases += 1
    # Preserve collective balance while removing mandatory axis 0 in d=3.
    d = 3
    rows = [mixed(d), pair(d, 1), pair(d, 2), mixed(d)]
    assert balanced(rows, d)
    assert common_facet_probability(rows, d) < Fraction(2 ** d, 2 ** len(rows))
    print(f'PASS: {cases} exact balanced constructions, plus one strict nonoptimizer')


if __name__ == '__main__':
    run()
