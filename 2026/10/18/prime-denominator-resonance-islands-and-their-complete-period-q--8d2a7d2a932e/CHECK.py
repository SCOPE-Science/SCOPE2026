#!/usr/bin/env python3
"""Reproducible finite checks for the prime-order piecewise-rotation theorem.

Run: python CHECK.py
Requires only Python's standard library. These checks supplement the proof;
finite tests do not establish the universal theorem.
"""
import itertools
import math

count = 0

def check(test, description):
    global count
    assert test, description
    count += 1


def rotation(z, lam):
    return lam * (z - (1 if z.imag >= 0 else -1))


def polygon_vertices(q, h, c, sign):
    R = h / math.cos(math.pi / q)
    return [c - sign * complex(math.sin(2 * math.pi * (k + 0.5) / q),
                        math.cos(2 * math.pi * (k + 0.5) / q)) * R
            for k in range(q)]


def area(vertices):
    return abs(sum(z.real*w.imag-w.real*z.imag
                   for z, w in zip(vertices, vertices[1:] + vertices[:1])) / 2)

for q in [5, 7, 11]:
    # Cyclotomic reduction modulo Phi_q=1+X+...+X^(q-1).
    for s in itertools.product([-1, 1], repeat=q):
        vanish = all(s[j] == s[-1] for j in range(q-1))
        check(vanish == (len(set(s)) == 1), (q, s))

    for p in range(1, q):
        phi = 2 * math.pi * p / q
        lam = complex(math.cos(phi), math.sin(phi))
        c_plus = lam / (lam-1)
        c_minus = -c_plus
        h = -0.5/math.tan(math.pi * p/q)
        check(abs(c_plus.real - 0.5)<2e-13, (q,p,'center x'))
        check(abs(c_plus.imag - h)<2e-13, (q,p,'center y'))
        if p < q/2:
            check(h < 0, (q,p,'upper-phase obstruction'))
            continue
        check(h > 0, (q,p,'lower-phase existence'))
        for sign, center in [(1, c_plus), (-1, c_minus)]:
            verts = polygon_vertices(q, h, center, sign)
            check(abs(area(verts) - q*h*h*math.tan(math.pi/q))<2e-10,
                  (q,p,sign,'polygon area'))
            for j in range(q):
                z = center + (verts[j]-center)*0.85
                for k in range(q):
                    check(z.imag*sign > 1e-11, (q,p,sign,j,k,'sign sector'))
                    z = rotation(z,lam)
                check(abs(z-(center+(verts[j]-center)*0.85))<2e-10,
                      (q,p,sign,j,'return'))
            for v in verts:
                check(all((center + (lam**k)*(v-center)).imag*sign >= -1e-10
                          for k in range(q)), (q,p,sign,'vertex inequalities'))

print(f'{count} finite checks passed (exact cyclotomic coefficient checks; '
      'floating-point geometry/iteration checks).')
