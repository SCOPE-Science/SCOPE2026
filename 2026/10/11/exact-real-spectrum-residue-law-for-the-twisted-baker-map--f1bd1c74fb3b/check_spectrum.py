"""Finite exact-arithmetic checks for the spectral residue theorem.

Run with Python 3 and SymPy; finite checks supplement, not replace, the proof.
"""
from itertools import product
from math import comb, gcd
from sympy import Matrix, Poly, eye, symbols, zeros

z = symbols('z')
for dim in range(2, 7):
    left = eye(dim)
    left[0, 0] = 2
    right = zeros(dim)
    right[0, dim - 1] = -2
    for j in range(dim - 1):
        right[j + 1, j] = 1
    shift = zeros(dim, 1)
    shift[0] = 1
    for n in range(1, 7):
        real_count = 0
        total = 0
        for word in product(('L', 'R'), repeat=n):
            k = word.count('R')
            if k == 0:
                continue
            total += 1
            linear = eye(dim)
            transl = zeros(dim, 1)
            for branch in word:
                step = right if branch == 'R' else left
                linear = step * linear
                transl = step * transl + shift
            fixed = (eye(dim) - linear).inv() * transl
            assert -1 <= fixed[0] <= 1
            assert all(0 <= fixed[j] <= 1 for j in range(1, dim))
            point = fixed
            for branch in word:
                actual = 'R' if point[0] >= 0 else 'L'
                assert actual == branch
                step = right if branch == 'R' else left
                point = step * point + shift
            assert point == fixed

            cycles = gcd(k, dim)
            degree = dim // cycles
            cycle_sign = -1 if (k // cycles) % 2 else 1
            expected = 1
            covered = set()
            total_exponents = 0
            for seed in range(dim):
                if seed in covered:
                    continue
                j = seed
                product_weight = 1
                count = 0
                while j not in covered:
                    covered.add(j)
                    successor = (j + k) % dim
                    factor = linear[successor, j]
                    assert factor != 0
                    product_weight *= factor
                    count += 1
                    j = successor
                assert j == seed and count == degree
                assert product_weight / abs(product_weight) == cycle_sign
                mag = abs(product_weight)
                exponent = 0
                while mag > 1:
                    assert mag % 2 == 0
                    mag /= 2
                    exponent += 1
                total_exponents += exponent
                expected *= z ** degree - product_weight
            assert total_exponents == n
            assert Poly(expected - linear.charpoly(z).as_expr(), z).is_zero
            if k % dim == 0:
                assert degree == 1
                real_count += 1
            else:
                assert degree >= 2
                assert degree != 2 or cycle_sign == -1
        assert total == 2 ** n - 1
        assert real_count == sum(comb(n, j) for j in range(0, n + 1, dim)) - 1
        print(f'dim={dim}; n={n}; real={real_count}; nonreal={total - real_count}')
print('CHECK_OK')
