"""Finite numerical diagnostics for exact two-patch logistic chemotaxis equilibrium formulas.

Analytical monotonicity and all-parameter uniqueness are proved in RESULT.md; these checks do not replace proof.
"""
import math

def curve(t, r, eta_n, eta_c, alpha, beta, cap):
    gamma = 2*r/eta_n
    B = beta + eta_c/2
    w = gamma*t/(1+(1-gamma)*t*t)
    if not (0<t<1 and 0<w<1):
        raise ValueError('outside patterned equilibrium branch')
    return B/(alpha*cap)*((1+t*t)/t)*(math.atanh(t)+math.atanh(w))

def endpoint(gamma):
    if gamma<=1: return 1.
    return 2/(gamma+math.sqrt(gamma*gamma+4*(gamma-1)))

def state(t,r,eta_n,eta_c,alpha,beta,cap):
    b=beta+eta_c/2
    u=cap/(1+t*t)
    return u*(1+t),u*(1-t),alpha*u/beta+alpha*u*t/b,alpha*u/beta-alpha*u*t/b

def residuals(state,chi,r,eta_n,eta_c,alpha,beta,cap):
    n1,n2,c1,c2=state
    z=chi*(c1-c2)/2
    f=math.tanh(z)
    flux=((n2-n1)+(n2+n1)*f)/2
    return (eta_n/2*flux+r*n1*(1-n1/cap),-eta_n/2*flux+r*n2*(1-n2/cap),eta_c/4*(c2-c1)+alpha*n1-beta*c1,eta_c/4*(c1-c2)+alpha*n2-beta*c2)

def run():
  tested=0
  for gamma in (0.15,0.6,1,1.4,2,4,12,50):
    r=gamma*.05/2; eta_n=.05;eta_c=.08;alpha=.2;beta=.1;cap=8.
    hi=endpoint(gamma)
    last=(1+gamma)*(beta+eta_c/2)/(alpha*cap)
    for pct in (.001,.02,.1,.3,.5,.75,.9,.99,.999):
      t=hi*pct
      chi=curve(t,r,eta_n,eta_c,alpha,beta,cap)
      assert chi>last,(gamma,t,chi,last)
      last=chi
      v=state(t,r,eta_n,eta_c,alpha,beta,cap)
      assert min(v)>0,(gamma,t,v)
      res=residuals(v,chi,r,eta_n,eta_c,alpha,beta,cap)
      assert max(map(abs,res))<1e-11,(gamma,t,res)
      tested+=1
    # Near-onset coefficient: chi(t)=chi_c+ B/(alpha K)*(4+3gamma²+gamma³)*t²/3+O(t⁴).
    t=hi*1e-3
    chi=curve(t,r,eta_n,eta_c,alpha,beta,cap)
    c=(beta+eta_c/2)/(alpha*cap)
    d=(4+3*gamma*gamma+gamma**3)/3
    assert abs((chi-c*(1+gamma))/(c*d*t*t)-1)<0.005,(gamma,chi,c,d)
  r=.1;eta_n=.05;eta_c=.08;alpha=.2;beta=.1;cap=8
  t=0.1
  chi=curve(t,r,eta_n,eta_c,alpha,beta,cap)
  print('FINITE_NUMERICAL_RESIDUALS_PASS',tested)
  print('SOURCE_PARAMETERS', 'chi_critical', (beta+eta_c/2)/(alpha*cap)*(1+2*r/eta_n),'chi_at_ratio_0.1',round(chi,12),'limit_t',round(endpoint(2*r/eta_n),12))
  print('ALL_PARAMETER_MONOTONICITY_AND_UNIQUENESS_REQUIRE_ANALYTICAL_PROOF')

if __name__=='__main__': run()
