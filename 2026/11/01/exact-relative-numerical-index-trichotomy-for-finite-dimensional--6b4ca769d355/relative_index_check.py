"""Supplementary finite-dimensional checks for the relative numerical-index theorem.

Only the explicit cases below are tested; the general result is analytic.
Run: python3 relative_index_check.py
"""
import cmath
import math
import random

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def dot(u, v):
    return sum(a.conjugate()*b for a, b in zip(u, v))

def mv(A, x):
    return [sum(a*xj for a, xj in zip(row, x)) for row in A]

def norm(x):
    return math.sqrt(dot(x, x).real)

def approx(x, y, tol=1e-12):
    return abs(x-y) < tol

# Proper top-singular range: the relative seminorm detects T e_1,
# but every norming functional for G e_1 annihilates T e_1.
G = [[1, 0], [0, .4]]
T = [[0, 0], [1, 0]]
e = [1+0j, 0+0j]
verify(approx(norm(mv(G, e)), 1), 'G top singular vector')
verify(approx(norm(mv(T, e)), 1), 'proper-range relative norm')
verify(approx(dot(mv(G, e), mv(T, e)), 0), 'proper-range radius zero')

# A square-zero witness for the sharp complex Hilbert index 1/2.
G = [[1, 0], [0, 1]]
T = [[0, 1], [0, 0]]
x = [1/math.sqrt(2), 1/math.sqrt(2)]
verify(approx(norm(mv(T, [0, 1])), 1), 'nilpotent norm one')
verify(approx(abs(dot(mv(T, x), mv(G, x))), .5), 'nilpotent radius half')

rng = random.Random(20261031)
for j in range(6000):
    a, b, c, d = (rng.gauss(0, 1) for _ in range(4))
    v = [complex(a, b), complex(c, d)]
    s = norm(v)
    v = [z/s for z in v]
    verify(abs(dot(mv(T, v), mv(G, v))) <= .5 + 2e-15,
           'nilpotent numerical-radius bound')

# Rectangular coisometry: restricting T to the top-singular subspace
# recovers the same two-dimensional numerical range.
G = [[1, 0, 0], [0, 1, 0]]
T = [[0, 1, 0], [0, 0, 0]]
for theta in [j*math.pi/128 for j in range(65)]:
    v = [math.cos(theta), math.sin(theta), 0]
    verify(abs(dot(mv(T, v), mv(G, v))) <= .5+1e-14,
           'rectangular coisometry radius')
verify(approx(abs(dot(mv(T, [1/math.sqrt(2), 1/math.sqrt(2), 0]),
                       mv(G, [1/math.sqrt(2), 1/math.sqrt(2), 0]))), .5),
       'rectangular coisometry equality')

# Isometric inclusion into a larger codomain: target orthogonal to G(E).
G = [[1, 0], [0, 1], [0, 0]]
T = [[0, 0], [0, 0], [1, 0]]
for j in range(91):
    theta = j*math.pi/180
    v = [math.cos(theta), math.sin(theta)]
    verify(approx(dot(mv(T, v), mv(G, v)), 0), 'orthogonal codomain witness')
verify(approx(norm(mv(T, [1, 0])), 1), 'nonzero relative norm')

# Real two-dimensional coisometry: skew-adjoint perturbation of norm one.
G = [[1, 0], [0, 1]]
T = [[0, -1], [1, 0]]
for j in range(541):
    theta = j*math.pi/270
    v = [math.cos(theta), math.sin(theta)]
    verify(approx(dot(mv(T, v), mv(G, v)), 0), 'real skew radius')
verify(approx(norm(mv(T, [1, 0])), 1), 'real skew norm')

# A one-dimensional codomain: all relative numerical radii equal norms.
G = [[1, 0]]
T = [[3, 5]]
verify(approx(norm(mv(G, [1, 0])), 1), 'scalar G norm')
verify(approx(norm(mv(T, [1, 0])), 3), 'scalar T norm on top space')
verify(approx(abs(dot(mv(G, [1, 0]), mv(T, [1, 0]))), 3),
       'scalar relative radius')

# An arbitrarily close non-coisometry has exact index zero:
# G_epsilon is diagonal with top singular space span(e1).
for epsilon in [.1, .01, .001, .00001]:
    G = [[1, 0], [0, 1-epsilon]]
    T = [[0, 0], [1, 0]]
    verify(approx(norm(mv(G, [1, 0])), 1), 'perturbed norm one')
    verify(approx(norm(mv(T, [1, 0])), 1), 'perturbed relative norm one')
    verify(approx(dot(mv(T, [1, 0]), mv(G, [1, 0])), 0),
           'perturbed relative numerical radius zero')

print(f'PASS: {checks} supplementary finite checks')
