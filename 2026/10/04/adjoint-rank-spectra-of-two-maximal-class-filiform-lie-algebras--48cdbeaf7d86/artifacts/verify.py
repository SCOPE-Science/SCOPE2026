from collections import Counter
from fractions import Fraction
from itertools import product

class Field:
    def __init__(self, q):
        self.q = q
        if q in (2, 3):
            self.kind = "prime"
        elif q == 4:
            self.kind = "gf4"
        else:
            raise ValueError("checker supports q=2,3,4")

    def add(self, a, b):
        if self.kind == "prime":
            return (a + b) % self.q
        return a ^ b

    def neg(self, a):
        if self.kind == "prime":
            return (-a) % self.q
        return a

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.kind == "prime":
            return (a * b) % self.q
        # GF(4) with alpha^2 + alpha + 1 = 0; elements are binary polynomials.
        z = 0
        aa, bb = a, b
        while bb:
            if bb & 1:
                z ^= aa
            bb >>= 1
            aa <<= 1
        if z & 0b1000:
            z ^= 0b1110
        if z & 0b100:
            z ^= 0b111
        return z & 0b11

    def inv(self, a):
        assert a != 0
        for b in range(1, self.q):
            if self.mul(a, b) == 1:
                return b
        raise AssertionError("no inverse")

    def div(self, a, b):
        return self.mul(a, self.inv(b))


def zeros(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def bracket_basis(family, i, j, n, F):
    # i,j are zero-based basis indices. Returns coordinate vector.
    out = [0] * n
    if i == j:
        return out
    sign = 1
    if i > j:
        i, j = j, i
        sign = -1
    val = 1 if sign == 1 else F.neg(1)
    # [e1,e_k]=e_{k+1}, with zero-based i=0, j=1..n-2.
    if i == 0 and 1 <= j <= n - 2:
        out[j + 1] = val
        return out
    # Extra m2 relation [e2,e_k]=e_{k+2}, k=3..n-2.
    if family == "M" and i == 1 and 2 <= j <= n - 3:
        out[j + 2] = val
    return out


def vadd(a, b, F):
    return [F.add(x, y) for x, y in zip(a, b)]


def smul(c, v, F):
    return [F.mul(c, x) for x in v]


def bracket(family, x, y, F):
    n = len(x)
    out = [0] * n
    for i, a in enumerate(x):
        if a == 0:
            continue
        for j, b in enumerate(y):
            if b == 0:
                continue
            c = F.mul(a, b)
            term = bracket_basis(family, i, j, n, F)
            out = vadd(out, smul(c, term, F), F)
    return tuple(out)


def ad_matrix(family, x, F):
    n = len(x)
    A = zeros(n)
    for j in range(n):
        ej = tuple(1 if k == j else 0 for k in range(n))
        col = bracket(family, x, ej, F)
        for i in range(n):
            A[i][j] = col[i]
    return A


def rank(A, F):
    A = [row[:] for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        z = F.inv(A[r][c])
        A[r] = [F.mul(z, x) for x in A[r]]
        for i in range(m):
            if i == r or A[i][c] == 0:
                continue
            z = A[i][c]
            A[i] = [F.sub(A[i][j], F.mul(z, A[r][j])) for j in range(n)]
        r += 1
    return r


def check_jacobi(family, n, F):
    basis = [tuple(1 if k == i else 0 for k in range(n)) for i in range(n)]
    zero = (0,) * n
    for x in basis:
        for y in basis:
            for z in basis:
                s = bracket(family, x, bracket(family, y, z, F), F)
                s = tuple(F.add(a, b) for a, b in zip(s, bracket(family, y, bracket(family, z, x, F), F)))
                s = tuple(F.add(a, b) for a, b in zip(s, bracket(family, z, bracket(family, x, y, F), F)))
                assert s == zero


def expected(family, q, n):
    if family == "L":
        return Counter({
            0: q,
            1: q ** (n - 1) - q,
            n - 2: (q - 1) * q ** (n - 1),
        })
    return Counter({
        0: q,
        1: q * (q - 1),
        2: q ** (n - 2) - q ** 2,
        n - 3: (q - 1) * q ** (n - 2),
        n - 2: (q - 1) * q ** (n - 1),
    })


def expected_degree(family, q, n):
    if family == "L":
        return Fraction(1, q ** 2) + Fraction(q ** 2 - 1, q ** n)
    return Fraction(1, q ** 4) + Fraction(2 * (q ** 2 - 1), q ** n)


def check_case(family, q, n):
    F = Field(q)
    check_jacobi(family, n, F)
    C = Counter()
    for x in product(range(q), repeat=n):
        C[rank(ad_matrix(family, x, F), F)] += 1
    E = expected(family, q, n)
    assert C == E, (family, q, n, C, E)
    assert sum(C.values()) == q ** n
    commuting = sum(mult * q ** (n - r) for r, mult in C.items())
    d = Fraction(commuting, q ** (2 * n))
    assert d == expected_degree(family, q, n), (family, q, n, d)
    return C, commuting, d


def direct_pairs(family, q, n):
    F = Field(q)
    elems = list(product(range(q), repeat=n))
    zero = (0,) * n
    count = 0
    for x in elems:
        for y in elems:
            if bracket(family, x, y, F) == zero:
                count += 1
    return count

rows = []
for q, n in [(2, 9), (3, 7), (4, 6)]:
    for family in ("L", "M"):
        C, commuting, d = check_case(family, q, n)
        rows.append((family, q, n, dict(sorted(C.items())), commuting, str(d)))

for family in ("L", "M"):
    C, commuting, d = check_case(family, 2, 6)
    assert direct_pairs(family, 2, 6) == commuting

print("VERIFY_OK")
for row in rows:
    print(row)
