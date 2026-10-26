"""Standalone exact-algebra and ODE checks for a smooth contact-feedback SIS threshold law.

The program corroborates finite calculations only; proof of global behavior is analytic.
Requires: Python 3, scipy, sympy.
"""
from fractions import Fraction
from math import isfinite
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from sympy import symbols, simplify, diff

x=symbols('x')
examples=[
    ('two_responses',1+x,1-x/2,1,1,.13,.72),
    ('prevalence_breaking',x,1,2,1,.17,.42),
    ('quadratic_breaking',x*x,1,3,1,.2,.55),
    ('slow_turnover',1+x,1-x/2,Fraction(1,20),Fraction(1,20),.3,.34),
]

for name,be,ce,ze,xi,yinit,zinit in examples:
    be=simplify(be); ce=simplify(ce)
    zstar=simplify(xi*ce/(ze*be+xi*ce))
    z0=simplify(zstar.subs(x,0))
    slope=simplify(diff(zstar,x).subs(x,0))
    tau=simplify(1/z0)
    K=simplify(1-tau*slope)
    assert z0>0 and K>=1
    if name in ('two_responses','slow_turnover'):
        assert z0==Fraction(1,2) and slope==Fraction(-3,8) and K==Fraction(7,4)
    if name=='prevalence_breaking':
        assert z0==1 and slope==-2 and K==3
    if name=='quadratic_breaking':
        assert z0==1 and slope==0 and K==1
    b=lambda t:float(be.subs(x,t))
    c=lambda t:float(ce.subs(x,t))
    def rhs(t,u):
        y,z=u
        return [y*(-1+float(tau)*(1-y)*z),-float(ze)*z*b(y)+float(xi)*(1-z)*c(y)]
    end=30000 if name!='slow_turnover' else 40000
    sol=solve_ivp(rhs,(0,end),(yinit,zinit),method='BDF',rtol=2e-11,atol=1e-13,dense_output=True,max_step=100)
    assert sol.success
    yp,zp=sol.y[:,-1]
    a=end*yp; expected=float(1/K)
    d=end*(zp-float(z0)); expected_d=float(slope/K)
    print(name,'K=',K,'critical_prevalence_t_times=',a,'predicted=',expected,'contact_t_times=',d,'predicted=',expected_d)
    assert abs(a-expected)<0.005, (name,a,expected)
    assert abs(d-expected_d)<0.009, (name,d,expected_d)
    if name=='two_responses':
        for r in (0.01,0.002,0.0005):
            tr=float(tau)*(1+r)
            root=brentq(lambda y:tr*(1-y)*float(zstar.subs(x,y))-1,0,.9,xtol=1e-15)
            print('equilibrium_branch',r,root,'normalized',root/r,'asymptotic_slope',float(1/K))
            assert abs(root/r-float(1/K))<.012
print('All critical-tail and onset checks passed.')
