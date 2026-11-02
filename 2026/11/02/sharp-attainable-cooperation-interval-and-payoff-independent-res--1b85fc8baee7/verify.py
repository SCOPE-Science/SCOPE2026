"""Checks for the logistic eco-evolutionary payoff reachability theorem.
Run: python verify.py (requires sympy, scipy, numpy).
These finite checks supplement, but do not replace, the analytical argument.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

x, n, N, K = sp.symbols('x n N K', positive=True)
u=sp.symbols('u0:4'); v=sp.symbols('v0:4')
U0=sp.Matrix(2,2,u); U1=sp.Matrix(2,2,v)
U=(1-n)*U0+n*U1
row=sp.Matrix([x,1-x])
fC=(U.row(0)*row)[0]; fD=(U.row(1)*row)[0]
fbar=sp.expand(x*fC+(1-x)*fD)
dN=N*(1-N/K)*fbar
dx=x*(1-x)*(1-N/K)*(fC-fD)
assert sp.simplify(x*dN+N*dx-N*x*(1-N/K)*fC)==0
assert sp.simplify((1-x)*dN-N*dx-N*(1-x)*(1-N/K)*fD)==0
print('Symbolic strategy-number differential identities: PASS')

z=(sp.sqrt(17)-1)/2
assert sp.simplify(z*z+z-4)==0
hi=sp.simplify(z*z/4); lo=sp.simplify(z/4)
assert (hi>sp.Rational(1,2))==True
assert (lo<sp.Rational(1,2))==True
assert sp.simplify(hi+lo-1)==0
print('Exact row-constant opposite-outcome witness:',hi,lo)

p0=sp.Rational(1,8); q0=sp.Rational(3,8)
assert sp.simplify(p0*sp.exp(sp.log(4))+q0*sp.exp(sp.log(sp.Rational(4,3)))-1)==0
assert sp.simplify(p0*sp.exp(sp.log(4))-sp.Rational(1,2))==0
print('Exact nonstationary critical limit witness: PASS')

Kval=1.0; N0=.5; x0=.5; n0=.5; theta=1.0; eps=.2
U1val=np.array([[4.,1.],[4.5,1.25]])

def run(U0val):
    def rhs(t,z):
        P,Q,h=z
        N=P+Q; x=P/N
        U=(1-h)*U0val+h*U1val
        fitness=U@np.array([x,1-x])
        return [(1-N/Kval)*P*fitness[0],(1-N/Kval)*Q*fitness[1],eps*((1+theta)*x-1)*h*(1-h)]
    z0=[N0*x0,N0*(1-x0),n0]
    sol=solve_ivp(rhs,[0,500],z0,rtol=1e-10,atol=1e-12,max_step=.5)
    P,Q,h=sol.y[:,-1]
    xi=P/(P+Q)
    assert P>z0[0] and Q>z0[1]
    assert .25<xi<.75
    assert abs(P+Q-1)<5e-10
    return xi,h
high=run(np.array([[1000.,1000.],[100.,100.]]))
low=run(np.array([[100.,100.],[1000.,1000.]]))
assert high[0]>.5 and high[1]>.999
assert low[0]<.5 and low[1]<.001
print('Fixed rich-state PD payoff, opposite resource outcomes:',high,low)
print('All checks passed.')
