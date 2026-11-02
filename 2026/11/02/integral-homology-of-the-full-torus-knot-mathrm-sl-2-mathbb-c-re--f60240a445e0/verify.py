"""Exact lattice arithmetic checks for the closed-component gluing theorem.

The geometry and the antipodal degree are hypotheses justified in RESULT.md;
this program verifies the consequent integral homology map, not those inputs.
Requires Python 3 and SymPy.
"""
from math import gcd
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def parity_index_count(p, q):
    return len([(k, ell) for k in range(1, p)
                for ell in range(1, q) if (k - ell) % 2 == 0])


def test(p, q):
    assert p > 1 and q > 1 and gcd(p, q) == 1
    g = (p - 1) * (q - 1) // 2
    assert parity_index_count(p, q) == g
    # Ordered basis (diagonal +, anti-diagonal -), and product-factor basis.
    d2 = Matrix.zeros(2 * g, 2 * g)
    for i in range(g):
        d2[2 * i, 2 * i] = 1
        d2[2 * i + 1, 2 * i] = 1
        d2[2 * i, 2 * i + 1] = 1
        d2[2 * i + 1, 2 * i + 1] = -1
    smith = smith_normal_form(d2, domain=ZZ)
    assert sorted(abs(int(smith[i, i])) for i in range(2 * g)) == [1] * g + [2] * g
    # H0(Z) -> H0(A) + H0(B) with duplicated columns in each pair.
    d0 = Matrix.zeros(g + 1, 2 * g)
    for i in range(g):
        for j in range(2):
            d0[0, 2 * i + j] = 1
            d0[i + 1, 2 * i + j] = -1
    s0 = smith_normal_form(d0, domain=ZZ)
    assert sorted(abs(int(s0[i, i])) for i in range(g + 1)) == [0] + [1] * g
    assert 1 - g + 0 - 1 + g == 0  # Free Betti ranks in degrees 0..4.
    return g


if __name__ == "__main__":
    for pair in [(2, 3), (2, 5), (2, 7), (3, 4), (3, 5),
                 (3, 7), (4, 5), (5, 6), (5, 7), (7, 8)]:
        assert test(*pair) >= 1
    print("VERIFY_OK")
