#!/usr/bin/env python3
"""Exact finite-field arithmetic certificate for a genus-six Artin--Schreier curve.
Only Python standard library; all finite sets are fully enumerated.
"""
from fractions import Fraction
from math import isqrt

PRIME = 3
MODULI = {
    1: (0, 1),
    2: (1, 0, 1),
    3: (1, 2, 0, 1),
    4: (2, 1, 0, 0, 1),
    5: (1, 2, 0, 0, 0, 1),
    6: (2, 1, 0, 0, 0, 0, 1),
}
EXPECTED = {1: 4, 2: 10, 3: 76, 4: 82, 5: 244, 6: 670}


def strip(poly):
    poly = [int(z) % PRIME for z in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def divzero(a, b):
    a, b = strip(a), strip(b)
    if b == [0]:
        raise ZeroDivisionError()
    while len(a) >= len(b) and a != [0]:
        coeff = a[-1] * pow(b[-1], -1, PRIME) % PRIME
        shift = len(a) - len(b)
        for j, bj in enumerate(b):
            a[shift + j] = (a[shift + j] - coeff * bj) % PRIME
        a = strip(a)
    return a == [0]


def verify_irreducible(poly):
    n = len(poly)-1
    if n == 1:
        return True
    for degree in range(1, n//2 + 1):
        for encoding in range(PRIME ** degree):
            g = [encoding // PRIME**j % PRIME for j in range(degree)] + [1]
            assert not divzero(poly, g), (poly, g)
    return True


class Field:
    def __init__(self, modulus):
        self.f = modulus
        self.n = len(modulus) - 1
        self.q = PRIME**self.n
        self.digits = [tuple(v//PRIME**j % PRIME for j in range(self.n)) for v in range(self.q)]
        self.index = {v: i for i, v in enumerate(self.digits)}
        assert len(self.index) == self.q
        assert verify_irreducible(modulus)

    def add(self, a, b):
        return self.index[tuple((u+v) % PRIME for u, v in zip(self.digits[a], self.digits[b]))]

    def neg(self, a):
        return self.index[tuple(-u % PRIME for u in self.digits[a])]

    def mul(self, a, b):
        n = self.n
        prod = [0]*(2*n-1)
        for i, ai in enumerate(self.digits[a]):
            for j, bj in enumerate(self.digits[b]):
                prod[i+j] += ai*bj
        for k in range(2*n-2,n-1,-1):
            factor = prod[k] % PRIME
            for j in range(n):
                prod[k-n+j] -= factor*self.f[j]
        return self.index[tuple(t%PRIME for t in prod[:n])]

    def power(self, a, exponent):
        assert exponent >= 0
        out = 1
        while exponent:
            if exponent & 1:
                out = self.mul(out,a)
            a = self.mul(a,a)
            exponent >>= 1
        return out


def count_points(n):
    F = Field(MODULI[n])
    # Direct enumeration of the image and fibres of y -> y^3-y.
    fibre = [0]*F.q
    for y in range(F.q):
        fy = F.add(F.power(y,3), F.neg(y))
        fibre[fy] += 1
    assert sum(fibre) == F.q
    assert set(fibre).issubset({0,3})
    points = 4  # Three rational simple-pole fibres plus infinity.
    good_x = 0
    for x in range(F.q):
        den = F.add(F.power(x,3),F.neg(x))
        if den == 0:
            continue
        good_x += 1
        rhs = F.add(x,F.power(den,F.q-2))
        points += fibre[rhs]
    assert good_x == F.q-3
    assert points == EXPECTED[n], (n, points)
    if n in (3, 6):
        # Independent Artin--Schreier fibre criterion: absolute field trace zero.
        frequency = [0, 0, 0]
        for x in range(F.q):
            den = F.add(F.power(x, 3), F.neg(x))
            if den == 0:
                continue
            rhs = F.add(x, F.power(den, F.q-2))
            acc = 0
            term = rhs
            for _ in range(n):
                acc = F.add(acc, term)
                term = F.power(term, 3)
            assert acc in (0, 1, 2)
            frequency[acc] += 1
        assert frequency == ({3: [24,0,0], 6: [222,252,252]})[n]
        assert points == 4 + 3*frequency[0]
        print('absolute-trace frequencies:', frequency)
    print('n=%d, q=%d, rational points=%d, affine x=%d' % (n,F.q,points,good_x))
    return points


def multiply(A,B):
    C = [0]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
        for j,y in enumerate(B):
            C[i+j] += x*y
    return C


def reconstruct(counts):
    genus = 6
    q = 3
    s = [0]+[q**n+1-counts[n] for n in range(1,genus+1)]
    a = [1]
    for k in range(1,genus+1):
        term = Fraction(-sum(a[k-i]*s[i] for i in range(1,k+1)),k)
        assert term.denominator == 1
        a.append(int(term))
    full = a + [0]*genus
    for k in range(genus):
        full[2*genus-k] = q**(genus-k)*a[k]
    E = [1,-1,3]
    A = [1,1,-2,3,9]
    assert full == multiply(multiply(E,A), multiply(E,A))
    assert full == [1,0,0,16,0,0,118,0,0,432,0,0,729]
    assert sum(full) == (E[0]+E[1]+E[2])**2 * (sum(A))**2
    # Q(T)=1+T-2T^2+3T^3+9T^4 is irreducible over Q:
    # its monic reciprocal has no integer root and no monic quadratic factor.
    def quartic(v):
        return v**4+v**3-2*v*v+3*v+9
    assert all(quartic(t) != 0 for t in (-9,-3,-1,1,3,9))
    for b in (-9,-3,-1,1,3,9):
        for d in (-9,-3,-1,1,3,9):
            if b*d != 9:
                continue
            if b == d:
                if b != 3: continue
                discriminant = 1 - 4*(-2-b-d)
                assert discriminant < 0 or isqrt(discriminant)**2 != discriminant
            else:
                numerator = 3-b
                denominator = d-b
                assert numerator % denominator != 0 or (numerator//denominator)*(1-numerator//denominator)+b+d != -2

    print('Weil numerator coefficients:', full)
    print('Factorization: (1-T+3T^2)^2 (1+T-2T^2+3T^3+9T^4)^2')
    print('Jacobian order over F3:', sum(full))


def main():
    counts = {n: count_points(n) for n in range(1,7)}
    reconstruct(counts)
    print('ALL EXACT CERTIFICATE CHECKS PASSED')

if __name__ == '__main__':
    main()
