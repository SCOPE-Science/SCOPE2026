"""Finite numerical consistency checks for fractional directed-cycle differences.
Scientific analytic arguments appear in RESULT.md; these checks do not certify an infinite claim.
Requires numpy and scipy. Run: python checker.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma, zeta

checks=0

def assert_close(x,y,rtol=2e-9,atol=3e-10):
 global checks
 if not math.isclose(float(x),float(y),rel_tol=rtol,abs_tol=atol):
  raise AssertionError((x,y))
 checks+=1

def verify(pred,label=''):
 global checks
 if not pred: raise AssertionError(label)
 checks+=1

def eigen(n,a):
 roots=np.exp(2j*np.pi*np.arange(n)/n)
 out=(1-roots)**a
 out[0]=0.0
 return out

def exact_matrix(n,a):
 la=eigen(n,a)
 # coefficient of S^r; negative inverse character convention
 return np.fft.fft(la)/n

def formula(n,a):
 if a==1: return 2.0
 r=0 if a<1 else 1
 def regular_factor(u):
  q=1-u
  return q**(n+r-a-1)/sum(q**k for k in range(n))
 # The integrand is u**(a-1)*regular_factor(u); weighted quadrature
 # integrates the exact endpoint singularity without cancellation.
 integral=quad(regular_factor,0,1,weight='alg',wvar=(a-1,0),epsabs=1e-10,epsrel=1e-10,limit=250)[0]
 return (2 if a<1 else 2*a)-2*abs(math.sin(math.pi*a))/math.pi*integral

def expansion(n,a):
 if a<1:
  c=a/gamma(1-a)
  return 2-2*c*zeta(1+a,1)/n**(1+a)-c*a*(a+1)*zeta(2+a,1)/n**(2+a)
 c=1/gamma(-a)
 return 2*a-2*c*zeta(1+a,1)/n**(1+a)+c*(a+1)*(2-a)*zeta(2+a,1)/n**(2+a)

for a in [0.12,0.3,0.7,0.91,1.0,1.15,1.4,1.7,1.91]:
 prev=None
 for n in [2,3,4,5,8,13,21,34]:
  c=exact_matrix(n,a)
  actual=sum(abs(c))
  assert_close(actual,formula(n,a),rtol=3e-8,atol=5e-9)
  verify(max(abs(np.imag(c)))<1e-8)
  assert_close(sum(np.real(c)),0.0)
  if a<1: verify(c[0].real>0 and np.all(c[1:].real<0))
  if a>1: verify(c[1].real<0 and all(c[k].real>0 for k in range(n) if k!=1))
  if n==2: assert_close(actual,2**a)
  if prev is not None:
   if a!=1:verify(actual>prev+1e-8)
   else:assert_close(actual,prev)
  prev=actual
for a in [0.25,0.65,1.25,1.75]:
 errs=[]
 for n in [15,30,60,120]:
  ex=sum(abs(exact_matrix(n,a)))
  errs.append(abs(ex-expansion(n,a)))
  verify(abs(ex-expansion(n,a))<5*n**(-3-a))
 verify(all(errs[i+1]<errs[i] for i in range(3)))
for n in range(3,21):
 for a in [0.4,0.99,1.01,1.3,1.55,1.8,1.99]:
  lam=eigen(n,a)[1:]
  target=a<n/(n-2)
  observed=min(lam.real)>1e-9
  verify(observed==target)
  c=exact_matrix(n,a)
  verify((np.all(c[1:].real<1e-9))==(a<=1))
for n in [5,6,7,9,13,20]:
 crit=n/(n-2)
 if crit<2:
  lam=eigen(n,crit)[1:]
  verify(min(abs(lam.real))<1e-8)
print('PASS',checks,'assertions')
