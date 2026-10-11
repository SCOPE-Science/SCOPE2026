"""Independent finite tests of the cycle-zonotope graph's spectral and tree formulas.
Uses Python 3 standard library. Does not constitute an infinite-dimensional proof.
"""
from math import comb, factorial


def determinant_mod(a, prime):
    a = [[z % prime for z in row] for row in a]
    n = len(a)
    d = 1
    for j in range(n):
        pivot = next((k for k in range(j, n) if a[k][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            d = -d
        piv = a[j][j]
        d = d * piv % prime
        inv = pow(piv, -1, prime)
        for i in range(j + 1, n):
            factor = a[i][j] * inv % prime
            if factor:
                for k in range(j + 1, n):
                    a[i][k] = (a[i][k] - factor * a[j][k]) % prime
            a[i][j] = 0
    return d % prime


def determinant_bareiss(a):
    a = [row[:] for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        val = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = val * a[i][j] - a[i][k] * a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
            a[i][k] = 0
        prev = val
    return sign * a[-1][-1]


def graph_laplacian(n):
    # All orientations of the cycle except the two directed cycles.
    vertices = [x for x in range(1, (1 << n) - 1)]
    index = {v: i for i, v in enumerate(vertices)}
    a = [[0] * len(vertices) for _ in vertices]
    for i, v in enumerate(vertices):
        for k in range(n):
            w = v ^ (1 << k)
            if w in index:
                j = index[w]
                a[i][j] -= 1
                a[i][i] += 1
    return a


def block_determinant(n, r, t, prime):
    # Integer continuant of det(tI-M_r), avoiding square roots.
    length = n - 1
    f0, f1 = 1, t - (n - 1)
    if length == 1:
        return f1 % prime
    for j in range(2, length + 1):
        f0, f1 = f1, (t - n + (j == n - 1)) * f1 - (j - r) * (n - j + 1 - r) * f0
    return f1 % prime


def spectral_formula_mod(n, t, prime):
    out = block_determinant(n, 0, t, prime)
    out = out * pow(block_determinant(n, 1, t, prime), n - 1, prime) % prime
    for r in range(2, n // 2 + 1):
        dimension = comb(n, r) - comb(n, r - 1)
        for k in range(r, n - r + 1):
            out = out * pow(t - 2 * k, dimension, prime) % prime
    return out


def tree_formula(n):
    numerator = factorial(n - 1) * (n - 2) * ((n - 2) * 2 ** (n - 1) + 2)
    denominator = (n - 1) ** 2
    assert numerator % denominator == 0
    d = numerator // denominator
    result_num = factorial(n - 1) * d ** (n - 1)
    assert result_num % n == 0
    answer = result_num // n
    for r in range(2, n // 2 + 1):
        factor = 2 ** (n - 2 * r + 1) * factorial(n - r) // factorial(r - 1)
        answer *= factor ** (comb(n, r) - comb(n, r - 1))
    return answer


def run():
    prime = 1000003
    spectral_count = 0
    tree_count = 0
    for n in range(3, 8):
        L = graph_laplacian(n)
        size = len(L)
        assert size == 2 ** n - 2
        assert sum(row == [] for row in L) == 0
        assert sum(sum(row) for row in L) == 0
        values = [0, 1, 2, 3, 4, 5, 7, 11, 13, 17, 23, 41]
        if n == 7:
            values = [0, 1, 2, 7, 13]
        for t in values:
            target = determinant_mod([[t * (i == j) - L[i][j] for j in range(size)] for i in range(size)], prime)
            predicted = spectral_formula_mod(n, t, prime)
            assert target == predicted, (n, t, target, predicted)
            spectral_count += 1
        if n <= 6:
            actual_tree = determinant_bareiss([row[:-1] for row in L[:-1]])
            predicted_tree = tree_formula(n)
            assert actual_tree == predicted_tree, (n, actual_tree, predicted_tree)
            tree_count += 1
    print('PASS spectral modular determinant comparisons:', spectral_count)
    print('PASS independent exact tree cofactor comparisons:', tree_count)
    print('Tested n=3,...,7 for spectrum and n=3,...,6 for trees.')
    print('These finite tests support, but do not replace, the all-dimensional proof.')


if __name__ == '__main__':
    run()
