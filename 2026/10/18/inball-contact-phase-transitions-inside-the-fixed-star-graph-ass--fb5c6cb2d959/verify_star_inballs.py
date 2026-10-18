"""Finite, independent support-and-facet checks for weighted star simplex sums.

Requires Python 3 and numpy. Run `python3 verify_star_inballs.py`.
The script checks finite instances; arbitrary-dimensional statements are proved
analytically in RESULT.md.
"""
from itertools import combinations, permutations
from math import comb, sqrt, isclose
import numpy as np


def simplex_sum_vertices(k, weights):
    """Enumerate vertices by independently maximizing every simplex in all orders."""
    edges = [(tuple((0,) + subset), int(weights[h]))
             for h in range(1, k + 1)
             if weights.get(h, 0) > 0
             for subset in combinations(range(1, k + 1), h)]
    vertices = set()
    for order in permutations(range(k + 1)):
        rank = {v: j for j, v in enumerate(order)}
        coordinates = [0] * (k + 1)
        for edge, weight in edges:
            coordinates[min(edge, key=rank.__getitem__)] += weight
        vertices.add(tuple(coordinates))
    return vertices


def affine_rank(points):
    arr = np.array(list(points), dtype=float)
    if not len(arr):
        raise AssertionError('empty equality face')
    return int(np.linalg.matrix_rank(arr - arr[0]))


def test_instance(k, weights):
    T = sum(comb(k, h) * weights.get(h, 0) for h in range(1, k + 1))
    vv = simplex_sum_vertices(k, weights)
    d = sqrt(k / (k + 1))

    def upper(u):
        return sum((comb(k, h) - (comb(k - u, h) if h <= k - u else 0))
                   * weights.get(h, 0) for h in range(1, k + 1))

    def denominator(u):
        return u * d + sqrt(u * (k - u + 1) / (k + 1))

    radii = [upper(u) / denominator(u) for u in range(1, k + 1)]
    r = min(radii)
    lower_value = d * r
    center = [T - k * lower_value] + [lower_value] * k
    assert isclose(sum(center), T, abs_tol=1e-9)
    actual_contact_count = 0
    upper_contact_sizes = []

    for i in range(1, k + 1):
        sat = {v[1:] for v in vv if v[i] == 0}
        assert affine_rank(sat) == k - 1
        assert min(v[i] for v in vv) == 0
        actual_contact_count += 1
        assert isclose(center[i] / d, r, rel_tol=1e-10, abs_tol=1e-10)

    for u in range(1, k + 1):
        for U in combinations(range(1, k + 1), u):
            bound = upper(u)
            sat = {v[1:] for v in vv if sum(v[i] for i in U) == bound}
            assert sat and max(sum(v[i] for i in U) for v in vv) == bound
            rank = affine_rank(sat)
            if weights.get(2, 0) > 0:
                assert rank == k - 1, (k, weights, U, rank)
            norm = sqrt(u * (k - u + 1) / (k + 1))
            distance = (bound - sum(center[i] for i in U)) / norm
            assert distance >= r - 1e-9, (k, weights, U, distance, r)
            if rank == k - 1 and isclose(distance, r, abs_tol=1e-9):
                actual_contact_count += 1
                upper_contact_sizes.append(u)

    if all(weights.get(h, 0) == 0 for h in range(2, k + 1)):
        expected_count, expected_upper = 2 * k, [1] * k
    elif weights.get(2, 0) and all(weights.get(h, 0) == 0 for h in range(3, k + 1)):
        a, b = weights[1], weights[2]
        expected_count = (2 * k if a > b else 2 * k + 1 if a == b else k + 1)
        expected_upper = ([1] * k if a > b else [1] * k + [k] if a == b else [k])
        d_formula = min((a + (k - 1) * b) / (2 * d),
                        (k * a + comb(k, 2) * b) / sqrt(k * (k + 1)))
        assert isclose(r, d_formula, rel_tol=1e-10)
    else:
        expected_count, expected_upper = k + 1, [k]
    assert actual_contact_count == expected_count, (k, weights, actual_contact_count, expected_count)
    assert sorted(upper_contact_sizes) == sorted(expected_upper), (k, weights, upper_contact_sizes, expected_upper)
    return len(vv)


def main():
    scenarios = 0
    for k in range(2, 7):
        for m in range(1, k + 1):
            weights = {h: 1 for h in range(1, m + 1)}
            count = test_instance(k, weights)
            if m >= 2:
                assert count == sum(comb(k, s) * __import__('math').factorial(s) for s in range(k + 1))
            else:
                assert count == 2 ** k
            scenarios += 1
    for k in range(3, 6):
        for a, b in [(1, 3), (1, 1), (3, 1), (1, 2), (2, 1)]:
            test_instance(k, {1: a, 2: b})
            scenarios += 1
    print(f'VERIFY_OK: {scenarios} exact-integer vertex/facet scenarios; rank and Euclidean-contact checks')


if __name__ == '__main__':
    main()
