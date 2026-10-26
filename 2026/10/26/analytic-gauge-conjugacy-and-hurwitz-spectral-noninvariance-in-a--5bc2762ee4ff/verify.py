#!/usr/bin/env python3
"""Standalone exact rational spectral witness and deterministic conjugacy checks."""
from fractions import Fraction as Q
from math import sin, cos

J=[[Q(97,9600), -Q(4009,4000),Q(0)],
   [Q(4027,4000), Q(1199,336000),Q(3,200)],
   [-Q(3,10),Q(0),-Q(1)]]
def det(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
          -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
          +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
a1=-sum(J[i][i] for i in range(3))
a2=sum(J[i][i]*J[j][j]-J[i][j]*J[j][i] for i in range(3) for j in range(i+1,3))
a3=-det(J)
assert (a1,a2,a3)==(Q(165703,168000),Q(16053466459,16128000000),Q(16201239163,16128000000))
assert a1*a2-a3==Q(-61700626728323,2709504000000000)
assert a1>0 and a2>0 and a3>0 and a1*a2<a3

def F(u,z,mu,e):
    R=abs(u)**2
    a=mu*((R-5)*(20/21-R)-400*z*z/21)
    b=z+R/10
    return (complex(a,1+e*b)*u,-b)
def H(u,z,e): return (complex(cos(e*z),sin(e*z))*u,z)
for mu,e in [(0.001,0.1),(0.04,1.7),(0.003,-0.23)]:
 for u,z in [(complex(1.3,-0.7),0.21),(complex(0,0),-0.3),(complex(-0.2,2.0),0.4)]:
  du,dz=F(u,z,mu,e); w,t=H(u,z,e)
  dh=complex(cos(e*z),sin(e*z))*(du+1j*e*dz*u)
  dw,zt=F(w,t,mu,0)
  assert abs(dh-dw)<1e-11 and abs(dz-zt)<1e-11
print('VERIFY_OK exact_rational_RH=negative gauge_identity_cases=9')
