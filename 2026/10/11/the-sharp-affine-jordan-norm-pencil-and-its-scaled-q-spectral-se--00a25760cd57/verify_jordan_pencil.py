"""Exact symbolic identities and finite matrix checks for a Jordan norm pencil.

Requires Python 3, SymPy and NumPy. All-dimensional claims are proved
analytically in the accompanying RESULT.md, not by this script.
"""
from sympy import Matrix, Rational, Symbol, symbols, factor, simplify, sqrt
import numpy as np

n,z = symbols('n z', integer=True, positive=True)
M=2*n+1
L=n*n+(n+1)**2+2*n*(n+1)*z
r=(n+1)/n
S0=M/4*(1-1/L)
S1=n*z/2+(r+z)*n*n/(2*L)
x1sq=n*n*(1-z*z)/L
assert simplify(S0-S1-(n+1)*x1sq)==0

for k in range(2,10):
    J=Matrix.zeros(k)
    for j in range(k-1):J[j,j+1]=1
    Q=(k*Matrix.eye(k)+(k+1)*J).T*(k*Matrix.eye(k)+(k+1)*J)
    W=Matrix.zeros(k)
    for j in range(k-1):
        a=k-j;b=k-j-1
        vec=Matrix.zeros(k,1)
        vec[j]=Rational(1,a)
        vec[j+1]=Rational(1,b)
        W+=k*(k+1)*a*b*vec*vec.T
    assert Q-Matrix.eye(k)==W
    v=Matrix([(-1)**j*(k-j) for j in range(k)])
    assert (Q-Matrix.eye(k))*v==Matrix.zeros(k,1)
    P=Q.charpoly().as_expr()
    assert simplify(P.subs(Q.charpoly().gen,1))==0
    m=2*k+1
    assert all(v>0 for v in np.linalg.eigvalsh(np.array(Q,float))[1:]-1)
    Jn=np.diag(np.ones(k-1),1)
    s0=(k+1)/(2*k+1)
    B0=(1-s0)*np.eye(k)+s0*Jn
    u,ss,vt=np.linalg.svd(B0)
    x=vt[0,:]
    assert abs(np.vdot(B0@x,(Jn-np.eye(k))@x))<1e-9
    vbest=np.linalg.norm(B0,2)
    for s in [-0.2,0,0.1,0.4,0.5,0.75,1,1.6,2]:
        assert np.linalg.norm((1-s)*np.eye(k)+s*Jn,2)>=vbest-1e-11

J2=Matrix([[0,1],[0,0]])
J3=Matrix([[0,1,0],[0,0,1],[0,0,0]])
assert (2*Matrix.eye(2)+3*J2).T*(2*Matrix.eye(2)+3*J2)!=Matrix.zeros(2)
Q2=(2*Matrix.eye(2)+3*J2).T*(2*Matrix.eye(2)+3*J2)
Q3=(3*Matrix.eye(3)+4*J3).T*(3*Matrix.eye(3)+4*J3)
t=Symbol('t')
assert factor(Q2.charpoly(t).as_expr())==(t-1)*(t-16)
assert factor(Q3.charpoly(t).as_expr())==(t-1)*(t*t-58*t+729)
print('JORDAN_PENCIL_EXACT_GRAM_AND_TRIG_IDENTITY_OK')
print('JORDAN_PENCIL_NUMERIC_SINGULAR_STATIONARITY_OK')
