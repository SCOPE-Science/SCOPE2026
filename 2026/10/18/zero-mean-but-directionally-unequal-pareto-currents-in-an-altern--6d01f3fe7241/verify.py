#!/usr/bin/env python3
"""Standalone numerical checks for alternating-Pareto exclusion current.
Uses only numpy and scipy. Computations are diagnostics, not a proof.
"""
import itertools
from math import pi, gamma
import numpy as np
from scipy.special import ive
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import expm_multiply

N_TESTS=0

def check(condition,msg):
 global N_TESTS
 N_TESTS+=1
 assert condition, msg

def mean_current(t):
 if t<=0: return 0.
 return t*(ive(0,2*t)+ive(1,2*t))

def mean_current_integral(t):
 return quad(lambda x: ive(0,2*x),0,t,epsabs=3e-11)[0]

def truncated_mean(alpha,cutoff):
 assert alpha>1.5 and cutoff>0
 central=quad(mean_current,0,cutoff,epsabs=1e-9)[0]
 # remove dominant sqrt(t/pi) analytically for stable improper integral
 tail_error=quad(lambda t:t**(-alpha)*(mean_current(t)-np.sqrt(t/pi)),cutoff,np.inf,epsabs=3e-9,limit=200)[0]
 tail=cutoff**alpha*tail_error+cutoff**1.5/(np.sqrt(pi)*(alpha-1.5))
 return central+tail

def cycle_mean(alpha,cutoff):
 return alpha*cutoff/(alpha-1)

def tail_constant(alpha,cutoff,denom):
 return cutoff**alpha*pi**(1-alpha)/(denom*(alpha-1))

for t in [0.02,0.1,1.,4.,12.,50.]:
 check(abs(mean_current(t)-mean_current_integral(t))<1e-8,'Bessel integrated current identity')
for t in [100.,1000.,10000.]:
 check(abs(mean_current(t)/np.sqrt(t/pi)-1)<0.005,'asymptotic current normalization')
for a in [1.61,1.7,1.9,1.99]:
 vs=[truncated_mean(a,s) for s in [0.05,0.2,1,3,10]]
 check(all(x<y for x,y in zip(vs,vs[1:])),'strict positive scale monotonicity')
 check(vs[0]>0,'positive mean numerator')
for a in [1.61,1.7,1.9,1.99]:
 for s in [0.1,1,4]:
  z=quad(lambda t:1 if t<s else (s/t)**a,0,np.inf,epsabs=1e-8)[0]
  check(abs(z-cycle_mean(a,s))<1e-8,'equilibrium age normalizing mean')

alpha_plus,alpha_minus,tplus=1.7,1.9,1.
required=truncated_mean(alpha_plus,tplus)
tminus=brentq(lambda s:truncated_mean(alpha_minus,s)-required,.0001,10.,xtol=1e-12)
check(abs(truncated_mean(alpha_minus,tminus)-required)<2e-10,'zero mean condition')
mu_plus=cycle_mean(alpha_plus,tplus);mu_minus=cycle_mean(alpha_minus,tminus)
total=mu_plus+mu_minus
Kp=tail_constant(alpha_plus,tplus,total);Km=tail_constant(alpha_minus,tminus,total)
print('Parameters: alpha_plus',alpha_plus,'alpha_minus',alpha_minus,'cutoff_plus',tplus,'cutoff_minus',repr(tminus))
print('Fplus=Fminus',repr(required),'mean holding times',repr(mu_plus),repr(mu_minus))
print('tail indices',2*(alpha_plus-1),2*(alpha_minus-1),'tail coefficients',repr(Kp),repr(Km))
# The deterministic current approximation has the correct age-induced tail coefficient;
# this test does not substitute for concentration of SEP current.
for a,t0,K in [(alpha_plus,tplus,Kp),(alpha_minus,tminus,Km)]:
 for threshold in [20.,60.,200.]:
  age_star=brentq(lambda t:mean_current(t)-threshold,.5,max(1000.,10*pi*threshold*threshold))
  tail=t0**a/(total*(a-1))*age_star**(1-a)
  check(abs(tail/(K*threshold**(-2*(a-1)))-1)<0.02,'deterministic age tail asymptotic')

# Independent finite-state SSEP generator: 8 reflecting sites, 4 occupied,
# initially left four sites occupied; mean and covariances can be computed exactly.
N=8; p=N//2
states=list(itertools.combinations(range(N),p)); inds={s:k for k,s in enumerate(states)}
Q=lil_matrix((len(states),len(states)),dtype=float)
for j,s in enumerate(states):
 occ=set(s)
 for x in range(N-1):
  if (x in occ)!=(x+1 in occ):
   sn=tuple(sorted((occ-{x,x+1})|({x+1} if x in occ else {x})))
   Q[inds[sn],j]+=1
   Q[j,j]-=1
Q=csc_matrix(Q)
v0=np.zeros(len(states)); v0[inds[tuple(range(p))]]=1
for t in [.03,.1,.3,.6,1.]:
 pt=expm_multiply(Q*t,v0)
 check(abs(pt.sum()-1)<2e-12,'finite SSEP CTMC mass')
 k=np.array([sum(i>=p for i in s) for s in states],dtype=float)
 mk=k@pt; var=(k*k)@pt-mk*mk
 check(var<=mk+1e-10,'negative covariance variance envelope')
 rho=np.array([sum(pt[j] for j,s in enumerate(states) if i in s) for i in range(N)])
 for i in range(p,N):
  for j in range(i+1,N):
   pij=sum(pt[z] for z,s in enumerate(states) if i in s and j in s)
   check(pij<=rho[i]*rho[j]+1e-10,'negative association pair witness')
 check(mk<=mean_current(t)+1e-10,'reflecting finite test half-line upper comparison')
print('PASSED',N_TESTS,'checks')
