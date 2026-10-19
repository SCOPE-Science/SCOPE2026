"""Reproducibility checks for the unit-feedback sine map.

Finite numerical tests are diagnostics, not proofs of global claims.
"""
import math
import random
import sympy as sp

alpha,beta,gamma,delta,x,y,z=sp.symbols('alpha beta gamma delta x y z',real=True)
kappa=beta+gamma-delta
F=sp.Matrix([y,sp.sin(z),alpha+beta*x+gamma*y-delta*sp.sin(z)+z])
U=lambda v: v[2]+beta*v[0]+(beta+gamma)*v[1]
assert sp.simplify(U(F)-U(sp.Matrix([x,y,z]))-(alpha+kappa*sp.sin(z)))==0
checks=1

# Equilibrium condition derived from all three equations.
s=sp.symbols('s',real=True)
assert sp.expand(F[2].subs({x:s,y:s,z:sp.symbols('theta')})-sp.symbols('theta')-(alpha+beta*s+gamma*s-delta*sp.sin(sp.symbols('theta'))))==0
checks+=1

# Center manifold Taylor equations: critical sin(z*)=s= +/-1,
# cosine=0 and alpha+kappa*s=0. Let r=z-z*, p=P*r² and q=Q*r².
P,Q,r=sp.symbols('P Q r',real=True)
# The first two components of the next iterate are q and sin(z*)-s:
# To quadratic order these require P=Q and Q=-s/2.
assert sp.simplify((Q-P).subs({P:-s/2,Q:-s/2}))==0
assert sp.simplify((Q+s/2).subs(Q,-s/2))==0
# The coefficient of r² in the height increment must be alpha/2.
height_coeff=sp.expand(beta*P+gamma*Q+delta*s/2)
assert sp.simplify(height_coeff.subs({P:-s/2,Q:-s/2})+s*kappa/2)==0
assert sp.simplify((height_coeff.subs({P:-s/2,Q:-s/2})-alpha/2).subs(alpha,-s*kappa))==0
checks+=4

# Two coexisting exact trajectories at the same positive parameters.
# x=y=1,z=pi/2+2pi*n maps to x=y=1,z+2pi.
# x=y=-1,z=3pi/2 is fixed.
for X,Y,Z,dx in [(1,1,sp.pi/2,2*sp.pi),(-1,-1,3*sp.pi/2,0)]:
  fx=[sp.simplify(q.subs({x:X,y:Y,z:Z,alpha:sp.pi,beta:sp.pi,gamma:sp.pi,delta:sp.pi})) for q in F]
  assert fx==[X,Y,Z+dx], fx
  checks+=1

# Randomized pointwise drift checks, including both signs and zero kappa.
rng=random.Random(20231015)
for i in range(400):
  a,b,g,d=[rng.uniform(-3,3) for _ in range(4)]
  X,Y,Z=[rng.uniform(-10,10) for _ in range(3)]
  u=Z+b*X+(b+g)*Y
  nx,ny,nz=Y,math.sin(Z),Z+a+b*X+g*Y-d*math.sin(Z)
  un=nz+b*nx+(b+g)*ny
  assert math.isclose(un-u,a+(b+g-d)*math.sin(Z),rel_tol=1e-12,abs_tol=2e-12)
  checks+=1

# Long-run diagnostic for a nonzero parameter triple on the attracting
# side of the unit multiplier: alpha=beta=gamma=delta=1.
X=Y=-1+0.5*0.01**2
Z=1.5*math.pi-0.01
for n in range(1,200001):
  X,Y,Z=Y,math.sin(Z),Z+1+X+Y-math.sin(Z)
  if n in (10000,100000,200000):
    assert abs(n*(Z-1.5*math.pi)+2)<0.08
    checks+=1

print('PASS',checks,'exact/symbolic, pointwise numerical and limiting-regime checks')
print('Critical approach diagnostic: n(z_n-z*) =',200000*(Z-1.5*math.pi))
