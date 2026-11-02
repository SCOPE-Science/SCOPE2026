#!/usr/bin/env python3
"""Exact and numerical checks for an eco-evolutionary period-two invasion theorem."""
from fractions import Fraction as Q
from math import sqrt, isclose
import sympy as sp

m,a,s,d = sp.symbols('m a s d', real=True)
W=(m+1)/m
V=(m+1)/m**2
p_formula=(a*a+(m+1)*(m-2)*a*s+(m+1)*s*s)/m**2
p_via_vieta=sp.expand(a*a*(1-W+V)+a*s*(W-2*V)+s*s*V)
assert sp.simplify(p_formula-p_via_vieta)==0
u=(m+1)/(2*m)
sbar=(1-u)*a+u*s
variance=(a-s)**2*(m-3)*(m+1)/(4*m*m)
assert sp.simplify(p_formula-(sbar**2-variance))==0
# Independently differentiate both discrete strategy updates at the resident edge.
x,n,t0,t1=sp.symbols('x n t0 t1',real=True)
Sco=(1-n)*a+n*s
Tde=(1-n)*t0+n*t1
fC=2*x+Sco*(1-x)
fD=Tde*x+1-x
mapI=x+x*(1-x)*(fC-fD)
mapII=x*fC/(x*fC+(1-x)*fD)
for fx in (mapI,mapII):
 assert sp.simplify(sp.diff(fx,x).subs(x,0)-Sco)==0
 assert sp.simplify(sp.diff(fx,n).subs(x,0))==0
resource=m*n*(1-n)+d*x*n
assert sp.simplify(sp.diff(resource,n).subs(x,0)-m*(1-2*n))==0
assert sp.simplify(sp.diff(resource,x).subs(x,0)-d*n)==0

mu=Q(16,5); alpha=Q(9,5); sigma=Q(3,5)
eL=Q(1); eH=Q(11,10); r=Q(43,10)
T0=Q(19,10);T1=Q(21,10)
assert mu == r-eH and eH-eL == Q(1,10)
assert (mu+eH-eL)**2 < 4*mu
assert Q(3)<mu and float(mu)<1+sqrt(6)
P=(alpha**2+(mu+1)*(mu-2)*alpha*sigma+(mu+1)*sigma**2)/(mu**2)
D=4+2*mu-mu**2
mean_n=(mu+1)/(2*mu)
mean_S=(1-mean_n)*alpha+mean_n*sigma
assert P==Q(1593,1600) and D==Q(4,25) and mean_S==Q(81,80)
assert 0<P<1 and -1<D<1 and mean_S>1
am=(1-mean_n*sigma)/(1-mean_n)
assert am==Q(97,55) and am<alpha
root=(-189+8*sqrt(2689))/125
assert float(alpha)<root<2.0

nlo=float((21-sp.sqrt(21))/32)
nhi=float((21+sp.sqrt(21))/32)
def resource(x,n):return float(mu)*n*(1-n)+0.1*x*n
def sco(n):return float(alpha)*(1-n)+float(sigma)*n
def tde(n):return float(T0)*(1-n)+float(T1)*n
def evolve(x,n,mode):
  C=2*x+sco(n)*(1-x)
  D=tde(n)*x+1-x
  if mode=='I': y=x+x*(1-x)*(C-D)
  else: y=x*C/(x*C+(1-x)*D)
  return y, resource(x,n)
assert isclose(resource(0,nlo),nhi,abs_tol=1e-13)
assert isclose(resource(0,nhi),nlo,abs_tol=1e-13)
assert isclose(sco(nlo)*sco(nhi),float(P),abs_tol=1e-13)

for mode in ['I','II']:
 for i in range(21):
  for j in range(21):
   xx=i/20; nn=j/20
   xx2,nn2=evolve(xx,nn,mode)
   assert -1e-12 <= xx2 <= 1+1e-12
   assert -1e-12 <= nn2 <= 1+1e-12
 # Fixed absolute perturbation near orbit; two-step contraction observable.
 xx=1e-5; nn=nlo
 initial=xx
 for _ in range(5000): xx,nn=evolve(xx,nn,mode)
 assert xx < initial*0.01, (mode,xx)
 assert min(abs(nn-nlo),abs(nn-nhi))<3e-3,(mode,nn)
 print('mode',mode,'x after 5000 steps',format(xx,'.7g'),'resource',format(nn,'.10g'))
print('Symbolic identities and exact rational certificates PASS')
print('P=',P,'D=',D,'mean payoff=',mean_S,'mean threshold=',am)
print('Grid invariance and near-cycle numerical trajectories PASS')
