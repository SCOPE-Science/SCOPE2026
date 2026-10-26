"""Reproducibility checks for exact friction-budget optimization in a free Langevin dimer.
Run: python CHECK.py (requires sympy, numpy, scipy).
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import solve_continuous_lyapunov
from scipy.optimize import minimize_scalar

x, r, k, G, m, dt = sp.symbols('x r k G m dt',positive=True,real=True)
f = x*(1-x)*(1+(r-1)*x)/(1+(r*r-1)*x)
N = sp.cancel(sp.diff(f,x)*(1+(r*r-1)*x)**2).expand()
assert sp.simplify(N.subs(x,sp.Rational(1,2)) +r*(r-1)/4) == 0 or sp.simplify(sp.diff(f,x).subs(x,sp.Rational(1,2)) + r*(r-1)/(r*r+1)**2)==0
assert sp.factor(sp.resultant(N,sp.diff(N,r),x)) == -2*r**4*(r-1)**2*(9*r**2-32*r+9)
assert sp.factor(sp.resultant(N,sp.diff(N,r),r)) == -x**6*(x-1)**4*(2*x-1)*(112*x*x-112*x+27)
r0=(sp.Integer(16)+5*sp.sqrt(7))/9
x0=sp.Rational(1,2)-sp.sqrt(7)/28
assert sp.simplify(N.subs({x:x0,r:r0}))==0
assert sp.simplify(sp.diff(N,r).subs({x:x0,r:r0}))==0
assert sp.simplify(N.subs({x:sp.Rational(1,2),r:1}))==0

m1,m2,g1,g2,T1,T2=sp.symbols('m1 m2 g1 g2 T1 T2', positive=True)
A=sp.Matrix([[0,1,-1],[-k/m1,-g1/m1,0],[k/m2,0,-g2/m2]])
B=sp.diag(0,2*g1*T1/m1**2,2*g2*T2/m2**2)
c=g1*g2*(T1-T2)*(g1*m2+g2*m1)/((g1+g2)*(g1*g2*(g1*m2+g2*m1)+k*(g1*m2*m2+g2*m1*m1)))
z=k*c*(m1-m2)/(g1*m2+g2*m1)
p1=T1/m1-k*c/g1
p2=T2/m2+k*c/g2
var_y=(m1*(p1-z)-g1*c)/k
C=sp.Matrix([[var_y,c,c],[c,p1,z],[c,z,p2]])
res=A*C+C*A.T+B
assert all(sp.cancel(v)==0 for v in res)
# The current is k*c; its fixed-friction expression must be monotone in f.
F=f/m
J=dt*k*G*F/(G*G*F+k)
assert sp.simplify((k*c).subs({g1:G*x,g2:G*(1-x),m1:m,m2:r*m,T1:T2+dt})-J)==0

rng=np.random.default_rng(270416)
for _ in range(340):
    m1v,m2v=10**rng.uniform(-2,2,size=2)
    kv,Gv=10**rng.uniform(-2,2,size=2)
    T1v=2.0; T2v=0.7
    xv=float(rng.uniform(.02,.98)); g1v=Gv*xv; g2v=Gv*(1-xv)
    Av=np.array([[0,1,-1],[-kv/m1v,-g1v/m1v,0],[kv/m2v,0,-g2v/m2v]],float)
    Dv=np.diag([0,2*g1v*T1v/m1v**2,2*g2v*T2v/m2v**2])
    Cv=solve_continuous_lyapunov(Av,-Dv)
    exact=(T1v-T2v)*kv*g1v*g2v*(g1v*m2v+g2v*m1v)/((g1v+g2v)*(g1v*g2v*(g1v*m2v+g2v*m1v)+kv*(g1v*m2v**2+g2v*m1v**2)))
    np.testing.assert_allclose(kv*Cv[0,2],exact,rtol=1e-7,atol=1e-8)
    assert np.linalg.norm(Av@Cv+Cv@Av.T+Dv)<1e-7*max(1,np.linalg.norm(Dv))
for rv in list(np.logspace(-4,4,160))+[float(r0),1.0,float(1/r0)]:
    fun=lambda xv: xv*(1-xv)*(1+(rv-1)*xv)/(1+(rv*rv-1)*xv)
    opt=minimize_scalar(lambda a:-fun(a),method='bounded',bounds=(0,1),options={'xatol':1e-14})
    assert opt.success
    xv=opt.x
    assert abs(xv-.5)<float(sp.sqrt(7)/28)+4e-7
    if rv>1+1e-9:assert xv<.5+1e-7
    if rv<1-1e-9:assert xv>.5-1e-7
    for q in [0.002,0.05,0.25,0.5,0.75,0.95,0.998]: assert fun(xv)+1e-13>=fun(q)
assert abs(minimize_scalar(lambda a:-a*(1-a)*(1+(float(r0)-1)*a)/(1+(float(r0)**2-1)*a),bounds=(0,1),method='bounded',options={'xatol':1e-14}).x-float(x0))<1e-7
print('PASS: 7 exact symbolic assertions; 340 independent 3x3 Lyapunov cases; 163 optimization families and sharp extremizers.')
