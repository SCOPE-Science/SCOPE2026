#!/usr/bin/env python3
from itertools import product
from collections import defaultdict

def det_bareiss(a):
    a = [row[:] for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
        for j in range(k + 1, n):
            a[k][j] = 0
    return sign * a[n-1][n-1]

def det3_mod(rows, q):
    a,b,c = rows
    return (
        a[0]*(b[1]*c[2]-b[2]*c[1])
        - a[1]*(b[0]*c[2]-b[2]*c[0])
        + a[2]*(b[0]*c[1]-b[1]*c[0])
    ) % q

def sphere(q, j):
    return sorted(
        x for x in product(range(q), repeat=3)
        if sum(t*t for t in x) % q == j % q
    )

def pair_fibers(points, q):
    fibers = defaultdict(list)
    n = len(points)
    for i in range(n):
        for j in range(i, n):
            s = tuple((points[i][k] + points[j][k]) % q for k in range(3))
            fibers[s].append((i,j))
    return fibers

def relation(n, i,j,k,l):
    r = [0]*n
    r[i] += 1
    r[j] += 1
    r[k] -= 1
    r[l] -= 1
    return r

# q=3: S={±e_1,±e_2,±e_3}; the only pair-sum collision is at zero.
p3 = sphere(3, 1)
assert len(p3) == 6
f3 = pair_fibers(p3, 3)
coll3 = [(s,pairs) for s,pairs in f3.items() if len(pairs) > 1]
assert len(coll3) == 1
s0, pairs0 = coll3[0]
assert s0 == (0,0,0)
assert len(pairs0) == 3
assert set(pairs0) == {(0,1),(2,3),(4,5)}

# q=5: S={Q=2}; every additive relation preserves total coefficient and first moment mod 5.
p5 = sphere(5, 2)
assert len(p5) == 20
selected = [
 (0,3,1,2), (0,7,13,15), (2,7,10,17), (0,19,2,18),
 (4,5,6,7), (16,17,18,19), (5,19,7,17), (3,11,13,17),
 (12,15,13,14), (8,11,9,10), (2,10,15,19), (2,17,8,9),
 (0,6,8,17), (9,18,10,16), (0,17,1,16), (2,8,13,19),
 (0,12,6,9), (0,3,9,14), (1,6,9,16)
]
rows = []
for i,j,k,l in selected:
    lhs = tuple((p5[i][a] + p5[j][a]) % 5 for a in range(3))
    rhs = tuple((p5[k][a] + p5[l][a]) % 5 for a in range(3))
    assert lhs == rhs
    r = relation(20,i,j,k,l)
    assert sum(r) == 0
    for a in range(3):
        assert sum(r[t] * p5[t][a] for t in range(20)) % 5 == 0
    rows.append(r[:19])

d = abs(det_bareiss(rows))
assert d == 125

# The moment map H -> F_5^3 is onto: these three point differences form a basis.
base = p5[0]
diffs = [
    tuple((p5[i][a] - base[a]) % 5 for a in range(3))
    for i in (1,2,4)
]
assert det3_mod(diffs,5) == 1

# Therefore the full relation lattice L lies in ker(moment), while the selected
# relation sublattice already has index 5^3=125 in H. Surjectivity gives
# [H:ker(moment)]=125, forcing L=ker(moment).

print("q3_points=6")
print("q3_zero_sum_pairs=3")
print("q5_points=20")
print("q5_selected_relation_determinant=125")
print("q5_difference_basis_determinant_mod5=1")
print("VERIFY_OK")
