#!/usr/bin/env python3
"""Exact rational checks of concrete Jacobians; universal theorem is analytical."""
from fractions import Fraction as F

def det2(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]

# A weighted scalar, lambda=K*A=2: h=3/4>1/2; cos=-23/30.
scalar=1+F(3,4)*2*(-F(23,30))
assert scalar==-F(3,20)
# Two-edge tree K=[[2,-1],[-1,2]], A=I: lambda=3, h=1/2.
h=F(1,2)
c0,c1=-F(4,5),-F(3,5)
jac=[[1+h*2*c0,h*(-1)*c1], [h*(-1)*c0,1+h*2*c1]]
assert jac==[[F(1,5),F(3,10)],[F(2,5),F(2,5)]]
assert det2(jac)==-F(1,25)
# Exact endpoint h=1/3: all cos=-1 yields singular Jacobian.
crit=[[1+F(1,3)*2*(-1),F(1,3)*(-1)*(-1)],[F(1,3)*(-1)*(-1),1+F(1,3)*2*(-1)]]
assert det2(crit)==0
# Degree +1; a single negative branch needs at least two positive branches.
assert (-1)+1+1==1
print('VERIFY_OK scalar_supercritical_det=-3/20 tree_supercritical_det=-1/25 endpoint_det=0')
