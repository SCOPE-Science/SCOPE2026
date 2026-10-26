#!/usr/bin/env python3
"""Independent direct check over F4 using an explicit multiplication table.

Elements 0,1,a,a+1 are encoded 0,1,2,3, with a^2=a+1.  This checker does
not use polynomial reduction or the general finite-field implementation in
verify_point_counts.py.  It directly evaluates each weighted-projective point
and the four partial derivatives for all three displayed equations.
"""
from itertools import product

MUL = (
    (0, 0, 0, 0),
    (0, 1, 2, 3),
    (0, 2, 3, 1),
    (0, 3, 1, 2),
)
ADD = lambda a, b: a ^ b

def m(a, b): return MUL[a][b]
def sq(a): return m(a, a)
def fourth(a): return sq(sq(a))
def summands(*xs):
    out = 0
    for x in xs: out = ADD(out, x)
    return out

def evaluate(kind, x, y, z, w):
    x2, y2, z2 = sq(x), sq(y), sq(z)
    x4, y4, z4 = fourth(x), fourth(y), fourth(z)
    yz = m(y, z)
    if kind == "A1":
        g = summands(y2, yz, z2)
        f = summands(sq(w), m(w, g), m(m(x2, y), z), m(m(x, y), z2), y4, m(y2, z2), z4)
        grad = (m(y, z2), summands(m(w, z), m(x2, z), m(x, z2)), summands(m(w, y), m(x2, y)), g)
    elif kind == "3A1":
        f = summands(sq(w), m(w, x2), x4, m(m(x2, y), z), m(m(x, y2), z), m(m(x, y), z2), m(y2, z2))
        grad = (x2, summands(m(y2, z), m(y, z2)), summands(m(x2, z), m(x, z2)), summands(m(x2, y), m(x, y2)))
    elif kind == "D4":
        g = summands(y2, yz, z2)
        f = summands(sq(w), m(w, g), m(m(x, y2), z), m(m(x, y), z2), y4, m(y2, z2), z4)
        grad = (summands(m(y2, z), m(y, z2)), summands(m(w, z), m(x, z2)), summands(m(w, y), m(x, y2)), g)
    else:
        raise ValueError(kind)
    return f, grad

def main():
    base = [(1, y, z) for y, z in product(range(4), repeat=2)]
    base += [(0, 1, z) for z in range(4)]
    base += [(0, 0, 1)]
    expected = {"A1": (33, 32, 1), "3A1": (37, 34, 3), "D4": (33, 32, 1)}
    for kind in ("A1", "3A1", "D4"):
        total = smooth = singular = 0
        for x, y, z in base:
            for w in range(4):
                f, grad = evaluate(kind, x, y, z, w)
                if f == 0:
                    total += 1
                    if any(grad): smooth += 1
                    else: singular += 1
        actual = (total, smooth, singular)
        assert actual == expected[kind], (kind, actual)
        print(f"{kind}: F4 total/smooth/singular = {actual}")
    print("INDEPENDENT_F4_CHECK_PASS")

if __name__ == "__main__":
    main()
