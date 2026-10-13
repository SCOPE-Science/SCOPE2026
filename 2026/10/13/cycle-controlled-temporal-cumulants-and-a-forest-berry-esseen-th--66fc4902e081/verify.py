#!/usr/bin/env python3
import itertools
import math
import cmath
from fractions import Fraction


def det_int(A):
    A = [[Fraction(x) for x in row] for row in A]
    n = len(A)
    d = Fraction(1)
    for j in range(n):
        p = next((i for i in range(j, n) if A[i][j] != 0), None)
        if p is None:
            return 0
        if p != j:
            A[j], A[p] = A[p], A[j]
            d = -d
        piv = A[j][j]
        d *= piv
        for k in range(j, n):
            A[j][k] /= piv
        for i in range(j + 1, n):
            q = A[i][j]
            if q:
                for k in range(j, n):
                    A[i][k] -= q * A[j][k]
    return d


def torus_moment(n, edges, amps, phases, order):
    # 2 r cos(theta_u-theta_v+phi)
    total = 0j
    m = len(edges)
    for choices in itertools.product(range(m), repeat=order):
        for signs in itertools.product((1, -1), repeat=order):
            balance = [0] * n
            coeff = 1 + 0j
            for ei, sg in zip(choices, signs):
                u, v = edges[ei]
                balance[u] += sg
                balance[v] -= sg
                coeff *= amps[ei] * cmath.exp(1j * sg * phases[ei])
            if all(x == 0 for x in balance):
                total += coeff
    return total.real

# Triangle 0-1-2-0 and four-cycle 2-3-4-5-2.
edges = [(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,2)]
amps = [0.7,0.5,0.9,0.6,0.4,0.8,0.3]
phases = [0.2,-0.4,0.7,0.1,0.5,-0.2,0.9]

m2 = torus_moment(6, edges, amps, phases, 2)
m3 = torus_moment(6, edges, amps, phases, 3)
m4 = torus_moment(6, edges, amps, phases, 4)
k4 = m4 - 3*m2*m2

f2 = 2*sum(r*r for r in amps)
f3 = 12*amps[0]*amps[1]*amps[2]*math.cos(phases[0]+phases[1]+phases[2])
f4 = -6*sum(r**4 for r in amps) + 48*math.prod(amps[3:7])*math.cos(sum(phases[3:7]))
assert abs(m2-f2) < 1e-11
assert abs(m3-f3) < 1e-11
assert abs(k4-f4) < 1e-10

# Forest coordinate matrix: root row plus child-parent edge-difference rows.
# Tree on vertices 0..4 with edges 0-1, 1-2, 1-3, 3-4.
T = [
    [1,0,0,0,0],
    [-1,1,0,0,0],
    [0,-1,1,0,0],
    [0,-1,0,1,0],
    [0,0,0,-1,1],
]
assert abs(det_int(T)) == 1

# Two-component forest: roots 0 and 3, edges 0-1,1-2 and 3-4.
F = [
    [1,0,0,0,0],
    [0,0,0,1,0],
    [-1,1,0,0,0],
    [0,-1,1,0,0],
    [0,0,0,-1,1],
]
assert abs(det_int(F)) == 1

# A triangle's three oriented edge-difference rows have a linear relation.
tri = [[1,-1,0],[0,1,-1],[-1,0,1]]
assert det_int(tri) == 0

# Berry--Esseen prefactor from E|cos Theta|^3 = 4/(3 pi).
pref = (32/(3*math.pi)) / (2*math.sqrt(2))
target = 8*math.sqrt(2)/(3*math.pi)
assert abs(pref-target) < 1e-15

print('VERIFY_OK')
