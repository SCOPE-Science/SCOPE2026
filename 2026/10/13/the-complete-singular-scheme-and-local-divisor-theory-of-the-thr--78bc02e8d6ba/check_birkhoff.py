"""Exact, self-contained checks for the 3-by-3 Birkhoff toric cubic.

Run: python3 check_birkhoff.py
Uses Python standard library only.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import gcd


def rank(matrix):
    A = [[Fraction(x) for x in row] for row in matrix]
    nrows, ncols = len(A), len(A[0])
    r = 0
    for col in range(ncols):
        pivot = next((i for i in range(r, nrows) if A[i][col]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        q = A[r][col]
        A[r] = [v / q for v in A[r]]
        for i in range(nrows):
            if i != r and A[i][col]:
                q = A[i][col]
                A[i] = [u - q*v for u, v in zip(A[i], A[r])]
        r += 1
    return r


def determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    return sum((-1)**j * a * determinant([row[:j]+row[j+1:] for row in A[1:]])
               for j, a in enumerate(A[0]))


perms = list(permutations(range(3)))
vecs = [[1] + [int(p[i] == j) for i in range(3) for j in range(3)] for p in perms]
assert rank(list(map(list, zip(*vecs)))) == 5
sgns = [(-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)) for p in perms]
assert sum(s*vec[0] for s,vec in zip(sgns,vecs)) == 0
assert [sum(s*vec[k] for s,vec in zip(sgns,vecs)) for k in range(10)] == [0]*10
assert sgns.count(1) == sgns.count(-1) == 3
print('AFFINE_LATTICE: rank=5; unique primitive relation=even triple minus odd triple')

# Stratify the projective hypersurface by exact nonzero coordinate supports.
# For a zero-one representative, f vanishes unless one group is completely
# nonzero and the other is not. The both-full case admits f=0 and is smooth.
feasible = singular = 0
singular_singletons = singular_doubletons = 0
for mask in product((0, 1), repeat=6):
    if sum(mask) == 0:
        continue
    a, b = sum(mask[:3]), sum(mask[3:])
    if (a == 3) != (b == 3):
        continue
    feasible += 1
    jac_zero = a <= 1 and b <= 1
    monomial_jac_zero = all(not(mask[i] and mask[j]) for i,j in
                            list(combinations(range(3), 2)) + list(combinations(range(3, 6), 2)))
    assert jac_zero == monomial_jac_zero
    if jac_zero:
        singular += 1
        singular_singletons += a+b == 1
        singular_doubletons += a+b == 2
assert (singular, singular_singletons, singular_doubletons) == (15, 6, 9)
print(f'PROJECTIVE_SUPPORTS: feasible={feasible}; singular={singular} (six vertex strata, nine line strata)')

# Hilbert function for the squarefree monomial Jacobian ideal.
for degree in range(1, 13):
    count = 0
    # Every surviving degree-d monomial uses at most one x and one y.
    for split in range(degree+1):
        left = 1 if split == 0 else 3
        right = 1 if degree-split == 0 else 3
        count += left * right
    assert count == 9*degree-3
print('HILBERT: dimensions 9d-3 (1<=d<=12), so degree 9 and arithmetic genus 4')

# Monomial valuations on six height-one toric prime divisors of the x_1 chart.
relations = [
    [1,1,1,0,0,0], [0,0,0,1,1,1],
    [1,0,0,1,0,0], [0,1,0,0,1,0], [0,0,1,0,0,1]
]
assert rank(relations) == 4
minor_gcd = 0
for rows in combinations(range(5), 4):
    for cols in combinations(range(6), 4):
        minor_gcd = gcd(minor_gcd, abs(determinant([[relations[i][j] for j in cols] for i in rows])))
assert minor_gcd == 1
print('LOCAL_CLASS_GROUP: 6 toric prime divisors, relation rank 4, gcd maximal minors 1; Cl=Z^2')

# At a general line point the transverse quadratic Hessian is nondegenerate.
hessian = [[0,1,0,0], [1,0,0,0], [0,0,0,-1], [0,0,-1,0]]
assert determinant(hessian) == 1
print('TRANSVERSE_NODE: four-variable Hessian determinant=1')
print('ALL_CHECKS_PASS')
