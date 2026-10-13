#!/usr/bin/env python3
"""Standalone exact-algebra checks for a ring-chain flat-band identity.

Run with Python 3 standard library only. The finite numerical checks below
are explicitly auxiliary and never substitute for the analytic quantifiers.
"""
from fractions import Fraction
from math import sin, cos, pi, sqrt, tan
import cmath

# Multivariate integer polynomials in u=m^2*ell^2 and c=cos(pi*t/3).
def add(a, b):
    out = dict(a)
    for p, v in b.items():
        out[p] = out.get(p, 0) + v
    return {p: v for p, v in out.items() if v}

def mul(a, b):
    out = {}
    for (j,k),v in a.items():
        for (r,s),w in b.items():
            key = (j+r,k+s)
            out[key] = out.get(key,0)+v*w
    return {p:v for p,v in out.items() if v}

def scale(a, k):
    return {p:k*v for p,v in a.items() if k*v}

ONE = {(0,0):1}; U={(1,0):1}; C={(0,1):1}
cm = add(C, scale(ONE,-1)); cp = add(C,ONE)
# The factor S=sin(m*l1)*sin(m*l3)^2 is suppressed on both sides.
# All terms arise from the *un-divided* secular determinant.
p6 = scale(mul(mul(mul(U,U),U),mul(cm,cm)),-72)
p4 = scale(mul(mul(U,U),mul(cm,cp)),-48)
p2 = scale(mul(U,mul(cp,cp)),-8)
left=add(add(p6,p4),p2)
right=scale(mul(U,mul(add(scale(mul(U,cm),3),cp),add(scale(mul(U,cm),3),cp))),-8)
assert left==right, (left,right)
assert left=={(3,2):-72,(3,1):144,(3,0):-72,(2,2):-48,(2,0):48,(1,2):-8,(1,1):-16,(1,0):-8}

# The auxiliary trigonometric reductions at integer m follow because
# sin(m*(l2+l3))=0, cos(m*(l2+l3))=1.
# Their common trigonometric combination is T=sin(a-2*b)-sin(a)+sin(a+2*b)
# = sin(a)*(1-4*sin(b)^2). Check representative off-grid values as sanity only.
for a,b in [(0.13,0.42),(sqrt(2),sqrt(3)),(1.2,2.8)]:
    T=sin(a-2*b)-sin(a)+sin(a+2*b)
    assert abs(T - sin(a)*(1-4*sin(b)**2)) < 2e-14

# For all interior 0<t<1, c in (1/2,1), and u>0,
# the cosine-Bloch prefactor 3*u*(c-1)-(c+1) is strictly negative.
for t in [1/50,1/2,49/50]:
    c=cos(pi*t/3)
    for u in [1/100,1,100]:
        assert 3*u*(c-1)-(c+1)<0
        assert abs((1-c)/(1+c)-tan(pi*t/6)**2) < 2e-14

# Exact algebraic equivalence of the tunable branch:
# 3*m^2*ell^2*tan(pi*t/6)^2=1.
for m,ell in [(1,1+2/sqrt(3)),(2,1),(5,0.3)]:
    t=6/pi * __import__('math').atan(1/(sqrt(3)*m*ell))
    assert (0<t<1) == (m*ell>1)
    assert abs(3*m*m*ell*ell*tan(pi*t/6)**2-1)<1e-12

# Check the two Bloch coefficients vanish at integer k independent of theta.
# The latter analytically follows from l2+l3=2*pi and integer k.
for m in [1,2,3]:
    l3=sqrt(3); l2=2*pi-l3
    assert abs(sin(m*l2)+sin(m*l3))<2e-14
    assert abs(cos(m*l3)-cos(m*l2))<2e-14

print('VERIFY_OK: exact polynomial factorization and finite checks')

# Separate finite fiber-determinant sanity check using the vertex matching
# matrix directly (not the secular coefficients), with no external packages.
def det_complex(rows):
    A=[list(row) for row in rows]
    n=len(A); value=1+0j
    for j in range(n):
        i=max(range(j,n),key=lambda r:abs(A[r][j]))
        if abs(A[i][j]) < 1e-12:
            return 0j
        if i!=j:
            A[j],A[i]=A[i],A[j]; value=-value
        d=A[j][j];value*=d
        for r in range(j+1,n):
            q=A[r][j]/d
            for s in range(j+1,n):
                A[r][s]-=q*A[j][s]
    return value

def fiber_det(theta, ell):
    t=0.5; k=1.0; l1=sqrt(2.0); l3=sqrt(3.0); l2=2*pi-l3
    w=cmath.exp(2j*pi/3)
    eig=[1.0,-cmath.exp(-1j*pi*t/3),-cmath.exp(1j*pi*t/3)]
    F=[[w**(-r*j)/sqrt(3.0) for j in range(3)] for r in range(3)]
    U3=[[sum(F[r][j]*eig[j]*F[s][j].conjugate() for j in range(3))
         for s in range(3)] for r in range(3)]
    U=[[U3[r%3][s%3] if r//3==s//3 else 0j for s in range(6)]
       for r in range(6)]
    z=cmath.exp(-1j*theta)
    a=cmath.exp(1j*k*l1/2); b=cmath.exp(-1j*k*l1/2)
    e2=cmath.exp(1j*k*l2)*z; f2=cmath.exp(-1j*k*l2)*z
    e3=cmath.exp(1j*k*l3)*z; f3=cmath.exp(-1j*k*l3)*z
    M=[[0j]*6 for _ in range(6)]
    N=[[0j]*6 for _ in range(6)]
    M[0][0:2]=[a,b]; N[0][0:2]=[-a,b]
    M[1][4:6]=[1,1];N[1][4:6]=[1,-1]
    M[2][2:4]=[1,1];N[2][2:4]=[1,-1]
    M[3][0:2]=[b,a];N[3][0:2]=[b,-a]
    M[4][2:4]=[e2,f2];N[4][2:4]=[-e2,f2]
    M[5][4:6]=[e3,f3];N[5][4:6]=[-e3,f3]
    Q=[[sum((U[i][r]-(1 if i==r else 0))*M[r][j] - k*ell*(U[i][r]+(1 if i==r else 0))*N[r][j]
            for r in range(6)) for j in range(6)] for i in range(6)]
    return det_complex(Q)

ell=1/(sqrt(3)*tan(pi/12))
for theta in [0.0,0.2,0.9,1.3,2.7]:
    assert abs(fiber_det(theta,ell)) < 1e-7, (theta,fiber_det(theta,ell))
assert abs(fiber_det(0.9,ell*1.01)) > 1e-6
print('VERIFY_OK: direct Bloch matrix finite sanity checks')
