"""Exact coefficient tests for a linear Pfaffian singular-curve calculation.

Only standard Python is used. Geometry and genericity require the written proof.
"""
from collections import defaultdict
from itertools import combinations, permutations
from math import comb

N = 4
MAX_DEG = 16


def multiply_sum(f):
    out = defaultdict(int)
    for exponent, coefficient in f.items():
        for j in range(N):
            new = list(exponent)
            new[j] += 1
            out[tuple(new)] += coefficient
    return dict(out)


def sum_power(degree):
    f = {(0, 0, 0, 0): 1}
    for _ in range(degree):
        f = multiply_sum(f)
    return f


def complete_homogeneous_pair_sums(up_to):
    hs = [{(0, 0, 0, 0): 1}] + [{} for _ in range(up_to)]
    for i, j in combinations(range(N), 2):
        new = [hs[0]]
        for degree in range(1, up_to + 1):
            polynomial = defaultdict(int, hs[degree])
            for exponent, coefficient in new[degree - 1].items():
                a = list(exponent)
                a[i] += 1
                polynomial[tuple(a)] += coefficient
                a = list(exponent)
                a[j] += 1
                polynomial[tuple(a)] += coefficient
            new.append(dict(polynomial))
        hs = new
    return hs


def grassmann_integral(f):
    target = (7, 6, 5, 4)
    result = 0
    for p in permutations(range(N)):
        vandermonde_exp = tuple(3 - p[i] for i in range(N))
        required = tuple(target[i] - vandermonde_exp[i]
                         for i in range(N))
        if min(required) < 0:
            continue
        inversions = sum(p[i] > p[j] for i in range(N)
                         for j in range(i + 1, N))
        result += (-1)**inversions * f.get(required, 0)
    return result


def main():
    hs = complete_homogeneous_pair_sums(MAX_DEG)
    grassmann_degree = grassmann_integral(sum_power(16))
    curve_degree = grassmann_integral(hs[16])
    c1_moment = grassmann_integral(multiply_sum(hs[15]))
    assert grassmann_degree == 24024
    assert curve_degree == 84
    assert c1_moment == 168
    # Adjunction before the Pfaffian-trivialization simplification.
    canonical_degree = 14 * curve_degree - 5 * c1_moment
    assert canonical_degree == 4 * curve_degree == 336
    genus = 1 + canonical_degree // 2
    assert genus == 169
    smooth_euler = 4 * sum(comb(8, j) * (-4)**(6-j)
                           for j in range(7))
    singular_euler = smooth_euler - (2*genus - 2)
    assert (smooth_euler, singular_euler) == (1648, 1312)
    print('PFAFFIAN_SINGULAR_CURVE_NUMERICS_OK')


if __name__ == '__main__':
    main()
