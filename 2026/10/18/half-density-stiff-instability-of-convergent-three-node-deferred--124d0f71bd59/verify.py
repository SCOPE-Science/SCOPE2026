#!/usr/bin/env python3
"""Exact checks for Simpson-collocation, implicit-Euler SDC stiff limits.

Requires Python 3.10+ and SymPy. Run: python verify.py
The proof of irrationality/equidistribution is mathematical, not a finite computation.
"""
from fractions import Fraction as F
import sympy as s

checks = 0
def check(v, msg):
    global checks
    assert bool(v), msg
    checks += 1

z, t = s.symbols('z t')
nodes = [s.Rational(0), s.Rational(1, 2), s.Rational(1)]
lagrange = [s.prod((t-nodes[j])/(nodes[i]-nodes[j]) for j in range(3) if j != i) for i in range(3)]
Q = s.Matrix([[s.integrate(p, (t, 0, x)) for p in lagrange] for x in nodes])
D = s.Matrix([[0,0,0], [0,s.Rational(1,2),0], [0,s.Rational(1,2),s.Rational(1,2)]])
expected_Q=s.Matrix([[0,0,0], [s.Rational(5,24),s.Rational(1,3),-s.Rational(1,24)], [s.Rational(1,6),s.Rational(2,3),s.Rational(1,6)]])
check(Q==expected_Q, 'Lagrange quadrature')
G=(s.eye(3)-z*D).inv()*z*(Q-D)
B=G[1:,1:]
check(s.simplify(s.trace(B)-z*(11*z-24)/(12*(z-2)**2))==0, 'dynamic trace')
check(s.simplify(B.det()-z**2/(4*(z-2)**2))==0, 'dynamic determinant')
check(s.simplify(s.trace(B)**2-4*B.det()-z**3*(48-23*z)/(144*(z-2)**4))==0, 'discriminant')

b=(s.eye(3)-z*D).inv()*s.ones(3,1)
coll=(s.eye(3)-z*Q).inv()*s.ones(3,1)
check(s.simplify(coll[2]-(z*z+6*z+12)/(z*z-6*z+12))==0,'collocation multiplier')
check(s.simplify(coll[0]-1)==0,'initial collocation stage')

Ginfty=G.applyfunc(lambda x:s.limit(x,z,-s.oo))
binfty=b.applyfunc(lambda x:s.limit(x,z,-s.oo))
check(Ginfty==s.Matrix([[0,0,0],[-s.Rational(5,12),s.Rational(1,3),s.Rational(1,12)],[s.Rational(1,12),-s.Rational(2,3),s.Rational(7,12)]]),'stiff sweep matrix')
check(binfty==s.Matrix([1,0,0]),'stiff affine forcing')
fix=s.Matrix([1,-s.Rational(1,2),1])
check(Ginfty*fix+binfty==fix,'stiff fixed point')
check(s.simplify(s.trace(Ginfty[1:,1:])-s.Rational(11,12))==0,'stiff trace')
check(s.simplify(Ginfty[1:,1:].det()-s.Rational(1,4))==0,'stiff determinant')

U=s.ones(3,1)
rat=[]
for K in range(1,61):
    U=Ginfty*U+binfty
    rk=U[2]
    rat.append(rk)
    if K==1: check(rk==0,'first stiff output')
    if K==2: check(rk==s.Rational(1,12),'second stiff output')
    if K>=3:
        check(s.simplify((rk-1)-s.Rational(11,12)*(rat[K-2]-1)+s.Rational(1,4)*(rat[K-3]-1))==0, 'second-order recurrence K='+str(K))
    if K<8:check(0<=rk<1,'first seven sweep stiff limits')
check(rat[7]==s.Rational(35934757,35831808),'eighth sweep exact amplification')
check(rat[7]>1,'first stiff overshoot')
check(rat[15]<1 and rat[23]>1 and rat[39]>1,'later strict sign reversals')

for zz in [s.Rational(-1),s.Rational(-2),s.Rational(-10),s.Rational(-5000)]:
    u=s.ones(3,1)
    for K in range(1,9):
        previous=u
        w=(b.subs(z,zz)+G.subs(z,zz)*u)
        # Independent direct backward-Euler triangular solve, not matrix multiplication.
        rhs1=1+zz*sum((Q[1,j]-D[1,j])*previous[j] for j in range(3))
        v1=s.cancel(rhs1/(1-zz/2))
        rhs2=1+zz*sum((Q[2,j]-D[2,j])*previous[j] for j in range(3)) + zz*v1/2
        v2=s.cancel(rhs2/(1-zz/2))
        direct=s.Matrix([1,v1,v2])
        check(direct==w,'independent stage solve K='+str(K))
        u=w
    if zz==-5000: check(u[2]>1,'finite exact scalar-decay instability witness')

print('VERIFIED: %d exact assertions' % checks)
print('R_8(-infinity) =', rat[7], '; R_8(-infinity)-1 =', rat[7]-1)
print('R_8(-5000) > 1: checked exactly')
print('Infinite density conclusion follows by the analytic irrational-rotation proof, not enumeration.')
