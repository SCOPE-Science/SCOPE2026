#!/usr/bin/env python3
"""Exact rational Rudin-Shapiro cyclic-filter verification, standard library only."""
from fractions import Fraction


def polynomials(level):
    p = [1]
    q = [1]
    for _ in range(level):
        p, q = p + q, p + [-t for t in q]
    return p, q


def residue_at_primitive_dyadic_root(coeffs, order_log2):
    # Phi_{2^r}(z) = z^{2^{r-1}}+1; reduction is exact in Z[z].
    half = 1 << (order_log2 - 1)
    rem = [0] * half
    for j, c in enumerate(coeffs):
        rem[j % half] += c if (j // half) % 2 == 0 else -c
    return rem


def integer_matrix_rank(matrix):
    mat = [[Fraction(x) for x in row] for row in matrix]
    nrows = len(mat)
    ncols = len(mat[0])
    pivot_row = 0
    for col in range(ncols):
        pivot = next((i for i in range(pivot_row, nrows) if mat[i][col]), None)
        if pivot is None:
            continue
        mat[pivot_row], mat[pivot] = mat[pivot], mat[pivot_row]
        a = mat[pivot_row][col]
        mat[pivot_row] = [v / a for v in mat[pivot_row]]
        for i in range(pivot_row + 1, nrows):
            if mat[i][col]:
                factor = mat[i][col]
                mat[i] = [v - factor * w for v, w in zip(mat[i], mat[pivot_row])]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def main():
    tested = 0
    primitive_checks = 0
    for level in range(1, 13):
        p, q = polynomials(level)
        n = 1 << level
        assert len(p) == len(q) == n
        assert all(x in (-1, 1) for x in p + q)
        for a in range(-3, 4):
            for b in range(-3, 4):
                if a == b == 0:
                    continue
                mixed = [a * x + b * y for x, y in zip(p, q)]
                at_one = sum(mixed)
                at_minus_one = sum(c if j % 2 == 0 else -c for j, c in enumerate(mixed))
                want_one = (a == 0) if level % 2 else (a == -b)
                want_minus_one = (b == 0) if level % 2 else (a == b)
                assert (at_one == 0) == want_one, (level, a, b, 'one')
                assert (at_minus_one == 0) == want_minus_one, (level, a, b, 'minus_one')
                assert not (at_one == 0 and at_minus_one == 0)
                for order_log2 in range(2, level + 1):
                    rem = residue_at_primitive_dyadic_root(mixed, order_log2)
                    assert any(rem), (level, a, b, order_log2)
                    primitive_checks += 1
                tested += 1
    matrices = 0
    for level in range(1, 5):
        p, q = polynomials(level)
        n = 1 << level
        for a, b in [(1, 0), (0, 1), (1, 1), (1, -1), (1, 2), (2, -3)]:
            mixed = [a * x + b * y for x, y in zip(p, q)]
            circulant = [[mixed[(i - j) % n] for j in range(n)] for i in range(n)]
            expect = n - (int((a == 0) if level % 2 else (a == -b)) +
                          int((b == 0) if level % 2 else (a == b)))
            assert integer_matrix_rank(circulant) == expect
            matrices += 1
    # With real (but non-rational) coefficients, primitive order-8 roots can vanish:
    # P_3(zeta_8) / Q_3(zeta_8) = sqrt(2)-1.
    # At primitive eighth roots z, z^{-1}=z^7 and
    # P_3(z) / Q_3(z) = z+z^{-1}-1. At z=e^{pi i/4} this is
    # sqrt(2)-1, real irrational; at its conjugate it is the same.
    p3, q3 = polynomials(3)
    inv_root_expression = [-1, 1, 0, 0, 0, 0, 0, 1]
    product = [0] * (len(inv_root_expression) + len(q3) - 1)
    for i, a in enumerate(inv_root_expression):
        for j, b in enumerate(q3):
            product[i + j] += a * b
    difference = [((p3[j] if j < len(p3) else 0) - product[j])
                  for j in range(len(product))]
    assert not any(residue_at_primitive_dyadic_root(difference, 3))
    print(f'VERIFY_OK levels=12 rational_pairs={tested} primitive_cyclotomic_checks={primitive_checks} exact_circulant_ranks={matrices} real_extension_counterexample=proved_symbolically')


if __name__ == '__main__':
    main()
