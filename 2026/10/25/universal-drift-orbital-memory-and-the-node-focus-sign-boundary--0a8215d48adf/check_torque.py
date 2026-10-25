"""Independent exact-and-numerical checks for planar OU drift angular activity.

Run with: python check_torque.py
Dependencies: SymPy, NumPy, SciPy. All assertions are deterministic.
"""
from __future__ import annotations
import math
import numpy as np
import sympy as sp
from scipy.linalg import solve_continuous_lyapunov, expm

checks=0
def check(b):
    global checks
    assert b
    checks+=1

a,b,c,d,dx,dy,w=sp.symbols('a b c d dx dy w',real=True)
H=sp.Matrix([[a,b],[c,d]])
Q=sp.Matrix([[-c,(a-d)/2],[(a-d)/2,b]])
check(sp.simplify(H.T*Q+Q*H-sp.trace(H)*Q)==sp.zeros(2))
check(sp.simplify(sp.det(Q)-(sp.det(H)-sp.trace(H)**2/4))==0)
x,y=sp.symbols('x y')
z=sp.Matrix([x,y]); f=sp.expand((z.T*Q*z)[0])
check(sp.expand(f-(x*(-H*z)[1]+(-y)*(-H*z)[0]))==0)
check(sp.factor(sp.diff(f,x)*(-H*z)[0]+sp.diff(f,y)*(-H*z)[1]+sp.trace(H)*f)==0)
# Arbitrary positive definite noise D yields constant generator shift.
D=sp.Matrix([[dx,w],[w,dy]])
Lconst=sp.expand(D[0,0]*sp.diff(f,x,2)+2*D[0,1]*sp.diff(f,x,y)+D[1,1]*sp.diff(f,y,2))
check(sp.simplify(Lconst-2*sp.trace(D*Q))==0)

systems=[
    (sp.Matrix([[2,sp.Rational(1,2)],[sp.Rational(1,2),1]]),sp.Matrix([[2,sp.Rational(1,4)],[sp.Rational(1,4),3]]),'node'),
    (sp.Matrix([[2,-2],[1,2]]),sp.Matrix([[3,sp.Rational(1,3)],[sp.Rational(1,3),2]]),'focus'),
    (sp.Matrix([[1,1],[0,1]]),sp.diag(1,2),'double'),
    (sp.Matrix([[2,0],[0,2]]),sp.diag(1,2),'scalar'),
    (sp.Matrix([[1,1],[0,2]]),sp.diag(1,1),'node_nonsymmetric'),
]
for B,N,label in systems:
    qq=sp.Matrix([[-B[1,0],(B[0,0]-B[1,1])/2],[(B[0,0]-B[1,1])/2,B[0,1]]])
    u,v,k=sp.symbols('u v k',real=True)
    C=sp.Matrix([[u,v],[v,k]])
    sol=sp.solve(list(B*C+C*B.T-2*N),(u,v,k),rational=True)
    check(len(sol)==3)
    C=C.subs(sol)
    check(B*C+C*B.T==2*N)
    check(sp.det(C)>0)
    mean=sp.trace(qq*C)
    variance=sp.simplify(2*sp.trace(qq*C*qq*C))
    check(variance>0 if label!='scalar' else variance==0)
    check(sp.simplify(sp.trace(B)*mean-2*sp.trace(N*qq))==0)
    check(sp.simplify(sp.det(qq)-sp.det(B)+sp.trace(B)**2/4)==0)
    discriminant=sp.trace(B)**2-4*sp.det(B)
    check(sp.sign(sp.det(qq))==-sp.sign(discriminant))
    # Two mathematically independent covariance calculations: Gaussian Wick
    # and the eigenfunction propagation law.
    BB=np.array(B,float)
    Cnum=np.array(C,float)
    Qnum=np.array(qq,float)
    for t in (0.0,.125,.55,1.25):
        c12=Cnum@expm(-BB.T*t)  # Cov(X_0,X_t) = C exp(-H^T t)
        wick=2*np.trace(Qnum@c12@Qnum@c12.T)
        predicted=float(variance)*np.exp(-float(sp.trace(B))*t)
        check(abs(wick-predicted)<5e-11*(1+abs(predicted)))
    if label=='node' or label=='node_nonsymmetric':
        check(float(sp.det(qq))<0)
    if label=='focus':
        check(float(sp.det(qq))>0)
    if label=='double':
        check(sp.det(qq)==0 and qq!=sp.zeros(2))
    if label=='scalar':
        check(qq==sp.zeros(2))
    # Quadratic Gaussian characteristic function: log determinant derivative.
    s=sp.symbols('s',real=True)
    normdet=sp.det(sp.eye(2)-2*sp.I*s*C*qq)
    expected=1-2*sp.I*s*mean-4*s*s*sp.det(C)*sp.det(qq)
    check(sp.expand(normdet-expected)==0)

# A dissipatively coupled Brownian ellipsoid has an exact raw drift term.
a,e,dx,dy=sp.symbols('a e dx dy',real=True,positive=True)
B=a*sp.Matrix([[1,e],[e,1]]);N=sp.diag(dx,dy)
u,v,k=sp.symbols('u v k')
C=sp.Matrix([[u,v],[v,k]])
sol=sp.solve(list(B*C+C*B.T-2*N),(u,v,k))
C=C.subs(sol)
Q=sp.Matrix([[-a*e,0],[0,a*e]])
mean=sp.factor(sp.trace(Q*C))
var=sp.factor(2*sp.trace(Q*C*Q*C))
check(sp.simplify(mean+e*(dx-dy))==0)  # H symmetric coupling: torque a e(y^2-x^2)
check(sp.simplify(var-e**2*((dx+dy)**2/(1-e**2)+(dx-dy)**2))==0)
check(sp.simplify(sp.limit((1-e**2)*var,e,1)-(dx+dy)**2)==0)
check(sp.limit(sp.sqrt(1-e**2)*mean,e,1)==0)
# Explicit covariance decomposition in slow/fast eigenbasis.
R=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
Crot=sp.simplify(R.T*C*R)
check(sp.simplify(sp.limit(Crot[0,0],e,1)-(dx+dy)/(4*a))==0)
check(sp.simplify(sp.limit((1-e**2)*Crot[1,1],e,1)-(dx+dy)/a)==0)
check(sp.simplify(sp.limit(sp.sqrt(1-e**2)*Crot[0,1],e,1))==0)

if __name__=='__main__':
    print('PASS: %d deterministic exact, independent Wick-matrix and limiting checks'%checks)
