#!/usr/bin/env python3
"""Exhaustive finite-field checks for mixed-length truncated coordinate crosses."""
from itertools import product
from collections import Counter


def gl_order(q, r):
    value = 1
    for i in range(r):
        value *= q**r - q**i
    return value


def predicted_order(q, lengths):
    n = len(lengths)
    short = sum(d == 2 for d in lengths)
    long = n - short
    multiplicities = Counter(d for d in lengths if d >= 3)
    permutation_factor = 1
    for m in multiplicities.values():
        for k in range(2, m + 1):
            permutation_factor *= k
    exponent = sum(d - 2 for d in lengths if d >= 3) + short * long + long * (n - 1)
    return gl_order(q, short) * permutation_factor * (q - 1)**long * q**exponent


def invertible(matrix, q):
    n = len(matrix)
    augmented = [list(row) + [int(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next((r for r in range(column, n) if augmented[r][column] % q), None)
        if pivot is None:
            return False
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        inverse = pow(augmented[column][column] % q, -1, q)
        augmented[column] = [(x * inverse) % q for x in augmented[column]]
        for row in range(n):
            if row != column and augmented[row][column] % q:
                factor = augmented[row][column] % q
                augmented[row] = [(augmented[row][j] - factor * augmented[column][j]) % q for j in range(2 * n)]
    return True


def brute_order(q, lengths):
    n = len(lengths)
    basis = [(branch, degree) for branch, d in enumerate(lengths) for degree in range(1, d)]
    dimension = len(basis)
    position = {monomial: j for j, monomial in enumerate(basis)}
    zero = (0,) * dimension
    elements = list(product(range(q), repeat=dimension))

    def multiply(left, right):
        result = [0] * dimension
        for a, (i, degree_a) in enumerate(basis):
            if left[a] == 0:
                continue
            for b, (j, degree_b) in enumerate(basis):
                if right[b] == 0 or i != j:
                    continue
                degree = degree_a + degree_b
                if degree < lengths[i]:
                    index = position[(i, degree)]
                    result[index] = (result[index] + left[a] * right[b]) % q
        return tuple(result)

    def power(element, exponent):
        result = element
        for _ in range(exponent - 1):
            result = multiply(result, element)
        return result

    admissible_images = []
    for d in lengths:
        admissible_images.append([element for element in elements if power(element, d) == zero])

    count = 0
    for images in product(*admissible_images):
        if any(multiply(images[i], images[j]) != zero for i in range(n) for j in range(i + 1, n)):
            continue
        cotangent = [
            [images[j][position[(i, 1)]] if (i, 1) in position else 0 for j in range(n)]
            for i in range(n)
        ]
        if invertible(cotangent, q):
            count += 1
    return count


def main():
    cases = [
        (2, (2,)),
        (2, (3,)),
        (2, (2, 2)),
        (2, (2, 3)),
        (2, (2, 2, 3)),
        (2, (2, 3, 3)),
        (2, (3, 3)),
        (2, (3, 4)),
        (2, (2, 3, 4)),
        (2, (3, 3, 4)),
        (3, (2, 3)),
        (3, (2, 2, 3)),
        (3, (2, 3, 3)),
    ]
    for q, lengths in cases:
        observed = brute_order(q, lengths)
        predicted = predicted_order(q, lengths)
        print(f"q={q}, lengths={lengths}: brute={observed}, formula={predicted}")
        if observed != predicted:
            raise SystemExit("VERIFY_FAIL")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
