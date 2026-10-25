"""Exact finite-field sanity checks for the length-three consecutive irreducible count.

Run with the standard Python interpreter. Exhaustive checks are finite tests;
the accompanying proof establishes the general theorem.
"""


def nonresidue(p):
    return next(d for d in range(2, p) if pow(d, (p - 1) // 2, p) == p - 1)


class Field:
    def __init__(self, p, degree):
        self.p, self.degree = p, degree
        if degree == 1:
            self.elements = list(range(p))
            self.zero = 0
            self.one = 1
        else:
            assert degree == 2
            self.d = nonresidue(p)
            self.elements = [(a, b) for a in range(p) for b in range(p)]
            self.zero = (0, 0)
            self.one = (1, 0)

    def add(self, x, y):
        p = self.p
        if self.degree == 1:
            return (x + y) % p
        return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

    def neg(self, x):
        p = self.p
        if self.degree == 1:
            return (-x) % p
        return ((-x[0]) % p, (-x[1]) % p)

    def mul(self, x, y):
        p = self.p
        if self.degree == 1:
            return (x * y) % p
        return ((x[0] * y[0] + self.d * x[1] * y[1]) % p,
                (x[0] * y[1] + x[1] * y[0]) % p)

    def from_prime(self, x):
        return x % self.p if self.degree == 1 else (x % self.p, 0)


def predicted(q):
    if q % 3 == 0:
        return q * (q - 1)**3 // 6
    if q % 3 == 1:
        return (q - 1)**4 // 6
    return (q - 1)**2 * (q - 3) * (q + 1) // 6


def exhaust(p, degree):
    field = Field(p, degree)
    add, mul, neg = field.add, field.mul, field.neg
    elements = field.elements
    q = len(elements)
    # The values -x^2-x are exactly the a for which X^2+X+a has a root.
    reducible_quadratics = {neg(add(mul(x, x), x)) for x in elements}
    eligible_a = [a for a in elements if a != field.zero and a not in reducible_quadratics]
    assert len(eligible_a) == (q - 1) // 2, (q, len(eligible_a))
    count = 0
    inv3 = None if p == 3 else field.from_prime(pow(3, -1, p))
    for a in eligible_a:
        image = set()
        for x in elements:
            x2 = mul(x, x)
            # X^3+X^2+aX+t has a root iff t lies in this image.
            image.add(neg(add(add(mul(x2, x), x2), mul(a, x))))
        fiber = q - len(image)
        if p == 3:
            expected = q // 3
        elif q % 3 == 1:
            expected = (q - 1) // 3
        else:
            expected = 0 if a == inv3 else (q + 1) // 3
        assert fiber == expected, (q, a, fiber, expected)
        count += fiber
    answer = count * (q - 1)**2
    assert answer == predicted(q), (q, answer, predicted(q))
    print(f'q={q:3d} | eligible={len(eligible_a):3d} | normalized={count:5d} | I3={answer:10d}')


def main():
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
        exhaust(p, 1)
    for p in (3, 5, 7, 11):
        exhaust(p, 2)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
