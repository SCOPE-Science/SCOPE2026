"""Exact-rational checks for a nullspace-branch saddle-point spectrum witness.
All calculations use Python's standard-library Fraction; run with python verify.py.
"""
from fractions import Fraction as F

def matvec(M,v):
    return [sum((F(a)*b for a,b in zip(row,v)),F(0)) for row in M]

def check(t,s):
    t,s=F(t),F(s)
    assert s*s == 3+6*t*t
    A=[F(1,2),F(4),F(6),F(7)]
    E=[F(1,2),F(3)]
    B=[[t,s,0,0],[0,0,10*t,0],[0,0,0,10*t]]
    C=[[0,1,0],[0,0,1]]
    x=[2*t,-s/3,F(0),F(0)]
    y=[F(0),F(0)]
    z=[F(1),F(0),F(0)]
    # For Acal w = lambda Pcal w at lambda=1,
    # Pcal=[I_4 0 0;0 I_2 C;0 0 -I_3].
    lhs_x=[a*xj+sum(F(B[k][j])*z[k] for k in range(3)) for j,(a,xj) in enumerate(zip(A,x))]
    rhs_x=x
    lhs_y=[E[j]*y[j]+sum(F(C[j][k])*z[k] for k in range(3)) for j in range(2)]
    rhs_y=[y[j]+sum(F(C[j][k])*z[k] for k in range(3)) for j in range(2)]
    lhs_z=[sum(F(B[k][j])*x[j] for j in range(4))+sum(F(C[j][k])*y[j] for j in range(2)) for k in range(3)]
    rhs_z=[-zz for zz in z]
    assert lhs_x==rhs_x and lhs_y==rhs_y and lhs_z==rhs_z
    assert matvec(C,z)==[0,0]
    # BB^T diagonal for disjoint row supports.
    BBt=[[sum(F(B[i][k])*F(B[j][k]) for k in range(4)) for j in range(3)] for i in range(3)]
    assert BBt == [[3+7*t*t,0,0],[0,100*t*t,0],[0,0,100*t*t]]
    bmin=3+7*t*t
    assert bmin > 7
    assert F(1)<bmin/7 # the source's stated lower bound fails
    assert F(1)>F(1,2) # the clipped lower bound is respected
    assert F(1) not in A and F(1) not in E
    return bmin

assert check(1,3)==10
assert check(11,27)==850
# The remaining family with irrational s is proved by the identity s^2=3+6t^2,
# and is not falsely claimed to have been exactly enumerated here.
# Universal clipping proof uses the positive inverse of (A-lambda I) only
# in the branch lambda<lambda_min(A).

# Sharpness on the low-coupling branch: a=3, b=4, beta=4.
# The positive root of lambda*(b-lambda)=beta is lambda=2.
A0=[F(3),F(4),F(4)]
B0=[[F(0),F(2),F(0)],[F(0),F(0),F(2)]]
C0=[[F(0),F(1)]]
x0=[F(0),F(-1),F(0)]
z0=[F(1),F(0)]
assert [A0[j]*x0[j]+sum(B0[k][j]*z0[k] for k in range(2)) for j in range(3)] == [2*v for v in x0]
assert matvec(B0,x0) == [-2*v for v in z0]
assert matvec(C0,z0)==[F(0)]
assert F(2)*(F(4)-F(2))==F(4)

print('VERIFY_OK exact_generalized_eigenpairs=2 nullspace_conditions=2 BBt_identites=2 eigenspectrum_exclusions=2 sharp_floor_equality=1')
