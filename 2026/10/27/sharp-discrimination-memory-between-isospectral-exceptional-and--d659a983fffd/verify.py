"""Exact-rational finite-size checks for the channel discrimination formulas.

These checks support, but do not replace, the analytic proof of the
completely bounded trace-norm upper bound and its saturation.
"""
from fractions import Fraction as F
from math import e


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def power(a, n):
    r = [[F(i == j) for j in range(3)] for i in range(3)]
    for _ in range(n):
        r = mul(r, a)
    return r


def main():
    checks = 0
    for lam in (F(1, 4), F(1, 2), F(3, 4), F(4, 5), F(9, 10)):
        co = 2 * lam / (1 + lam**2)
        si = (1 - lam**2) / (1 + lam**2)
        exceptional = [[lam**2 * co, F(0), si],
                       [F(0), lam**2, F(0)],
                       [-lam**2 * si, F(0), co]]
        pauli = [[lam, F(0), F(0)],
                 [F(0), lam**2, F(0)],
                 [F(0), F(0), lam]]
        weights = ((1 + lam)**2 / 4, (1 - lam)**2 / 4,
                   (1 - lam**2) / 4, (1 - lam**2) / 4)
        assert sum(weights) == 1 and all(w >= 0 for w in weights)
        u = (F(1), F(0), lam)
        v = (-lam, F(0), F(1))
        assert sum(u[i] * v[i] for i in range(3)) == 0
        assert sum(z * z for z in u) == 1 + lam**2
        assert sum(z * z for z in v) == 1 + lam**2
        for n in range(1, 16):
            actual = power(exceptional, n)
            baseline = power(pauli, n)
            b = (1 - lam**2) / (1 + lam**2)
            c = n * lam**(n - 1) * b
            expected = [[baseline[i][j] + c * u[i] * v[j]
                         for j in range(3)] for i in range(3)]
            assert actual == expected
            diamond = n * lam**(n - 1) * (1 - lam**2)
            assert diamond == c * (1 + lam**2)
            assert 0 <= diamond <= 2
            checks += 1
    # Sequence shape: a tie at lambda = 1/2 and a peak at n = 5,6
    # for lambda = 4/5, follows from the exact adjacent-term ratio.
    for lam, winners in ((F(1, 2), {1, 2}), (F(4, 5), {4, 5})):
        vals = [n * lam**(n - 1) * (1 - lam**2) for n in range(1, 25)]
        assert {i + 1 for i, x in enumerate(vals) if x == max(vals)} == winners
    for t in (F(1, 2), F(1), F(3, 2), F(2)):
        seq = []
        for k in (1000, 3000, 10000):
            lam = 1 - 1 / k
            n = int(t * k)
            seq.append(n * lam**(n - 1) * (1 - lam**2))
        assert abs(seq[-1] - 2 * float(t) * e**(-float(t))) < .002
    print(f'PASS: {checks} rational Bloch-power identities; Pauli CP checks;'
          ' sharp-time ties; critical-scale limits.')


if __name__ == '__main__':
    main()
