"""Independent finite sanity checks for a three-term sup-norm inequality.
The general theorem is proved analytically in RESULT.md; these checks are finite only.
"""
from fractions import Fraction as F
from math import cos, sin, pi, sqrt
import cmath


def min_squared(t, placement):
    if placement == 'outer':
        return 4+t*t
    if t <= .2:
        return (2-t)**2
    return 1/(4*t)+1.5+2.25*t+t*t


def run():
    assertions = 0
    assert 27 > 25
    assertions += 1
    assert 2**(4/3) < 13/5
    assertions += 1
    assert (4/3)*3**(1/3)<2
    assertions += 1
    assert 22*22-4*25*5<0
    assertions += 1
    for j in range(1,501):
        t=F(j,500)
        if t<=F(1,5):
            assert (2-t)**2 - (F(13,5)+t+t*t)==F(7,5)-5*t
        else:
            lhs=F(1,4)/t+F(3,2)+F(9,4)*t+t*t-(F(13,5)+t+t*t)
            assert lhs==(25*t*t-22*t+5)/(20*t)
        assertions+=1
        assert (F(7,5)-5*t>0 if t<=F(1,5) else (25*t*t-22*t+5)>0)
        assertions+=1
    # Numerical torus checks: phase-sampled peaks must not fall substantially below
    # the exact phase-independent lower bound. Sampling is not a proof.
    for placement in ['outer','center']:
        for ti in range(21):
            t=ti/20
            if placement == 'outer': u,v,b=1.,1.,t
            else: u,v,b=1.,t,1.
            bound=min_squared(t,placement)
            for phasej in range(13):
                bphase=phasej*pi/13
                p=b*cmath.exp(1j*bphase)
                peak=max(abs(u*cmath.exp(-2j*pi*k/512)+p+v*cmath.exp(2j*pi*k/512))**2 for k in range(512))
                assert peak>bound-.0004,(placement,t,bphase,peak,bound)
                assertions+=1
    assert 3**(3/4)>sqrt(5)
    assertions+=1
    return assertions

if __name__=='__main__':
    print('passed finite assertions:',run())
