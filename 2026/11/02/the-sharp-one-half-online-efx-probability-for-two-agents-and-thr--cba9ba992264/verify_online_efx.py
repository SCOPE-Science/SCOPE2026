#!/usr/bin/env python3
"""Exact finite checks for the two-person, three-good online EFX result.

Only verification code; the infinite valuation-domain argument is analytic.
No external dependencies are required.
"""
from fractions import Fraction
from itertools import product


def efx(values, recipient):
    """Check the EFX inequalities directly, including zero item values."""
    for i in range(2):
        own = sum(values[i][t] for t in range(3) if recipient[t] == i)
        for j in range(2):
            if i == j:
                continue
            other = tuple(t for t in range(3) if recipient[t] == j)
            for removed in other:
                residual = sum(values[i][t] for t in other if t != removed)
                if own < residual:
                    return False
    return True


def probability_of_efx(values):
    """Evaluate exactly the policy including optimal third-good completion."""
    p = Fraction(0)
    pref_first = tuple(values[i][0] >= values[i][1] for i in range(2))
    for first in range(2):
        if pref_first[0] != pref_first[1]:
            first_lover = 0 if pref_first[0] else 1
            choices = [(1 - first if first == first_lover else first, Fraction(1))]
        else:
            choices = [(first, Fraction(1, 2)), (1 - first, Fraction(1, 2))]
        for second, conditional_weight in choices:
            can_complete = any(efx(values, (first, second, third)) for third in range(2))
            if can_complete:
                p += Fraction(1, 2) * conditional_weight
    return p


def run():
    checked = 0
    distribution = {Fraction(1, 2): 0, Fraction(3, 4): 0, Fraction(1): 0}
    for v in product(range(5), repeat=6):
        values = (v[:3], v[3:])
        p = probability_of_efx(values)
        assert p >= Fraction(1, 2), (values, p)
        distribution[p] = distribution.get(p, 0) + 1
        checked += 1
    assert checked == 15625
    # The adversarial pair is indistinguishable until the final good;
    # on one instance the first two must be split, on the other paired.
    for last in (Fraction(1, 4), Fraction(4)):
        vals = ((Fraction(1), Fraction(1), last),) * 2
        feasible_patterns = set()
        for a in product(range(2), repeat=3):
            if efx(vals, a):
                feasible_patterns.add(a[0] == a[1])
        assert feasible_patterns == {last > 1}, (last, feasible_patterns)
        assert probability_of_efx(vals) == Fraction(1, 2)
    print("VERIFY_OK profiles=15625 min_probability=1/2", "histogram=", repr(distribution), "upper_witnesses=2")


if __name__ == "__main__":
    run()
