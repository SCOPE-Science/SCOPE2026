#!/usr/bin/env python3
"""Exact arithmetic checks for the characteristic-three cyclic cubic fourfold."""
from itertools import product

P = 3

def rank_mod3(M):
    m = [list(map(lambda x: x % P, row)) for row in M]
    r = 0
    for col in range(len(m[0])):
        pivot = next((i for i in range(r, len(m)) if m[i][col]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        inv = pow(m[r][col], -1, P)
        m[r] = [(v * inv) % P for v in m[r]]
        for i in range(len(m)):
            if i != r:
                fac = m[i][col]
                m[i] = [(v - fac * w) % P for v, w in zip(m[i], m[r])]
        r += 1
    return r

# The homogeneous cyclic equation is sum_{i=0}^5 X_i^2 X_{i+1}.
# Its characteristic-three partials are Xi-1^2 - Xi*Xi+1.
# If any Xi vanishes, successive partials force all variables to vanish.
# On X0=1, the first four affine partials solve coordinates in terms of t=X1.
exponents = [0, 1, -1, 3, -5, 11]
assert all((2 * exponents[(i - 1) % 6] == exponents[i] + exponents[(i + 1) % 6]) for i in range(1, 5))
# Full partials vanish modulo (t^21-1), including the one for X0.
for i in range(6):
    delta = 2 * exponents[(i - 1) % 6] - exponents[i] - exponents[(i + 1) % 6]
    assert delta % 21 == 0, (i, delta)
terms = [2 * exponents[i] + exponents[(i + 1) % 6] for i in range(6)]
assert terms == [1, 1, 1, 1, 1, 22]
# The affine equation reduces to (5t+t^22) and is 6t=0 after t^21=1.
assert (5 + 1) % 3 == 0
# In characteristic 3, (t^7-1)^3=t^21-1 by freshman's dream.
assert all((pow(3, i, 7) != 1 for i in range(1, 6)))
assert pow(3, 6, 7) == 1

# Affine Hessian at P=[1:1:1:1:1:1] is twice the tridiagonal (1,1,1).
H = [[2 * (int(i == j) + int(abs(i - j) == 1)) for j in range(5)] for i in range(5)]
assert rank_mod3(H) == 4
v = [2, 1, 0, 2, 1]
assert all(sum(a * b for a, b in zip(row, v)) % 3 == 0 for row in H)
# Cubic homogeneous part of F(1, 1+u1,...,1+u5) is sum_i u_i^2 u_{i+1}.
cubic = sum(v[i] ** 2 * v[i + 1] for i in range(4)) % 3
assert cubic == 2

# Independent prime-field projective singular-point enumeration, finite check only.
# Every zero-free tuple normalized X0=1 has each coordinate in {1,2};
# exactly one of the geometric singularities is F3-rational.
zeros = []
for coords in product([1, 2], repeat=5):
    x = (1,) + coords
    f = sum(x[i] ** 2 * x[(i + 1) % 6] for i in range(6)) % 3
    deriv = [((x[(i - 1) % 6] ** 2) - x[i] * x[(i + 1) % 6]) % 3 for i in range(6)]
    if f == 0 and all(d == 0 for d in deriv):
        zeros.append(x)
assert zeros == [(1, 1, 1, 1, 1, 1)], zeros
print('VERIFY_OK: Laurent elimination, characteristic-three factorization, Hessian corank, cubic kernel, Frobenius, and F3 points')
