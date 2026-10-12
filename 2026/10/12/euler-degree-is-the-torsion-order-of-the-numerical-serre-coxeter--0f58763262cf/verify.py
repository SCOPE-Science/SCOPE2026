from itertools import combinations
from math import gcd

REPS = [
    (22, (4,4,7,7,3,20), (1,1,22,0)),
    (40, (5,5,5,5,3,18), (1,1,40,0)),
    (54, (4,5,5,4,4,11), (1,3,18,0)),
    (64, (4,4,4,4,6,6), (2,2,16,0)),
    (72, (3,6,3,6,7,7), (1,1,72,0)),
]

def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(c, A):
    return [[c*x for x in row] for row in A]

def transpose(A):
    return [list(x) for x in zip(*A)]

def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def det(M):
    n = len(M)
    if n == 0:
        return 1
    if n == 1:
        return M[0][0]
    total = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in M[1:]]
        total += (-1)**j * M[0][j] * det(minor)
    return total

def minor(M, rows, cols):
    return det([[M[i][j] for j in cols] for i in rows])

def determinant_divisors(M):
    n = len(M)
    ds = []
    for k in range(1, n+1):
        g = 0
        for rows in combinations(range(n), k):
            for cols in combinations(range(n), k):
                g = gcd(g, abs(minor(M, rows, cols)))
        ds.append(g)
    return ds

def smith_from_divisors(ds):
    rank = sum(d != 0 for d in ds)
    out = []
    prev = 1
    for k in range(rank):
        out.append(ds[k] // prev)
        prev = ds[k]
    out.extend([0] * (len(ds) - rank))
    return tuple(out)

def unitriangular_inverse(A):
    n = len(A)
    I = eye(n)
    N = sub(A, I)
    # For strictly upper triangular 4x4 N, N^4=0:
    N2 = mul(N, N)
    N3 = mul(N2, N)
    inv = add(sub(I, N), sub(N2, N3))
    assert mul(A, inv) == I
    assert mul(inv, A) == I
    return inv

def make_A(params):
    a,b,c,d,e,f = params
    return [
        [1,a,e,d],
        [0,1,b,f],
        [0,0,1,c],
        [0,0,0,1],
    ]

for D, params, expected_snf in REPS:
    A = make_A(params)
    AT = transpose(A)
    B = add(A, AT)
    Ainv = unitriangular_inverse(A)
    AinvT = transpose(Ainv)
    T = scale(-1, mul(AinvT, A))
    M = sub(T, eye(4))
    assert M == scale(-1, mul(AinvT, B))

    dB = determinant_divisors(B)
    dM = determinant_divisors(M)
    sB = smith_from_divisors(dB)
    sM = smith_from_divisors(dM)

    assert dB == dM
    assert sB == expected_snf
    assert sM == expected_snf
    assert dB[2] == D
    torsion_order = 1
    for x in expected_snf:
        if x:
            torsion_order *= x
    assert torsion_order == D

    print(f"D={D} determinant_divisors={dB} smith={list(sB)} torsion_order={torsion_order}")

print("identity_T_minus_I=ok")
print("all_five_smith_forms=ok")
print("torsion_order_equals_euler_degree=ok")
print("VERIFY_OK")
