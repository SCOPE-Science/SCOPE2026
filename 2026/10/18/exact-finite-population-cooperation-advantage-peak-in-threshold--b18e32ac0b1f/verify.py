"""Exact independent checks for finite-population collective-action payoff modes.

Requires only Python 3 standard library. This finite test supports, but does not
replace, the general combinatorial proof in RESULT.md.
"""
from fractions import Fraction
from math import comb


def C(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def hg(t, successes, draws, observed):
    return Fraction(C(successes, observed) *
                    C(t - successes, draws - observed), C(t, draws))


def direct_payoff_gap(z, n, m, k, f):
    # Independent evaluation from each focal strategy's own co-player pool.
    coop = -1 + Fraction(f, n) * sum(
        (j + 1) * hg(z - 1, k - 1, n - 1, j)
        for j in range(n) if j + 1 >= m
    )
    defect = Fraction(f, n) * sum(
        j * hg(z - 1, k, n - 1, j)
        for j in range(n) if j >= m
    )
    return coop - defect


def H(z, n, m, k):
    return sum(
        (1 if j >= m else m if j == m - 1 else 0) *
        hg(z - 2, k - 1, n - 1, j)
        for j in range(n)
    )


def reduced_payoff_gap(z, n, m, k, f):
    return -1 + Fraction(f, n) * Fraction(z - n, z - 1) * H(z, n, m, k)


def h_increment(z, n, m, k):
    return (Fraction(n - 1, z - 2) *
            Fraction(C(k - 1, m - 2) * C(z - k - 2, n - m - 1),
                     C(z - 3, n - 2)) *
            Fraction(m * z - n * (k + 1), n - m))


def main():
    independent = 0
    increments = 0
    for z in range(4, 21):
        for n in range(3, z):
            for m in range(2, n):
                values = [H(z, n, m, k) for k in range(1, z)]
                assert values[0] == 0 and values[-1] == 1
                modes = [k for k in range(1, z) if values[k - 1] == max(values)]
                numerator = m * z - n
                quotient, residue = divmod(numerator, n)
                expected_modes = ([quotient, quotient + 1]
                                  if residue == 0 else [quotient + 1])
                assert modes == expected_modes, (z, n, m, modes, expected_modes)
                assert max(values) > 1
                for k in range(1, z - 1):
                    assert values[k] - values[k - 1] == h_increment(z, n, m, k)
                    increments += 1
                for k in range(1, z):
                    for f in [Fraction(1, 3), Fraction(7, 2), Fraction(13)]:
                        assert direct_payoff_gap(z, n, m, k, f) == reduced_payoff_gap(z, n, m, k, f)
                        independent += 1

    z, n, m, f = 10, 5, 3, Fraction(6)
    h = [H(z, n, m, k) for k in range(1, z)]
    gaps = [direct_payoff_gap(z, n, m, k, f) for k in range(1, z)]
    assert h == list(map(Fraction, [0, 0, Fraction(9, 14), Fraction(19, 14),
                                    Fraction(25, 14), Fraction(25, 14),
                                    Fraction(10, 7), 1, 1]))
    assert gaps == list(map(Fraction, [-1, -1, Fraction(-4, 7), Fraction(-2, 21),
                                       Fraction(4, 21), Fraction(4, 21),
                                       Fraction(-1, 21), Fraction(-1, 3),
                                       Fraction(-1, 3)]))
    critical = Fraction(n * (z - 1), (z - n) * max(h))
    upper = Fraction(n * (z - 1), z - n)
    assert critical == Fraction(126, 25) and upper == 9
    print('PASS', independent, 'independent exact payoff checks; ',
          increments, 'hypergeometric-difference checks')
    print('PASS universal mode rule for tested integer triples')
    print('PASS example H:', [str(a) for a in h])
    print('PASS example payoff gaps:', [str(a) for a in gaps])
    print('PASS thresholds:', critical, upper)


if __name__ == '__main__':
    main()
