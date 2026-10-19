"""Symbolic identities and supplementary numerical checks for a triadic Lotka--Volterra camouflage example.

Run: python verify.py. Requires sympy and scipy.
The accompanying proof, not these finite checks, establishes the infinite-time conclusions.
"""
from math import isclose, log
import sympy as sp
from scipy.integrate import solve_ivp

u,v,w,alpha,kappa,gamma,delta,b,d,t=sp.symbols('u v w alpha kappa gamma delta b d t', positive=True)
vf=v*(alpha-kappa*w)
wf=w*(gamma*v-delta)
g=alpha-delta+gamma*v-kappa*w
uf_pw=u*g
uf_ho=u*(g+b*v*w-d*u)
field={u:uf_ho,v:vf,w:wf}
D=lambda z:sp.factor(sum(sp.diff(z,x)*field[x] for x in (u,v,w)))
S=b*v*w/(d*u)-1
H=gamma*v-delta*sp.log(v)+kappa*w-alpha*sp.log(w)
assert sp.simplify(D(H))==0
assert sp.simplify(D(S)+b*v*w*S)==0
assert sp.factor(uf_ho.subs(u,b*v*w/d)-uf_pw.subs(u,b*v*w/d))==0
assert sp.factor(uf_pw.subs(u,b*v*w/d)-(b/d)*(vf*w+v*wf))==0
assert sp.diff(uf_ho/u,v,w)==b
assert sp.factor(uf_ho/u-uf_pw/u - (b*v*w-d*u))==0
# Integrated quantity: derivative equals v*w whenever (v,w) solve the base equations.
G=alpha*delta*t/(kappa*gamma)+alpha*sp.log(w)/(kappa*gamma)-v/kappa
G_dot=sp.diff(G,t)+sp.diff(G,v)*vf+sp.diff(G,w)*wf
assert sp.simplify(G_dot-v*w)==0
# Stationary prey and predator and mixed-moment averages follow from
# average (log w)'=0 and average v'=0 on each closed base orbit.
# Quantitative checks away from the exact-camouflage surface.
pars=dict(alpha=1.5,kappa=1.2,gamma=0.7,delta=0.9,b=1.1,d=0.8)
a,k,gam,de,bb,dd=[pars[k] for k in ('alpha','kappa','gamma','delta','b','d')]
v0,w0=1.9,0.8
c=bb/dd

def base(_t,Y):
 V,W=Y
 return [V*(a-k*W),W*(gam*V-de)]

def ho(_t,Y):
 U,V,W=Y
 return [U*(a-de+gam*V-k*W+bb*V*W-dd*U),V*(a-k*W),W*(gam*V-de)]

def pw(_t,Y):
 U,V,W=Y
 return [U*(a-de+gam*V-k*W),V*(a-k*W),W*(gam*V-de)]

for ratio in [1.,0.8,1.3]:
 U0=ratio*c*v0*w0
 sol=solve_ivp(ho,[0,25],[U0,v0,w0],rtol=1e-10,atol=1e-12,dense_output=True,max_step=.02)
 assert sol.success
 y=sol.sol
 for tt in [.0,2.,5.,11.,19.,25.]:
  U,V,W=y(tt)
  S0=c*v0*w0/U0-1
  I=a*de/(k*gam)*tt+a/(k*gam)*log(W/w0)-(V-v0)/k
  expected=S0*sp.exp(-bb*I)
  assert abs((c*V*W/U-1)-float(expected))<2e-8
  if ratio==1: assert abs(U-c*V*W)<2e-8
 if ratio==1:
  compare=solve_ivp(pw,[0,25],[U0,v0,w0],rtol=1e-10,atol=1e-12,dense_output=True,max_step=.02)
  for tt in [.5,5.,20.,25.]:
   assert max(abs(float(z)) for z in (sol.sol(tt)-compare.sol(tt))) < 2e-8
 print('trajectory ratio',ratio,': exact formula and trajectory tests passed')

print('PASS: invariant surface, nonzero mixed Hessian, first integral, integral law, and trajectory tests')
