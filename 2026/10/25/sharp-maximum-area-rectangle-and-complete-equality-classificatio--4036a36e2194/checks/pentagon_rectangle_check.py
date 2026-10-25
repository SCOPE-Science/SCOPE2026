"""Exact identities and supplementary orientation sampling for the regular-pentagon rectangle theorem.
No computational sampling is used as a substitute for the general inequality proof.
"""
import sympy as sp
import math
from scipy.optimize import minimize

pi=sp.pi
phi=(1+sp.sqrt(5))/2
r=sp.cos(pi/5)
ns=[sp.Matrix([sp.cos(pi/2+2*j*pi/5),sp.sin(pi/2+2*j*pi/5)]) for j in range(5)]
for vec in [ns[0]+ns[1]+phi*ns[3], phi*ns[1]+ns[3]+ns[4]]:
    assert all(sp.simplify(z)==0 for z in vec)

# On 0<=theta<=pi/10 these are precisely the signs of the absolute scalar products.
T=sp.symbols('T',real=True)
theta=T+pi/20
alpha=sp.sin(theta)+sp.cos(pi/10+theta)+phi*sp.cos(3*pi/10+theta)
beta=sp.cos(theta)+sp.cos(2*pi/5-theta)+phi*sp.cos(pi/5-theta)
gamma=phi*sp.cos(pi/10+theta)+sp.cos(3*pi/10+theta)+sp.cos(pi/10-theta)
delta=phi*sp.cos(2*pi/5-theta)+sp.cos(pi/5-theta)+sp.cos(2*pi/5+theta)
expected=[2*sp.cos(T+3*pi/20),2*phi*sp.cos(T-3*pi/20),
          2*phi*sp.cos(T+3*pi/20),2*sp.cos(T-3*pi/20)]
for actual,target in zip([alpha,beta,gamma,delta],expected):
    # Both are linear combinations of cos(T),sin(T): compare constant and derivative at 0.
    assert sp.simplify((actual-target).subs(T,0))==0
    assert sp.simplify(sp.diff(actual-target,T).subs(T,0))==0

assert sp.simplify((2+phi)*r/(1+phi)-sp.sqrt(5)/2)==0
max_area=sp.Rational(5,4)/(sp.cos(pi/5)*sp.cos(pi/10))
assert sp.simplify(max_area-(5-sp.sqrt(5))*sp.sin(pi/5))==0
halfwidth=sp.sin(pi/5)
halfheight=(5-sp.sqrt(5))/4
center=sp.Matrix([0,r-halfheight])
for normal in ns:
    slack=sp.simplify(r-normal.dot(center)-halfwidth*sp.Abs(normal[0])-halfheight*sp.Abs(normal[1]))
    assert slack==0,slack
assert sp.simplify(4*halfwidth*halfheight-max_area)==0

# Supplemental numerical finite sample only: independent constrained optimization at orientations.
import numpy as np
N=np.asarray([[float(v) for v in n] for n in ns])
rad=float(r)
for degree in range(0,19):
    th=np.deg2rad(degree)
    u=np.array([np.cos(th),np.sin(th)])
    v=np.array([-np.sin(th),np.cos(th)])
    C=np.column_stack([N,abs(N@u),abs(N@v)])
    def fun(z): return -np.log(z[2])-np.log(z[3])
    z=minimize(fun,[0,0,.59,.66],method='SLSQP',bounds=[(-2,2),(-2,2),(1e-5,2),(1e-5,2)],
               constraints=[{'type':'ineq','fun':lambda zz: rad-C@zz}],options={'ftol':1e-11,'maxiter':250})
    assert z.success,(degree,z.message)
    area=4*np.exp(-z.fun)
    assert area <= float(max_area)+1e-7,(degree,area)
    assert np.min(rad-C@z.x)>-1e-7

print('PASS: exact vector/angle/constant/construction checks; 19 supplemental optimizations')
print('maximum area',sp.simplify(max_area),float(max_area))
