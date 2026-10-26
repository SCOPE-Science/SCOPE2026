"""Independent numerical and symbolic checks for intermittent-trap conditional excursion ages."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln, betaln
from scipy.optimize import minimize_scalar


def posterior_u_moment(R, A, B, n, p=1, state='on'):
    # Laplace quadrature, non-normalized normalization cancels; state off shifts Gamma shape by one.
    shape = B+(state == 'off')
    q=math.sqrt(2*A)
    uhat=max(R/q,0.5)
    def logw(u):
        return (shape-1)*math.log(u)-A*u-(n/2)*math.log1p(u)-R*R/(2*(1+u))
    center=logw(uhat)
    def f(v, power):
        if v<=0: return 0
        u=R*v
        a=logw(u)-center
        return math.exp(a)*(v**power)
    limit=20/q+20
    denom=quad(lambda v:f(v,0),0,limit,epsabs=1e-12,epsrel=1e-11,limit=500)[0]
    numer=quad(lambda v:f(v,p),0,limit,epsabs=1e-12,epsrel=1e-11,limit=500)[0]
    return numer/denom

def raw_posterior_on_fraction(R,A,B,n):
    # State-conditioned Gaussian/Gamma convolution (independent integration).
    q=math.sqrt(2*A)
    uhat=max(R/q,1)
    def logw(v,shape):
        u=R*v
        return (shape-1)*math.log(u)-A*u-(n/2)*math.log1p(u)-R*R/(2*(1+u)) + shape*math.log(A)-gammaln(shape)
    center=logw(uhat/R,B+1)
    def conv(shape):
        return quad(lambda v: math.exp(min(logw(v,shape)-center,680)) if v>0 else 0, 1e-6,20/q+20,epsabs=1e-11,epsrel=1e-10,limit=500)[0]
    on=A/(A+B)*conv(B)
    off=B/(A+B)*conv(B+1)
    return on/(on+off)

checks=0
for n in [1,2,5]:
  for A,B in [(0.75,1.0),(2.0,0.5),(0.6,2.2)]:
    q=math.sqrt(2*A)
    for R in [15.,40.,100.,250.]:
      e=posterior_u_moment(R,A,B,n,p=1,state='off')
      # Exact identity for posterior odds derived from Gamma(B+1)/Gamma(B).
      eon=posterior_u_moment(R,A,B,n,p=1,state='on')
      exact_on=1/(1+R*eon)
      actual_on=raw_posterior_on_fraction(R,A,B,n)
      assert abs(actual_on-exact_on)<2e-8,(n,A,B,R,actual_on,exact_on)
      checks+=1
      if R>=100:
        assert abs(e-1/q)<0.16,(n,A,B,R,e,1/q)
        assert abs(actual_on*R-q)<0.25,(n,A,B,R,actual_on*R,q)
        checks+=2
# Beta-gamma convolution transforms and moments
for A,B in [(0.75,1.0),(2.,0.5),(0.6,2.2)]:
  for m in range(1,6):
    # Off-age fraction J ~ Beta(1,B): E[J^m]=m! / product(B+j, j=1..m)
    beta_val=math.exp(betaln(1+m,B)-betaln(1,B))
    moment=math.factorial(m)/math.prod(B+j for j in range(1,m+1))
    assert abs(beta_val-moment)<1e-12
    checks+=1
  # Sum of gamma(shape B) + gamma(shape 1) has Gamma(shape B+1) moments.
  for m in range(1,5):
    from_sum=sum(math.comb(m,j)*math.prod(B+i for i in range(j))/(A**j)*math.factorial(m-j)/(A**(m-j)) for j in range(m+1))
    from_gamma=math.prod(B+1+i for i in range(m))/(A**m)
    assert abs(from_sum/from_gamma-1)<1e-12
    checks+=1
print(f'PASS: {checks} deterministic tests')
