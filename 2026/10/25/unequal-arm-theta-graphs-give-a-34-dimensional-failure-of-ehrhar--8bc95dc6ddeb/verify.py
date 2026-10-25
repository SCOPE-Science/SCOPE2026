"""Exact certificate for an unequal-arm theta symmetric-edge polytope.

Run with Python 3 (standard library only): python verify.py
Two independent finite-sum computations count the same spanning-tree data:
binomial decomposition by the deleted position and direct orientation words.
The cited spanning-tree-dissection theorem identifies this count with the
Ehrhart h-star polynomial for the specified bipartite theta graph.
"""
from collections import Counter
from itertools import product, permutations
from math import comb


def convolution(p, q):
    ans = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            ans[i + j] += a * b
    return ans


def broken_binomial(length, nplus, deleted_plus):
    """Enumerate signs before/after a deleted edge by binomial coefficients."""
    poly = [0] * length
    if deleted_plus:
        for n_before_plus in range(nplus):
            for n_before_minus in range(length - nplus + 1):
                coeff = comb(n_before_plus + n_before_minus, n_before_plus)
                coeff *= comb(length - 1 - n_before_plus - n_before_minus,
                              nplus - 1 - n_before_plus)
                degree = length - nplus + n_before_plus - n_before_minus
                poly[degree] += coeff
    else:
        for n_before_plus in range(nplus + 1):
            for n_before_minus in range(length - nplus):
                coeff = comb(n_before_plus + n_before_minus, n_before_plus)
                coeff *= comb(length - 1 - n_before_plus - n_before_minus,
                              nplus - n_before_plus)
                degree = length - nplus - 1 + n_before_plus - n_before_minus
                poly[degree] += coeff
    return poly


def hstar_binomial(lengths):
    """Exact common-height / planar-dual-tree sum for same-parity arms."""
    assert len(lengths) >= 2 and all(x >= 2 for x in lengths)
    assert len({x % 2 for x in lengths}) == 1
    dimension = sum(lengths) - len(lengths) + 1
    answer = [0] * (dimension + 1)
    minimum = min(lengths)
    for height in range(-minimum, minimum + 1, 2):
        plus_count = [(length + height) // 2 for length in lengths]
        data = []
        for length, count in zip(lengths, plus_count):
            intact = [0] * count + [comb(length, count)]
            data.append((intact, broken_binomial(length, count, True),
                         broken_binomial(length, count, False)))
        for unbroken_path in range(len(lengths)):
            polynomial = [1]
            for path_index, row in enumerate(data):
                choice = 0 if path_index == unbroken_path else (
                    1 if path_index < unbroken_path else 2)
                polynomial = convolution(polynomial, row[choice])
            for j, value in enumerate(polynomial):
                answer[j] += value
    return answer


def path_by_binary_words(length, height):
    """Independently count every orientation word and every deleted position."""
    intact, missing_plus, missing_minus = Counter(), Counter(), Counter()
    for word in product((0, 1), repeat=length):
        if 2 * sum(word) - length != height:
            continue
        intact[sum(word)] += 1
        for deleted_index, sign in enumerate(word):
            away_from_source = sum(word[:deleted_index]) + sum(
                1 - x for x in word[deleted_index + 1:])
            (missing_plus if sign else missing_minus)[away_from_source] += 1
    def coefficients(c):
        return [c[j] for j in range(max(c) + 1)] if c else [0]
    return (coefficients(intact), coefficients(missing_plus),
            coefficients(missing_minus))


def hstar_by_words(lengths):
    assert len(lengths) >= 2 and len({x % 2 for x in lengths}) == 1
    dimension = sum(lengths) - len(lengths) + 1
    answer = [0] * (dimension + 1)
    minimum = min(lengths)
    for height in range(-minimum, minimum + 1, 2):
        rows = [path_by_binary_words(length, height) for length in lengths]
        for unbroken_path in range(len(lengths)):
            poly = [1]
            for path_index, row in enumerate(rows):
                choice = 0 if path_index == unbroken_path else (
                    1 if path_index < unbroken_path else 2)
                poly = convolution(poly, row[choice])
            for j, value in enumerate(poly):
                answer[j] += value
    return answer


def gamma_vector(hstar):
    """Triangular basis change h*(z)=sum gamma_j z^j (1+z)^(d-2j)."""
    d = len(hstar) - 1
    gamma = []
    for j in range(d // 2 + 1):
        gamma.append(hstar[j] - sum(
            gamma[i] * comb(d - 2 * i, j - i) for i in range(j)))
    return gamma


def reexpand(gamma, dimension):
    hstar = [0] * (dimension + 1)
    for j, coeff in enumerate(gamma):
        for k in range(dimension - 2 * j + 1):
            hstar[j + k] += coeff * comb(dimension - 2 * j, k)
    return hstar


def verify():
    cases = [(6, 8, 8, 8, 8), (8, 8, 8, 8, 8),
             (2, 2, 2), (2, 4, 6), (4, 6, 8), (3, 5, 7)]
    for arms in cases:
        a = hstar_binomial(arms)
        assert a == hstar_by_words(arms)
        assert a == a[::-1]
        assert a[1] == 2 * sum(arms) - (len(a) - 1)
        assert reexpand(gamma_vector(a), len(a) - 1) == a
    target = (6, 8, 8, 8, 8)
    hstar = hstar_binomial(target)
    gamma = gamma_vector(hstar)
    assert len(hstar) == 35
    assert gamma == [1, 8, 48, 256, 1280, 6144, 28672, 117344,
                     379536, 1019456, 2433408, 5081472, 10692480,
                     19652864, 23686656, -236544, 0, 0]
    assert hstar[1] == 42
    assert hstar[17] == 145853691452
    assert sum(hstar) == 848559652864
    for order in set(permutations(target)):
        assert hstar_binomial(order) == hstar
        assert hstar_by_words(order) == hstar
    # Reproduce the published equal-arm benchmark.
    assert gamma_vector(hstar_binomial((8,) * 5))[16] == -9799680
    print('EXACT_OK dimension=34 gamma_15=-236544')
    print('Six independent orientation-word comparisons; five orderings;')
    print('palindromicity, first Ehrhart numerator coefficient, gamma basis,')
    print('and published dimension-36 benchmark confirmed.')


if __name__ == '__main__':
    verify()
