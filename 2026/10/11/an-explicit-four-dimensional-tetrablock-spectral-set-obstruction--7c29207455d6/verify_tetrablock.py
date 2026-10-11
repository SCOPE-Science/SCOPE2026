#!/usr/bin/env python3
"""Exact finite arithmetic diagnostics for an explicit tetrablock counterexample.

The scalar spectral-set and matrix-boundary arguments are analytic and supplied
in the accompanying mathematical proof; this verifies only exact finite identities.
"""
from fractions import Fraction as Q

Z = Q(0)
O = Q(1)
RHO = Q(3, 4)

def matmul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))

def upper_block(A):
    return tuple(tuple((Z if (i < 2 or j < 2) else Z) if not (i < 2 and j >= 2)
                       else A[i][j-2] for j in range(4)) for i in range(4))

def mmv(A, v):
    return tuple(sum(A[i][j]*v[j] for j in range(len(v)))
                 for i in range(len(A)))

E11=((O,Z),(Z,Z))
E22=((Z,Z),(Z,O))
J=((Z,O),(O,Z))
for A in (E11,E22,J):
    for B in (E11,E22,J):
        AB=matmul(upper_block(A),upper_block(B))
        assert all(x==0 for row in AB for x in row), 'square-zero products'
K=((O,Z,Z,RHO),(Z,Z,RHO,Z),(Z,RHO,Z,Z),(RHO,Z,Z,O))
vecs=((1,0,0,1),(1,0,0,-1),(0,1,1,0),(0,1,-1,0))
eigs=(O+RHO,O-RHO,RHO,-RHO)
for v, e in zip(vecs,eigs):
    assert mmv(K,v)==tuple(e*x for x in v), 'tensor block eigenpair'
assert O+RHO==Q(7,4)
# The golden ratio is the positive root of t^2 - t - 1.
# This polynomial is strictly increasing for t >= 1/2, so a positive value
# at 7/4 proves 7/4 > golden ratio without floating-point arithmetic.
x=Q(7,4)
assert x*x-x-O==Q(5,16)>0
assert Q(3,4)*Q(3,4)<1
print('EXPLICIT_TETRABLOCK_CERTIFICATE_OK')
