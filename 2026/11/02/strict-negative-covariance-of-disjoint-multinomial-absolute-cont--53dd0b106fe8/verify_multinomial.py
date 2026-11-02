"""Independent exact checks for disjoint multinomial absolute contrasts.

Run with Python 3; no non-standard libraries. These checks are finite
corroboration of the analytic all-parameter sign proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial

checks=0

def require(assertion, desc):
    global checks
    checks+=1
    if not assertion:
        raise AssertionError(desc)

def absolute_walk_mean(m,theta):
    return sum((F(comb(m,k))*theta**k*(1-theta)**(m-k)*abs(2*k-m)
                for k in range(m+1)), F(0))

def contrast_covariance(N,p):
    # Five multinomial categories: the four displayed cells and the rest.
    assert len(p)==5 and sum(p)==1 and all(z>=0 for z in p)
    eu=ev=euv=F(0)
    fact=factorial(N)
    for a in range(N+1):
      for b in range(N-a+1):
       for c in range(N-a-b+1):
        for d in range(N-a-b-c+1):
         e=N-a-b-c-d
         co=(a,b,c,d,e)
         mass=F(fact, factorial(a)*factorial(b)*factorial(c)*factorial(d)*factorial(e))
         for val,pj in zip(co,p): mass*=pj**val
         u=abs(a-b); v=abs(c-d)
         eu+=mass*u; ev+=mass*v; euv+=mass*u*v
    return euv-eu*ev

def regression_covariance(N,p):
    a=p[0]+p[1]; b=p[2]+p[3]
    theta=p[0]/a; phi=p[2]/b
    r=a/(1-b)
    h=[]; w=[]; f=[]
    for ell in range(N+1):
        z=sum((F(comb(N-ell,k))*r**k*(1-r)**(N-ell-k)*absolute_walk_mean(k,theta)
               for k in range(N-ell+1)),F(0))
        h.append(z)
        w.append(F(comb(N,ell))*b**ell*(1-b)**(N-ell))
        f.append(absolute_walk_mean(ell,phi))
    eh=sum((wz*hz for wz,hz in zip(w,h)),F(0))
    ef=sum((wz*fz for wz,fz in zip(w,f)),F(0))
    efh=sum((wz*hz*fz for wz,hz,fz in zip(w,h,f)),F(0))
    return efh-ef*eh, h

families=[
  (F(1,4),F(1,4),F(1,4),F(1,4),F(0)),
  (F(1,10),F(3,10),F(2,10),F(1,10),F(3,10)),
  (F(1,7),F(1,7),F(1,7),F(1,7),F(3,7)),
  (F(1,2),F(1,8),F(1,8),F(1,4),F(0)),
  (F(1,20),F(1,20),F(1,20),F(1,20),F(4,5)),
]
for p in families:
    require(sum(p)==1, 'probabilities sum to one')
    require(all(z>0 for z in p[:4]), 'positive displayed masses')
    for N in range(1,8):
        direct=contrast_covariance(N,p)
        via_regression,h=regression_covariance(N,p)
        require(direct==via_regression, 'direct regression agreement')
        require(direct<0, 'strict negativity')
        require(all(h[k]>=h[k+1] for k in range(len(h)-1)), 'opposite regression monotonicity')

for theta in [F(1,100),F(1,4),F(1,2),F(3,4),F(99,100)]:
    last=F(0)
    for m in range(1,41):
        nxt=absolute_walk_mean(m,theta)
        require(nxt>=last, 'biased-walk absolute mean monotonicity')
        last=nxt
print('PASS:',checks,'exact-rational assertions')
print('All checked disjoint multinomial absolute-count contrasts have strict negative covariance.')
print('The complete all-N theorem follows from conditional binomial regression, not enumeration.')
