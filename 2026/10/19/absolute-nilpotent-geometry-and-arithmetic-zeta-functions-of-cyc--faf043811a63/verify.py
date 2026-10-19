"""Reproduce finite-field absolute-nilpotent counts for graph evolution algebras of simple cycles.

Uses only the Python standard library. The multiplication is defined from the
cycle's adjacency rule, independently of the stated closed counting formula.
"""
from itertools import product
from math import prod


class FiniteField:
    def __init__(self, p, degree=1):
        self.p = p
        self.degree = degree
        self.q = p ** degree
        if degree == 1:
            self.modulus = None
        elif (p, degree) == (2, 2):
            self.modulus = [1, 1, 1]  # T^2 + T + 1
        elif (p, degree) == (3, 2):
            self.modulus = [1, 0, 1]  # T^2 + 1
        else:
            raise ValueError('Unsupported extension')
        self.squares = [self.mul(x, x) for x in range(self.q)]
        self.addition = [[self.add(x, y) for y in range(self.q)]
                         for x in range(self.q)]

    def digits(self, n):
        ds = []
        for _ in range(self.degree):
            ds.append(n % self.p)
            n //= self.p
        return ds

    def number(self, digits):
        return sum(int(x) * self.p ** i for i, x in enumerate(digits))

    def add(self, a, b):
        return self.number([(x+y) % self.p for x, y in zip(self.digits(a), self.digits(b))])

    def mul(self, a, b):
        if self.degree == 1:
            return (a*b) % self.p
        da, db = self.digits(a), self.digits(b)
        c = [0] * (self.degree*2-1)
        for i, x in enumerate(da):
            for j, y in enumerate(db):
                c[i+j] = (c[i+j]+x*y) % self.p
        for i in range(len(c)-1, self.degree-1, -1):
            factor = c[i]
            for j in range(self.degree):
                c[i-self.degree+j] = (c[i-self.degree+j]-factor*self.modulus[j]) % self.p
        return self.number(c[:self.degree])


def formula(q, n):
    assert n >= 3
    if q % 2 == 0:
        return q if n % 2 else q*q
    if n % 4:
        return 1
    if q % 4 == 3:
        return 1
    L = 2**(n//2-1)
    return (1+L*(q-1))**2


def direct_count(F, n):
    count = 0
    plus = F.addition
    square = F.squares
    for x in product(range(F.q), repeat=n):
        y = [square[v] for v in x]
        if all(plus[y[(i-1) % n]][y[(i+1) % n]] == 0 for i in range(n)):
            count += 1
    return count


def verify():
    trials = [(FiniteField(2), list(range(3, 13))),
              (FiniteField(3), list(range(3, 11))),
              (FiniteField(2, 2), list(range(3, 9))),
              (FiniteField(5), list(range(3, 9))),
              (FiniteField(7), list(range(3, 7))),
              (FiniteField(3, 2), list(range(3, 7)))]
    tested = 0
    for F, dimensions in trials:
        for n in dimensions:
            if F.q ** n > 600000:
                continue
            observed = direct_count(F, n)
            expected = formula(F.q, n)
            assert observed == expected, (F.q, n, observed, expected)
            print(f'q={F.q:2d} n={n:2d} direct={observed:8d} predicted={expected:8d}')
            tested += 1
    # A count for F_{3^2} detects the quadratic splitting of the F_3 case.
    assert formula(3,4) == 1 and formula(9,4) == 289
    assert formula(5,4) == 81 and formula(7,4) == 1
    # Check the proposed rational zeta factors independently, via formal
    # logarithms: a factor (1-a*T^d)^e contributes -d*e*a^(r/d) to N_r.
    for q, n in ((3,4),(3,8),(5,4),(5,8),(2,7),(4,8),(7,4),(3,6)):
        L = 2**(n//2-1)
        B = (L-1)**2
        if q%2 == 0:
            factors = [(-1, 1, q if n%2 else q*q)]
        elif n%4:
            factors = [(-1,1,1)]
        elif q%4 == 1:
            factors = [(-L*L,1,q*q), (2*L*(L-1),1,q), (-B,1,1)]
        else:
            factors = [(-L*L//2,2,q**4), (L*(L-1),2,q*q),
                       (-(B+1)//2,1,1), (-(B-1)//2,1,-1)]
        for r in range(1,7):
            from_factors = sum(-d*e*a**(r//d) for e,d,a in factors if r%d==0)
            assert from_factors == formula(q**r,n), (q,n,r,from_factors)
    print('VERIFY_OK', tested, 'exhaustive finite-field and zeta checks')


if __name__ == '__main__':
    verify()
