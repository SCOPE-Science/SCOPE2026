"""Exact identity checks and independent quadrature for centroidal cuts of simplices."""
from fractions import Fraction
from math import comb, factorial
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import betainc, beta

def exact_tail(k,l):
 m=k+l; x=Fraction(k,m)
 return sum(Fraction(comb(m-1,j))*x**j*(1-x)**(m-1-j) for j in range(k))

def beta_pdf(k,l):
 x=k/(k+l)
 return x**(k-1)*(1-x)**(l-1)/beta(k,l)

def expectation_quad(k,l,eps,mode,N=60):
 # Finite-dimensional Dirichlet integration, independent of the Taylor derivation.
 x,w=leggauss(N); x=(x+1)/2; w=w/2
 m=k+l
 F=0.
 if mode=='plus':
  assert k==2
  for u,wu in zip(x,w):
   zp=2*u-1
   t=k/(m+eps*zp)
   F+=wu*(1-betainc(k,l,t))
 else:
  assert l==3
  for u,wu in zip(x,w):
   for v,wv in zip(x,w):
    zn=u-(1-u)*v
    t=(k-eps*zn)/(m-eps*zn)
    F+=wu*wv*2*(1-u)*(1-betainc(k,l,t))
 return F

for m in range(3,11):
 for k in range(1,m):
  l=m-k
  q=exact_tail(k,l)
  assert 0<q<1
  assert q+exact_tail(l,k)==1
  f=beta_pdf(k,l)
  # check the full quadratic-form coefficients after Dirichlet variance reduction
  hp=-f/(l*m*m*(k+1))
  hn=f/(k*m*m*(l+1))
  assert hp<0<hn
print('ALL_DIMENSIONS_EXACT_BETA_TAIL_AND_HESSIAN_SIGNS_PASSED')

k,l=2,3;m=k+l
F0=float(exact_tail(k,l))
f=beta_pdf(k,l)
hp=-f/(l*m*m*(k+1))*2
hn=f/(k*m*m*(l+1))*2
for mode,pred in [('plus',hp),('minus',hn)]:
 h=0.004
 v=(expectation_quad(k,l,h,mode)-2*F0+expectation_quad(k,l,-h,mode))/h**2
 assert abs(v-pred)<8e-7,(mode,pred,v)
print('INDEPENDENT_DIRICHLET_QUADRATURE_HESSIAN_PASSED')

# symmetric truncation removes disjoint homothetic vertex caps, size epsilon**n.
# Every partition section has each coordinate <= max(k,l)/m <= (m-1)/m.
for m in range(3,12):
 eps=Fraction(1,2*m);n=m-1
 assert 1-eps>Fraction(m-1,m)
 for k in range(1,m):
  l=m-k
  F=exact_tail(k,l)
  Ft=(F-k*eps**n)/(1-m*eps**n)
  assert 0<Ft<1
  assert Ft+(1-F-l*eps**n)/(1-m*eps**n)==1
print('EXACT_SYMMETRIC_TRUNCATION_PROFILE_AND_SECTION_SEPARATION_PASSED')
print('ALL_CHECKS_PASSED')
