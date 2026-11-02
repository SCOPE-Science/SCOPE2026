"""Reproducible numerical and symbolic checks for the temporal three-body game theorem.
Run: python verify.py ; needs scipy >=1.10, sympy >=1.10, numpy >=1.24.
Numerical checks illustrate, but do not replace, the analytic proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

x,d=sp.symbols('x d', real=True)
S=sp.Rational(-1,2); T=sp.Rational(3,2); a=sp.Integer(5)
b=T-S-1; c=a+b
source_payoff_difference=-x*x*c*d+x*(c*d-b-2*S)+S
assert sp.simplify(source_payoff_difference-(6*d*x*(1-x)-sp.Rational(1,2)))==0
print('SOURCE-PAYOFF ALGEBRA: PASS', source_payoff_difference)

# Integrate logit dynamics and its first-variation equation.
def run(z0,mu,eta,omega,half=False,trajectory=False):
    T=2*math.pi/omega
    stop=T/2 if half else T
    def rhs(t,Z):
        y,v=Z
        g=1/math.cosh(y/2)**2
        h=math.tanh(y/2)
        A=0.5+1.5*(mu+eta*math.cos(omega*t))
        return [A*g-0.5, -A*g*h*v]
    if trajectory:
        times=np.linspace(0,stop,1601)
        sol=solve_ivp(rhs,(0,stop),(z0,1.),t_eval=times,atol=2e-12,rtol=2e-12)
    else:
        sol=solve_ivp(rhs,(0,stop),(z0,1.),atol=2e-12,rtol=2e-12)
    assert sol.success
    return sol

def shoot(eta,omega):
    f=lambda mu:run(0.,mu,eta,omega,half=True).y[0,-1]
    # Positive harmonic forcing is used, so the true root is positive and small.
    m=brentq(f,0.,0.1,xtol=1e-14)
    res=run(0.,m,eta,omega)
    # The exactly symmetric fold crosses logit zero at phase t=0,
    # has both half-period and full-period return, and unit multiplier.
    assert abs(res.y[0,-1])<2e-9,(eta,omega,res.y[0,-1])
    assert abs(res.y[1,-1]-1)<2e-9,(eta,omega,res.y[1,-1])
    return m

for omega in [0.7,1.,2.]:
    for eta in [0.02,0.05,0.1]:
        m=shoot(eta,omega)
        predicted=3*eta**2/(32*omega**2)
        assert m>0 and abs(m/predicted-1)<0.006
        print('FOLD omega eta mean_fraction actual_shift leading_ratio:',
              omega,eta,format(1/3+m,'.12f'),format(m/predicted,'.9f'))

# For a sample above the fold there are two interior period orbits,
# a lower repeller and an upper attractor in logit coordinate.
omega=1.; eta=0.05; shift=shoot(eta,omega)
mu=shift+0.0002
D=lambda z:run(z,mu,eta,omega).y[0,-1]-z
low=brentq(D,-0.5,0.,xtol=1e-12)
high=brentq(D,0.,0.5,xtol=1e-12)
assert low<0<high
for z,typ in [(low,'unstable'),(high,'stable')]:
    sol=run(z,mu,eta,omega,trajectory=True)
    mult=sol.y[1,-1]
    assert (mult>1 if typ=='unstable' else 0<mult<1)
    y=sol.y[0,:]
    xtraj=1/(1+np.exp(-y))
    dtraj=1/3+mu+eta*np.cos(omega*sol.t)
    weighted=np.trapezoid(dtraj*(2*xtraj-1)**2,sol.t)/(2*math.pi)
    assert abs(weighted-mu)<1e-8, (weighted,mu)
    print('PERIODIC-ORBIT:',typ,'logit_at_phase_zero',z,'multiplier',mult,
          'budget_residual',weighted-mu)

# Critical endpoint for zero forcing is semistable, not globally extinct.
for start in [-0.3,0.3]:
    sol=run(start,0,0,1)
    assert sol.y[0,-1]<start and (sol.y[0,-1]>0 if start>0 else sol.y[0,-1]<0)
print('CRITICAL CONSTANT-FORCING BOUNDARY: PASS')
print('ALL CHECKS PASSED')
