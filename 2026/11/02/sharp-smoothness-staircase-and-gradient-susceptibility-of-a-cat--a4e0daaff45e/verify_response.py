#!/usr/bin/env python3
"""Symbolic and numerical checks for the cat-driven Möbius graph response.
Uses Python/SymPy/mpmath, and does not assert uniqueness beyond the analytical proof.
"""
from fractions import Fraction
import math
import sympy as sp

A=sp.Matrix([[2,1],[1,1]])
B=A.inv()
assert A.det()==1 and A.charpoly().as_expr()==sp.Symbol('lambda')**2-3*sp.Symbol('lambda')+1
assert B==sp.Matrix([[1,-1],[-1,2]])
e1=sp.Matrix([1,0]); r=sp.symbols('r')
G=sp.simplify(B*(sp.eye(2)-r*B).inv()*e1)
assert sp.simplify(G[0]-(1-r)/(1-3*r+r*r))==0
assert sp.simplify(G[1]+1/(1-3*r+r*r))==0
for n in range(1,20):
  v=B**n*e1
  assert v==sp.Matrix([sp.fibonacci(2*n-1),-sp.fibonacci(2*n)])
  if n>=3: assert v==3*(B**(n-1)*e1)-(B**(n-2)*e1)

eps=sp.symbols('eps',positive=True)
r_e=(1-eps)/(1+eps)
assert sp.simplify((1-3*r+r*r).subs(r,r_e)-(5*eps*eps-1)/(1+eps)**2)==0
assert sp.simplify(-2*sp.pi*G[1].subs(r,r_e) - 2*sp.pi*(1+eps)**2/(5*eps**2-1))==0
lam=(3+sp.sqrt(5))/2
assert sp.simplify(((lam-1)/(lam+1))**2-sp.Rational(1,5))==0
assert sp.simplify(sp.log((1+1/sp.sqrt(5))/(1-1/sp.sqrt(5)))-sp.log(lam))==0
# Characteristic spectral growth and exact orthogonality of sampled Fourier modes
vs=[tuple(B**n*e1) for n in range(1,36)]
assert len(set(vs))==len(vs)
assert len(set(vs).intersection({(-x,-y) for x,y in vs}))==0
# Exact Fourier correlation formula for truncated response under integer cat map
q=sp.Rational(1,4)
for N in [5,12,25]:
  for k in [0,1,2,4]:
    left=sum(q**(m-1)*q**(m+k-1)/2 for m in range(1,N-k+1))
    expected=(q**k/2)*(1-q**(2*(N-k)))/(1-q*q)
    assert sp.simplify(left-expected)==0

# Direct graph transform from exact rational base coordinates, vs Fourier response.
# This tests normalization at finite weak forcing, not the infinite regularity theorem.
def m_map(x,e):
    return x - math.atan(e*math.sin(2*math.pi*x)/(1+e*math.cos(2*math.pi*x)))/math.pi

def base_back_states(N,den=1009):
    t,s=123,456
    back=[(t,s)]
    for j in range(N):
        t,s=(t-s)%den,(-t+2*s)%den
        back.append((t,s))
    return back

for e in [0.3333333333333333,0.6,0.8]:
    rr=(1-e)/(1+e)
    back=base_back_states(90)
    h=sum(rr**(n-1)*math.sin(2*math.pi*back[n][0]/1009) for n in range(1,91))
    mu=1e-6
    x=0.0
    for n in range(90,0,-1):
        x=m_map(x,e)+mu*math.sin(2*math.pi*back[n][0]/1009)
    err=abs(x/mu-h)
    assert err<2e-5,(e,err)
    print('epsilon',e,'mu_graph_over_mu',x/mu,'response_series',h,'error',err)
print('SYMBOLIC_IDENTITIES_AND_GRAPH_CHECKS_PASS')
