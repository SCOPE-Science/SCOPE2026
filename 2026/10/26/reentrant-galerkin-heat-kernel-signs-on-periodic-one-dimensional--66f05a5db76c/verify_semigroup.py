"""Exact-rational finite certificate for a periodic Galerkin heat semigroup.

Requires Python 3 standard library only. The proof explains why the 45
finite checks plus a Laurent-coefficient bound cover every cycle size.
"""
from fractions import Fraction as F
from math import comb, factorial


def inverse_cyclic_four_plus_adjacency_row(n):
    assert n >= 6
    u, v = [1, 0], [0, 1]
    for _ in range(2, n):
        u.append(-4 * u[-1] - u[-2])
        v.append(-4 * v[-1] - v[-2])
    a, b = 4 + u[-1], 1 + v[-1]
    c, d = 1 + u[-2] + 4 * u[-1], v[-2] + 4 * v[-1]
    det = a * d - b * c
    x, y = F(d, det), F(-c, det)
    row = [u[j] * x + v[j] * y for j in range(n)]
    assert all(4 * row[j] + row[(j - 1) % n] + row[(j + 1) % n] == (j == 0)
               for j in range(n))
    return row


def exponential_taylor_kernel(n, degree=21):
    inv = inverse_cyclic_four_plus_adjacency_row(n)
    # Dimensionless generator Q=6I-36(4I+A)^(-1); evaluate exp(Q/3).
    q = [F(6 * (j == 0), 3) - 12 * inv[j] for j in range(n)]
    term = [F(j == 0) for j in range(n)]
    total = term[:]
    for k in range(1, degree + 1):
        term = [sum(q[(j - r) % n] * term[r] for r in range(n)) / k
                for j in range(n)]
        total = [total[j] + term[j] for j in range(n)]
    return total[3]


def poly_value(coeffs, x):
    return sum(c * x ** k for k, c in enumerate(coeffs))


def main():
    # H(x)=1-2x+x^2-2x^3+x^4+x^6+x^8.
    H = [1, -2, 1, -2, 1, 0, 1, 0, 1]
    # (1+y)^8 H(y/(1+y)) has two sign changes.
    converted = [sum(H[k] * comb(8 - k, j - k)
                     for k in range(j + 1) if 0 <= j - k <= 8 - k)
                 for j in range(9)]
    assert converted == [1, 6, 15, 18, 6, -10, -12, -4, 1]
    assert poly_value(H, F(1, 2)) > 0
    assert poly_value(H, F(3, 5)) < 0
    assert poly_value(H, F(4, 5)) < 0
    assert poly_value(H, F(9, 10)) > 0

    largest = (0, F(-1))
    for n in range(6, 51):
        val = exponential_taylor_kernel(n)
        assert val < -F(7, 1000), (n, val)
        if n == 50:
            assert val < -F(73, 10000)
        if n == 6 or val > largest[1]:
            largest = (n, val)

    # Spectral bound for Q/3 in [-4,0] gives a uniform Taylor error.
    remainder = F(4 ** 22, factorial(22))
    assert remainder < F(1, 10 ** 6)
    # For n>=50, all alias corrections to the infinite lattice are bounded
    # on |z|=2 and |z|=1/2 by the displayed Cauchy estimate.
    alias_bound = F(3 ** 10) * (F(8) + F(1, 8)) / (2 ** 50 - 1)
    assert alias_bound < F(1, 10 ** 8)
    # For n>=51 compare to n=50 using two such alias bounds.
    assert -F(73, 10000) + remainder + 2 * alias_bound < -F(7, 1000)
    print('PASS: 45 exact-rational finite cases n=6,...,50')
    print('Largest Taylor kernel: n=%d, approx=%.12f' %
          (largest[0], float(largest[1])))
    print('Uniform spectral Taylor remainder <', float(remainder))
    print('Uniform large-cycle alias bound <', float(alias_bound))
    print('PASS: algebraic root-count samples and all-size continuation bounds')


if __name__ == '__main__':
    main()
