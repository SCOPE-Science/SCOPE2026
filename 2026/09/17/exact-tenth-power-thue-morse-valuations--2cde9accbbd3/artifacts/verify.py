
from math import comb

def v2(n):
    if n == 0:
        raise ValueError("v2(0)")
    n = abs(n)
    return (n & -n).bit_length() - 1

def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c

def factor_poly(step, power):
    p = [0] * (step * power + 1)
    for j in range(power + 1):
        p[step*j] = (-1)**j * comb(power, j)
    return p

# H(x)=(1-x)^10(1-x^2)^10(1-x^4)^10.
H = [1]
for step in (1, 2, 4):
    H = poly_mul(H, factor_poly(step, 10))

b = [0, 1, 0, 2, 0, 1, 0]
section_data = []
for r in range(7):
    P = [H[k] for k in range(r, len(H), 8)]
    while P and P[-1] == 0:
        P.pop()
    scale = 1 << b[r]
    assert all(c % scale == 0 for c in P)
    Q = [c // scale for c in P]
    # Q(z) == (1-z)^8 (mod 2) == 1+z^8.
    assert len(Q) == 9
    assert [c & 1 for c in Q] == [1,0,0,0,0,0,0,0,1]
    section_data.append(Q)

def mat_zero(n):
    return [[0] * n for _ in range(n)]

def mat_eye(n):
    M = mat_zero(n)
    for i in range(n):
        M[i][i] = 1
    return M

def mat_add(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))]
            for i in range(len(X))]

def mat_scale(c, X):
    return [[c*x for x in row] for row in X]

def mat_mul(X, Y):
    n, mid, p = len(X), len(Y), len(Y[0])
    Z = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(mid):
            if X[i][k]:
                xik = X[i][k]
                for j in range(p):
                    Z[i][j] += xik * Y[k][j]
    return Z

def mat_pow(A, n):
    R = mat_eye(len(A))
    B = A
    while n:
        if n & 1:
            R = mat_mul(R, B)
        B = mat_mul(B, B)
        n >>= 1
    return R

# Dyadic recurrence matrix for m=10:
# V_n=(t_10(n-1),...,t_10(n-9))^T and V_{2n}=A V_n.
A = []
for i in range(1, 10):
    row = []
    for j in range(1, 10):
        k = 2*j - i
        row.append(((-1)**i) * comb(10, k) if 0 <= k <= 10 else 0)
    A.append(row)

# Characteristic polynomial:
# x^9 + c1 x^8 + ... + c9.
char_coeff = [
    1, 2, -19680, -34560, 76783616, 298975232,
    -64718110720, 85899345920, 8658654068736, 35184372088832
]
powers = [mat_eye(9)]
for _ in range(9):
    powers.append(mat_mul(powers[-1], A))
CH = mat_zero(9)
for idx, c in enumerate(char_coeff):
    power = 9 - idx
    CH = mat_add(CH, mat_scale(c, powers[power]))
assert all(x == 0 for row in CH for x in row)

d = [6, 1, 2, 1, 3, 1, 2, 1, 6]
J = [[1 if j in (0,8) else 0 for j in range(9)] for _ in range(9)]

# R_s = 2^{-s} D^{-1} A^{s+4}.  Verify the finite bases
# needed for the Cayley-Hamilton induction.
for s in range(9):
    P = mat_pow(A, s+4)
    R = []
    for i in range(9):
        den = 1 << (s + d[i])
        assert all(x % den == 0 for x in P[i])
        R.append([x // den for x in P[i]])
    assert [[x & 1 for x in row] for row in R] == J

# Normalized Cayley-Hamilton recurrence coefficients.
rec = [
    -1,
    19680 // 4,
    34560 // 8,
    -76783616 // 16,
    -298975232 // 32,
    64718110720 // 64,
    -85899345920 // 128,
    -8658654068736 // 256,
    -35184372088832 // 512,
]
assert all(isinstance(x, int) for x in rec)
assert all((x & 1) == 0 for x in rec[1:])

# Numerical sanity check of the final theorem.
N = 100000
t = [0] * (N + 1)
t[0] = 1
for n in range(1, N + 1):
    q = n // 2
    if n % 2 == 0:
        t[n] = sum(comb(10, 2*j) * (t[q-j] if q-j >= 0 else 0)
                   for j in range(6))
    else:
        t[n] = -sum(comb(10, 2*j+1) * (t[q-j] if q-j >= 0 else 0)
                    for j in range(5))

for n, tn in enumerate(t):
    rhs = v2(comb(n+9, 9)) + (2 if n % 8 == 7 else 0)
    assert tn != 0
    assert v2(tn) == rhs

print("section congruences: PASS")
print("Cayley-Hamilton identity: PASS")
print("normalized matrix bases R_0,...,R_8: PASS")
print("normalized recurrence parity condition: PASS")
print("valuation formula checked for 0 <= n <= 100000: PASS")
