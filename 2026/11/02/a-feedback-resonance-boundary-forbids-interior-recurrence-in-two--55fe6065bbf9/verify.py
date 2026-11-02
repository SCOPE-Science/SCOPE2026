#!/usr/bin/env python3
"""Reproduce exact environmental-log-odds balance and finite-time tests.
Requires Python 3.10+, sympy, numpy, scipy. No external files or network.
"""
from fractions import Fraction as F
from math import log
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

x,y,n1,n2,n12,t1,t2,t12=sp.symbols('x y n1 n2 n12 t1 t2 t12', real=True)
L=lambda n: sp.log(n/(1-n))
a=(1+t12)/(2*(1+t1))
b=(1+t12)/(2*(1+t2))
k=(1+t12)*sp.Rational(1,2)*(1/(1+t1)+1/(1+t2))-1
# Exact directional derivative, expressed without numerical differentiation.
D=sp.diff(L(n12),n12)*n12*(1-n12)*((1+t12)*(x+y)/2-1)
D-=a*sp.diff(L(n1),n1)*n1*(1-n1)*((1+t1)*x-1)
D-=b*sp.diff(L(n2),n2)*n2*(1-n2)*((1+t2)*y-1)
assert sp.simplify(D-k)==0
res=(t1+t2+2*t1*t2)/(2+t1+t2)
assert sp.simplify(k.subs(t12,res))==0

# The two reported feedback choices from Fig. 8 of the source paper.
for q,expected in [((F(3),F(5),F(8)),F(7,8)),
                   ((F(3,10),F(2,5),F(9,20)),F(55,728)),
                   ((F(1),F(3),F(5,3)),F(0))]:
    aa=(1+q[2])/(2*(1+q[0]))
    bb=(1+q[2])/(2*(1+q[1]))
    kk=(1+q[2])/2*(1/(1+q[0])+1/(1+q[1]))-1
    assert kk==expected, (q,kk)
    print('feedbacks',q,'weights',aa,bb,'drift',kk)

# An admissible whole line of strictly interior equilibria at resonance.
# The depleted and rich payoff matrices are respectively
# [[2,2],[1,1]] and [[1,1],[2,2]], hence payoff gaps 1-2*n.
# Mixing delta=1/2; interior strategies x=1/2, y=1/4.
u=sp.symbols('u',real=True)
xx,yy=sp.Rational(1,2),sp.Rational(1,4)
N1=N2=1-u; N12=u
delta=sp.Rational(1,2)
fx=xx*(1-xx)*(1-2*((1-delta)*N1+delta*N12))
fy=yy*(1-yy)*(1-2*((1-delta)*N2+delta*N12))
fn1=N1*(1-N1)*((1+1)*xx-1)
fn2=N2*(1-N2)*((1+3)*yy-1)
fn12=N12*(1-N12)*((1+sp.Rational(5,3))*(xx+yy)/2-1)
assert all(sp.simplify(q)==0 for q in (fx,fy,fn1,fn2,fn12))
print('exact equilibrium line verified for every 0<u<1')

# Independent time-integration check with admissible game matrices;
# analytical proof does not rely on this experiment.
th1,th2,th12=0.3,0.4,0.45
mix=0.35
A0=np.array([[2.0,2.0],[1.0,1.0]])
A1=np.array([[1.0,1.0],[2.0,2.0]])
def rhs(_,s):
    xx,yy,e1,e2,e12=s
    p=lambda e:(1-e)*A0+e*A1
    p1=(1-mix)*p(e1) @ np.array([xx,1-xx]) + mix*p(e12) @ np.array([yy,1-yy])
    p2=(1-mix)*p(e2) @ np.array([yy,1-yy]) + mix*p(e12) @ np.array([xx,1-xx])
    return [xx*(1-xx)*(p1[0]-p1[1]),yy*(1-yy)*(p2[0]-p2[1]),
            e1*(1-e1)*((1+th1)*xx-1),e2*(1-e2)*((1+th2)*yy-1),
            e12*(1-e12)*((1+th12)*(xx+yy)/2-1)]
y0=[.5,.5,.5,.5,.5]
sol=solve_ivp(rhs,[0,10],y0,rtol=1e-12,atol=1e-13,dense_output=True)
assert sol.success
A=(1+th12)/(2*(1+th1));B=(1+th12)/(2*(1+th2))
K=(1+th12)/2*(1/(1+th1)+1/(1+th2))-1
Z=sol.sol(np.linspace(0,10,101))
I=lambda z: log(z[4]/(1-z[4]))-A*log(z[2]/(1-z[2]))-B*log(z[3]/(1-z[3]))
err=max(abs(I(Z[:,j])-I(Z[:,0])-K*(10*j/100)) for j in range(101))
assert err < 1e-8, err
print('max time-integrated affine-drift residual',f'{err:.4e}')
print('all checks passed')
