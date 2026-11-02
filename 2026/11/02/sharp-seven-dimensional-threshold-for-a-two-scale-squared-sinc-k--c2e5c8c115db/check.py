#!/usr/bin/env python3
"""Exact symbolic reproducibility checks for the two-scale squared-sinc dimension cutoff."""
import itertools
import sympy as S

r,t=S.symbols('r t',positive=True,real=True)
EPS=[(tuple(e), S.prod(e), sum(ei*ai for ei,ai in zip(e,(1,1,t,t))))
     for e in itertools.product((1,-1),repeat=4)]

# The cubic B-spline of four independent uniform coordinates.
def piece_chamber(t_sample,r_sample):
    q1=q2=q3=0
    for e,sgn,offset in EPS:
        if (offset+r).subs({t:t_sample,r:r_sample})>0:
            q1+=sgn*3*(r+offset)**2
            q2+=sgn*6*(r+offset)
            q3+=sgn*6
    q1/=96*t*t; q2/=96*t*t; q3/=96*t*t
    p5=S.factor(S.Rational(2,3)*(r*r*q2-r*q1))
    p7=S.factor(S.Rational(2,15)*(3*r*r*q2-3*r*q1-r**3*q3))
    return p5,p7

p7_A=[r**3/(120*t*t),
      r*(r*r-4*(t-1)**2)/(80*t*t),
      r*(r*r-12*t*t+24*t+12)/(240*t*t),
      r*(12*(t+1)**2-r*r)/(240*t*t)]
p7_B=[r**3/(120*t*t),
      r/(10*t*t),
      p7_A[2],p7_A[3]]

# For each open chamber, the signs of the hinge arguments remain constant.
for ts,knots,want in ((S.Rational(3,2),[0,2*(t-1),2,2*t,2*(t+1)],p7_A),
                       (S.Integer(3),[0,2,2*(t-1),2*t,2*(t+1)],p7_B)):
    for i in range(4):
        mid=(S.sympify(knots[i])+S.sympify(knots[i+1])).subs(t,ts)/2
        got5,got7=piece_chamber(ts,mid)
        assert S.simplify(got7-want[i])==0, (ts,i,got7,want[i])

# Normalization and second moments in both analytic parameter chambers.
for knots,pieces in (([0,2*(t-1),2,2*t,2*(t+1)],p7_A),
                     ([0,2,2*(t-1),2*t,2*(t+1)],p7_B)):
    for k,want in ((0,S.Integer(1)),(2,S.Rational(14,3)*(1+t*t))):
        got=sum(S.integrate(r**k*pieces[i],(r,knots[i],knots[i+1])) for i in range(4))
        assert S.simplify(got-want)==0, (k,got)

# The spectral obstruction is exactly the quadratic threshold.
endpoint=S.factor(p7_B[2].subs(r,2*(t-1)))
assert S.simplify(endpoint - (t-1)*(-t*t+2*t+2)/(15*t*t))==0

# Every admissible pair has a positive upward jump in its 7D spectral density.
jump=S.factor((p7_B[3]-p7_B[2]).subs(r,2*t))
assert S.simplify(jump-S.Rational(2,15)*t)==0
jump_A=S.factor((p7_A[3]-p7_A[2]).subs(r,2*t))
assert S.simplify(jump_A-S.Rational(2,15)*t)==0

# Independent rational-exact probes of each branch, including an inadmissible ratio.
for tv in (S.Integer(1),S.Rational(3,2),S.Integer(2),S.Rational(5,2),
           S.Rational(11,4),S.Integer(3)):
    breaks=sorted(set([S.Integer(0),S.Integer(2),2*tv,2*abs(tv-1),2*(tv+1)]))
    for lo,hi in zip(breaks,breaks[1:]):
        x=(lo+hi)/2
        five,seven=piece_chamber(tv,x)
        g5=S.factor(five.subs({t:tv,r:x}))
        g7=S.factor(seven.subs({t:tv,r:x}))
        assert g5>=0, (tv,x,g5)
        if tv<=S.Rational(5,2): assert g7>=0, (tv,x,g7)
    if tv>=S.Rational(11,4):
        # Immediately to the right of the lower breakpoint the density is negative.
        x=2*(tv-1)
        assert p7_B[2].subs({t:tv,r:x})<0
print('PASS: exact B-spline formulas in both chambers; normalization and moments;')
print('       threshold and jump identities; rational nonnegative/negative probes.')
