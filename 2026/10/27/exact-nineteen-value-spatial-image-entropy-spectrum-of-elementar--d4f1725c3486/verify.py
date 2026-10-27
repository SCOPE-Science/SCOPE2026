#!/usr/bin/env python3
"""Exact certificate for the one-step spatial entropy spectrum of elementary CA.
Requires Python 3 and SymPy. Run `python3 verify.py` beside the two CSV files.
`python3 verify.py --write` deterministically regenerates both tables.
No numerical eigensolver is used in the certification.
"""
import csv
import io
import sys
from collections import defaultdict
from pathlib import Path
import sympy as sp

# Pair (lower, upper), both divided by 10^9. Intervals are pairwise disjoint.
ROOT_BRACKETS = [
    (1999999999, 2000000001),
    (1917168418, 1917168421),
    (1915259445, 1915259448),
    (1897179400, 1897179403),
    (1891598682, 1891598685),
    (1890385777, 1890385780),
    (1889697430, 1889697434),
    (1886527043, 1886527047),
    (1886499637, 1886499641),
    (1882618722, 1882618727),
    (1866760397, 1866760402),
    (1839286752, 1839286759),
    (1784598930, 1784598937),
    (1772330220, 1772330227),
    (1764131370, 1764131375),
    (1754877663, 1754877670),
    (1618033986, 1618033992),
    (1465571229, 1465571235),
    (999999999, 1000000001),
]
EXPECTED_CLASS_SIZES = [30, 4, 4, 8, 8, 4, 8, 8, 4, 4,
                        28, 44, 16, 8, 8, 32, 28, 8, 2]
X = sp.Symbol('z')


def exact_machine(rule):
    """Accessible nonempty subset machine of the labeled 4-state de Bruijn graph."""
    delta = [[0, 0] for _ in range(16)]
    for subset in range(16):
        for pair in range(4):
            if (subset >> pair) & 1:
                for bit in (0, 1):
                    triple = 2 * pair + bit
                    label = (rule >> triple) & 1
                    next_pair = triple & 3
                    delta[subset][label] |= 1 << next_pair
    states = [15]  # All four possible two-bit input contexts.
    indices = {15: 0}
    for state in states:
        for next_state in delta[state]:
            if next_state and next_state not in indices:
                indices[next_state] = len(states)
                states.append(next_state)
    matrix = [[0] * len(states) for _ in states]
    for i, state in enumerate(states):
        for next_state in delta[state]:
            if next_state:
                matrix[i][indices[next_state]] += 1
    assert 1 <= len(states) <= 15
    assert all(0 <= sum(row) <= 2 for row in matrix)
    return states, matrix


def root_class(poly):
    """Exact real-root isolation: the largest positive zero lies in one bracket."""
    candidates = []
    for k, (low, high) in enumerate(ROOT_BRACKETS):
        a = sp.Rational(low, 10**9)
        b = sp.Rational(high, 10**9)
        # All eigenvalues have modulus <= 2 by the matrix row-sum bound;
        # no roots above b up to 3 ensures this is the Perron root.
        if poly.count_roots(a, b) > 0 and poly.count_roots(b, 3) == 0:
            candidates.append(k)
    assert len(candidates) == 1, (poly, candidates)
    return candidates[0]


def matrix_word_counts(matrix, max_n):
    counts = [1]
    vector = [0] * len(matrix)
    vector[0] = 1
    for _ in range(max_n):
        nxt = [0] * len(vector)
        for i, value in enumerate(vector):
            if value:
                for j, entry in enumerate(matrix[i]):
                    nxt[j] += value * entry
        vector = nxt
        counts.append(sum(vector))
    return counts


def direct_word_count(rule, n):
    """Independent enumeration of every input block of length n+2."""
    found = set()
    for input_word in range(1 << (n + 2)):
        output_word = 0
        for j in range(n):
            triple = (input_word >> j) & 7
            output_word |= ((rule >> triple) & 1) << j
        found.add(output_word)
    return len(found)


def csv_bytes(rows):
    out = io.StringIO(newline='')
    writer = csv.writer(out, lineterminator='\n')
    writer.writerows(rows)
    return out.getvalue().encode('utf-8')


def certify():
    by_class = defaultdict(list)
    spectra = {}
    class_factors = {}
    rule_rows = [["rule", "entropy_class", "reachable_subset_states", "characteristic_polynomial"]]
    for rule in range(256):
        states, matrix = exact_machine(rule)
        charpoly = sp.Poly(sp.Matrix(matrix).charpoly(X).as_expr(), X)
        k = root_class(charpoly)
        by_class[k].append(rule)
        spectra[rule] = charpoly
        rule_rows.append([rule, k, len(states), str(charpoly.as_expr())])
        if k not in class_factors:
            low, high = ROOT_BRACKETS[k]
            a, b = sp.Rational(low, 10**9), sp.Rational(high, 10**9)
            candidates = []
            for factor, power in sp.factor_list(charpoly.as_expr())[1]:
                f = sp.Poly(factor, X)
                if f.count_roots(a, b) > 0:
                    candidates.append(f)
            assert len(candidates) == 1, (rule, k, candidates)
            class_factors[k] = candidates[0]
        # Exact finite independent test of word counting and normalization.
        for n, count in enumerate(matrix_word_counts(matrix, 8)):
            assert count == direct_word_count(rule, n), (rule, n, count)
    assert list(sorted(by_class)) == list(range(19))
    assert [len(by_class[k]) for k in range(19)] == EXPECTED_CLASS_SIZES
    assert sum(map(len, by_class.values())) == 256
    assert by_class[1] == [22, 104, 151, 233]
    assert by_class[2] == [37, 91, 164, 218]
    assert by_class[18] == [0, 255]
    assert len(by_class[0]) == 30

    class_rows = [["entropy_class", "n_rules", "representative_rule", "rules",
                   "root_lower_numerator_over_1e9", "root_upper_numerator_over_1e9",
                   "irreducible_perron_polynomial"]]
    for k in range(19):
        rules = by_class[k]
        p = class_factors[k]
        lower, upper = ROOT_BRACKETS[k]
        a, b = sp.Rational(lower, 10**9), sp.Rational(upper, 10**9)
        assert p.count_roots(a, b) == 1
        assert p.count_roots(b, 3) == 0
        for rule in rules:
            assert spectra[rule].rem(p).is_zero, (rule, k)
            assert root_class(spectra[rule]) == k
        class_rows.append([k, len(rules), rules[0], ' '.join(map(str, rules)),
                           lower, upper, str(p.as_expr())])
    return {"entropy_spectrum.csv": csv_bytes(class_rows),
            "rule_catalog.csv": csv_bytes(rule_rows)}


def main():
    data = certify()
    for name, encoded in data.items():
        path = Path(__file__).resolve().parent / name
        if len(sys.argv) == 2 and sys.argv[1] == '--write':
            path.write_bytes(encoded)
        else:
            assert path.is_file(), f'missing {name}'
            assert path.read_bytes() == encoded, f'content mismatch {name}'
    print('VERIFY_OK: 256 exhaustive exact image automata, 19 distinct isolated Perron roots, '
          '2304 independent finite-block comparisons, common irreducible class factors, '
          'all saved CSV bytes reproduced')


if __name__ == '__main__':
    main()
