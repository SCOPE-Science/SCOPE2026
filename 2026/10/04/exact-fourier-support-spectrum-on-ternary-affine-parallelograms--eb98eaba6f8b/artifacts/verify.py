from fractions import Fraction as F
from itertools import combinations

class Qw:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    def __add__(self, other):
        other = co(other)
        return Qw(self.a + other.a, self.b + other.b)
    __radd__ = __add__
    def __neg__(self):
        return Qw(-self.a, -self.b)
    def __sub__(self, other):
        return self + (-co(other))
    def __rsub__(self, other):
        return co(other) - self
    def __mul__(self, other):
        other = co(other)
        a, b, c, d = self.a, self.b, other.a, other.b
        return Qw(a*c - b*d, a*d + b*c - b*d)
    __rmul__ = __mul__
    def norm(self):
        return self.a*self.a - self.a*self.b + self.b*self.b
    def inv(self):
        if not self:
            raise ZeroDivisionError
        n = self.norm()
        return Qw((self.a-self.b)/n, -self.b/n)
    def __truediv__(self, other):
        return self * co(other).inv()
    def __eq__(self, other):
        other = co(other)
        return self.a == other.a and self.b == other.b
    def __bool__(self):
        return self.a != 0 or self.b != 0

def co(x):
    return x if isinstance(x, Qw) else Qw(x)

ONE, W = Qw(1), Qw(0, 1)
W2 = W*W
ROOTS = [ONE, W, W2]
assert W2 == Qw(-1, -1) and W*W2 == ONE
GRID = [(x, y) for x in ROOTS for y in ROOTS]

def eval_poly(coeff, x, y):
    a, b, c, d = coeff
    return a + b*x + c*y + d*x*y

WITNESSES = {
    0: (1, 1, 1, 1),
    1: (-4, -3, 3, 4),
    2: (-4, -3, -3, 1),
    3: (1, 1, -1, -1),
    5: (1, -1, -1, 1),
}
for expected_zeros, raw in WITNESSES.items():
    coeff = tuple(Qw(v) for v in raw)
    assert all(coeff)
    zeros = [pt for pt in GRID if not eval_poly(coeff, *pt)]
    assert len(zeros) == expected_zeros, (expected_zeros, zeros)

def rank_and_null(rows):
    A = [[co(v) for v in row] for row in rows]
    m, n = len(A), len(A[0])
    pivots, r = [], 0
    for col in range(n):
        pivot = next((i for i in range(r, m) if A[i][col]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = A[r][col].inv()
        A[r] = [v*inv for v in A[r]]
        for i in range(m):
            if i != r and A[i][col]:
                factor = A[i][col]
                A[i] = [A[i][j] - factor*A[r][j] for j in range(n)]
        pivots.append(col)
        r += 1
        if r == m:
            break
    if r == n:
        return r, None
    free = next(c for c in range(n) if c not in pivots)
    x = [Qw(0) for _ in range(n)]
    x[free] = Qw(1)
    for i in range(r-1, -1, -1):
        pc = pivots[i]
        s = Qw(0)
        for j in range(pc+1, n):
            s += A[i][j]*x[j]
        x[pc] = -s
    return r, x

rows = [[ONE, x, y, x*y] for x, y in GRID]
count = 0
rank3_all_nonzero = 0
for idxs in combinations(range(9), 4):
    count += 1
    rank, null = rank_and_null([rows[i] for i in idxs])
    assert rank >= 3
    if rank == 3 and all(null):
        rank3_all_nonzero += 1
        zeros = [i for i, (x, y) in enumerate(GRID) if not eval_poly(null, x, y)]
        assert len(zeros) == 5, (idxs, zeros)
assert count == 126
print(f"four_subsets={count} rank3_all_nonzero={rank3_all_nonzero} examples={len(WITNESSES)}")
print("VERIFY_OK")
