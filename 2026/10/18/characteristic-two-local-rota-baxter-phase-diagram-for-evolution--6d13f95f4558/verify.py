"""Finite-field reproduction checks for characteristic-two evolution-algebra local Rota--Baxter operators. Run: python3 verify.py"""
from itertools import product


def field_mul(q):
    reduction = {2: 0b11, 4: 0b111, 8: 0b1011}[q]
    def mul(a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            b >>= 1
            a <<= 1
            if a & q:
                a ^= reduction
        return result
    return mul


def test_two_dimensional(q, all_structures):
    mul = field_mul(q)
    vectors = list(product(range(q), repeat=2))
    matrices = list(product(vectors, repeat=2))
    zero = (0, 0)
    basis = [(1, 0), (0, 1)]
    def plus(a, b):
        return (a[0] ^ b[0], a[1] ^ b[1])
    def scale(c, x):
        return (mul(c, x[0]), mul(c, x[1]))
    def evaluate(matrix, x):
        return plus(scale(x[0], matrix[0]), scale(x[1], matrix[1]))
    def product_e(squares, x, y):
        return plus(scale(mul(x[0], y[0]), squares[0]), scale(mul(x[1], y[1]), squares[1]))
    def rank_of_squares(squares):
        det = mul(squares[0][0], squares[1][1]) ^ mul(squares[0][1], squares[1][0])
        if det:
            return 2
        return 0 if squares[0] == squares[1] == zero else 1
    def predicted_counts(squares):
        rank = rank_of_squares(squares)
        if rank == 0:
            return 'zero-square', q**4, q**4
        if rank == 2:
            return 'independent-squares', 1, 1
        if zero in squares:
            return 'one-zero-square', q**2, q**2
        generator = squares[0]
        if product_e(squares, generator, generator) == zero:
            return 'dependent-isotropic', q, q
        return 'dependent-anisotropic', 2*q-1, q**2
    if all_structures:
        structures = matrices
        expected_types = {
            'zero-square': 1,
            'one-zero-square': 2*(q**2-1),
            'independent-squares': q*(q-1)**2*(q+1),
            'dependent-isotropic': (q-1)**2,
            'dependent-anisotropic': q*(q-1)**2,
        }
    else:
        structures = [((1, 0), (1, 0)), ((1, 1), (1, 1)),
                      ((1, 0), (0, 0)), ((1, 0), (0, 1)), ((0, 0), (0, 0))]
        expected_types = None
    observed = {}
    for squares in structures:
        category, expected_ordinary, expected_local = predicted_counts(squares)
        ordinary = []
        for matrix in matrices:
            if all(
                product_e(squares, evaluate(matrix, e), evaluate(matrix, f))
                == evaluate(matrix, plus(product_e(squares, evaluate(matrix, e), f),
                                         product_e(squares, e, evaluate(matrix, f))))
                for e in basis for f in basis
            ):
                ordinary.append(matrix)
        assert len(ordinary) == expected_ordinary, (q, squares, category, 'ordinary')
        point_values = {x: {evaluate(matrix, x) for matrix in ordinary} for x in vectors}
        local = [matrix for matrix in matrices
                 if all(evaluate(matrix, x) in point_values[x] for x in vectors)]
        assert len(local) == expected_local, (q, squares, category, 'local')
        observed[category] = observed.get(category, 0) + 1
    if expected_types is not None:
        assert observed == expected_types, (q, observed, expected_types)
    print('DIM2_FIELD', q, 'STRUCTURES', len(structures), 'CATEGORIES', sorted(observed.items()), 'PASS')


def test_chain_binary(n):
    zeros = (0,)*n
    basis = [tuple(int(i == j) for i in range(n)) for j in range(n)]
    vectors = list(product((0, 1), repeat=n))
    def plus(x, y):
        return tuple(a ^ b for a, b in zip(x, y))
    def evaluate(matrix, x):
        output = zeros
        for j in range(n):
            if x[j]:
                output = plus(output, matrix[j])
        return output
    def product_e(x, y):
        output = [0]*n
        for j in range(n-1):
            output[j+1] ^= x[j] & y[j]
        return tuple(output)
    ordinary = []
    for matrix in product(vectors, repeat=n):
        if all(product_e(evaluate(matrix, e), evaluate(matrix, f))
               == evaluate(matrix, plus(product_e(evaluate(matrix, e), f),
                                       product_e(e, evaluate(matrix, f))))
               for e in basis for f in basis):
            ordinary.append(matrix)
    assert len(ordinary) == 2**n, (n, len(ordinary))
    assert all(all(col[:-1] == (0,)*(n-1) for col in matrix) for matrix in ordinary)
    value_sets = {x: {evaluate(matrix, x) for matrix in ordinary} for x in vectors}
    local = [matrix for matrix in product(vectors, repeat=n)
             if all(evaluate(matrix, x) in value_sets[x] for x in vectors)]
    assert len(local) == 2**n, (n, len(local))
    assert set(local) == set(ordinary)
    print('BINARY_NILPOTENT_CHAIN', n, 'ENDOMORPHISMS', 2**(n*n),
          'ORDINARY', len(ordinary), 'LOCAL', len(local), 'PASS')


if __name__ == '__main__':
    test_two_dimensional(2, True)
    test_two_dimensional(4, True)
    test_two_dimensional(8, False)
    test_chain_binary(3)
    test_chain_binary(4)
    print('VERIFY_OK')
