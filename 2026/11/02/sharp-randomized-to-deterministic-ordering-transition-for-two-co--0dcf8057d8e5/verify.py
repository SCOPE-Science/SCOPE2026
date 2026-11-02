#!/usr/bin/env python3
"""Exact checks for curvature-dependent permutation sampling in a two-loss scalar model.
Run: python verify.py. Requires sympy as declared in requirements.txt.
"""
from fractions import Fraction as Q
import itertools
import sympy as S

a,b,h,p,d = S.symbols('a b h p d', positive=True)
t = (1-h*a)*(1-h*b)
Umean = p*(a+b)-a
Usq = p*b*b+(1-p)*a*a
varU=S.factor(Usq-Umean**2)
mean=S.factor(h*h*d*Umean/(1-t))
var=S.factor(h**4*d**2*varU/(1-t*t))
E=S.factor(mean**2+var)
pfree=a/(a+b)+(a-b)*(1-t)/(4*t*(a+b))
assert S.simplify(varU-(a+b)**2*p*(1-p))==0
assert S.simplify(S.diff(E,p).subs(p,pfree))==0
assert S.simplify(S.diff(E,p,2)-4*h**4*d**2*t*(a+b)**2/((1-t)**2*(1+t)))==0
assert S.simplify(pfree-1-(a-b-t*(a+3*b))/(4*t*(a+b)))==0
assert S.simplify(pfree-((a-b)+t*(3*a+b))/(4*t*(a+b)))==0
assert S.simplify(S.limit(E.subs(p,S.Rational(1,2))/h**2,h,0)-(d*(a-b)/(2*(a+b)))**2)==0
assert S.simplify(S.limit(E.subs(p,pfree)/h**3,h,0)-d**2*a*b/(2*(a+b)))==0
# At a=b, uniquely optimal uniform choice within the open nonovershoot domain.
assert S.simplify(pfree.subs(b,a)-S.Rational(1,2))==0
# A fully exact rational phase boundary at a=3, b=1.
threshold=(2-S.sqrt(2))/3
assert S.simplify(t.subs({a:3,b:1,h:threshold})-S.Rational(1,3))==0
assert S.simplify(pfree.subs({a:3,b:1,h:S.Rational(1,4)})-1)>0
assert S.simplify(E.subs({a:3,b:1,h:S.Rational(1,4),p:1,d:1})-S.Rational(1,169))==0
assert S.simplify(E.subs({a:3,b:1,h:S.Rational(1,4),p:S.Rational(1,2),d:1})-S.Rational(1,169))>0

checks=12
# Enumerate every random order sequence for finite horizons, compare moment recurrences.
for aa,bb,hh,pp,z0,dd in [
 (3,1,Q(1,10),Q(415,504),Q(2,3),Q(2)),
 (3,1,Q(1,4),Q(1),Q(1,5),Q(3)),
 (2,3,Q(1,7),Q(1,4),Q(-2),Q(1,3)),
 (1,1,Q(1,2),Q(1,2),Q(0),Q(1)),
 (5,2,Q(1,8),Q(3,5),Q(3),Q(1)),
 (4,7,Q(1,12),Q(1,3),Q(-1,7),Q(5,4)),
 ]:
    if not isinstance(aa,Q): aa=Q(aa)
    if not isinstance(bb,Q): bb=Q(bb)
    if not isinstance(hh,Q): hh=Q(hh)
    if not isinstance(pp,Q): pp=Q(pp)
    if not isinstance(z0,Q): z0=Q(z0)
    if not isinstance(dd,Q): dd=Q(dd)
    tt=(1-hh*aa)*(1-hh*bb)
    U1=bb
    U0=-aa
    mu=pp*U1+(1-pp)*U0
    eu2=pp*U1*U1+(1-pp)*U0*U0
    mom=z0; mom2=z0*z0
    for k in range(1,10):
        mom2=tt*tt*mom2 + 2*tt*hh*hh*dd*mu*mom+hh**4*dd**2*eu2
        mom=tt*mom+hh*hh*dd*mu
        brute1=Q(0); brute2=Q(0)
        for seq in itertools.product((0,1),repeat=k):
            z=z0; w=Q(1)
            for bit in seq:
                z=tt*z+hh*hh*dd*(U1 if bit else U0)
                w*= pp if bit else (1-pp)
            brute1+=w*z
            brute2+=w*z*z
        assert brute1==mom and brute2==mom2,(aa,bb,hh,pp,k)
        checks+=2
# Show exact match of linear recursion stationary mean and second moment.
mu_inf=mean
second_inf=E
assert S.simplify(mu_inf-(t*mu_inf+h*h*d*Umean))==0
assert S.simplify(second_inf-(t*t*second_inf+2*t*h*h*d*Umean*mu_inf+h**4*d*d*Usq))==0
checks+=2
print('PASS: symbolic stationary identities, sharp phase, exact asymptotic constants,')
print(f'      exhaustive rational sampling paths and moment recurrences; {checks} exact checks.')
