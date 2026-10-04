#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations

class Q2:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)
    def __add__(self, other):
        other = q(other)
        return Q2(self.a + other.a, self.b + other.b)
    __radd__ = __add__
    def __neg__(self):
        return Q2(-self.a, -self.b)
    def __sub__(self, other):
        return self + (-q(other))
    def __rsub__(self, other):
        return q(other) - self
    def __mul__(self, other):
        other = q(other)
        return Q2(self.a*other.a + 2*self.b*other.b,
                  self.a*other.b + self.b*other.a)
    __rmul__ = __mul__
    def inv(self):
        den = self.a*self.a - 2*self.b*self.b
        if den == 0:
            raise ZeroDivisionError
        return Q2(self.a/den, -self.b/den)
    def __truediv__(self, other):
        return self * q(other).inv()
    def __rtruediv__(self, other):
        return q(other) / self
    def __eq__(self, other):
        other = q(other)
        return self.a == other.a and self.b == other.b
    def sign(self):
        a, b = self.a, self.b
        if a == 0 and b == 0:
            return 0
        if b == 0:
            return 1 if a > 0 else -1
        if a == 0:
            return 1 if b > 0 else -1
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        if a > 0:  # b < 0: compare a with -b sqrt(2)
            d = a*a - 2*b*b
            return 1 if d > 0 else (-1 if d < 0 else 0)
        d = 2*b*b - a*a  # a < 0 < b
        return 1 if d > 0 else (-1 if d < 0 else 0)
    def __lt__(self, other):
        return (self - q(other)).sign() < 0
    def __le__(self, other):
        return (self - q(other)).sign() <= 0
    def __repr__(self):
        return f"({self.a})+({self.b})*sqrt(2)"

def q(x):
    return x if isinstance(x, Q2) else Q2(x, 0)

S = Q2(0, 1)
H = S / 2
FACETS = [
    (Q2(1), Q2(0)), (Q2(-1), Q2(0)),
    (Q2(0), Q2(1)), (Q2(0), Q2(-1)),
    (H, H), (H, -H), (-H, H), (-H, -H),
]


def rref(matrix):
    M = [[q(x) for x in row] for row in matrix]
    m, n = len(M), len(M[0])
    pivots, r = [], 0
    for c in range(n-1):
        pivot = next((i for i in range(r, m) if M[i][c] != 0), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        z = M[r][c]
        M[r] = [x/z for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                z = M[i][c]
                M[i] = [M[i][j] - z*M[r][j] for j in range(n)]
        pivots.append(c)
        r += 1
        if r == m:
            break
    for row in M:
        if all(row[c] == 0 for c in range(n-1)) and row[-1] != 0:
            return None, None
    return M, pivots


def eqrow(facet, kind):
    a, b = facet
    if kind == "x":
        co = [a, b, Q2(), Q2()]
    elif kind == "y":
        co = [Q2(), Q2(), a, b]
    else:
        co = [a, b, -a, -b]
    return co + [Q2(1)]


def eadd(u, v): return (u[0]+v[0], u[1]+v[1])
def esub(u, v): return (u[0]-v[0], u[1]-v[1])
def escale(c, u): return (c*u[0], c*u[1])
def evale(u, t): return u[0] + u[1]*t

def fexpr(facet, u, v):
    return eadd(escale(facet[0], u), escale(facet[1], v))


def parameterize(i, j, k):
    M, pivots = rref([eqrow(FACETS[i], "x"),
                      eqrow(FACETS[j], "y"),
                      eqrow(FACETS[k], "d")])
    if M is None:
        return None
    free = [c for c in range(4) if c not in pivots]
    if len(free) != 1:
        raise AssertionError("unexpected rank")
    qcol = free[0]
    ex = [None]*4
    ex[qcol] = (Q2(0), Q2(1))
    for rr, col in enumerate(pivots):
        ex[col] = (M[rr][-1], -M[rr][qcol])
    return ex


def branch_min(i, j, k):
    ex = parameterize(i, j, k)
    if ex is None:
        return None
    x = (ex[0], ex[1])
    y = (ex[2], ex[3])
    d = (esub(ex[0], ex[2]), esub(ex[1], ex[3]))
    lo = hi = None
    for z in (x, y, d):
        for facet in FACETS:
            e = fexpr(facet, *z)  # e(t) <= 1
            A, B = e[1], e[0]-1
            if A == 0:
                if B.sign() > 0:
                    return None
            else:
                bd = (-B)/A
                if A.sign() > 0:
                    hi = bd if hi is None or bd < hi else hi
                else:
                    lo = bd if lo is None or lo < bd else lo
    if lo is None or hi is None or hi < lo:
        return None

    sm = (eadd(ex[0], ex[2]), eadd(ex[1], ex[3]))
    lines = [fexpr(facet, *sm) for facet in FACETS]
    candidates = [lo, hi]
    for a, b in combinations(range(8), 2):
        diff = esub(lines[a], lines[b])
        if diff[1] != 0:
            t = (-diff[0])/diff[1]
            if lo <= t <= hi:
                candidates.append(t)
    best = None
    best_t = None
    for t in candidates:
        value = max(evale(line, t) for line in lines)
        if best is None or value < best:
            best, best_t = value, t
    return best, best_t, ex


def norm_pair(u, v):
    vals = [a*u+b*v for a,b in FACETS]
    return max(vals)


def main():
    inconsistent = 0
    feasible = 0
    global_min = None
    equality_branches = 0
    for i, j, k in product(range(8), repeat=3):
        ex = parameterize(i, j, k)
        if ex is None:
            inconsistent += 1
            continue
        bm = branch_min(i, j, k)
        if bm is None:
            continue
        feasible += 1
        value = bm[0]
        if global_min is None or value < global_min:
            global_min = value
            equality_branches = 1
        elif value == global_min:
            equality_branches += 1

    target = Q2(3, -1)
    assert inconsistent == 32
    assert feasible == 48
    assert global_min == target
    assert equality_branches == 32

    # Explicit witness.
    x = (Q2(1), Q2(-3, 2))                 # (1, 2 sqrt(2)-3)
    y = (Q2(2, -1), Q2(-2, 2))            # (2-sqrt(2), 2 sqrt(2)-2)
    d = (x[0]-y[0], x[1]-y[1])
    sm = (x[0]+y[0], x[1]+y[1])
    assert norm_pair(*x) == 1
    assert norm_pair(*y) == 1
    assert norm_pair(*d) == 1
    assert norm_pair(*sm) == target

    # rho = 1 - target^2/2 = 3 sqrt(2) - 9/2.
    rho = Q2(1) - target*target/2
    assert rho == Q2(Fraction(-9,2), 3)

    print("ACTIVE_TRIPLES=512")
    print("INCONSISTENT_TRIPLES=32")
    print("FEASIBLE_BRANCHES=48")
    print("EQUALITY_BRANCHES=32")
    print("MIN_SUM_NORM=3-sqrt(2)")
    print("RHO_A_AT_1=3*sqrt(2)-9/2")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
