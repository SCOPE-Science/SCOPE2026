"""Exact integer-cyclotomic verification for small-order Fourier-minor census.

The infinite family is proved analytically in RESULT.md. This program tests
its stated structural criterion for p=3, 5, 7, without floating point.
"""
from itertools import combinations, permutations
from math import comb

PERMS = list(permutations(range(3)))
SIGNS = [(-1) ** sum(order[i] > order[j]
                        for i in range(3) for j in range(i + 1, 3))
         for order in PERMS]


def pure_parity(triple):
    return len({x for x, _ in triple}) == 1


def repeated_prime_coordinate(triple):
    return len({j for _, j in triple}) < 3


def predicted_singular(rows, columns):
    return ((pure_parity(rows) and repeated_prime_coordinate(columns))
            or (pure_parity(columns) and repeated_prime_coordinate(rows)))


def exact_determinant_zero(rows, columns, p):
    """Formal integer polynomial in a primitive pth root, reduced by Phi_p."""
    coefficients = [0] * p
    for order, sign in zip(PERMS, SIGNS):
        exponent = sum(rows[i][1] * columns[order[i]][1] for i in range(3)) % p
        parity = sum(rows[i][0] * columns[order[i]][0] for i in range(3)) % 2
        coefficients[exponent] += sign * (-1 if parity else 1)
    # Phi_p(X)=1+...+X^(p-1). The polynomial is zero in Q[zeta_p]
    # if and only if its p coefficients are all equal.
    return len(set(coefficients)) == 1


def check_prime(p):
    points = [(x, j) for x in range(2) for j in range(p)]
    triples = list(combinations(points, 3))
    exceptional = 0
    for rows in triples:
        for columns in triples:
            actual = exact_determinant_zero(rows, columns, p)
            predicted = predicted_singular(rows, columns)
            assert actual == predicted, (p, rows, columns, actual, predicted)
            exceptional += actual
    expected = 8 * p * (p - 1) * comb(p, 3)
    assert exceptional == expected, (p, exceptional, expected)
    print(f"p={p}, minors={len(triples)**2}, singular={exceptional}: PASS")


if __name__ == "__main__":
    for prime in (3, 5, 7):
        check_prime(prime)
    print("Every exact determinant and structural prediction checked.")
