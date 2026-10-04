from itertools import product
from math import gcd

def mat_mul(A, B, p):
    n = len(A)
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(n)) % p for j in range(n))
        for i in range(n)
    )

def mat_vec(A, v, p):
    n = len(A)
    return tuple(sum(A[i][j] * v[j] for j in range(n)) % p for i in range(n))

def eye(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))

def mat_pow(A, e, p):
    R = eye(len(A))
    while e:
        if e & 1:
            R = mat_mul(R, A, p)
        A = mat_mul(A, A, p)
        e >>= 1
    return R

def vadd(v, w, p):
    return tuple((a + b) % p for a, b in zip(v, w))

def vmul_scalar(a, v, p):
    return tuple((a*x) % p for x in v)

def zero(r):
    return (0,) * r

def semidirect_mul(g, h, p, q, A):
    v, i = g
    w, j = h
    return (vadd(v, mat_vec(mat_pow(A, i, p), w, p), p), (i + j) % q)

def element_order(g, p, q, A):
    r = len(g[0])
    e = (zero(r), 0)
    x = e
    for k in range(1, p**r * q + 1):
        x = semidirect_mul(x, g, p, q, A)
        if x == e:
            return k
    raise AssertionError("order bound failed")

def check_case(p, r, q, A):
    I = eye(r)
    assert mat_pow(A, q, p) == I
    for j in range(1, q):
        Aj = mat_pow(A, j, p)
        assert Aj != I
        for v in product(range(p), repeat=r):
            if v == zero(r):
                continue
            assert mat_vec(Aj, v, p) != v, (p, r, q, j, v)

    elems = [
        (tuple(v), j)
        for v in product(range(p), repeat=r)
        for j in range(q)
    ]

    counts = {}
    psi = 0
    for g in elems:
        o = element_order(g, p, q, A)
        counts[o] = counts.get(o, 0) + 1
        psi += o

    assert counts.get(1, 0) == 1
    assert counts.get(p, 0) == p**r - 1
    assert counts.get(q, 0) == p**r * (q - 1)
    assert sum(counts.values()) == p**r * q

    D = p**(r + 1) - p + 1
    expected = D + p**r * q * (q - 1)
    assert psi == expected, (p, r, q, psi, expected)
    assert (p**r - 1) % q == 0
    assert gcd(D, psi) == gcd(D, q - 1)
    assert gcd(D, psi) < D
    assert psi % D != 0

# A4: irreducible order-3 action on F_2^2.
A_223 = ((0, 1), (1, 1))

# Order-7 irreducible action on F_2^3, companion matrix of x^3+x+1.
A_237 = (
    (0, 0, 1),
    (1, 0, 1),
    (0, 1, 0),
)

# Scalar actions.
A_332 = ((2, 0), (0, 2))       # -I over F_3, order 2
A_523 = ((0, 4), (1, 4))       # x^2+x+1 over F_5, order 3
A_723 = ((2, 0), (0, 2))       # scalar 2 over F_7, order 3

for case in [
    (2, 2, 3, A_223),
    (2, 3, 7, A_237),
    (3, 2, 2, A_332),
    (5, 2, 3, A_523),
    (7, 2, 3, A_723),
]:
    check_case(*case)

print("VERIFY_OK")
