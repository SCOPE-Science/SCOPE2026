#!/usr/bin/env python3
"""Reproduce exact zeta data for y^3-y=x^2/(x^3+2*x^2+1) over F_3.

Pure Python 3, no third-party packages. Field elements are base-three digits.
This finite calculation, combined with the genus-four Weil functional equation,
proves the stated L-polynomial. It does not independently prove the published
automorphism-group theorem.
"""
from itertools import product

P = 3
MODULI = {
    1: [0, 1],
    2: [1, 0, 1],
    3: [1, 2, 0, 1],
    4: [2, 1, 0, 0, 1],
    5: [1, 2, 0, 0, 0, 1],
    6: [2, 1, 0, 0, 0, 0, 1],
    7: [2, 0, 1, 0, 0, 0, 0, 1],
    8: [2, 0, 1, 0, 0, 0, 0, 0, 1],
}


def remainder(a, b):
    a = [u % P for u in a]
    while a and a[-1] == 0:
        a.pop()
    while a and len(a) >= len(b):
        lead = a[-1]  # b is monic
        shift = len(a) - len(b)
        for i, v in enumerate(b):
            a[shift + i] = (a[shift + i] - lead * v) % P
        while a and a[-1] == 0:
            a.pop()
    return a


def check_irreducible(f):
    n = len(f) - 1
    assert f[-1] == 1
    for d in range(1, n // 2 + 1):
        for cs in product(range(P), repeat=d):
            assert remainder(f, list(cs) + [1]) or False, (n, d, cs)


class Field:
    def __init__(self, modulus):
        check_irreducible(modulus)
        self.modulus = modulus
        self.n = len(modulus) - 1
        self.q = P ** self.n
        self.powers = [P ** i for i in range(self.n)]
        self.digits = [[u // P ** i % P for i in range(self.n)] for u in range(self.q)]

    def add(self, a, b):
        return sum(((self.digits[a][i] + self.digits[b][i]) % P) * self.powers[i]
                   for i in range(self.n))

    def neg(self, a):
        return sum((-self.digits[a][i] % P) * self.powers[i] for i in range(self.n))

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        n = self.n
        c = [0] * (2 * n - 1)
        for i in range(n):
            if self.digits[a][i]:
                for j in range(n):
                    c[i + j] += self.digits[a][i] * self.digits[b][j]
        for k in range(2 * n - 2, n - 1, -1):
            v = c[k] % P
            if v:
                for j in range(n):
                    c[k - n + j] -= v * self.modulus[j]
        return sum((c[i] % P) * self.powers[i] for i in range(n))

    def power(self, a, exponent):
        out = 1
        while exponent:
            if exponent & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            exponent //= 2
        return out

    def eval_poly(self, a, coeffs):
        out = 0
        for b in reversed(coeffs):
            out = self.add(self.mul(out, a), b)
        return out

    def trace(self, a):
        out = 0
        for i in range(self.n):
            out = self.add(out, a)
            a = self.power(a, 3)
        assert 0 <= out <= 2
        return out


def count(n):
    F = Field(MODULI[n])
    buckets = [0] * F.q
    for y in range(F.q):
        v = F.sub(F.power(y, 3), y)
        buckets[v] += 1
    assert all(z in (0, 3) for z in buckets)
    count_direct = 3  # infinity splits into three rational points
    counts = [0, 0, 0]
    ramified_poles = 0
    for a in range(F.q):
        d = F.eval_poly(a, [1, 0, 2, 1])
        if d == 0:
            ramified_poles += 1
            count_direct += 1  # a single rational ramification point
            continue
        f = F.mul(F.mul(a, a), F.power(d, F.q - 2))
        counts[F.trace(f)] += 1
        count_direct += buckets[f]
    count_trace = 3 * (counts[0] + 1) + ramified_poles
    assert count_direct == count_trace
    assert ramified_poles == (3 if n % 3 == 0 else 0)
    return count_direct, tuple(counts), ramified_poles


def check_genus_two_witness():
    # The monic degree-five hyperelliptic model v^2=u^5+u^4+u^2+1.
    coeffs = [1, 0, 1, 0, 1, 1]
    derivative = [0, 2, 0, 1, 2]
    bezout_a = [1, 0, 2, 2]  # -u^3-u^2+1
    bezout_b = [0, 0, 2, 0, 2]  # -u^4-u^2

    def mulpoly(a, b):
        c = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i+j] = (c[i+j] + x*y) % 3
        return c

    left = mulpoly(bezout_a, coeffs)
    right = mulpoly(bezout_b, derivative)
    identity = [(left[i] if i < len(left) else 0)
                + (right[i] if i < len(right) else 0)
                for i in range(max(len(left), len(right)))]
    assert [a % 3 for a in identity] == [1] + [0] * (len(identity)-1)

    for n, required in [(1, 5), (2, 11)]:
        F = Field(MODULI[n])
        squares = [0] * F.q
        for y in range(F.q):
            squares[F.mul(y,y)] += 1
        nc = 1  # one rational point at infinity, odd degree
        for a in range(F.q):
            nc += squares[F.eval_poly(a, coeffs)]
        assert nc == required
        print('GENUS_TWO_WITNESS_EXTENSION', n, 'POINTS', nc)
    print('GENUS_TWO_L_POLYNOMIAL', [1, 1, 1, 3, 9])


def main():
    expected_points = [6, 12, 42, 132, 156, 708, 2022, 6564]
    expected_counts = [(1, 1, 1), (3, 3, 3), (12, 6, 6),
                       (43, 19, 19), (51, 96, 96), (234, 246, 246),
                       (673, 757, 757), (2187, 2187, 2187)]
    for n in range(1, 9):
        actual, distribution, poles = count(n)
        assert actual == expected_points[n - 1], (n, actual)
        assert distribution == expected_counts[n - 1], (n, distribution)
        print('degree', n, 'points', actual, 'trace_distribution', distribution,
              'rational_poles', poles)

    power_sums = [3 ** n + 1 - expected_points[n - 1] for n in range(1, 9)]
    c = [1]
    for n in range(1, 9):
        rhs = -sum(c[n - k] * power_sums[k - 1] for k in range(1, n + 1))
        assert rhs % n == 0
        c.append(rhs // n)
    assert c == [1, 2, 3, 8, 25, 24, 27, 54, 81]
    assert all(c[8 - j] == 3 ** (4 - j) * c[j] for j in range(5))
    half = [1, 1, 1, 3, 9]
    square = [sum(half[j] * half[k - j] for j in range(5)
                  if 0 <= k - j < 5) for k in range(9)]
    assert square == c
    assert sum(c) == 225
    # P(Frob)(t) = t^4+t^3+t^2+3*t+9 reduces to Phi_5(t) modulo two.
    # Since the order of 2 mod 5 is 4, Phi_5 is irreducible over F_2.
    assert (2 ** 4 - 1) % 5 == 0 and all((2 ** j - 1) % 5 != 0 for j in range(1, 4))
    check_genus_two_witness()
    print('NUMERATOR_COEFFS', c)
    print('SQUARE_FACTOR_COEFFS', half)
    print('JACOBIAN_F3_ORDER', sum(c))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
