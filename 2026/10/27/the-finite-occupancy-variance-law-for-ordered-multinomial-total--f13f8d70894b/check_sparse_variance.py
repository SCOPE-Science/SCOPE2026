#!/usr/bin/env python3
"""Numerical and finite-enumeration checks for ordered multinomial DTV variance.
Run: python check_sparse_variance.py. Python 3 standard library only.
This is a reproducibility check, not a proof of any asymptotic theorem.
"""
import math
from fractions import Fraction
from itertools import product
from functools import lru_cache

assertions=0

def check(cond,msg):
 global assertions
 assertions+=1
 if not cond: raise AssertionError(msg)

def bessel_pair(lam):
 # I_0(2lam) and I_1(2lam) as convergent power series.
 t0=1.;t1=lam; i0=1.;i1=lam
 for m in range(1,500):
  t0*=lam*lam/(m*m)
  t1*=lam*lam/(m*(m+1))
  i0+=t0;i1+=t1
  if abs(t0)+abs(t1)<1e-17*(i0+i1):break
 return i0,i1

def poissons(lam):
 cap=max(55, int(lam+18*math.sqrt(lam+1)+22))
 p=[math.exp(-lam)]
 for k in range(1,cap+1):p.append(p[-1]*lam/k)
 return p

def limit_moments(lam):
 p=poissons(lam)
 h=[sum(p[j]*abs(k-j) for j in range(len(p))) for k in range(len(p))]
 mu=sum(p[k]*h[k] for k in range(len(p)))
 tau=sum(p[k]*h[k]*h[k] for k in range(len(p)))
 i0,i1=bessel_pair(lam)
 mu_closed=2*lam*math.exp(-2*lam)*(i0+i1)
 c=2*lam*math.exp(-2*lam)*i0
 sigma=2*lam+2*tau-3*mu*mu-c*c/lam
 return mu,tau,c,sigma,mu_closed

@lru_cache(None)
def cond(k,s):
 # Conditional on s balls among k selected bins, the vector is Mult(s;1/k,...).
 fa=[math.factorial(j) for j in range(s+1)]
 fac=fa[s]/(k**s)
 a=b=0.
 if k==2:
  for x in range(s+1):
   h=abs(2*x-s);w=fac/(fa[x]*fa[s-x]);a+=w*h;b+=w*h*h
 else:
  for x in range(s+1):
   for y in range(s-x+1):
    if k==3:
     z=s-x-y
     w=fac/(fa[x]*fa[y]*fa[z]);a+=w*abs(x-y)*abs(y-z)
    else:
     for z in range(s-x-y+1):
      v=s-x-y-z
      w=fac/(fa[x]*fa[y]*fa[z]*fa[v]);a+=w*abs(x-y)*abs(z-v)
 return a,b

def bin_pmf_prefix(N,p,L):
 # Exact forward recurrence away from the endpoint p=1.
 if p==1: return [1. if j==N else 0. for j in range(L+1)]
 v=[(1-p)**N]
 for j in range(1,L+1):v.append(v[-1]*(N-j+1)/j*p/(1-p))
 return v

def finite(n,N,L=34):
 L=min(N,L);mm={}
 for k in (2,3,4):
  w=bin_pmf_prefix(N,k/n,L)
  vals=[cond(k,s) for s in range(L+1)]
  mm[k]=(sum(w[s]*vals[s][0] for s in range(L+1)),sum(w[s]*vals[s][1] for s in range(L+1)))
 mu=mm[2][0]
 A=mm[2][1]-mu*mu
 B=mm[3][0]-mu*mu
 C=mm[4][0]-mu*mu
 return (n-1)*A+2*(n-2)*B+(n-2)*(n-3)*C, C, mu

def compositions(N,n):
 if n==1:
  yield (N,);return
 for z in range(N+1):
  for rest in compositions(N-z,n-1):yield (z,)+rest

def exact_check(n,N):
 fac=[math.factorial(i) for i in range(N+1)]
 q=Fraction(1,n)
 mass=Fraction(0)
 E=Fraction(0); E2=Fraction(0)
 for xx in compositions(N,n):
  w=Fraction(fac[N],math.prod(fac[x] for x in xx))*q**N
  f=sum(abs(xx[j+1]-xx[j]) for j in range(n-1))
  mass+=w;E+=w*f;E2+=w*f*f
 check(mass==1,'multinomial normalization')
 actual=float(E2-E*E)
 approx=finite(n,N,L=N)[0]
 check(abs(actual-approx)<3e-8*(1+actual),f'finite exact {n},{N}: {actual},{approx}')

for lam in [0.02,0.1,0.3,0.5,1,2,3,6,20,60]:
 mu,tau,c,s,mc=limit_moments(lam)
 check(abs(mu-mc)<3e-11*(1+mu),f'Skellam mean {lam}')
 check(s>0,f'variance coefficient positive {lam}')
 if lam<=6:
  h=1e-4*max(1,lam)
  mup=limit_moments(lam+h)[0]
  mum=limit_moments(lam-h)[0]
  check(abs((mup-mum)/(2*h)-c/lam)<2e-5, f'Poisson score derivative {lam}')
for n in (5,6,8):
 for N in (1,2,3,4,5,6): exact_check(n,N)
for lam in [0.2,0.5,1.,2.]:
 target=limit_moments(lam)[3]; c=limit_moments(lam)[2]
 for n in (40,80,160):
  N=round(lam*n)
  v,cov,mean=finite(n,N,L=34)
  check(abs(v-n*target)<12,'uniform bounded residual check')
  check(abs(n*cov+c*c/lam)<0.1,'disjoint edge limit check')
small=1e-3
v=limit_moments(small)[3]
check(abs(v-(4*small**2-12*small**3))<1e-9,'small-intensity series')
large_const=8/3+4*(math.sqrt(3)-3)/math.pi
check(abs(limit_moments(60)[3]/60-large_const)<0.035,'Gaussian large-intensity check')
print(f'PASS {assertions} assertions (finite exact, Poisson series, conditioned asymptotic checks)')
for lam in (0.2,0.5,1.,2.,3.,6.):
 mu,tau,c,s,_=limit_moments(lam)
 print(f'lambda={lam:.1f} mu={mu:.12f} sigma2={s:.12f} disjoint_ncov={-c*c/lam:.12f}')
print('limitations: finite checks and numerical truncation do not establish asymptotic uniformity.')
