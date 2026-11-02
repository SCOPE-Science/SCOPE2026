"""Exact-rational checks for a spherical random-simplex mixed-moment identity."""
from fractions import Fraction as Q
from itertools import product, permutations
from math import factorial


def determinant(matrix):
    size = len(matrix)
    result = Q(0)
    for permutation in permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        term = Q(-1 if inversions % 2 else 1)
        for i in range(size):
            term *= matrix[i][permutation[i]]
        result += term
    return result


def check(dimension, family):
    d = dimension
    count = d + 1
    if family == "regular_simplex":
        support_size = count
        weights = [Q(1, count)] * support_size
        def inner(i, j):
            return Q(1) if i == j else Q(-1, d)
        expected_kappa = Q(d - 1, d * d)
    elif family == "crosspolytope":
        support_size = 2 * d
        weights = [Q(1, support_size)] * support_size
        def inner(i, j):
            return Q(0) if i // 2 != j // 2 else Q(1 if i % 2 == j % 2 else -1)
        expected_kappa = Q(0)
    elif family == "mixed_opposite_simplices":
        support_size = 2 * count
        weights = [Q(3, 4 * count)] * count + [Q(1, 4 * count)] * count
        def inner(i, j):
            sign = (1 if i < count else -1) * (1 if j < count else -1)
            return sign * (Q(1) if i % count == j % count else Q(-1, d))
        expected_kappa = Q(d - 1, 4 * d * d)
    else:
        raise ValueError(family)

    E_volume2 = Q(0)
    E_radius2 = Q(0)
    E_product = Q(0)
    E_cubic_inner = Q(0)
    samples = 0
    for assignment in product(range(support_size), repeat=count):
        samples += 1
        weight = Q(1)
        for label in assignment:
            weight *= weights[label]
        def dot(a, b):
            return inner(assignment[a], assignment[b])
        edge_gram = [[dot(i + 1, j + 1) - dot(0, j + 1)
                      - dot(i + 1, 0) + Q(1) for j in range(d)]
                     for i in range(d)]
        volume2 = determinant(edge_gram) / factorial(d) ** 2
        radius2 = (Q(count) + 2 * sum(dot(i, j)
                    for i in range(count) for j in range(i + 1, count))) / count ** 2
        E_volume2 += weight * volume2
        E_radius2 += weight * radius2
        E_product += weight * volume2 * radius2
        E_cubic_inner += weight * dot(0, 1) ** 3

    expected_volume2 = Q(factorial(count), d ** d * factorial(d) ** 2)
    covariance = E_product - E_volume2 * E_radius2
    normalized = covariance / E_volume2
    assert E_volume2 == expected_volume2
    assert E_radius2 == Q(1, count)
    assert E_cubic_inner == expected_kappa
    assert normalized == -Q(2 + d * d * expected_kappa, count ** 2)
    assert E_product / E_volume2 == Q(d - 1 - d * d * expected_kappa, count ** 2)
    assert Q(-1, count) <= normalized <= Q(-2, count * count)
    if family == "regular_simplex":
        assert normalized == Q(-1, count)
        assert E_product == Q(0)
    elif family == "crosspolytope":
        assert normalized == Q(-2, count * count)
    else:
        assert Q(-1, count) < normalized < Q(-2, count * count)
    print(f"PASS: d={d}, {family}, {samples} ordered draws, "
          f"E[V^2]={E_volume2}, kappa={expected_kappa}, "
          f"Cov/E[V^2]={normalized}")


if __name__ == "__main__":
    for dimension in (2, 3):
        for family in ("regular_simplex", "crosspolytope", "mixed_opposite_simplices"):
            check(dimension, family)
    print("All exact checks passed; the all-dimension claims use the analytic proof.")
