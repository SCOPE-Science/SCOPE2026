#!/usr/bin/env python3
"""Reproduce exact algebra and illustrative rational/numerical tests of the SIRCm equilibrium theorem.

Requires Python 3.10+ and SymPy. The infinite theorem is established by the accompanying proof;
this script checks the main identities exactly and samples the model equations.
"""
from fractions import Fraction
import sympy as s

m,a,b,d,g,p,e1,e2,z=s.symbols('mu alpha beta delta gamma sigma epsilon_1 epsilon_2 I', real=True)
u,v=s.symbols('G_1 G_2',real=True)
q=(m+a)/b
U=1-q
K=b*z+m+g*v+d*(1-p)*u
D=(m+d*u)*(m+g*v)+b*z*(m+p*d*u)
C=a*d*u*z/D
R=a*z*(b*z+m+g*v)/D
S=q-p*C
H=z+R+(1-p)*C
assert s.cancel(H-z-a*z*K/D)==0
# All equilibrium equations are exactly reconstructed on H(I)=U.
generic=[m*(1-S)-b*S*z+g*v*C,
         b*S*z+p*b*C*z-(m+a)*z,
         (1-p)*b*C*z+a*z-m*R-d*u*R,
         d*u*R-b*C*z-m*C-g*v*C]
assert s.cancel(generic[0]-m*(U-H))==0
for resid in generic[1:]: assert s.cancel(resid)==0
D0=s.expand(D.subs({u:1+e1*z,v:1+e2*z}))
K0=s.expand(K.subs({u:1+e1*z,v:1+e2*z}))
d0=(m+d)*(m+g)
d1=d*e1*(m+g)+g*e2*(m+d)+b*(m+p*d)
d2=d*g*e1*e2+b*p*d*e1
k0=m+g+d*(1-p)
k1=b+g*e2+d*(1-p)*e1
assert s.expand(D0-(d0+d1*z+d2*z*z))==0
assert s.expand(K0-(k0+k1*z))==0
E=(b*b*(m+p*d)+b*e1*d*(1-p)*(g+2*m)
  +b*e2*g*(d*(1+p)+2*m)+e1*e1*d*d*(g+m)*(1-p)
  +e1*e2*d*g*m*(1-p)+e2*e2*g*g*(d+m))
assert s.expand(k1*d1-k0*d2-E)==0
Hderiv=s.cancel(s.diff(z*K0/D0,z)-
 (k0*d0+2*k1*d0*z+E*z*z)/D0**2)
assert Hderiv==0
P1=s.expand(s.diff(K,u)*D-K*s.diff(D,u))
P2=s.expand(s.diff(K,v)*D-K*s.diff(D,v))
assert s.expand(P1+d*(b*z+g*v+m)*(b*z*p+g*v+m*p))==0
assert s.expand(P2+d*g*u*(1-p)*(b*z+d*u+m))==0
print('EXACT_SYMBOLIC_IDENTITIES=11')

# Exact rational sampled checks; nothing here is substituted for the analytic positivity proof.
cases=[(Fraction(1,50),Fraction(3),Fraction(8),Fraction(5,8),Fraction(7,20),Fraction(ps,4),Fraction(ee1,3),Fraction(ee2,7))
       for ps in range(5) for ee1 in (0,1,4,20) for ee2 in (0,2,5,50)]
def scalar(I,mu,al,be,de,ga,si,ep1,ep2):
    g1=1+ep1*I;g2=1+ep2*I
    DD=(mu+de*g1)*(mu+ga*g2)+be*I*(mu+si*de*g1)
    KK=be*I+mu+ga*g2+de*(1-si)*g1
    return I+al*I*KK/DD
for par in cases:
    mu,al,be,de,ga,si,ep1,ep2=par
    assert be>mu+al
    ceiling=1-(mu+al)/be
    low,high=Fraction(0),ceiling
    for _ in range(110):
        mid=(low+high)/2
        if scalar(mid,*par)<ceiling: low=mid
        else: high=mid
    I=(low+high)/2
    assert low<I<high and scalar(low,*par)<ceiling<scalar(high,*par)
    g1=1+ep1*I;g2=1+ep2*I
    DD=(mu+de*g1)*(mu+ga*g2)+be*I*(mu+si*de*g1)
    C=al*de*g1*I/DD
    R=al*I*(be*I+mu+ga*g2)/DD
    S=(mu+al)/be-si*C
    assert S>mu/be and R>0 and C>0
    assert scalar(I,*par)-ceiling == I+R+(1-si)*C-ceiling
    if ep1: assert scalar(I,mu,al,be,de,ga,si,0,ep2)>scalar(I,*par)
    if ep2 and si<1: assert scalar(I,mu,al,be,de,ga,si,ep1,0)>scalar(I,*par)
    if si==1: assert scalar(I,mu,al,be,de,ga,si,ep1,0)==scalar(I,*par)
print('EXACT_RATIONAL_CASES=',len(cases))
print('ALL_CHECKS_PASS')
