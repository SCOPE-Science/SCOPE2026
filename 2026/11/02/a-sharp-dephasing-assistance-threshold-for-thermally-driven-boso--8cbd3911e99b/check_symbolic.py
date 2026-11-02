"""Exact algebraic substitution into the Lindblad second-moment equations.

Run: python check_symbolic.py
Requires sympy. This uses symbolic parameters and all nine covariance entries.
"""
import sympy as s
J,k,D,g,NL,NR=s.symbols('J k D g NL NR', positive=True, real=True)
t=4*J**2+k*(k+g)
B=t**2+4*D**2*k**2
q=NL-NR
x=J*k*q*t/B
u=-2*D*J*k**2*q/B
z=-4*D*J**2*k*q/B
C=s.Matrix([[NL-2*J*x/k,u+s.I*x,s.I*z],
            [u-s.I*x,(NL+NR)/2,-u+s.I*x],
            [-s.I*z,-u-s.I*x,NR+2*J*x/k]])
h=s.Matrix([[0,J,0],[J,D,J],[0,J,0]])
E=-s.I*(h*C-C*h)
for i in range(3):
    for j in range(3):
        E[i,j]-= ((k if i in (0,2) else 0) + (k if j in (0,2) else 0))*C[i,j]/2
        if i!=j and (i==1 or j==1):
            E[i,j]-=g*C[i,j]/2
E[0,0]+=k*NL;E[2,2]+=k*NR
for e in E:
    assert s.factor(e)==0,s.factor(e)
print('PASS: exact zero residual in all 9 second-moment equations')
