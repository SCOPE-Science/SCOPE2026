#!/usr/bin/env python3
"""Exact, standard-library point-count certificate for an Artin--Schreier curve over F_3.

The curve is the smooth projective model of y**3-y=x**5+x**4+x**2.
Run: python3 check_supersingular_as.py
"""
from itertools import product

P = 3
MODULI = {
    1: (0, 1),
    2: (1, 0, 1),
    3: (1, 2, 0, 1),
    4: (2, 1, 0, 0, 1),
}
EXPECTED = [7, 19, 28, 91]


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def polynomial_remainder(a, b):
    a = trim(a)
    b = trim(b)
    assert b and b[-1] == 1, 'monic divisor required'
    while len(a) >= len(b):
        lead = a[-1]
        shift = len(a) - len(b)
        for j, t in enumerate(b):
            a[j + shift] = (a[j + shift] - lead*t) % P
        a = trim(a)
    return a


def assert_irreducible(poly):
    n = len(poly) - 1
    assert poly[-1] == 1
    for d in range(1, n//2 + 1):
        for coefficients in product(range(P), repeat=d):
            divisor = coefficients + (1,)
            assert polynomial_remainder(poly, divisor), (poly, divisor)


class FiniteField:
    def __init__(self, n):
        self.n = n
        self.q = P**n
        self.modulus = MODULI[n]
        assert_irreducible(self.modulus)
        self.digits = [tuple((v//P**i)%P for i in range(n))
                       for v in range(self.q)]
        self.weights = [P**i for i in range(n)]

    def add(self, x, y):
        return sum(((a+b)%P)*w for a,b,w in
                   zip(self.digits[x], self.digits[y], self.weights))

    def mul(self, x, y):
        if self.n == 1:
            return x*y % P
        n = self.n
        a = self.digits[x]
        b = self.digits[y]
        c = [0]*(2*n-1)
        for i in range(n):
            for j in range(n):
                c[i+j] = (c[i+j] + a[i]*b[j]) % P
        for deg in range(2*n-2, n-1, -1):
            lead = c[deg]
            for j in range(n):
                c[deg-n+j] = (c[deg-n+j] - lead*self.modulus[j]) % P
        return sum(c[i]*self.weights[i] for i in range(n))

    def power(self, x, e):
        z = 1
        while e:
            if e&1:
                z = self.mul(z,x)
            x = self.mul(x,x)
            e >>= 1
        return z

    def trace(self, x):
        value = 0
        for _ in range(self.n):
            value = self.add(value,x)
            x = self.power(x,3)
        assert value < 3
        return value


def count(n):
    f = FiniteField(n)
    q = f.q
    rhs = [f.add(f.add(f.power(x,5),f.power(x,4)),f.power(x,2))
           for x in range(q)]
    lhs = [f.add(f.power(y,3),f.mul(2,y)) for y in range(q)]
    # Directly check every affine point without using the trace condition.
    affine_direct = sum(a==b for a in rhs for b in lhs)
    histogram = [sum(f.trace(z)==c for z in rhs) for c in range(3)]
    affine_trace = 3*histogram[0]
    assert affine_direct == affine_trace
    assert sum(histogram) == q
    return 1+affine_direct, histogram


def polynomial_product(a,b):
    z = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            z[i+j] += x*y
    return z


def verify():
    counts = []
    for n in MODULI:
        N, h = count(n)
        counts.append(N)
        print('n={}, modulus={}, traces={}, #X={}'.format(n,MODULI[n],h,N))
    assert counts == EXPECTED
    sums = [3**n+1 - counts[n-1] for n in range(1,5)]
    coeffs = [1]
    for k in range(1,5):
        numerator = -sum(coeffs[k-i] * sums[i-1]
                         for i in range(1,k+1))
        assert numerator % k == 0
        coeffs.append(numerator//k)
    # Weil reciprocity for genus 4, q=3: c_(8-i)=3^(4-i)c_i.
    coeffs += [3**(i-4)*coeffs[8-i] for i in range(5,9)]
    # This coefficient list corresponds to (1+3T^2)(1+3T+3T^2)(1+3T^2+9T^4).
    expected = polynomial_product(
        polynomial_product([1,0,3],[1,3,3]),[1,0,3,0,9])
    assert coeffs == expected, (coeffs,expected)
    assert coeffs == [1,3,9,18,36,54,81,81,81]
    # For the Newton polygon with the endpoint (8,4), v_3(c_i)>=i/2;
    # the endpoint equality then forces ALL slopes to be exactly 1/2.
    for i, c in enumerate(coeffs):
        exponent = 0
        while c % 3 == 0:
            c//=3
            exponent+=1
        assert 2*exponent >= i, (i,exponent)
    print('Weil power sums:',sums)
    print('L-polynomial coefficients:',coeffs)
    print('EXACT_CERTIFICATE_PASS')


if __name__ == '__main__':
    verify()
