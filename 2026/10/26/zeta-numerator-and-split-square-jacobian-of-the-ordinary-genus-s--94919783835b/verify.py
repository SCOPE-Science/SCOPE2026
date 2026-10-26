#!/usr/bin/env python3
"""Exact independent finite-field verification for the genus-six Artin--Schreier zeta numerator.
Only Python's standard library is used. All arithmetic is over F_3.
"""
from itertools import product

P = 3
MODULI = {
    3: (1, 0, 2, 1),       # U^3 + 2 U^2 + 1
    6: (1, 0, 0, 0, 1, 1, 1),  # U^6 + U^5 + U^4 + 1
}


def trim(v):
    out = list(v)
    while out and out[-1] % P == 0:
        out.pop()
    return tuple(a % P for a in out)


def polynomial_remainder(a, b):
    a, b = list(trim(a)), trim(b)
    assert b
    while len(a) >= len(b):
        shift = len(a) - len(b)
        lead = a[-1] * pow(b[-1], -1, P) % P
        for j, v in enumerate(b):
            a[shift + j] = (a[shift + j] - lead * v) % P
        a = list(trim(a))
    return tuple(a)


def polynomial_gcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, polynomial_remainder(a, b)
    return tuple(v * pow(a[-1], -1, P) % P for v in a) if a else ()


def mul_polynomial_mod(a, b, modulus):
    w = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            w[i + j] = (w[i + j] + ai * bj) % P
    return polynomial_remainder(w, modulus)


def power_polynomial_mod(a, exponent, modulus):
    y = (1,)
    while exponent:
        if exponent & 1:
            y = mul_polynomial_mod(y, a, modulus)
        a = mul_polynomial_mod(a, a, modulus)
        exponent >>= 1
    return y


def irreducible(modulus):
    n = len(modulus) - 1
    t = (0, 1)
    if power_polynomial_mod(t, P ** n, modulus) != t:
        return False
    divisors = [i for i in range(2, n + 1) if n % i == 0 and all(i % j for j in range(2, int(i ** .5) + 1))]
    for prime_divisor in divisors:
        power = power_polynomial_mod(t, P ** (n // prime_divisor), modulus)
        diff = list(power) + [0] * max(0, 2 - len(power))
        diff[1] = (diff[1] - 1) % P
        if polynomial_gcd(diff, modulus) != (1,):
            return False
    return True


class Field:
    def __init__(self, degree):
        self.d = degree
        self.q = P ** degree
        self.modulus = MODULI[degree]
        assert irreducible(self.modulus)
        self.vectors = [self.unpack(n) for n in range(self.q)]

    def unpack(self, n):
        v = []
        for _ in range(self.d):
            v.append(n % P)
            n //= P
        return v

    def pack(self, v):
        return sum((a % P) * P ** i for i, a in enumerate(v))

    def add(self, x, y):
        return self.pack([a + b for a, b in zip(self.vectors[x], self.vectors[y])])

    def negate(self, x):
        return self.pack([-a for a in self.vectors[x]])

    def multiply(self, x, y):
        a, b = self.vectors[x], self.vectors[y]
        w = [0] * (2 * self.d - 1)
        for i in range(self.d):
            for j in range(self.d):
                w[i + j] += a[i] * b[j]
        for k in range(2 * self.d - 2, self.d - 1, -1):
            lead = w[k] % P
            for j in range(self.d):
                w[k - self.d + j] -= lead * self.modulus[j]
        return self.pack(w[:self.d])

    def pow(self, x, n):
        y = 1
        while n:
            if n & 1:
                y = self.multiply(y, x)
            x = self.multiply(x, x)
            n //= 2
        return y

    def trace(self, x):
        y, s = x, 0
        for _ in range(self.d):
            s = self.add(s, y)
            y = self.pow(y, P)
        assert s in (0, 1, 2)
        return s

    def direct_image_count(self):
        image = {self.add(self.pow(y, P), self.negate(y)) for y in range(self.q)}
        assert len(image) == self.q // P
        good = 0
        for x in range(self.q):
            denom = self.add(self.pow(x, P), self.negate(x))
            if denom == 0:
                continue
            if self.add(x, self.pow(denom, self.q-2)) in image:
                good += 1
        return good

    def zero_trace_distribution(self):
        out = [0, 0, 0]
        pole_count = 0
        for x in range(self.q):
            xp = self.pow(x, P)
            denom = self.add(xp, self.negate(x))
            if denom == 0:
                pole_count += 1
                continue
            inv = self.pow(denom, self.q - 2)
            assert self.multiply(inv, denom) == 1
            fx = self.add(x, inv)
            out[self.trace(fx)] += 1
        assert pole_count == 3
        assert sum(out) == self.q - pole_count
        return out


def p_product(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def main():
    F3, F6 = Field(3), Field(6)
    dist3 = F3.zero_trace_distribution()
    dist6 = F6.zero_trace_distribution()
    assert F3.direct_image_count() == dist3[0]
    assert F6.direct_image_count() == dist6[0]
    assert dist3 == [24, 0, 0], dist3
    assert dist6 == [222, 252, 252], dist6
    # At degrees prime to three, translation x -> x+1 permutes trace classes.
    counts = [4, 10, 4 + 3 * dist3[0], 82, 244, 4 + 3 * dist6[0]]
    assert counts == [4, 10, 76, 82, 244, 670]
    q, g = 3, 6
    powers = [0] + [q ** n + 1 - counts[n-1] for n in range(1, g+1)]
    coeff = [1]
    for n in range(1, g+1):
        s = sum(coeff[n-j] * powers[j] for j in range(1, n+1))
        assert s % n == 0
        coeff.append(-s // n)
    coeff.extend(q ** (n-g) * coeff[2*g-n] for n in range(g+1, 2*g+1))
    desired = [1, 0, 0, 16, 0, 0, 118, 0, 0, 432, 0, 0, 729]
    assert coeff == desired, coeff
    E = [1, -1, 3]
    A = [1, 1, -2, 3, 9]
    assert p_product(p_product(E, E), p_product(A, A)) == desired
    # Rational roots and monic quadratic factorizations of Frobenius polynomial.
    f = [9, 3, -2, 1, 1]
    assert all(sum(c * x**i for i,c in enumerate(f)) != 0 for x in [-9,-3,-1,1,3,9])
    for b in [-9,-3,-1,1,3,9]:
        if 9 % b:
            continue
        d = 9 // b
        # a+c=1, a*c=-2-b-d; |a| is bounded by 20 since |a*c|<=20.
        for a in range(-20,21):
            c = 1 - a
            assert not (a*c + b + d == -2 and a*d + b*c == 3)
    print('VERIFY_OK', 'trace-distribution-3:', dist3, 'trace-distribution-6:', dist6,
          'point-counts:', counts, 'Weil:', coeff, 'Jacobian-order:', sum(coeff))


if __name__ == '__main__':
    main()
