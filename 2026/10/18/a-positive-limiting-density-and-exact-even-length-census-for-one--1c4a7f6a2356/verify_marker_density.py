#!/usr/bin/env python3
"""Cross-check literal one-head saturation and independently computed finite sums."""
from itertools import product
from fractions import Fraction


def saturated_literal(w):
    m = len(w)
    # For the one-symbol head A, saturation of that head requires
    # the right tail not be constant.
    if all(c == w[0] for c in w):
        return False
    # From Definition 3.1: the first tail position fails only if
    # the tail is constant (already excluded). For d>=2 the preceding
    # symbol must not be A when the remaining suffix is an initial prefix.
    for d in range(2, m + 1):
        if w[d - 2] == 0 and w[d:] == w[:m - d]:
            return False
    return True


def count_literal(m):
    return sum(saturated_literal(w) for w in product((0, 1), repeat=m))


def direct_prefix_probability(J):
    good = 0
    for left in product((0, 1), repeat=J):
        for right in product((0, 1), repeat=J + 2):
            if all(right[j + 1] == 1 or left[:j] != right[:j][::-1]
                   for j in range(J + 1)):
                good += 1
    return good, 1 << (2 * J + 2)


def cylinder_formula(J):
    good = 0
    for right in product((0, 1), repeat=J + 2):
        active_minimal = []
        for j in range(J + 1):
            if right[j + 1] == 1:
                continue
            if any(right[:i] == right[j - i:j] for i in active_minimal):
                continue
            active_minimal.append(j)
        unused = (1 << J) - sum(1 << (J - j) for j in active_minimal)
        assert unused >= 0
        good += unused
    return good, 1 << (2 * J + 2)


def main():
    for J in range(0, 7):
        direct = direct_prefix_probability(J)
        formula = cylinder_formula(J)
        assert direct == formula, (J, direct, formula)
        m = 2 * J + 2
        assert count_literal(m) == direct[0] - 1, (m, count_literal(m), direct)
    odd_counts = [count_literal(m) for m in range(3, 16, 2)]
    assert odd_counts == [2, 9, 39, 151, 601, 2381, 9489], odd_counts
    print('PASS: all even counts through length 14; odd counts through 15; two finite sums agree through J=6')


if __name__ == '__main__':
    main()
