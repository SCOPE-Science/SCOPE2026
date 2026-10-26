#!/usr/bin/env python3
"""Independent quotient-ring certificate over the quadratic base field."""
p = 41
q = p * p
lam = (2, 16)
zero = (0, 0)
one = (1, 0)

def add(x, y):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

def mul(x, y):
    return ((x[0] * y[0] + 3 * x[1] * y[1]) % p,
            (x[0] * y[1] + x[1] * y[0]) % p)

def neg(x):
    return ((-x[0]) % p, (-x[1]) % p)

def power(x, n):
    out = one
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n //= 2
    return out

def multiply_polynomials(a, b):
    temp = [zero for _ in range(2 * p - 1)]
    for i, x in enumerate(a):
        if x == zero:
            continue
        for j, y in enumerate(b):
            if y != zero:
                temp[i+j] = add(temp[i+j], mul(x, y))
    # Reduce by Z^41 + Z + lambda.
    for k in range(2 * p - 2, p - 1, -1):
        v = temp[k]
        if v != zero:
            temp[k-p] = add(temp[k-p], neg(mul(v, lam)))
            temp[k-p+1] = add(temp[k-p+1], neg(v))
    return temp[:p]

def power_of_z(n):
    out = [one] + [zero] * (p - 1)
    z = [zero, one] + [zero] * (p - 2)
    while n:
        if n & 1:
            out = multiply_polynomials(out, z)
        z = multiply_polynomials(z, z)
        n //= 2
    return out

assert power((3, 0), 20) == (40, 0)
assert q - 1 == 1680
for ell in (2, 3, 5, 7):
    assert power(lam, (q-1)//ell) != one
assert pow(q, p, 83) == 1
N = q**p - 1
assert N % 83 == 0
assert power_of_z(N//83) == [one] + [zero] * (p-1)
print('CERTIFICATE_OK independent_extension_ring p=41 degree=41 divisor=83')
