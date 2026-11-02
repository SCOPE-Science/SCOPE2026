"""Exact cyclotomic characteristic-polynomial check for a 9-point Fourier block.

Uses integer arithmetic only. It verifies the three Gram characteristic
polynomials and elementary orbit counts; no numerical solver is required.
"""
from itertools import product
from math import gcd

K = 6
ZERO = (0,) * K
ONE = (1, 0, 0, 0, 0, 0)

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def neg(a):
    return tuple(-x for x in a)

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    arr = [0] * 11
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            arr[i + j] += u * v
    # Cyclotomic relation: z^6+z^3+1=0.
    for j in range(10, 5, -1):
        t = arr[j]
        arr[j] = 0
        arr[j - 3] -= t
        arr[j - 6] -= t
    return tuple(arr[:6])

def scale(a, k):
    return tuple(k * x for x in a)

def divide_exact(a, k):
    assert all(x % k == 0 for x in a)
    return tuple(x // k for x in a)

def power_z(k):
    k = k % 9
    a = ONE
    z = (0, 1, 0, 0, 0, 0)
    for _ in range(k):
        a = mul(a, z)
    return a

Z = [power_z(k) for k in range(9)]
assert add(add(ONE, Z[3]), Z[6]) == ZERO
assert Z[9 - 1] == power_z(-1)

def mm(A, B):
    n = len(A)
    return [[sum_ring(mul(A[i][k], B[k][j]) for k in range(n))
             for j in range(n)] for i in range(n)]

def sum_ring(items):
    a = ZERO
    for v in items:
        a = add(a, v)
    return a

def gram_unscaled(X, Y):
    return [[sum_ring(Z[((xj - xi) * y) % 9] for y in Y)
             for xj in X] for xi in X]

def characteristic(A):
    n = len(A)
    B = A
    traces = []
    for i in range(1, n + 1):
        traces.append(sum_ring(B[j][j] for j in range(n)))
        if i != n:
            B = mm(B, A)
    out = [ONE]
    for k in range(1, n + 1):
        numerator = sum_ring(mul(out[k-j], traces[j-1])
                             for j in range(1, k+1))
        out.append(neg(divide_exact(numerator, k)))
    return out

X = (0, 1, 3, 4)
Y_cases = ((0, 1, 3, 4), (0, 1, 3, 7), (0, 1, 4, 6))
for j, Y in zip((1, 2, 4), Y_cases):
    coeffs = characteristic(gram_unscaled(X, Y))
    expected = [ONE, scale(ONE,-16),
                sub(scale(ONE,80), add(Z[j],Z[-j])),
                scale(ONE,-144), scale(ONE,81)]
    assert coeffs == expected, (j,coeffs,expected)

def maximal_porosity_sets():
    out = []
    for missing in range(3):
        residues = [k for k in range(3) if k != missing]
        for absent in product(range(3), repeat=2):
            out.append(tuple(sorted(k + 3*t for k, x in zip(residues, absent)
                                    for t in range(3) if t != x)))
    return set(out)
S = maximal_porosity_sets()
assert len(S) == 27
assert X in S
units = (1,2,4,5,7,8)
assert {tuple(sorted((u*x+a)%9 for x in X))
        for u in units for a in range(9)} == S
remaining = set(S)
orbits = []
while remaining:
    rep = min(remaining)
    orbit = {tuple(sorted((x+a)%9 for x in rep)) for a in range(9)}
    assert len(orbit) == 9
    assert orbit <= remaining
    orbits.append(orbit)
    remaining -= orbit
assert len(orbits) == 3
assert all(sum(Y in O for O in orbits)==1 for Y in Y_cases)
assert sum(len(O) for O in orbits)==27
print('PASS: 3 exact cyclotomic characteristic polynomials; 27 maximal supports; 3 translation orbits')
