#!/usr/bin/env python3
"""Independent finite-field checks for shortcut-quiver class-number formulas.

The radical basis consists of all nonempty directed paths. The computation
constructs its multiplication directly from path concatenation, then computes
linear centralizers without using the symbolic rank-case proof.
"""
from itertools import product


def algebra(m):
    assert m >= 1
    # Arrow 0: 1->2; 1: 2->3; 2: 3->4; 3..m+2: 1->3.
    starts = [1, 2, 3] + [1] * m
    ends = [2, 3, 4] + [3] * m
    paths = [(i,) for i in range(m + 3)]
    paths += [(0, 1), (1, 2)]
    paths += [(i, 2) for i in range(3, m + 3)]
    paths += [(0, 1, 2)]
    lookup = {path: index for index, path in enumerate(paths)}
    n = len(paths)
    assert n == 6 + 2 * m
    products = []
    for i, left in enumerate(paths):
        for j, right in enumerate(paths):
            if ends[left[-1]] == starts[right[0]]:
                combined = left + right
                assert combined in lookup
                products.append((i, j, lookup[combined]))
    return n, products


def rank_mod_prime(a, p):
    arr = [list(row) for row in a]
    height = len(arr)
    width = len(arr[0]) if arr else 0
    rank = 0
    for col in range(width):
        pivot = next((r for r in range(rank, height) if arr[r][col] % p), None)
        if pivot is None:
            continue
        arr[rank], arr[pivot] = arr[pivot], arr[rank]
        scale = pow(arr[rank][col] % p, -1, p)
        arr[rank] = [(a * scale) % p for a in arr[rank]]
        for r in range(rank + 1, height):
            factor = arr[r][col] % p
            if factor:
                arr[r] = [(x - factor * y) % p for x, y in zip(arr[r], arr[rank])]
        rank += 1
        if rank == height:
            break
    return rank


def centralizer_polynomial_count(q, m):
    n, products = algebra(m)
    class_sum = 0
    distribution = {}
    for x in product(range(q), repeat=n):
        ad = [[0] * n for _ in range(n)]
        for i, j, k in products:
            ad[k][j] += x[i]
            ad[k][i] -= x[j]
        rank = rank_mod_prime(ad, q)
        distribution[rank] = distribution.get(rank, 0) + 1
        class_sum += q ** (n - rank)
    assert class_sum % q ** n == 0
    return class_sum // q ** n, class_sum, distribution


def predicted_classes(q, m):
    return q ** m * (2 * q ** (m + 2) + 2 * q ** 3 - q ** m - q ** 2 - 2 * q + 1)


def predicted_ranks(q, m):
    counts = {}

    def add(k, amount):
        counts[k] = counts.get(k, 0) + amount

    add(0, q ** (m + 1))
    add(1, q ** (m + 1) * (q ** 2 - 1) + q ** (m + 2) * (q ** m - 1))
    add(2, (q - 1) * q ** (m + 3) + (q - 1) * q ** (2 * m + 3)
        + (q ** m - 1) * (q - 1) * q ** (m + 2))
    add(3, (q - 1) * (q ** (m + 1) - 1) * q ** (m + 3))
    add(m + 2, (q - 1) * q ** (2 * m + 4))
    add(m + 3, (q - 1) ** 2 * q ** (2 * m + 4))
    assert sum(counts.values()) == q ** (2 * m + 6)
    assert sum(v // q ** k for k, v in counts.items()) == predicted_classes(q, m)
    return counts


def brute_commutation(q, m):
    n, products = algebra(m)
    elements = list(product(range(q), repeat=n))
    count = 0
    for x in elements:
        for y in elements:
            bracket = [0] * n
            for i, j, k in products:
                bracket[k] += x[i] * y[j] - y[i] * x[j]
            if all(z % q == 0 for z in bracket):
                count += 1
    return count


def main():
    for q, m in [(2, 1), (2, 2), (2, 3), (3, 1)]:
        actual, pairs, ranks = centralizer_polynomial_count(q, m)
        predicted = predicted_classes(q, m)
        assert actual == predicted, (q, m, actual, predicted)
        assert ranks == predicted_ranks(q, m), (q, m, ranks, predicted_ranks(q, m))
        print(f'CENTRALIZERS_OK q={q} m={m} dim={6+2*m} classes={actual} pairs={pairs} ranks={sorted(ranks.items())}')
    n = 8
    brute = brute_commutation(2, 1)
    expected = predicted_classes(2, 1) * 2 ** n
    assert brute == expected, (brute, expected)
    print(f'BRUTE_COMMUTATION_OK q=2 m=1 pairs={brute}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
