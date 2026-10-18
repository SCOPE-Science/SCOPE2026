"""Exact independent finite-field checks of unit-plus-involution fibre formulas.
Run with Python 3, standard library only. Public mathematical reproducibility artifact.
"""
from itertools import product
from math import prod


def algebra(n, arrows, full_upper=False):
    # Matrix units E_ij, multiplication E_ij E_kl = delta_jk E_il
    edges = [(i, i) for i in range(n)]
    if full_upper:
        edges += [(i, j) for i in range(n) for j in range(i+1, n)]
    else:
        edges += arrows
    idx = {edge: pos for pos, edge in enumerate(edges)}
    table = {(r, s): idx[(i, l)]
             for r, (i, j) in enumerate(edges)
             for s, (k, l) in enumerate(edges)
             if j == k and (i, l) in idx}
    return edges, table


def multiply(x, y, table, p):
    z = [0] * len(x)
    for (i, j), k in table.items():
        z[k] = (z[k] + x[i] * y[j]) % p
    return tuple(z)


def cut_weight(sign, arrows, full_upper):
    n = len(sign)
    if full_upper:
        return sum(sign[i] != sign[j] for i in range(n) for j in range(i+1, n))
    return sum(sign[i] != sign[j] for i, j in arrows)


def test_case(p, n, arrows, full_upper=False):
    edges, table = algebra(n, arrows, full_upper)
    dim = len(edges)
    one = (1,) * n + (0,) * (dim-n)
    elements = list(product(range(p), repeat=dim))
    involutions = [x for x in elements if multiply(x, x, table, p) == one]
    by_diag = {}
    for x in involutions:
        by_diag[x[:n]] = by_diag.get(x[:n], 0) + 1
    for signs in product((1, p-1), repeat=n):
        expected = p ** cut_weight(signs, arrows, full_upper)
        assert by_diag.get(signs, 0) == expected, (p, n, signs, expected, by_diag)
    for a in elements:
        actual = sum(all((a[i]-v[i]) % p != 0 for i in range(n)) for v in involutions)
        expected = sum(p ** cut_weight(signs, arrows, full_upper)
                       for signs in product((1, p-1), repeat=n)
                       if all((a[i]-signs[i]) % p != 0 for i in range(n)))
        assert actual == expected, (p, n, a, actual, expected)
    return p, n, dim, len(elements), len(involutions)


def main():
    cases = [
        test_case(3, 3, [], True),                 # T_3(F_3), nonzero J^2
        test_case(5, 2, [], True),                 # T_2(F_5)
        test_case(3, 3, [(0,1),(1,2)]),            # radical-square-zero chain quiver
        test_case(3, 3, [(1,0),(1,2)]),            # radical-square-zero fork quiver
        test_case(3, 3, [(0,1),(0,2)])             # reversing fork, same graph
    ]
    assert cases[2][-1] == cases[3][-1] == 32
    for c in cases:
        print('q=%d vertices=%d algebra_dimension=%d elements=%d involutions=%d: OK' % c)
    print('VERIFY_OK: exhaustive involutions and all unit-plus-involution fibres for all five algebras')

if __name__ == '__main__':
    main()
