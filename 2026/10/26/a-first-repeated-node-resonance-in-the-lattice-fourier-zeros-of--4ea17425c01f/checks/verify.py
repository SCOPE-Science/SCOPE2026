"""Exact finite checks for the 4-simplex lattice Fourier-zero classification.

The proof in RESULT.md is analytic. This script verifies the residue-polynomial
identity exactly over Q for every multiset in a bounded lattice window; the
finite window is diagnostic, not the proof of the infinite classification.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb, factorial


def multiply_truncated(A, B, max_y):
    out = defaultdict(Fraction)
    for (ya, sa), ca in A.items():
        for (yb, sb), cb in B.items():
            y = ya + yb
            if y <= max_y:
                out[(y, sa + sb)] += ca * cb
    return {key: value for key, value in out.items() if value}


def residue_polynomial(nodes):
    """Return coefficients of P(s) in Q[s] as {power: Fraction}.

    For integer nodes a with multiplicity m_a and c=-2*pi*i, the divided
    difference of exp at nodes c*a equals P(1/c), where
      P(s) = sum_a s**(5-m_a) [y**(m_a-1)]
             exp(y) product_{b != a}(a-b+s*y)**(-m_b).
    """
    mult = Counter(nodes)
    assert len(nodes) == 5 and 0 in mult
    total = defaultdict(Fraction)
    for a, ma in mult.items():
        max_y = ma - 1
        expr = {(r, 0): Fraction(1, factorial(r)) for r in range(max_y + 1)}
        for b, mb in mult.items():
            if b == a:
                continue
            factor = {
                (r, r): Fraction((-1) ** r * comb(mb + r - 1, r), (a - b) ** (mb + r))
                for r in range(max_y + 1)
            }
            expr = multiply_truncated(expr, factor, max_y)
        for (y_degree, s_degree), coeff in expr.items():
            if y_degree == max_y:
                total[5 - ma + s_degree] += coeff
    return {power: coeff for power, coeff in total.items() if coeff}


def predicted_zero(nodes):
    mult = Counter(nodes)
    if len(mult) == 5:
        return True
    if sorted(mult.values()) != [1, 2, 2]:
        return False
    repeated = sorted(a for a, m in mult.items() if m == 2)
    singleton = next(a for a, m in mult.items() if m == 1)
    return repeated[0] + repeated[1] == 2 * singleton


def main():
    tested = 0
    zero_cases = 0
    exceptional = []
    for nodes in combinations_with_replacement(range(-3, 4), 5):
        if 0 not in nodes:
            continue
        p = residue_polynomial(nodes)
        actual_identity_zero = not p
        expected = predicted_zero(nodes)
        assert actual_identity_zero == expected, (nodes, p, expected)
        tested += 1
        zero_cases += int(actual_identity_zero)
        if actual_identity_zero and len(set(nodes)) < 5:
            exceptional.append(nodes)
    assert residue_polynomial((0, 0, 1, 2, 2)) == {}
    assert residue_polynomial((0, 0, 1, 3, 3)) == {3: Fraction(-1, 18)}
    assert residue_polynomial((0, 0, 0, 0, 0)) == {0: Fraction(1, 24)}
    assert len(exceptional) > 0
    print(f"exact_multisets_checked={tested}")
    print(f"identity_zero_multisets={zero_cases}")
    print(f"repeated-node_zero_multisets_in_window={len(exceptional)}")
    print("exceptional_examples=" + repr(exceptional[:8]))
    print("nonzero_control_polynomial=" + repr(residue_polynomial((0, 0, 1, 3, 3))))
    print("PASS")


if __name__ == "__main__":
    main()
