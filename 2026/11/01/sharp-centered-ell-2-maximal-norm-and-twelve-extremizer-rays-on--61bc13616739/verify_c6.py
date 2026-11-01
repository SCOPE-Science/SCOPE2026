"""Exact, self-contained certificate for the centered maximal l2 norm on C6.

Run with Python 3: python verify_c6.py
All asserted comparisons and arithmetic are exact over the integers or rationals.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

N = 6
D = 30
THRESHOLD = F(1517, 1000)
WINNER = (0, 1, 2, 3, 0, 1)
LO = F(15204009213, 10**10)
HI = F(15204009214, 10**10)

# Coefficients are in ascending degree order. P is the nonzero
# characteristic factor of (B.T @ B)/900 for the exceptional matrix.
P = [-48, 2011, -20992, 68847, -73710, 24300]
V = [
    [142, -5617, 51336, -127089, 72900],
    [-71, 2255, -16569, 13041],
    [-71, 2255, -16569, 13041],
    [52, 233, -5346, 4941],
    [-2, 149, -3852, 13041],
    [-122, 3641, -13572, 10125],
]


def evaluate(poly, x):
    z = F(0)
    for c in reversed(poly):
        z = z*x + c
    return z


def mul(A, B):
    out = [F(0)] * (len(A)+len(B)-1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            out[i+j] += a*b
    return out


def remainder(A, modulus):
    a = [F(v) for v in A]
    while len(a) >= len(modulus):
        t = a[-1] / modulus[-1]
        m = len(a)-len(modulus)
        for j, c in enumerate(modulus):
            a[m+j] -= t*c
        assert a[-1] == 0
        a.pop()
    return a


def proven_positive(poly):
    """Mean-value bound rigorously proves poly(lambda)>0 on [LO,HI]."""
    width = HI-LO
    derivative_bound = sum(F(k)*abs(c)*HI**(k-1)
                           for k,c in enumerate(poly) if k)
    return evaluate(poly, LO) > width*derivative_bound


# Shifted P(y+THRESHOLD) has one sign change (negative constant,
# positive coefficients of every higher power); Descartes shows exactly
# one root above THRESHOLD. The rational bracket isolates it.
shift = [sum(F(P[k])*comb(k, j)*THRESHOLD**(k-j)
             for k in range(j,len(P))) for j in range(len(P))]
assert shift[0] < 0 and all(a > 0 for a in shift[1:])
assert THRESHOLD < LO < HI
assert evaluate(P, LO) < 0 < evaluate(P, HI)

# Four distinct centered balls of radii 0,1,2,3 at each vertex.
ROWS = []
for i in range(N):
    rr = []
    for rad in range(4):
        indices = [j for j in range(N)
                   if min((i-j)%N, (j-i)%N) <= rad]
        assert len(indices) in (1,3,5,6)
        rr.append(tuple(D//len(indices) if j in indices else 0
                        for j in range(N)))
    ROWS.append(tuple(rr))


def gram(rs):
    B = [ROWS[i][rs[i]] for i in range(N)]
    return [[sum(B[k][i]*B[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]


def positive_definite_integer(A):
    """Exact Sylvester test using fraction-free leading principal minors."""
    T = [row[:] for row in A]
    prev = 1
    for k in range(N-1):
        pivot = T[k][k]
        if pivot <= 0:
            return False
        for i in range(k+1,N):
            for j in range(i,N):
                numerator = pivot*T[i][j] - T[i][k]*T[k][j]
                assert numerator % prev == 0
                T[i][j] = numerator // prev
                T[j][i] = T[i][j]
        prev = pivot
    return T[N-1][N-1] > 0


exceptions = []
pass_count = 0
for rs in product(range(4), repeat=N):
    Q = gram(rs)
    # 13653*I - 10*Q = 9000*(THRESHOLD*I - A.T*A).
    T = [[13653*int(i == j) - 10*Q[i][j]
          for j in range(N)] for i in range(N)]
    if positive_definite_integer(T):
        pass_count += 1
    else:
        exceptions.append(rs)
assert pass_count == 4084 and len(exceptions) == 12

# Every exceptional selection is a dihedral image of WINNER.
permutations = {tuple((k + sign*i)%N for i in range(N))
                for sign in (-1,1) for k in range(N)}
assert len(permutations) == 12
orbit = {tuple(WINNER[p.index(j)] for j in range(N))
         for p in permutations}
assert len(orbit) == 12 and set(exceptions) == orbit

Q = gram(WINNER)
assert Q == [
 [1161,161,161,61,161,125],
 [161,161,161,61,61,25],
 [161,161,161,61,61,25],
 [61,61,61,61,61,25],
 [161,61,61,61,1061,125],
 [125,25,25,25,125,125]]

# Faddeev--LeVerrier recovers the exact characteristic polynomial of Q.
def matrix_mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]

S = [[int(i==j) for j in range(N)] for i in range(N)]
coefs = [1]
for k in range(1,N+1):
    U = matrix_mul(Q, S)
    tr = sum(U[i][i] for i in range(N))
    assert tr%k == 0
    ck = -tr//k
    coefs.append(ck)
    S = [[U[i][j] + ck*int(i==j) for j in range(N)]
         for i in range(N)]
assert coefs == [1,-2730,2294900,-629760000,54297000000,
                 -1166400000000,0]
# In particular det(xI-Q/900)=x*P(x)/24300.
assert [F(coefs[i],900**i) for i in range(7)] == [
    F(P[5],24300),F(P[4],24300),F(P[3],24300),
    F(P[2],24300),F(P[1],24300),F(P[0],24300),F(0)]

# Polynomial vector V(lambda) is a strictly positive eigenvector.
for i in range(N):
    qv = [F(0)] * 6
    for j in range(N):
        for k,c in enumerate(V[j]):
            qv[k] += Q[i][j] * c
    for k,c in enumerate(V[i]):
        qv[k+1] -= 900*c
    assert all(z==0 for z in remainder(qv,P))
    assert proven_positive(V[i])

# Strict pointwise preference: at V(lambda) the chosen ball radius
# at each vertex uniquely maximizes all four possible averages.
strict_checks = 0
for i in range(N):
    for r in range(4):
        if r == WINNER[i]:
            continue
        diff = [F(0)] * 5
        for j in range(N):
            weight = ROWS[i][WINNER[i]][j] - ROWS[i][r][j]
            for k,c in enumerate(V[j]):
                diff[k] += weight*c
        assert proven_positive(diff)
        strict_checks += 1
assert strict_checks == 18

print('CERTIFICATE_OK selections=4096 strict=4084 exceptional=12'
      ' characteristic_quintic=exact root_isolation=exact'
      ' eigenvector=exact active_selection_tests=18')
