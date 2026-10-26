"""Standalone exact-rational verification of the two-state harmonic-variance invariant law.
Requires Python standard library and SymPy 1.13+; run: python verify_switching_trap.py
"""
from fractions import Fraction as Q
import random, math


def prod(items):
    ans=Q(1)
    for y in items:ans*=y
    return ans


def rising(a,n):return prod(a+j for j in range(n))

def beta_moment(k,h,D,u,v,n):
    a=u/(2*k); b=v/(2*h); be=b-a
    if be<=n:raise ValueError('divergent moment')
    pi_plus=v/(u+v); pi_minus=u/(u+v)
    kappa=1+k/h
    total=Q(0)
    for j in range(n+1):
        denominator=prod(be-l for l in range(1,j+1))
        term=Q(math.comb(n,j))*kappa**j*(pi_plus*rising(a,j)+pi_minus*rising(a+1,j))/denominator
        total+=term
    return (D/k)**n*total

def rec_moments(k,h,D,u,v,n):
    pi_plus=v/(u+v);pi_minus=u/(u+v)
    xp,xm=pi_plus,pi_minus
    for l in range(1,n+1):
        aa=2*l*k+u;ab=-v;ba=-u;bb=v-2*l*h
        den=aa*bb-ab*ba
        rp=2*l*D*xp;rm=2*l*D*xm
        xp=(rp*bb-ab*rm)/den
        xm=(aa*rm-rp*ba)/den
    return xp+xm

random.seed(23941)
checks=0
for _ in range(180):
    k=Q(random.randint(2,8));h=Q(random.randint(1,int(k)-1))
    u=Q(random.randint(1,14));
    n=random.randint(1,5)
    v=Q(random.randint(2,16))+Q(2*h*n)+u*h/k
    D=Q(random.randint(1,7),random.randint(1,5))
    assert v/h-u/k>2*n
    lhs=beta_moment(k,h,D,u,v,n)
    rhs=rec_moments(k,h,D,u,v,n)
    assert lhs==rhs, (k,h,D,u,v,n,lhs,rhs)
    checks+=1

# Local generator balance test at rational states: density flux derivative, switching flow and mixture mass.
from sympy import symbols, diff, simplify
z,k,h,u,v=symbols('z k h u v', positive=True)
a=u/(2*k);b=v/(2*h);eta=1+k/h
J=-z**a*(z+eta)**(-b)
pplus=-J/(2*k*z)
pminus=-J/(2*h*(z+eta))
assert simplify(diff(J,z)+u*pplus-v*pminus)==0
assert simplify(-2*k*z*pplus+2*h*(z+eta)*pminus)==0
print('PASS: 180 exact-rational all-order moments and symbolic stationary flux equations.')

# Asymptotic exponent and coefficient tests from exact Beta prime density, numeric quadrature.
import mpmath as mp
mp.mp.dps=40
params=[(2,1,2,3),(3,1,5,14),(4,2,3,13)]
for k,h,u,v in params:
  a=mp.mpf(u)/(2*k); b=mp.mpf(v)/(2*h); B=b-a; eta=1+mp.mpf(k)/h
  pip=mp.mpf(v)/(u+v); pim=mp.mpf(u)/(u+v)
  assert B>0
  c=pip*eta**(B+1)/(B*mp.beta(a,B))
  # Compare exact mixture tail via incomplete Beta regularization to its asymptotic.
  for z0 in (10**5,10**7):
   t=eta/(z0+eta)
   surv=pip*mp.betainc(B,a,0,t,regularized=True)+pim*mp.betainc(B,a+1,0,t,regularized=True)
   ratio=surv/(c*z0**(-B))
   assert abs(ratio-1)< mp.mpf('0.002'), (params, z0, ratio)
print('PASS: 6 independent high-tail asymptotic checks.')
