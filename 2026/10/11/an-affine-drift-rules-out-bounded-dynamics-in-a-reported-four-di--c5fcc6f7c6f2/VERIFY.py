#!/usr/bin/env python3
"""Exact coefficient check for the affine drift identity in the 4D Sprott-S extension."""
from fractions import Fraction as Q

# Variables are ordered (x, y, z, w, a, b).
N = 6

def mono(*e):
    assert len(e) == N
    return tuple(e)

def add(*ps):
    out = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, Q(0)) + c
            if out[m] == 0:
                del out[m]
    return out

def scale(p, c):
    c = Q(c)
    return {m: c*v for m, v in p.items() if c*v}

def mul(p, q):
    out = {}
    for m, c in p.items():
        for n, d in q.items():
            k = tuple(i+j for i, j in zip(m, n))
            out[k] = out.get(k, Q(0)) + c*d
            if out[k] == 0:
                del out[k]
    return out

ONE = {mono(0,0,0,0,0,0): Q(1)}
X   = {mono(1,0,0,0,0,0): Q(1)}
Y   = {mono(0,1,0,0,0,0): Q(1)}
B   = {mono(0,0,0,0,0,1): Q(1)}

# Only dx, dz, dw enter L_F because F_y = F_a = 0.
dx = add(scale(X, -1), scale(Y, -4))
dz = add(ONE, X)
dw = scale(mul(B, Y), -1)

# F_x = -b/4, F_z = -b/4, F_w = 1.
lie = add(scale(mul(B, dx), Q(-1,4)),
          scale(mul(B, dz), Q(-1,4)),
          dw)
expected = scale(B, Q(-1,4))

assert lie == expected, (lie, expected)
print("VERIFY_OK")
