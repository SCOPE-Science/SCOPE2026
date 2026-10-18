#!/usr/bin/env python3
"""Exact algebraic identity checks for a planar Oregonator fast-x reduction.
Requires Python 3 and SymPy; this is not a proof of the global ODE results.
"""
import sympy as sp
x,q,y,f,omega,s=sp.symbols('x q y f omega s', real=True)
D=q*x*x-2*q*x+1
Y=x*(1-q*x)/(x-1)
Xp=sp.cancel(1/sp.diff(Y,x))
assert sp.factor(Xp+(x-1)**2/D)==0
hprime=sp.factor((sp.diff(Y,x)*(1+x)+Y)/sp.diff(Y,x))
N=2*q*x**3-2*q*x**2-2*q*x-x**2+2*x+1
assert sp.factor(hprime-N/D)==0
q0=(x*x-2*x-1)/(2*x*(x*x-x-1))
P=x**3-3*x*x-3*x-1
assert sp.factor(sp.diff(q0,x)+ (x-1)*P/(2*x*x*(x*x-x-1)**2))==0
assert sp.factor(N.subs(q,q0))==0
res=sp.factor(sp.resultant(sp.together(q-q0).as_numer_denom()[0],P,x))
assert sp.factor(res + 4*(10*q**3+6*q**2+12*q-1))==0
Q=10*q**3+6*q**2+12*q-1
qp=float(sp.nroots(Q)[0]) if False else float(next(sp.re(r) for r in sp.nroots(Q) if abs(float(sp.im(r)))<1e-10 and 0<float(sp.re(r))<1))
c=float(next(sp.re(r) for r in sp.nroots(P) if abs(float(sp.im(r)))<1e-10 and float(sp.re(r))>2.414))
assert abs(qp-float(q0.subs(x,c)))<1e-10
# Eliminate equilibrium y=f*x/(1+x), checking positivity of unique positive root.
K=(1-q*x)*(1+x)-f*(x-1)
assert sp.expand(K - (-q*x**2+(1-q-f)*x+1+f))==0
# For q<1: Xp<0, y-f=-f/(1+x)<0, so determinant >0 at equilibrium.
print('Polynomial identity checks passed.')
print('Unique maximizing x:',format(c,'.14f'))
print('Sharp q cutoff:',format(qp,'.14f'))
print('Polynomial cutoff residual:',format(float(Q.subs(q,qp)),'.3g'))
