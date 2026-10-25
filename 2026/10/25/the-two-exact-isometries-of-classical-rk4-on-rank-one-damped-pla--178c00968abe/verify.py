#!/usr/bin/env python3
"""Exact matrix-polynomial and high-precision interval checks for a planar RK4 theorem."""
from fractions import Fraction as F
from decimal import Decimal as D, getcontext
getcontext().prec=72

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def madd(A,B):return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
def mul(t,A):return [[t*A[i][j] for j in range(2)] for i in range(2)]
def eye(t):return [[t,0*t],[0*t,t]]
def r4(A,one):
    Z=eye(one);W=eye(one)
    for k in range(1,5):
        W=mm(W,A);Z=madd(Z,mul(one/F(1 if k==1 else 1),mul(F(1, __import__('math').factorial(k)),W)))
    return Z
nchecks=0
for x in [F(1,2),F(5,4),F(3,1),F(7,2),F(9,1)]:
 for y in [F(1,3),F(2,1),F(5,2),F(7,3)]:
    A=[[-x,-y],[y,F(0)]];Y=y*y
    U=1+Y*(Y-(x*x-4*x+12))/24
    V=-(x**3-4*x*x-2*x*Y+12*x+4*Y-24)/24
    expected=madd(mul(U,eye(F(1))),mul(V,A))
    assert r4(A,F(1))==expected
    Q=mm([[expected[0][0],expected[1][0]],[expected[0][1],expected[1][1]]],expected)
    assert Q[0][1]==x*y*V*V
    nchecks+=2

def bisect(f,left,right):
  lo=D(left);hi=D(right)
  assert f(lo)<0<f(hi)
  for _ in range(380):
    mid=(lo+hi)/2
    if f(mid)<0:lo=mid
    else:hi=mid
  return (lo+hi)/2
rho=bisect(lambda z:z**3-4*z*z+12*z-24,'2','3')
v=bisect(lambda z:z**3+12*z*z-96*z-64,'5','6');a=v.sqrt()
for s,x,Y in [(D(1),4-rho,24/rho),(D(-1),2+a,4+a+v/2-4/a)]:
    U=1+Y*(Y-(x*x-4*x+12))/24
    V=-(x**3-4*x*x-2*x*Y+12*x+4*Y-24)/24
    assert abs(U-s)<D('1e-60') and abs(V)<D('1e-60')
    uy=(2*Y-(x*x-4*x+12))/24;vy=(x-2)/12
    d1=2*s*(uy-x*vy);d2=2*s*uy
    if s==1:assert d1>0 and d2>0
    else:assert d1>0 and d2<0
    nchecks+=4
assert abs((3+v/2-4/a)*(3+v/2+4/a)-33)<D('1e-60')
assert (-12-v+16/a)<0 and (-12-v-16/a)<0 and a>2
print('VERIFY_OK',nchecks, 'rho',format(rho,'.24f'),'v',format(v,'.24f'))
