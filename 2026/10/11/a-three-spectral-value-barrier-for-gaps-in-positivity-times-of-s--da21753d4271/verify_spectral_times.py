#!/usr/bin/env python3
"""Exact supplementary checks for the spectral-cardinality positivity theorem."""
from fractions import Fraction as F
from math import exp, log

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def vecmul(a,v):
    return [sum(a[i][j]*v[j] for j in range(len(v))) for i in range(len(a))]

T=[[F(-29,22),F(-7,22),F(6,11)], [F(-7,22),F(-29,22),F(6,11)], [F(6,11),F(6,11),F(-4,11)]]
assert vecmul(T,[F(1),F(1),F(3)]) == [F(0)]*3
assert vecmul(T,[F(1),F(-1),F(0)]) == [F(-1),F(1),F(0)]
assert vecmul(T,[F(3),F(3),F(-2)]) == [F(-6),F(-6),F(4)]
assert F(1,11)-F(1,2)/(F(9,2)+1)==0
assert (F(1,11)-F(1,2)/2) < 0
assert F(1,11)>0
# The normalized infinite positive vector has norm squared 2*(3/2)*sum 4**(-k)=1.
assert 2*F(3,2)*F(1,3)==1
J=[[F(0),F(1),F(0),F(0)], [F(1),F(0),F(1),F(0)], [F(0),F(1),F(0),F(1)], [F(0),F(0),F(1),F(0)]]
J2=matmul(J,J); J3=matmul(J2,J)
assert J2[0][2]==1 and J3[0][3]==1
assert J[0][3]==0 and J2[0][3]==0
B=[[(F(1) if i==j else F(0)) + J[i][j]/4 for j in range(4)] for i in range(4)]
B2=matmul(B,B)
assert min(min(row) for row in B)>=0
assert min(min(row) for row in B2)>=0
# Finite spectral interpolation: signs computed at sample exponents are checks, not proofs.
try:
    import numpy as np
    vals,vecs=np.linalg.eigh(np.array([[float(t) for t in row] for row in B]))
    assert min(vals)>0 and np.min(np.diff(vals))>0
    for t in (0.3,0.7):
        P=(vecs*vals**t)@vecs.T
        assert P[0,2]<-1e-7
    for t in (1.3,1.7):
        P=(vecs*vals**t)@vecs.T
        assert P[0,3]<-1e-7
    for t in (2.2,3):
        P=(vecs*vals**t)@vecs.T
        assert P.min()>-1e-10
except ImportError:
    pass
print('THREE_SPECTRAL_LEVEL_POSITIVITY_TIME_EXACT_CHECKS_OK')
