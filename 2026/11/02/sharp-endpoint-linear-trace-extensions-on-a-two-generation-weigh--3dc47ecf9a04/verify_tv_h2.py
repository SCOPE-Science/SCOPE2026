#!/usr/bin/env python3
"""Exact arithmetic checks for the weighted binary-height-2 trace theorem.

No external packages; verifies all six gradient-coordinate images, weighted
column sums, and exact branch formulas on a rational grid. This is a finite
sanity test, not a proof of the universal theorem.
"""
from fractions import Fraction as F
from itertools import product

def extension_matrix(t):
    """six original gradients -> six extended gradients, root=0 in input."""
    z=F(0); one=F(1)
    root=[z]*6
    a=[one,z,z,z,z,z]
    b=[z,one,z,z,z,z]
    leaves=[a[:], a[:],b[:],b[:]]
    leaves[0][2]+=one; leaves[1][3]+=one
    leaves[2][4]+=one; leaves[3][5]+=one
    leafmean=[sum(leaf[j] for leaf in leaves)/4 for j in range(6)]
    leftmean=[(leaves[0][j]+leaves[1][j])/2 for j in range(6)]
    rightmean=[(leaves[2][j]+leaves[3][j])/2 for j in range(6)]
    A=[((one+t)*leftmean[j]+(one-t)*rightmean[j])/2 for j in range(6)]
    B=[((one-t)*leftmean[j]+(one+t)*rightmean[j])/2 for j in range(6)]
    return [[A[j]-leafmean[j] for j in range(6)],
            [B[j]-leafmean[j] for j in range(6)],
            *[[leaves[i][j]-(A if i<2 else B)[j] for j in range(6)] for i in range(4)]]

def direct_norm(r,t):
    P=extension_matrix(t)
    w=[r,r,F(1),F(1),F(1),F(1)]
    cols=[sum(w[i]*abs(P[i][j]) for i in range(6))/w[j] for j in range(6)]
    return max(cols),cols

def formula(r,t):
    return max((2+(r-2)*t)/r, (3+(r-1)*t)/2)

def optimum(r):
    if r<=1: return F(1), 1+r/2
    if r<=F(4,3):
        t=(4-3*r)/(r*r-3*r+4)
        return t,(4-r)/(r*r-3*r+4)
    return F(0),F(3,2)

N=0
for rn in range(1,101):
    r=F(rn,30)
    tstar,opt=optimum(r)
    assert 0<=tstar<=1
    for tn in range(21):
        t=F(tn,20)
        a,cols=direct_norm(r,t)
        assert a==formula(r,t), (r,t,a,formula(r,t),cols)
        assert a>=opt,(r,t,a,opt)
        N+=1
    a,_=direct_norm(r,tstar)
    assert a==opt,(r,tstar,a,opt)
    N+=1
print('PASS',N,'exact rational column/optimization comparisons')
print('special endpoint r=1/2:', optimum(F(1,2)))
print('special transition r=4/3:', optimum(F(4,3)))
