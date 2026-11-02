"""Reproducible algebraic and numerical checks for the stadium rectangle theorem.

Requires Python 3.10+ and SymPy 1.10+. These checks supplement, not replace,
the geometric proof in RESULT.md.
"""
from math import pi, sqrt, hypot, cos, sin
from random import Random
import sympy as sp

v=sp.symbols('v', positive=True)
p=sp.pi
fill=4*(1-v**2)**sp.Rational(3,2)/(4-8*v*v+p*v)
normalized=v*(1-v**2)**sp.Rational(3,2)/(2-4*v*v+p*v)**2
fill_d=4*sp.sqrt(1-v*v)*(4*v-p)*(2*v*v+1)/(4-8*v*v+p*v)**2
normalized_d=sp.sqrt(1-v*v)*(2*v*v+1)*(p*v-2)/(4*v*v-p*v-2)**3
assert sp.simplify(sp.diff(fill,v)-fill_d)==0
assert sp.simplify(sp.diff(normalized,v)-normalized_d)==0
assert sp.simplify(fill.subs(v,1/sp.sqrt(2))-2/p)==0
assert sp.simplify(normalized.subs(v,2/p)-1/(8*sp.sqrt(p*p-4)))==0
assert sp.simplify(normalized.subs(v,1/sp.sqrt(2))-1/(2*p*p))==0
assert sp.simplify((1-2*v*v)/v-(1/v-2*v))==0
print('EXACT_PROFILE_DERIVATIVES_AND_SHARP_CONSTANT_PASSED')

# A centered rectangle with half-sides (u,w) and rotation angle phi
# has diagonal points (u*cos(phi) +/- w*sin(phi), u*sin(phi) -/+ w*cos(phi)).
# Independently scale each trial rectangle until its corners first touch
# the stadium; compare feasible area with the proposed closed expression.
def belongs(x,y,a):
    return hypot(max(abs(x)-a,0.0), y)<=1+1e-13

def radial_scale(x,y,a):
    lo,hi=0.0,(a+1)/hypot(x,y)
    for _ in range(54):
        mid=(lo+hi)/2
        if belongs(mid*x,mid*y,a):lo=mid
        else:hi=mid
    return lo

rng=Random(245716)
for a in [0.02,0.19,pi/2-4/pi,1.0,2.75,8.0]:
    t=(sqrt(a*a+8)-a)/4
    M=4*(a+t)*sqrt(1-t*t)
    assert abs(t*a+2*t*t-1)<2e-12
    # The predicted maximizer has all four vertices in the right cap.
    assert abs(hypot(t,sqrt(1-t*t))-1)<2e-12
    # Random rectangle orientations and aspect ratios, feasible scaling.
    sampled=0.0
    for k in range(4500):
        angle=(pi/2)*rng.random()
        aspect=10**(rng.uniform(-1.3,1.3))
        u,w=aspect,1.0
        c,s=cos(angle),sin(angle)
        p1=(u*c-w*s,u*s+w*c)
        p2=(u*c+w*s,u*s-w*c)
        factor=min(radial_scale(*p1,a),radial_scale(*p2,a))
        area=4*u*w*factor*factor
        sampled=max(sampled,area)
        assert area<=M*(1+5e-12), (a,k,area,M)
    # Check a feasible witness exactly at the predicted optimal shape.
    w=sqrt(1-t*t)
    witness=min(radial_scale(a+t,w,a),radial_scale(a+t,-w,a))
    assert abs(4*(a+t)*w*witness*witness-M)<1e-9
print('INDEPENDENT_FEASIBLE_ROTATED_RECTANGLE_SAMPLING_PASSED')
print('ALL_CHECKS_PASSED')
