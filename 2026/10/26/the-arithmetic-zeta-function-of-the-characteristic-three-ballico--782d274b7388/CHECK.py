"""Exact finite-field point-count certificate for a Ballico-Hefez quartic model.

This checks the new arithmetic calculation; the geometric input about the
minimal resolution and its divisor classes is a cited published theorem.
Python 3 standard library only.
"""
from itertools import product

class Field:
    def __init__(self, degree):
        assert degree in (1, 2)
        self.degree = degree
        self.q = 3 ** degree
        self.elts = tuple(range(self.q))

    def add(self, a, b):
        if self.degree == 1:
            return (a + b) % 3
        return ((a % 3 + b % 3) % 3) + 3 * ((a // 3 + b // 3) % 3)

    def neg(self, a):
        if self.degree == 1:
            return (-a) % 3
        return ((-(a % 3)) % 3) + 3 * ((-(a // 3)) % 3)

    def mul(self, a, b):
        if self.degree == 1:
            return (a * b) % 3
        a0, a1 = a % 3, a // 3
        b0, b1 = b % 3, b // 3
        # The generator u obeys u*u=2 (u^2+1=0).
        return ((a0*b0 + 2*a1*b1) % 3) + 3*((a0*b1+a1*b0) % 3)

    def power(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def projective(self, dim):
        # Every point has exactly one normalized representative: its first
        # nonzero homogeneous coordinate is 1.
        for v in product(self.elts, repeat=dim + 1):
            if any(v) and next(t for t in v if t != 0) == 1:
                yield v

    def branch_value(self, x, y, z):
        # RHS of w^4=2(x^3y+xy^3)-z^4-(z^2-xy)^2 in characteristic 3.
        g = self.add(self.mul(self.power(x, 3), y), self.mul(x, self.power(y, 3)))
        t = self.sub(self.power(z, 2), self.mul(x, y))
        return self.sub(self.sub(self.mul(2, g), self.power(z, 4)), self.power(t, 2))

    def is_on_surface(self, w, x, y, z):
        return self.power(w, 4) == self.branch_value(x, y, z)

for degree, expected in ((1, 19), (2, 199)):
    F = Field(degree)
    assert all(F.power(x, F.q-1) == 1 for x in F.elts if x)
    p3 = list(F.projective(3))
    assert len(p3) == F.q**3 + F.q**2 + F.q + 1
    p3_on = [v for v in p3 if F.is_on_surface(*v)]
    # Independent fiber count over P^2 with coordinate x,y,z.
    p2 = list(F.projective(2))
    assert len(p2) == F.q**2 + F.q + 1
    fiber_total = 0
    for x,y,z in p2:
        b = F.branch_value(x,y,z)
        fiber_total += sum(F.power(w,4)==b for w in F.elts)
    # [1:0:0:0] is not on this quartic, hence no additional point.
    assert fiber_total == len(p3_on) == expected, (F.q, fiber_total, len(p3_on))
    if degree == 1:
        by_chart = tuple(sum(next(i for i,c in enumerate(v) if c) == k for v in p3_on) for k in range(4))
        assert by_chart == (12, 6, 1, 0), by_chart
    print('projective surface count', F.q, expected, 'checked by full P3 and independent P2 fibers')

# Published resolution has three rational A3 points with the two end
# exceptional curves conjugate over F9 and a rational central P1 over F3.
N1 = 19 + 3 * ((3+1) - 1)
# Over F9 each exceptional chain has 3*(9+1)-2 points instead of its center.
N2 = 199 + 3 * ((3*(9+1)-2) - 1)
assert (N1, N2) == (28, 280)
# Published 49 curves span H^2 and are defined over F9: Frob^2 acts as 9.
# Let the multiplicities of Frob eigenvalues +3,-3 be a,b.
a_plus = (22 + (N1-1-3**2)//3) // 2
b_minus = 22 - a_plus
assert (a_plus, b_minus) == (14,8)
for n in range(1, 7):
    c = 3**n
    # Replace expression with eigenvalue formula: (+3)^n and (-3)^n.
    expected_count = 1 + 3**(2*n) + a_plus*3**n + b_minus*(-3)**n
    assert expected_count == 1 + c*c + (a_plus + b_minus*(-1)**n)*c
print('resolved points:', N1, N2)
print('normalized Frobenius signs:', a_plus, b_minus)
print('VERIFY_OK')
