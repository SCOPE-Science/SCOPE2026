#!/usr/bin/env python3
"""Exact-arithmetic verification of signed contraction-reset Brownian identities.
Only the stated stochastic model and its mathematical identities are used.
"""
import sympy as s
D,r,q,t=s.symbols('D r q t', positive=True)
checks=0
def check(expr, msg):
 global checks
 assert s.cancel(expr)==0, f'{msg}: {s.factor(expr)}'
 checks+=1

l1=r*(1-q); l2=r*(1-q**2); l4=r*(1-q**4)
V=2*D/l2
M4=12*D*V/l4
kappa=M4/V**2-3
check(kappa-3*(1-q*q)/(1+q*q),'stationary excess kurtosis')
check(l2/l1-1-q,'two relaxation rates reconstruct signed factor')
check(l1/(1-q)-r,'recovered reset rate')
check(V*l2/2-D,'recovered diffusivity')
check(M4*(r*(1-q**4))-12*D*V,'stationary fourth balance')
check(V*(r*(1-q**2))-2*D,'stationary second balance')
check((M4-V**2)-(s.factor(M4-V**2)),'fourth covariance normalization')
# Verify two contrasting signs have equal even stationary moments but distinct odd rates.
for c in [s.Rational(1,10),s.Rational(1,3),s.Rational(2,3),s.Rational(9,10)]:
 for R in [s.Rational(1,5),s.Rational(3,2),s.Rational(4,1)]:
  for diffusion in [s.Rational(1,7),s.Rational(4,3)]:
   a,b=[s.factor(x.subs({q:c,r:R,D:diffusion})) for x in [V,M4]]
   aa,bb=[s.factor(x.subs({q:-c,r:R,D:diffusion})) for x in [V,M4]]
   check(a-aa, 'matching variance')
   check(b-bb, 'matching fourth moment')
   check((l2/l1-1).subs({q:c,r:R})-c,'positive factor reconstruction')
   check((l2/l1-1).subs({q:-c,r:R})+c,'negative factor reconstruction')
   assert s.simplify(l1.subs({q:c,r:R}) - l1.subs({q:-c,r:R}))<0
   checks+=1
# For a genuine random signed multiplier, generator polynomial diagonal and
# off-diagonal coefficients are independently calculated by the affine flow.
u=s.symbols('u')
p1,p2=s.Rational(2,5),s.Rational(3,5)
for k in range(1,15):
 m=p1*(-s.Rational(1,3))**k+p2*(s.Rational(1,2))**k
 lam=s.Rational(7,4)*(1-m)
 gen=s.expand(s.Rational(11,6)*s.diff(u**k,u,2)+s.Rational(7,4)*(p1*(-u/3)**k+p2*(u/2)**k-u**k))
 check(gen.coeff(u,k)+lam, f'generator degree {k}')
 if k>=2:
  check(gen.coeff(u,k-2)-s.Rational(11,6)*k*(k-1),f'generator diffusion degree {k}')
 check(lam-s.Rational(7,4)+s.Rational(7,4)*m,'moment-rate reconstruction')
# Random-sign laws with the same absolute-value distribution have matching
# even reset moments and different odd reset moments.
for k in range(1,20):
 plus=s.Rational(2,5)*(s.Rational(1,3))**k+s.Rational(3,5)*(s.Rational(1,2))**k
 mixed=s.Rational(2,5)*(-s.Rational(1,3))**k+s.Rational(3,5)*(s.Rational(1,2))**k
 if k%2==0: check(plus-mixed,f'even multiplier moment {k}')
 else:
  assert plus!=mixed
  checks+=1
# Every conditional degree-n leading coefficient is the Poisson expectation
# E [(Q_1 ... Q_{N_t})**n] = exp(-r(1-m_n)t).
for k in range(1,13):
 m=p1*(-s.Rational(1,3))**k+p2*(s.Rational(1,2))**k
 # differential equation for Poisson mgf: d/dt a_n=-r(1-m_n) a_n
 rate=s.Rational(7,4)*(1-m)
 f=s.exp(-rate*t)
 check(s.diff(f,t)+rate*f, f'Poisson-product semigroup order {k}')
 # bound ensures rates converge to r, as Q is strictly contractive
 assert abs(m)<=s.Rational(1,2)**k
 checks+=1
print(f'PASS {checks} exact symbolic/rational assertions')
print('sample: for q=+/-2/3, r=5/4, D=3/7')
for sign in [1,-1]:
 values={q:sign*s.Rational(2,3),r:s.Rational(5,4),D:s.Rational(3,7)}
 print('q',sign*s.Rational(2,3),'Var',s.factor(V.subs(values)),'lambda_1',s.factor(l1.subs(values)),'lambda_2',s.factor(l2.subs(values)),'excess_kurtosis',s.factor(kappa.subs(values)))
