#!/usr/bin/env python3
"""Exact finite verification of the F4 alternate-Hermitian exception."""

def add(a, b):
    return a ^ b


def mul(a, b):
    # F4 = F2[t]/(t^2+t+1), encoded as a0 + a1*t.
    a0, a1 = a & 1, (a >> 1) & 1
    b0, b1 = b & 1, (b >> 1) & 1
    c0 = (a0 & b0) ^ (a1 & b1)
    c1 = (a0 & b1) ^ (a1 & b0) ^ (a1 & b1)
    return c0 | (c1 << 1)


def star(a):
    return mul(a, a)


def vadd(u, v):
    return (add(u[0], v[0]), add(u[1], v[1]))


def smul(v, a):
    return (mul(v[0], a), mul(v[1], a))


def mat_vec(M, X):
    a, b, x = M
    return (
        add(mul(a, X[0]), mul(star(x), X[1])),
        add(mul(x, X[0]), mul(b, X[1])),
    )


def phi0(M):
    _, _, x = M
    return (x, star(x))


def in_column_space(M, y):
    return any(mat_vec(M, (u, v)) == y for u in range(4) for v in range(4))


# Coordinates are (a,b,x0,x1) over F2, with x=x0+x1*t.
domain = [(a, b, x) for a in range(2) for b in range(2) for x in range(4)]
coords = [(a, b, x & 1, (x >> 1) & 1) for a, b, x in domain]

# All F2-linear maps are determined by the images of four basis vectors.
outputs = [(u, v) for u in range(4) for v in range(4)]
range_compatible = set()
for code in range(16 ** 4):
    t = code
    basis_images = []
    for _ in range(4):
        basis_images.append(outputs[t % 16])
        t //= 16
    values = []
    good = True
    for M, c in zip(domain, coords):
        y = (0, 0)
        for bit, image in zip(c, basis_images):
            if bit:
                y = vadd(y, image)
        if not in_column_space(M, y):
            good = False
            break
        values.append(y)
    if good:
        range_compatible.add(tuple(values))

local = set()
classified = set()
for X0 in range(4):
    for X1 in range(4):
        local_values = tuple(mat_vec(M, (X0, X1)) for M in domain)
        local.add(local_values)
        for alpha in range(4):
            values = tuple(
                vadd(y, smul(phi0(M), alpha))
                for M, y in zip(domain, local_values)
            )
            classified.add(values)

print(f"range-compatible F2-linear maps: {len(range_compatible)}")
print(f"local maps: {len(local)}")
print(f"classified maps: {len(classified)}")
print(f"nonlocal range-compatible maps: {len(range_compatible - local)}")
print(f"unclassified: {len(range_compatible - classified)}")
print(f"classification extras: {len(classified - range_compatible)}")
assert len(range_compatible) == 64
assert len(local) == 16
assert len(classified) == 64
assert len(range_compatible - local) == 48
assert range_compatible == classified
