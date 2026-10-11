#!/usr/bin/env python3
import sympy as s

q = s.sqrt(5)

V = [
    s.Matrix([1, 0]),
    s.Matrix([(q-1)/4, 1]),
    s.Matrix([-(q+1)/4, (q-1)/2]),
    s.Matrix([-(q+1)/4, -(q-1)/2]),
    s.Matrix([(q-1)/4, -1]),
]
opposite = [3, 4, 0, 1, 2]

W = [
    s.Matrix([(q-1)/4, q-2]),
    s.Matrix([(2-q)/2, (3-q)/2]),
    s.Matrix([(q-3)/2, 0]),
    s.Matrix([(2-q)/2, -(3-q)/2]),
    s.Matrix([(q-1)/4, -(q-2)]),
]

def cross(a, b, c):
    return s.simplify(
        (b[0]-a[0])*(c[1]-a[1])
        - (b[1]-a[1])*(c[0]-a[0])
    )

def signed_area(poly):
    return s.simplify(sum(
        poly[i][0]*poly[(i+1)%len(poly)][1]
        - poly[(i+1)%len(poly)][0]*poly[i][1]
        for i in range(len(poly))
    ) / 2)

A = signed_area(V)
assert s.simplify(A - s.Rational(5,2)) == 0

triangles = []
for j in range(5):
    T = [V[j], V[(j+1)%5], V[opposite[j]]]
    assert s.simplify(cross(T[0], T[1], T[2]) - q) == 0
    At = signed_area(T)
    assert s.simplify(At - q/2) == 0
    triangles.append(T)

# The five pentagram diagonals.
diags = [(0,2), (1,3), (2,4), (3,0), (4,1)]
incidence = [
    ((0,2),(4,1)),
    ((0,2),(1,3)),
    ((1,3),(2,4)),
    ((2,4),(3,0)),
    ((3,0),(4,1)),
]
for p, pairs in zip(W, incidence):
    for a,b in pairs:
        assert s.simplify(cross(V[a], V[b], p)) == 0

# Every central vertex lies in every triangle. All possible exact
# half-plane values reduce to a small positive list or zero.
allowed = {
    s.Integer(0),
    s.simplify(5-2*q),
    s.simplify((-5+3*q)/2),
    s.simplify((5-q)/2),
}
for T in triangles:
    for p in W:
        vals = [s.simplify(cross(T[k], T[(k+1)%3], p)) for k in range(3)]
        for val in vals:
            assert val in allowed

# The nonzero allowed values are strictly positive, certified by squaring.
assert 5-2*q > 0
assert -5+3*q > 0
assert 5-q > 0

A5 = signed_area(W)
assert s.simplify(A5 - (35-15*q)/4) == 0
p5 = s.simplify(A5/A)
assert s.simplify(p5 - (7-3*q)/2) == 0

# The pentagram central pentagon has Euclidean linear scale phi^{-2}.
phi = (1+q)/2
lam = (3-q)/2
assert s.simplify(lam - phi**-2) == 0
assert s.simplify(lam**2 - p5) == 0

p3 = s.simplify((q-1)/2 - 2*p5)
p1 = s.simplify(1-p3-p5)
assert s.simplify(p3 - (7*q-15)/2) == 0
assert s.simplify(p1 - (5-2*q)) == 0

assert p1 > 0 and p3 > 0 and p5 > 0
assert s.simplify(p1+p3+p5-1) == 0
mean = s.simplify(p1+3*p3+5*p5)
assert s.simplify(mean-q) == 0
second = s.simplify(p1+9*p3+25*p5)
assert s.simplify(second-(25-8*q)) == 0
variance = s.simplify(second-mean**2)
assert s.simplify(variance-(20-8*q)) == 0

print("VERIFY_OK")
print("area_P =", A)
print("triangle_area =", q/2)
print("p1 =", p1)
print("p3 =", p3)
print("p5 =", p5)
print("mean =", mean)
print("variance =", variance)
