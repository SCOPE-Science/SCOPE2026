"""Standalone arithmetic checks for a sampled bang-bang value-gap theorem.

Only the explicit quadratic switching-function example is checked numerically;
general C^2 assertions are proved analytically in the accompanying result.
"""
from fractions import Fraction as F
from math import pi

ROOTS=(F(1,4),F(3,4))

def primitive(t):
    return t**3/F(3)-t**2/F(2)+F(3,16)*t

def signed_integral(a,b):
    return primitive(b)-primitive(a)

def gap_fraction(m,theta):
    h=F(1,m)
    cuts=[F(0)]
    k=-1
    while (k+theta)*h < 1:
        t=(k+theta)*h
        if 0<t<1: cuts.append(t)
        k+=1
    cuts.append(F(1))
    cuts.sort()
    gap=F(0)
    for l,r in zip(cuts,cuts[1:]):
        parts=[l]+[z for z in ROOTS if l<z<r]+[r]
        absolute=sum(abs(signed_integral(u,v)) for u,v in zip(parts,parts[1:]))
        gap+=absolute-abs(signed_integral(l,r))
    return gap

def phase(s):
    s=s%1
    return min(s*s,(1-s)*(1-s))

def prediction(m,theta):
    return sum(F(1,2)*phase(F(m)*z-theta) for z in ROOTS)/m**2

cases=0
for m in (8,9,16,17,40,41,80,81):
    for j in range(64):
        theta=F(j,64)
        actual=gap_fraction(m,theta)
        pred=prediction(m,theta)
        assert actual>=0
        assert abs(actual-pred) <= F(4,3*m**3), (m,theta,actual,pred)
        cases+=1

# Exact elementary values of g(U) on a uniformly random phase.
assert F(2)*F(1,2)**3/F(3)==F(1,12)
assert F(2)*F(1,2)**5/F(5)==F(1,80)
assert F(1,80)-F(1,12)**2==F(1,180)

# Two equal-slope switches: m even has coincident phases;
# m odd has half-period-separated phases.
a=F(1,2)
assert 4*a*a/F(180)==F(1,180)
assert a*a/F(720)==F(1,2880)
assert (F(1,180)/F(1,2880))==16

# Numerical check: exact discrete integration over 1024 rational shifts,
# including cancellations induced by the same random grid origin.
for m in (40,41,80,81):
    vals=[float(m*m*gap_fraction(m,F(j,1024))) for j in range(1024)]
    avg=sum(vals)/len(vals)
    var=sum((z-avg)**2 for z in vals)/len(vals)
    target=float(F(1,180) if m%2==0 else F(1,2880))
    assert abs(avg-1/12) < 1/m*0.4, (m,avg)
    assert abs(var-target) < (2/m)*target+1e-5, (m,var,target)

print('VERIFY_OK fraction_phase_cases=',cases,'two_switch_variance_ratio=16', 'mean_coefficient=1/12')
