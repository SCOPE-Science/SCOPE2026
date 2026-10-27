#!/usr/bin/env python3
"""Exact checks for the ten-line discriminant of a diagonal degree-four del Pezzo fibration."""
from collections import Counter
from functools import reduce
from itertools import combinations
from math import gcd

# Coordinates of the five eigenvalue linear forms in the base plane.
forms = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, -1, -1), (0, 0, 0))

def primitive(v):
    common = reduce(gcd, v, 0)
    if common == 0:
        raise ValueError('Zero vector is not a projective point or line')
    v = tuple(x // abs(common) for x in v)
    return tuple(-x for x in v) if next(x for x in v if x) < 0 else v

def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

lines = {(i,j): primitive(tuple(forms[i][k] - forms[j][k] for k in range(3)))
         for i,j in combinations(range(5), 2)}
assert len(lines) == len(set(lines.values())) == 10
points = {primitive(cross(a, b)) for a,b in combinations(lines.values(), 2)}
assert len(points) == 25
strata = Counter()
for point in points:
    vals = [dot(f, point) for f in forms]
    partition = tuple(sorted((vals.count(v) for v in set(vals)), reverse=True))
    incident = sum(dot(line, point) == 0 for line in lines.values())
    strata[(incident, partition)] += 1
assert strata == {(3, (3,1,1)): 10, (2, (2,2,1)): 15}, strata
for label, line in lines.items():
    hits = [p for p in points if dot(line, p) == 0]
    assert len(hits) == 6
    assert sum(Counter(dot(f,p) for f in forms).most_common(1)[0][1] == 3
               for p in hits) == 3
assert tuple(sorted(Counter(dot(f,(1,1,3)) for f in forms).values(), reverse=True)) == (2,1,1,1)

# Univariate polynomial Chern classes, represented as bivariate h,g monomials.
def mul(a, b):
    result = {}
    for (i,j), c in a.items():
        for (k,l), d in b.items():
            if i+k <= 2 and j+l <= 4 and i+j+k+l <= 6:
                exp = (i+k, j+l)
                result[exp] = result.get(exp, 0) + c*d
    return result

def pow_poly(a, n):
    out = {(0,0): 1}
    for _ in range(n):
        out = mul(out, a)
    return out

one = {(0,0):1}
H = {(1,0):1}
G = {(0,1):1}
oneH = {(0,0):1,(1,0):1}
oneG = {(0,0):1,(0,1):1}
inv2G = {(0,k): (-2)**k for k in range(5)}
invH2G = {(0,0):1}
for power in range(1,5):
    term = pow_poly({(1,0):1,(0,1):2},power)
    for index, coeff in term.items():
        invH2G[index] = invH2G.get(index,0) + (-1)**power*coeff
chern = mul(mul(pow_poly(oneH,3), pow_poly(oneG,5)), mul(inv2G,invH2G))
c4 = {idx: coeff for idx, coeff in chern.items() if sum(idx)==4 and coeff}
assert c4 == {(0,4):5, (1,3):4, (2,2):4}, c4
Euler = mul(mul(c4,{(0,1):2}),{(1,0):1,(0,1):2})[(2,4)]
assert Euler == 24
# Additive Euler comparison: generic surfaces e=8, two/four nodes e=6/4.
e_discriminant = 10*2 - 10*(3-1) - 15*(2-1)
e_open = 3-e_discriminant
e_line_open = e_discriminant-25
fiber_euler = 8*e_open + 6*e_line_open + 6*10 + 4*15
assert (e_discriminant, e_open, e_line_open, fiber_euler) == (-15,18,-40,24)
print('VERIFY_OK lines=10 triple_points=10 double_pair_points=15 singular_base_points=25')
print('VERIFY_OK generic_line_fibers=10 each_two_A1 total_nodes=20')
print('VERIFY_OK c4=5g4+4hg3+4h2g2 euler_from_Chern=24 euler_from_fibers=24')
