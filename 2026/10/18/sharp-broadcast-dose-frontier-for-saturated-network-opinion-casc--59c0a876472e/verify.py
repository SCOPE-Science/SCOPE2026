"""Independent numerical and symbolic checks of the broadcast-dose theorem.
Run: python verify.py  (needs scipy and sympy). The proof is analytic; tests do not prove universality.
"""
import math
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, minimize_scalar
import sympy as sp

A=0.5; K=1.0; Q=A/K; BC=A*A/(4*K)
def g(s): return A*s-K*s*s
def switch(b):
    if b >= 1: return 0.0
    z=(-0.5+math.sqrt(0.25+4*(1-b)))/2 # from z^2+0.5 z=1-b
    return min(Q,max(0.0,z))
def T(b):
    return quad(lambda s:max(1/(1-s),1/(b-g(s))),0,Q,epsabs=2e-12,points=[switch(b)] if 0<switch(b)<Q else None)[0]
def E(b): return b*T(b)
bopt=minimize_scalar(E,bounds=(0.51,0.9),method='bounded',options={'xatol':1e-14}).x
D=(1+K-A)*Q+K*Q**2/2+(K-A)*math.log(1-Q)
T0=-math.log(1-Q)
assert abs(D-(0.875+math.log(0.5)/2))<1e-13
assert 0.52<bopt<0.6
assert E(bopt)>D

def der(b):
    z=switch(b)
    return -quad(lambda s:g(s)/(b-g(s))**2,0,z,epsabs=1e-12)[0]+math.log((1-z)/(1-Q))
root=brentq(der,0.501,0.9999,xtol=1e-14)
assert abs(root-bopt)<1e-7
assert abs(der(root))<1e-10
assert all(E(root)<=E(b)+1e-10 for b in (0.08,0.12,0.35,0.50,0.7,0.9,1.0,3.0))

s=sp.symbols('s',real=True); a,k,b=sp.symbols('a k b', positive=True, real=True)
gsym=a*s-k*s*s; c=1-s+gsym; phi=c/(1-s)
assert sp.simplify(b-phi*(b-gsym)-gsym*(c-b)/(1-s))==0
F=(1+k-a)*s+k*s*s/2+(k-a)*sp.log(1-s)
assert sp.simplify(sp.diff(F,s)-phi)==0 and sp.simplify(F.subs(s,0))==0

# Three-node strongly connected row stochastic coupling; uniform pulses must synchronize exactly.
W=[[0.,1.,0.],[0.,0.,1.],[1.,0.,0.]]
mu=gamma=0.25

def sim(b,duration):
    def f(t,x):
        return [-x[i]+min(1,max(0,mu*x[i]+K*x[i]*x[i]+gamma*sum(W[i][j]*x[j] for j in range(3))+b)) for i in range(3)]
    sol=solve_ivp(f,[0,duration],[0.,0.,0.],atol=1e-11,rtol=1e-11)
    return sol.y[:,-1]
for b in (0.08,0.20,root,0.7,1.2):
    tcrit=T(b)
    for mult in (0.99,1.01):
        x=sim(b,tcrit*mult)
        assert max(x)-min(x)<1e-10
        assert (x[0]<Q if mult<1 else x[0]>Q)
# Verify near-minimal shaped input gives exactly scalar fastest trajectory.
def shaped(t,x):
    s0=1-math.exp(-t)
    u=1-(1-A)*s0-K*s0*s0
    return -x[0]+min(1,max(0,(1-A)*x[0]+K*x[0]**2+u))
sol=solve_ivp(shaped,[0,T0],[0],rtol=1e-12,atol=1e-12)
print('shaped',sol.y[0,-1],Q); assert abs(sol.y[0,-1]-Q)<1e-7
print(f'PASS: D*={D:.15f}, optimal rectangle b={root:.15f}, T={T(root):.15f}, rectangular dose={E(root):.15f}; fastest T={T0:.15f}.')
print('PASS: exact symbolic calibration and antiderivative; 10 network pulse crossovers; shaped pulse reaches critical boundary.')
