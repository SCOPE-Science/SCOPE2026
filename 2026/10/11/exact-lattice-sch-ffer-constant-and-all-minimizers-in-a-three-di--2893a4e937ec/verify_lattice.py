"""Exact rational checks for the three-coordinate lattice norm extremal classification.

The accompanying analytic proof, not finite sampling, establishes the universal claims.
"""
from fractions import Fraction as Q

F = [
    (Q(1), Q(0), Q(1,2)),
    (Q(0), Q(1), Q(1,2)),
    (Q(2,3), Q(2,3), Q(1,3)),
    (Q(5,6), Q(5,6), Q(0)),
]

def dot(a, x):
    return sum((p*q for p,q in zip(a,x)), Q(0))

def norm(x):
    return max(dot(a, tuple(abs(t) for t in x)) for a in F)

# The exact universal positive-cone norming-functional domination.
for f in F:
    assert all(3*r - 2*s >= 0 for r, s in zip(F[2],f))

# Equality with the third facet can come only from the first two facets.
assert (tuple(3*r-2*s for r,s in zip(F[2],F[0])) ==
        (Q(0),Q(2),Q(0)))
assert (tuple(3*r-2*s for r,s in zip(F[2],F[1])) ==
        (Q(2),Q(0),Q(0)))
for k in (2,3):
    assert all(3*r - 2*s > 0 for r,s in zip(F[2],F[k]))

def pair(a,b):
    u=(a,Q(0),2*(1-a))
    v=(Q(0),b,2*(1-b))
    return u,v

# The minimizing polygon has exactly these three rational vertices.
vertices=((Q(2,3),Q(2,3)), (Q(14,15),Q(2,3)),(Q(2,3),Q(14,15)))
for a,b in vertices + ((Q(4,5),Q(4,5)),):
    assert Q(2,3)<=a<=1 and Q(2,3)<=b<=1 and a+b<=Q(8,5)
    u,v=pair(a,b)
    assert norm(u)==norm(v)==1
    assert dot(F[2],u)==dot(F[2],v)==Q(2,3)
    assert norm(tuple(x+y for x,y in zip(u,v)))==Q(4,3)

# On the two active faces the sum-facet values are exact affine expressions.
for a,b in vertices:
    u,v=pair(a,b)
    w=tuple(x+y for x,y in zip(u,v))
    assert dot(F[0],w)==2-b
    assert dot(F[1],w)==2-a
    assert dot(F[2],w)==Q(4,3)
    assert dot(F[3],w)==Q(5,6)*(a+b)

# Previously established disjoint-comparison constant and its exact gap.
beta=Q(15,11)
lam=Q(4,3)
assert beta-lam==Q(1,33)
assert beta/lam==Q(45,44)
print('LATTICE_SCHAFFER_EXACT_DOMINANCE_AND_EXTREMAL_TRIANGLE_OK')
