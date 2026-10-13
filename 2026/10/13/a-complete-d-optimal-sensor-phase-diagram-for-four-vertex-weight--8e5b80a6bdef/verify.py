"""Exact checks for a four-vertex weighted-path observation design theorem.
This is a reproducibility supplement, not an independent assessment.
"""
from fractions import Fraction
from itertools import permutations, product
from math import isclose

PERMS4 = tuple(permutations(range(4)))

def det4(M):
    total = 0
    for perm in PERMS4:
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1,4))
        term = 1
        for row, col in enumerate(perm):
            term *= M[row][col]
        total += -term if inversions % 2 else term
    return total

def gram_krylov(p,q,r,j):
    Q = [(-p,p,0,0), (p,-p-q,q,0),
         (0,q,-q-r,r), (0,0,r,-r)]
    v = tuple(1 if i == j else 0 for i in range(4))
    cols = []
    for _ in range(4):
        cols.append(v)
        v = tuple(sum(Q[i][k]*v[k] for k in range(4)) for i in range(4))
    return det4([[cols[c][i] for c in range(4)] for i in range(4)])

def expected_krylov(p,q,r):
    a=p*p-p*q-2*p*r+q*r
    b=p*q-2*p*r-q*r+r*r
    h=p*q*q*r
    return (h*p*p,-h*a,-h*b,h*r*r)

# Degree of every determinant and proposed expression is <= 6 in every variable.
# Seven distinct evaluations per variable prove polynomial identity over Q.
for p,q,r in product(range(7), repeat=3):
    predicted=expected_krylov(p,q,r)
    computed=tuple(gram_krylov(p,q,r,j) for j in range(4))
    assert computed == predicted, (p,q,r,computed,predicted)
print('FOUR_NODE_UNIVERSAL_POLYNOMIAL_IDENTITIES_OK')

# Cover all combinatorial branches, ties, and rational phase boundaries.
def predicted_optimal(p,q,r):
    if p==r:
        return {0,1,2,3}
    if p<r:
        return {3-i for i in predicted_optimal(r,q,p)}
    delta=p*p-4*p*r+r*r
    theta=(p*p+2*p*r-r*r)/(p-r)
    if delta<0:
        return {0} if q<2*p else ({0,1} if q==2*p else {1})
    if delta>0:
        return {0} if q<theta else ({0,2} if q==theta else {2})
    return {0} if q<2*p else ({0,1,2} if q==2*p else {1,2})

for p,r,q in product(range(1,22),range(1,22),range(1,61)):
    scores=[x*x for x in (p*p,p*p-p*q-2*p*r+q*r,p*q-2*p*r-q*r+r*r,r*r)]
    maximizers={j for j,x in enumerate(scores) if x==max(scores)}
    assert maximizers==predicted_optimal(Fraction(p),Fraction(q),Fraction(r))
print('ALL_26460_INTEGER_TRIPLES_BRANCHES_OK')

for p,q,r,expect in [
    (2,5,1,{1}),(4,10,1,{2}),(4,Fraction(23,3),1,{0,2}),
    (1,9,1,{0,1,2,3}),(3,2,1,{0}),(2,4,1,{0,1}),
    (1,5,2,{2})]:
    assert predicted_optimal(Fraction(p),Fraction(q),Fraction(r))==expect
print('EXACT_BOUNDARY_AND_REFLECTION_CASES_OK')

# In dimensions 2 and 3, an interior vertex cannot strictly maximize.
for p,q in product(range(1,100), repeat=2):
    assert abs(p-q) < max(p,q)
print('LOWER_DIMENSION_MINIMALITY_OK')
print('VERIFY_OK')
