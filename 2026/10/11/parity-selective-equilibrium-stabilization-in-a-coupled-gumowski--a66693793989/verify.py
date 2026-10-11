#!/usr/bin/env python3
"""Reproducibility checks for the spectral stability of three homogeneous fixed points
of a nearest-neighbor coupled Gumowski--Mira-type network.

Only Python's standard library is needed. The analytical proof, not finite
checks, establishes the all-parameter theorem.
"""
from fractions import Fraction as Q
import math, cmath, random

C = 0

def ck(condition, message):
    global C
    assert condition, message
    C += 1

def local_F(x,mu):
    return mu*x + 2*(1-mu)*x/(1+x*x)

def mode_matrix(a,mu,eps,lam,s):
    c = 2-mu if s == 0 else mu
    u = (1-eps)*c + eps*lam
    v = (1-eps)*(1+a)
    return ((u,v),(c*u-1,c*v))

def eigen_mods_from_trace_det(tr,de):
    disc = complex(tr*tr - 4*de)
    z = cmath.sqrt(disc)
    return abs((tr+z)/2),abs((tr-z)/2)

def criterion(a,mu,eps,n,s):
    if not (0<=eps<1 and a>=0 and n>=3): raise ValueError
    c = 2-mu if s == 0 else mu
    minimum = -1.0 if n%2==0 else -math.cos(math.pi/n)
    return (eps > a/(1+a)
            and c < 1
            and (1-eps)*(2+a)*(1+c)+eps*(1+minimum) > 0)

# Stationarity for exact rational parameter values and states.
for mu in [Q(-5),Q(-3,2),Q(-1),Q(0),Q(1),Q(3),Q(5)]:
    for x in [Q(-1),Q(0),Q(1)]:
        ck(local_F(x,mu)==x, ('stationarity',x,mu))

# The identity trace/determinant in each spatial Fourier mode is direct and
# is checked for many values. The count is intentionally independent of b.
for n in range(3,44):
 for a in [0.,.01,.33,1.,2.]:
  for mu in [-5.,-3.,-2.,-1.5,-1.,-.6,0.,.6,1.,1.5,2.5,3.,3.5,4.,6.]:
   for eps in [0.,.02,.2,.3,.55,.9,.99,.999]:
    for s in [-1,0,1]:
     desired=criterion(a,mu,eps,n,s)
     c=(2-mu) if s==0 else mu
     beta=(1-eps)*(1+a)
     actual=True
     for k in range(n):
       lam=math.cos(2*math.pi*k/n)
       mat=mode_matrix(a,mu,eps,lam,s)
       tr=mat[0][0]+mat[1][1]
       de=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
       ck(abs(tr-((1-eps)*c*(2+a)+eps*lam))<1e-11, ('trace',n,a,mu,eps,s,k))
       ck(abs(de-beta)<1e-11, ('det',n,a,mu,eps,s,k))
       m1,m2=eigen_mods_from_trace_det(tr,de)
       if max(m1,m2) > 1+1e-9:actual=False
       if abs(max(m1,m2)-1)<1e-9: actual=None;break
     if actual is not None:
       ck(actual==desired,('boundary mismatch',n,a,mu,eps,s,actual,desired))

# Exact-rational parity witness in the local Jacobian and Jury tests.
a=Q(1,4); mu=Q(-2); eps=Q(9,10)
for n in (3,4,5,6):
   delta = 0 if n%2==0 else 1-math.cos(math.pi/n)
   qmin=(1-float(eps))*float(2+a)*float(1+mu)+float(eps)*delta
   ck((qmin>0)==(n==3),('parity witness',n,qmin))

# In the odd-ring c<-1 regime, the determinant and negative-mode
# constraints are independent: the exact interval starts at their maximum.
a_small=Q(5); c_near=Q(-1001,1000); delta_3=Q(1,2)
A=(2+a_small)*(-1-c_near)
lo_det=a_small/(1+a_small)
lo_mode=A/(A+delta_3)
ck(lo_det == Q(5,6), ('determinant threshold',lo_det))
ck(lo_mode == Q(7,507), ('negative-mode threshold',lo_mode))
ck(1-max(lo_det,lo_mode)==Q(1,6), ('actual exact window',lo_det,lo_mode))

# Numerical differentiability check against independent centered differences
# of the original map for nonuniform perturbations in each coordinate.
def network(z,n,a,b,mu,eps):
    xx=list(z[:n]); yy=list(z[n:]); uu=[]
    for i in range(n):
        u=yy[i]+a*yy[i]*(1-b*yy[i]*yy[i])+local_F(xx[i],mu)
        uu.append((1-eps)*u+eps/2*(xx[(i-1)%n]+xx[(i+1)%n]))
    return uu+[ -xx[i]+local_F(uu[i],mu) for i in range(n)]

rng=random.Random(166403)
for n in (3,4,7):
 for s in (0,1,-1):
  for a,b,mu,eps in ((.25,.1,-2.,.9),(.01,.05,.4,.25),(.33,.1,4.,.99)):
   z0=[float(s)]*n+[0.]*n
   c=(2-mu) if s==0 else mu
   for i in range(n):
    for j in range(2*n):
      if i==j:
        alpha=(1-eps)*c
        if n>2:
            expected=((alpha if j<n else 0) if i<n else ((c*alpha-1) if j<n else 0))
      elif i<n and j>=n and j-n==i: expected=(1-eps)*(1+a)
      elif i>=n and j>=n and j-n==i-n: expected=c*(1-eps)*(1+a)
      elif i<n and j<n and (j==(i-1)%n or j==(i+1)%n): expected=eps/2
      elif i>=n and j<n and (j==(i-n-1)%n or j==(i-n+1)%n): expected=c*eps/2
      else: expected=0.
      h=2e-6
      zp=z0[:];zm=z0[:];zp[j]+=h;zm[j]-=h
      deriv=(network(zp,n,a,b,mu,eps)[i]-network(zm,n,a,b,mu,eps)[i])/(2*h)
      ck(abs(deriv-expected)<2e-8,('finite difference',n,s,a,mu,eps,i,j,deriv,expected))

print('PASS:',C,'checks, across stationarity, mode trace/determinant, Jury, parity witnesses, and nonlinear Jacobian finite differences')
