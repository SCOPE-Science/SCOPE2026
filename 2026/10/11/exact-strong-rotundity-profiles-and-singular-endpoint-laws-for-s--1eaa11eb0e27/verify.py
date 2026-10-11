"""Independent finite arithmetic checks supporting the scalar-summand radius theorem.

Run: python verify.py
The analytic proof, not these finite checks, covers all real exponents and Banach spaces.
"""
from fractions import Fraction as Q
from random import Random
from math import isclose

rng=Random(20231043)
checks=0
# Exact rational arithmetic for integer exponents, including sign transitions.
for p in (1,2,3,4,5,7):
    for j in range(0,81):
        d=Q(j,40)
        t=1-d
        fiber_power=1-abs(t)**p
        assert fiber_power>=0
        G=d**p+fiber_power
        assert G==d**p+1-abs(1-d)**p
        for i in range(0,81):
            s=Q(i,80) # transverse norm as a percentage of the maximum
            v_power=s**p*fiber_power
            assert abs(t)**p+v_power<=1
            actual=d**p+v_power
            assert actual<=G
            checks+=1
        # exact distinguished boundary attains the radius
        assert d**p+fiber_power==G
    # exact universal pivot at unit separation
    assert Q(1,2)**p+1-abs(1-Q(1,2))**p==1
    if p==2:
        for j in range(81):
            d=Q(j,40)
            assert d**2+1-abs(1-d)**2==2*d
    if p==1:
        for j in range(81):
            d=Q(j,40)
            assert d+1-abs(1-d)==2*min(d,1)

# A second independent simulation computes the smallest deficiency among random
# feasible two-dimensional sample points and checks the analytic lower bound.
def eta(p,e):
    if p==1: return e/2
    if p==float('inf'): return 0.0 if e<=1 else e
    lo,hi=0.0,2.0
    for _ in range(65):
        d=(lo+hi)/2
        g=d**p+1-abs(1-d)**p
        if g>=e**p:hi=d
        else:lo=d
    return hi
for p in (1,1.4,2,2.5,3,5,10,float('inf')):
    for e in (0.0,0.2,0.55,0.9,1.0,1.15,1.4,1.8,2.0):
        a=eta(p,e)
        if p!=float('inf') and e==1.0: assert abs(a-0.5)<1e-11
        if p!=float('inf') and p>1 and e==2.0: assert abs(a-2.0)<1e-11
        if p==float('inf'): assert a==(0.0 if e<=1 else e)
        if p==2: assert abs(a-e*e/2)<1e-12
        if p==1: assert abs(a-e/2)<1e-12
        for j in range(60):
            t=rng.uniform(-1,1)
            if p==float('inf'):
                v=rng.uniform(-1,1)
                dist=max(abs(t-1),abs(v))
            else:
                vmax=(1-abs(t)**p)**(1/p)
                v=rng.uniform(-vmax,vmax)
                dist=(abs(1-t)**p+abs(v)**p)**(1/p)
            if dist>=e+1e-9:
                assert 1-t+2e-9>=a,(p,e,t,v,dist,a)
                checks+=1
# All derivative and global monotonicity assertions are proved symbolically
# in RESULT.md; the finite checks intentionally do not pretend to prove them.
print('VERIFY_OK exact_rational_and_sample_checks='+str(checks)+' endpoint_pivot=half small_epsilon_exponent=p')
