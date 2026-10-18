"""Exact polynomial verification of the Cartier-rank stratification.

Requires Python 3 standard library only. All arithmetic is in F_7[t].
No finite-field sampling is used to establish the polynomial identities.
"""
from collections import defaultdict
from itertools import permutations
from math import comb

P = 7

def trim(a):
    while a and a[-1] % P == 0:
        a.pop()
    return tuple(x % P for x in a)

def scalar(c):
    return trim([c])

def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])

def neg(a):
    return trim([-x for x in a])

def mul(a, b):
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)

def power(a, n):
    v = scalar(1)
    for _ in range(n):
        v = mul(v, a)
    return v

def evaluate(a, t):
    return sum(c * pow(t, i, P) for i, c in enumerate(a)) % P

def determinant(A):
    n = len(A)
    out = ()
    for v in permutations(range(n)):
        inv = sum(v[i] > v[j] for i in range(n) for j in range(i + 1, n))
        term = scalar(-1 if inv % 2 else 1)
        for i, j in enumerate(v):
            term = mul(term, A[i][j])
        out = add(out, term)
    return out

def rank_mod(A):
    B = [[v % P for v in row] for row in A]
    m = len(B)
    n = len(B[0])
    rank = 0
    for c in range(n):
        pivot = next((i for i in range(rank, m) if B[i][c]), None)
        if pivot is None:
            continue
        B[rank], B[pivot] = B[pivot], B[rank]
        inv = pow(B[rank][c], -1, P)
        B[rank] = [(inv * z) % P for z in B[rank]]
        for i in range(rank + 1, m):
            coeff = B[i][c]
            if coeff:
                B[i] = [(B[i][j] - coeff * B[rank][j]) % P
                        for j in range(n)]
        rank += 1
    return rank

def sparse_product(A, B):
    result = defaultdict(tuple)
    for a, u in A.items():
        for b, v in B.items():
            key = tuple(a[i] + b[i] for i in range(len(a)))
            result[key] = add(result[key], mul(u, v))
    return {k: v for k, v in result.items() if v}

# F_t = y^8-x^7z-xz^7-t(y^2-2xz)^4.
F = {(0, 8, 0): scalar(1),
     (7, 0, 1): scalar(-1),
     (1, 0, 7): scalar(-1)}
for j in range(5):
    monomial = (j, 8 - 2*j, j)
    F[monomial] = add(F.get(monomial, ()),
                      (0, -comb(4, j) * (-2)**j))

F6 = {(0, 0, 0): scalar(1)}
for _ in range(6):
    F6 = sparse_product(F6, F)

basis = [(a, b, 8-a-b) for a in range(1, 8)
         for b in range(1, 8-a) if 8-a-b >= 1]
assert len(basis) == 21
H = [[F6.get(tuple(7*a[k] - b[k] for k in range(3)), ())
      for b in basis] for a in basis]

# Connected components of the undirected graph of nonzero matrix entries.
remaining = set(range(21))
components = []
while remaining:
    origin = min(remaining)
    component = {origin}
    frontier = [origin]
    while frontier:
        x = frontier.pop()
        for y in range(21):
            if y not in component and (H[x][y] or H[y][x]):
                component.add(y)
                frontier.append(y)
    remaining.difference_update(component)
    components.append(sorted(component))

assert sorted(map(len, components)) == [1]*4 + [2]*4 + [3]*3
assert sum(len(c) for c in components) == 21

T = (0, 1)
exception_factor = mul(add(power(T, 2), scalar(-2)), scalar(-1))
for indices in components:
    B = [[H[i][j] for j in indices] for i in indices]
    d = determinant(B)
    expected = T if len(indices) == 1 else mul(power(T, len(indices)), exception_factor)
    assert d == expected, (indices, d, expected)
    if len(indices) > 1:
        # Every nontrivial block drops rank by exactly one at both roots.
        for special in (3, 4):
            Bspecial = [[evaluate(c, special) for c in row] for row in B]
            assert rank_mod(Bspecial) == len(indices) - 1

assert all(not H[i][j] for c in components for i in c
           for j in range(21) if j not in c)
for t, expected_rank in [(0, 0), (2, 21), (3, 14), (4, 14), (5, 21)]:
    numeric = [[evaluate(c, t) for c in row] for row in H]
    assert rank_mod(numeric) == expected_rank

# The order-seven additive quotient is a genus-three hyperelliptic curve
# eta^2 = xi^7 - 2t xi^4 + xi.
f = {(7,): scalar(1), (4,): mul(scalar(-2), T), (1,): scalar(1)}
f3 = {(0,): scalar(1)}
for _ in range(3):
    f3 = sparse_product(f3, f)
Q = [[f3.get((7*i-j,), ()) for j in range(1, 4)]
     for i in range(1, 4)]
expected_diag = [T, add(neg(power(T, 3)), mul(scalar(2), T)), T]
assert Q == [[expected_diag[i] if i == j else () for j in range(3)]
             for i in range(3)]

print('VERIFY_OK: exact coefficient extraction, 21x21 Cartier rank,')
print('          block sizes 1^4,2^4,3^3; determinants t or -t^d(t^2-2);')
print('          ranks 0,14,21; quotient genus-three diagonal calculation')
