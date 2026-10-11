#!/usr/bin/env python3
"""Exact finite checks supporting the uniform-support orthograph construction.

The general theorem is proved analytically; finite enumeration is supplementary.
"""
from itertools import combinations, product
from math import comb


def representatives(n, k):
    for support in combinations(range(n), k):
        for tail in product((-1, 1), repeat=k - 1):
            x = [0] * n
            for j, val in zip(support, (1,) + tail):
                x[j] = val
            yield tuple(x)


def orthogonal(x, y):
    # Valid over real scalars for unit ternary x.  If a norming x-coordinate
    # has y=0, the original x-coordinate is fixed under any perturbation;
    # otherwise signed products of both signs imply |1+t|,|1-t| witnesses.
    products = [a * b for a, b in zip(x, y) if a != 0]
    return min(products) <= 0 <= max(products)


def main():
    pair_count = 0
    check_count = 0
    for n in range(1, 9):
        nums = [comb(n, k) * 2**(k - 1) for k in range(1, n + 1)]
        k = (2*n + 2)//3
        assert nums[k - 1] == max(nums), (n, k, nums)
        for j in range(1, n):
            a, b = nums[j - 1], nums[j]
            assert b * (j+1) == a * 2 * (n - j), (n, j)
        for r in range(1, n + 1):
            check_count += 1
            if n <= 6 or (n <= 8 and r == k):
                vectors = list(representatives(n, r))
                assert len(vectors) == comb(n, r) * 2**(r - 1)
                assert len(set(vectors)) == len(vectors)
                for i, x in enumerate(vectors):
                    for y in vectors[:i]:
                        assert orthogonal(x, y) and orthogonal(y, x), (n, r, x, y)
                        pair_count += 1
        print(f"n={n} k={k} bound={nums[k-1]} former_bound={2**(n-1)}")
    assert [comb(n, (2*n+2)//3)*2**((2*n+2)//3-1) for n in range(1,9)] == [1,2,6,16,40,120,336,896]
    print(f"VERIFY_OK layer_count_checks={check_count} mutually_orthogonal_pairs={pair_count} all_pairs_exact=True")


if __name__ == '__main__':
    main()
