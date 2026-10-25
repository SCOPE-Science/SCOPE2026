"""Reproduce exact stationary-moment identities for a behavioral SIS flow.
This checks algebraic consequences and a numerically approximated stable cycle;
it is not an infinite proof of the invariance statements or cycle existence.
Dependencies: sympy, scipy, numpy.
"""
import math
import sympy as sp
from scipy.integrate import solve_ivp, quad

R, mu, k, z = sp.symbols('R mu k z', positive=True)
m, v, n = sp.symbols('m v n', real=True)
F = (1-m)*(1-(k-2*m)/z)
q = sp.expand(F-mu/R)
# Vieta: sum of roots and product, from the equilibrium polynomial.
sum_roots = (k+2-z)/2
prod_roots = (k-z+z*mu/R)/2
assert sp.simplify(q + 2*(m*m-sum_roots*m+prod_roots)/z) == 0
# Averaged identities imply exact variance-shell factorization.
assert sp.simplify((F-mu/R-2*v/z) + 2*(m*m-sum_roots*m+prod_roots+v)/z) == 0
print('Symbolic factorization: PASS')

r=3.0; u=1.0; K=4.0; Z=9.5
root_plus = float((-21+sp.sqrt(1113))/24)
root_minus=float((-21-sp.sqrt(1113))/24)
y_star=(K-2*root_plus)/Z

def f(t,xy):
 x,y=xy
 return [x*(1-x)*(2*x+Z*y-K), y*(r*(1-x)*(1-y)-u)]

def peak(t,xy):
 x,y=xy
 return 2*x+Z*y-K
peak.direction=-1;peak.terminal=False
sol=solve_ivp(f,(0,1500),(0.6,0.6),rtol=2e-11,atol=1e-13,max_step=0.09,dense_output=True,events=peak)
assert sol.success and len(sol.t_events[0])>3
lo,hi=sol.t_events[0][-2:]
T=hi-lo
averages=[]
for h in [lambda a,b:a,lambda a,b:b,lambda a,b:a*a,lambda a,b:a*b,lambda a,b:(1-a)*(1-b)]:
 integral,_=quad(lambda t:h(*sol.sol(t)),lo,hi,epsabs=5e-10,epsrel=5e-10,limit=1000)
 averages.append(integral/T)
M,N,EX2,EXY,EUV=averages
V=EX2-M*M
Cov=EXY-M*N
checks={
'mean behavioral nullcline':2*M+Z*N-K,
'negative covariance identity':2*V+Z*Cov,
'contact-infection balance':r*EUV-u,
'exact quadratic shell':V-(M-root_minus)*(root_plus-M),
'mean infection premium':(N-y_star)-2*(root_plus-M)/Z,
}
print('cycle period',T,'mean protection',M,'mean infection',N)
print('endemic point',root_plus,y_star,'variance',V,'covariance',Cov)
print('checks',checks)
assert all(abs(e)<1e-6 for e in checks.values())
assert V>1e-3 and Cov<0 and M<root_plus and N>y_star
print('Numerical cycle identities and strict inequalities: PASS')
