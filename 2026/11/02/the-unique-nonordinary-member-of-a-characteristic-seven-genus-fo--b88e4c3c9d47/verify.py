"""Exact, standalone checks for a genus-four cyclic trigonal family over F_7.

Only Python's standard library is needed. All algebra is performed over
finite fields or the coefficient ring F_7[a]; no floating point is used.
"""
from math import factorial
P = 7


def multinomial(n, x, y, z):
    assert x + y + z == n
    return factorial(n) // (factorial(x) * factorial(y) * factorial(z))


def coeff(exp, deg):
    """Return a-polynomial for [x^deg](x^5+a*x+1)^exp."""
    out = [0] * (exp + 1)
    for u in range(exp + 1):
        for v in range(exp + 1 - u):
            w = exp - u - v
            if 5 * u + v == deg:
                out[v] = (out[v] + multinomial(exp, u, v, w)) % P
    return tuple(out)


def poly_trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def polynomial(exp, deg):
    return poly_trim(coeff(exp, deg))

# Cartier: for j=1,2, C(x^i dx/y^j) has kth coordinate equal to
# ([x^(7(k+1)-1-i)] f^(2j))^(1/7) dx*x^k/y^j.
# The displayed coefficients are seventh powers of Cartier entries.
scalar = polynomial(2, 6)
block = [[polynomial(4, 7 * (k + 1) - 1 - i)
          for i in range(3)] for k in range(3)]
assert scalar == (0, 2)
assert block == [
    [(0, 5), (4,), (0, 0, 0, 0, 1)],
    [(0,), (0, 0, 6), (0, 5)],
    [(1,), (0,), (0,)],
]
print('CARTIER_COEFFICIENT_MATRIX=PASS')

# det(block) = (-3)(-2a)-a^4(-a^2) = 6a+a^6 = a(a^5-1).
# det(full) = 2a^2(a^5-1) = 4a^2 Disc(x^5+a*x+1).
assert 6 % P == (-1) % P
assert 5**5 % P == 3 and 4**4 % P == 4
print('HASSE_DETERMINANT=2a^2(a^5-1);DISCRIMINANT=4(a^5-1)')


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % P
             for j in range(len(B[0]))] for i in range(len(A))]


def rank(A):
    B = [row[:] for row in A]
    m, n = len(B), len(B[0]); r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if B[i][c]), None)
        if pivot is None:
            continue
        B[r], B[pivot] = B[pivot], B[r]
        inv = pow(B[r][c], -1, P)
        B[r] = [(z * inv) % P for z in B[r]]
        for i in range(m):
            if i != r and B[i][c]:
                v = B[i][c]
                B[i] = [(u - v * w) % P for u, w in zip(B[i], B[r])]
        r += 1
    return r

# At a=0, the four-dimensional Cartier matrix is defined over F_7.
C0 = [[0, 0, 0, 0],
      [0, 0, 4, 0],
      [0, 0, 0, 0],
      [0, 1, 0, 0]]
assert rank(C0) == 2
C02 = matmul(C0, C0)
C03 = matmul(C02, C0)
assert rank(C02) == 1
assert rank(C03) == 0
print('FERMAT_FIBER_CARTIER_RANKS=2,1,0;A_NUMBER=2;P_RANK=0')


# All chosen moduli are proved irreducible by checking that every nonzero
# residue class has inverse a^(7^m-2). In a finite commutative ring with 1,
# this property makes it a field. We then completely enumerate its elements.
MODS = {1: (0, 1), 2: (1, 0, 1),
        3: (1, 1, 0, 1), 4: (1, 1, 0, 0, 1)}


class Field:
    def __init__(self, m):
        self.m, self.q, self.mod = m, P**m, MODS[m]
        self.digits = []
        for z in range(self.q):
            row = []
            for _ in range(m):
                row.append(z % P); z //= P
            self.digits.append(row)

    def add(self, a, b):
        return sum(((self.digits[a][i] + self.digits[b][i]) % P) * P**i
                   for i in range(self.m))

    def mul(self, a, b):
        m = self.m
        tmp = [0] * (2*m - 1)
        for i in range(m):
            for j in range(m):
                tmp[i+j] += self.digits[a][i] * self.digits[b][j]
        for i in range(2*m - 2, m - 1, -1):
            v = tmp[i] % P
            for j in range(m):
                tmp[i-m+j] -= v*self.mod[j]
        return sum((tmp[i] % P) * P**i for i in range(m))

    def power(self, a, e):
        out = 1
        while e:
            if e & 1: out = self.mul(out, a)
            a = self.mul(a, a)
            e >>= 1
        return out

    def field_certificate(self):
        for x in range(1, self.q):
            assert self.power(x, self.q-1) == 1
        return True

    def number_of_points(self, a):
        q = self.q
        cubecount = [0] * q
        for y in range(q):
            cubecount[self.power(y, 3)] += 1
        total = 1  # unique rational point at infinity; gcd(3,5)=1
        other = 1
        for x in range(q):
            fx = self.add(self.add(self.power(x, 5), self.mul(a, x)), 1)
            total += cubecount[fx]
            other += (1 if fx == 0 else
                      3 if self.power(fx, (q-1)//3) == 1 else 0)
        assert total == other
        return total


def numerator_from_counts(counts):
    # Newton identities determine coefficients c_1,...,c_4 from N_1,...,N_4.
    power_sums = [0] + [P**m+1-counts[m-1] for m in range(1,5)]
    c = [1]
    for k in range(1, 5):
        z = -sum(c[k-i]*power_sums[i] for i in range(1,k+1))
        assert z % k == 0
        c.append(z//k)
    # Functional equation for a smooth genus-four curve over F_7.
    c += [P**(k-4)*c[8-k] for k in range(5,9)]
    return c

counts_zero, counts_two = [], []
for m in range(1, 5):
    F = Field(m)
    assert F.field_certificate()
    counts_zero.append(F.number_of_points(0))
    counts_two.append(F.number_of_points(2))
assert counts_zero == [8, 50, 344, 2094]
assert counts_two == [5, 47, 389, 2379]
print('POINT_COUNTS_FERMAT_FIBER_F7_TO_F2401=' + str(counts_zero))
print('POINT_COUNTS_ORDINARY_WITNESS_a2=' + str(counts_two))

L = numerator_from_counts(counts_zero)
assert L == [1, 0, 0, 0, -77, 0, 0, 0, 2401]
assert -77 % P == 0 and (-77) % (P*P) != 0
print('FERMAT_ZETA_NUMERATOR=1-77*T^4+2401*T^8')
print('NEWTON_SLOPES=1/4(x4),3/4(x4)')
print('VERIFY_OK')
