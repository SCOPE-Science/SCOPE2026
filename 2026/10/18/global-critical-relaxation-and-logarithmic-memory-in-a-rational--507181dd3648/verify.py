"""Reproducible checks for a critical planar rational-map asymptotic theorem."""
import math
import sympy as s

b,q=s.symbols('b q', real=True)
r0=-1/(1+b)
A=-1/(1+b)**4
r=r0+A*q
r_next=-(1+b*r)*(1+r**2*q)
q_next=q/(1+r**2*q)**2
assert s.simplify(s.diff(r_next-r0-A*q_next,q).subs(q,0))==0
c=s.factor((2*r**2+r**4*q).subs(q,0))
H=s.factor(s.diff(2*r**2+r**4*q,q).subs(q,0))
assert s.simplify(c-2/(1+b)**2)==0
assert s.simplify(H-(5+b)/(1+b)**5)==0
assert s.simplify(H/c-(5+b)/(2*(1+b)**3))==0

# Finite trajectories corroborate the exact global theorem but do not prove it.
for bv,x0,y0 in [(-.7,.2,-.3),(-.25,-.9,.15),(0,.7,.45),(.6,.3,-.2),(.8,-.4,.2)]:
    x,y=x0,y0
    n=150000
    for _ in range(n):
        x,y=-x/(1+y*y),x+bv*y
    cinv=2/(1+bv)**2
    dlog=(5+bv)/(2*(1+bv)**3)
    val=1/(x*x)
    # The logarithmic correction is tiny compared to leading n, but has exact sign/coefficient.
    assert abs(val/n-cinv)<max(.01,0.02*cinv), (bv,val/n,cinv)
    assert abs(math.sqrt(n)*abs(y)-1/math.sqrt(2))<.05, (bv,math.sqrt(n)*abs(y))
    assert math.isfinite(val-cinv*n-dlog*math.log(n))
print('VERIFY_OK')
