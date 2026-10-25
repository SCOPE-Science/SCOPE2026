#!/usr/bin/env python3
"""Exact certificate for the characteristic-five Wiman--Edge genus-six family.

Requires SymPy.  All polynomial claims are identities in F_5[t,r] or
F_5[t,X,Y,Z]; finite-field counts are optional consistency checks.
"""
import itertools
import sympy as S

p=5
X,Y,Z,r,v,t=S.symbols('X Y Z r v t')
def mod5(expr,*symbols):
    return S.Poly(S.expand(expr),*symbols,modulus=5).as_expr()
def eq5(a,b,*symbols):
    assert mod5(a-b,*symbols)==0

a,b,c=X**2,Y**2,Z**2
W=X**6+Y**6+Z**6+(a+b+c)*(X**4+Y**4+Z**4)-12*a*b*c
Q=(a-b)*(b-c)*(c-a)
eq5(W,2*(a+b+c)**3+a*b*c,X,Y,Z)
# Node-projection affine chart a=1+rv, b=1+v, c=1:
A=3*r**2+2*r+3
B=2*r**3+(1-t)*r**2+(1+t)*r+2
T=S.expand(2*((1+r*v)+(1+v)+1)**3+(1+r*v)*(1+v) + t*(r*v-v)*v*(1-(1+r*v)))
eq5(T,v**2*(A+v*B),r,v,t)
# r parametrizes the normalization: v=-A/B. Three coordinate
# branch polynomials give the zeros/poles of a/c and b/c.
C=S.expand(B-A)
D=S.expand(B-r*A)
for f,g,expect in (
  (A,B,2*t*t+1),
  (B,C,t*t-2),(B,D,2-t*t),(C,D,t*t-2),
  (B,S.diff(B,r),-t*t*(2*t*t+1)),
  (C,S.diff(C,r),-t*t*(2*t*t+1)),
  (D,S.diff(D,r),t*t*(t*t-2)),
):
  eq5(S.resultant(f,g,r),expect,t)
# Distinct/transverse branch places if t !=0 and t^2 !=2;
# the 9 places have inertia two for the V4 cover.
# The 3 genus-2 quotients are cyclically isomorphic.
h=mod5(B*C,r,t)
h2=S.Poly(S.expand(h*h),r,t,modulus=5)
def coeff(index):
    return mod5(sum(c*t**j for (i,j),c in h2.terms() if i==index),t)
M=S.Matrix([[coeff(4),coeff(3)],[coeff(9),coeff(8)]])
expected=S.Matrix([[t**4-t**3+t,2*t**3-2*t],[2*t**3-2*t,t**4+t**3-t]])
for i in range(2):
 for j in range(2): eq5(M[i,j],expected[i,j],t)
eq5(M.det(),t**8,t)
# Independent elementary F5 point-count check at each nonzero t:
def pow5(a,n): return pow(a%5,n,5)
def F5(x,y,z,tt):
    a,b,c=pow5(x,2),pow5(y,2),pow5(z,2)
    return (2*(a+b+c)**3+a*b*c+tt*(a-b)*(b-c)*(c-a))%5
def plane_count(tt):
    pts={(1,y,z) for y in range(5) for z in range(5)}
    pts|={(0,1,z) for z in range(5)}
    pts.add((0,0,1))
    return sum(F5(x,y,z,tt)==0 for x,y,z in pts)
def curveD_count(tt):
    # two points at infinity since leading coefficient of B*C is 2*2=4
    count=2
    for rr in range(5):
        bb=int(B.subs({r:rr,t:tt}))%5
        cc=int(C.subs({r:rr,t:tt}))%5
        rhs=(bb*cc)%5
        count+=sum((yy*yy)%5==rhs for yy in range(5))
    return count
for tt in range(1,5):
    assert plane_count(tt)==4
    assert curveD_count(tt)==4
    assert mod5(M.det().subs(t,tt),t)!=0
    # For cyclically isomorphic quotients, the trace on C is 3 times
    # the D trace: #C = 3 #D - 2(q+1) over F5, all four nodes rational.
    assert plane_count(tt)-4 == 3*curveD_count(tt)-12
print('VERIFY_OK: exact F5 Wiman reduction, nodal quotient, nine disjoint branch places, genus-two Cartier determinant t^8; F5 counts for t=1,2,3,4')
