"""Independent finite checks for Dirichlet-mixture concept-lattice saturation.

Only Python's standard library is used. Run: python verify_dirichlet_context.py
"""
from fractions import Fraction
from itertools import product
from math import comb


def rising(a, n):
    out = Fraction(1)
    for j in range(n):
        out *= a + j
    return out


def beta_moment(a, beta, k):
    return rising(a, k) / rising(beta, k)


def exact_completion_probability(m, n, beta):
    a = beta / (m + 1)
    total = Fraction(0)
    for j in range(m + 1):
        mass = sum(
            (Fraction(comb(n, k)) * Fraction(-j, m) ** k
             * beta_moment(a, beta, k))
            for k in range(n + 1)
        )
        total += (-1) ** j * comb(m, j) * mass
    return total


def full_concept_lattice(rows, m):
    top = (1 << m) - 1
    for requested in range(1 << m):
        closure = top
        for row in rows:
            if (row & requested) == requested:
                closure &= row
        if closure != requested:
            return False
    return True


def direct_dirichlet_context_probability(rows, m, beta):
    counts = [0] * (m + 1)
    weight = Fraction(1)
    for row in rows:
        k = row.bit_count()
        counts[k] += 1
        weight /= comb(m, k)
    a = beta / (m + 1)
    for c in counts:
        weight *= rising(a, c)
    return weight / rising(beta, len(rows))


def check():
    cases = 0
    contexts = 0
    for m in (1, 2, 3):
        top = (1 << m) - 1
        coatoms = {top ^ (1 << i) for i in range(m)}
        for beta in (Fraction(2), Fraction(m + 1), Fraction(m + 4)):
            for n in range(0, 5):
                actual = Fraction(0)
                mass = Fraction(0)
                for rows in product(range(1 << m), repeat=n):
                    contexts += 1
                    bool_by_closure = full_concept_lattice(rows, m)
                    bool_by_coatoms = coatoms.issubset(rows)
                    assert bool_by_closure == bool_by_coatoms, (m, n, rows)
                    w = direct_dirichlet_context_probability(rows, m, beta)
                    mass += w
                    if bool_by_closure:
                        actual += w
                assert mass == 1, (m, n, beta, mass)
                expected = exact_completion_probability(m, n, beta)
                assert actual == expected, (m, n, beta, actual, expected)
                cases += 1
    print(f"VERIFY_OK exact_cases={cases} contexts={contexts}")


if __name__ == '__main__':
    check()
