#!/usr/bin/env python3
"""Exact symbolic and finite-rational checks for scalar stochastic heavy-ball stability.

Requires Python 3 and SymPy. Finite checks corroborate (but never replace) the
analytic all-distribution, all-iteration proof.
"""
from fractions import Fraction as F
from itertools import product
import sympy as s

b, mu, eta, sig2, x, y = s.symbols('b mu eta sig2 x y', real=True)
m = 1+b-eta*mu
T = s.Matrix([[m*m+eta*eta*sig2,-2*b*m,b*b],[m,-b,0],[1,0,0]])
crit_drift = eta*(2*mu*(1-b)-eta*((1-b)/(1+b)*mu*mu+sig2))
assert s.simplify((s.eye(3)-T).det()-(1+b)*crit_drift)==0
P = s.Matrix([[1,-b*m/(1+b)],[-b*m/(1+b),b*b]])
assert s.simplify(P.det()-b*b*eta*mu*(2*(1+b)-eta*mu)/(1+b)**2)==0
znext=(m*x-b*y)
E_Vnext=znext*znext+eta*eta*sig2*x*x-2*b*m/(1+b)*znext*x+b*b*x*x
V=(s.Matrix([[x,y]])*P*s.Matrix([x,y]))[0]
assert s.simplify(E_Vnext-V+crit_drift*x*x)==0
r=s.symbols('r',positive=True)
q=s.symbols('q',real=True)
ceiling=2*(1-b*b)/(1+r*r+(r*r-1)*b)
assert s.simplify(s.diff(ceiling,b)+2*(b*r-b+r+1)*(b*r+b+r-1)/(b*r*r-b+r*r+1)**2)==0
assert s.simplify(ceiling.subs(b,(1-r)/(1+r))-4/(1+r)**2)==0
assert s.simplify(ceiling.subs(b,0)-2/(1+r*r))==0
assert s.simplify(ceiling.subs({b:F(1,2),r:F(1,3)})-F(9,4))==0

# Independent exact conditional-expectation computations from the random update,
# with several positive-curvature sampling laws and deterministic starts.
laws=[[(F(1,1),F(1,1))],[(F(1,1),F(1,2)),(F(2,1),F(1,2))],
      [(F(1,1),F(3,4)),(F(9,1),F(1,4))],
      [(F(1,4),F(1,2)),(F(3,4),F(1,4)),(F(7,4),F(1,4))]]
steps=[F(1,20),F(1,6),F(2,5),F(3,5),F(1,1),F(3,2),F(12,5)]
betas=[F(0),F(1,10),F(1,3),F(1,2),F(3,4),F(9,10)]
starts=[(F(u),F(v)) for u,v in product(range(-2,3),repeat=2)]
checks=0
for law in laws:
    assert sum(p for _,p in law)==1
    muv=sum(a*p for a,p in law)
    variance=sum((a-muv)**2*p for a,p in law)
    for h,be in product(steps,betas):
        mm=1+be-h*muv
        if be == 0:
            c0=sum(p*(1-h*a)**2 for a,p in law)
            assert c0==1-2*h*muv+h*h*(muv*muv+variance)
            checks+=1
            continue
        e=2*be*mm/(1+be)
        D=h*(2*muv*(1-be)-h*((1-be)/(1+be)*muv*muv+variance))
        for X,Y in starts:
            init=X*X-e*X*Y+be*be*Y*Y
            res=sum(p*((1+be-h*a)*X-be*Y)**2-p*e*((1+be-h*a)*X-be*Y)*X+p*be*be*X*X for a,p in law)
            assert res-init==-D*X*X
            checks+=1
# Specific high-noise example and low-noise improvement.
a,beta=F(1,1),F(1,2)
assert 2*F(3,2)*(1-beta**2)/((1-beta)*F(9,4)+(1+beta)*F(1,4))==F(3,2)  # mu=3/2, variance=1/4
# threshold of iid {1,2}, eta=3/2; eta at zero momentum = 6/5
assert 2*F(3,2)/F(5,2)==F(6,5)
# For A in {1,9} with p={3/4,1/4}: mu=3, var=12 -> CV²=4/3 > 1.
assert (F(3,4)*(F(1)-3)**2+F(1,4)*(F(9)-3)**2)/F(9)==F(4,3)
print('VERIFY_OK exact_drift_and_transfer symbolic; rational_cases=',checks)
