"""Independent numerical checks for a stationary OU process with point resetting.
Run: python verify.py (requires numpy and scipy)."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import pbdv


def ratio(s, y):
    """U_s'(y)/U_s(y), calculated through parabolic-cylinder functions."""
    value, deriv = pbdv(-s, -y)
    if value <= 0 or not np.isfinite(value):
        raise ArithmeticError('Nonpositive/invalid cylinder evaluation')
    return y / 2 - deriv / value


def stationary_formula(s, y0, y):
    m = ratio(s, y0)
    mr = ratio(s, -y0)
    height = s / (m + mr)
    if y <= y0:
        v, _ = pbdv(-s, -y)
        v0, _ = pbdv(-s, -y0)
    else:
        v, _ = pbdv(-s, y)
        v0, _ = pbdv(-s, y0)
    # exp(-y²/2)U_s(+/-y) = Gamma(s)*exp(-y²/4)D_-s(-/+y)
    return height * math.exp((y0*y0-y*y)/4) * v/v0


def stationary_renewal(s, y0, y):
    """Independent OU Gaussian-age renewal integral, with t=e^{-age}."""
    def integrand(t):
        variance = 1-t*t
        return s*t**(s-1)/math.sqrt(2*math.pi*variance) * math.exp(-(y-y0*t)**2/(2*variance))
    # endpoint singularities are integrable, subdivide for quadrature
    return (quad(integrand,0,0.5,epsabs=1e-10,limit=200)[0]
            +quad(integrand,0.5,1,epsabs=1e-10,limit=200)[0])


def s_critical(y0):
    return brentq(lambda s:ratio(s,y0)-y0,0.000001,0.999999,xtol=1e-13)


def free_mode(s):
    if not 0<s<1:raise ValueError('free mode only for 0<s<1')
    return brentq(lambda y:ratio(s,y)-y,0,15,xtol=1e-13)


def run():
    cases=0
    max_rel=0
    # Closed form vs numerically independent Gaussian renewal resolvent.
    for s in (0.2,0.5,0.8,1.2,2.3):
        for y0 in (0.25,0.8,1.7,3.0):
            for delta in (-2.3,-1.0,-0.25,0.2,0.8,2.1):
                y=y0+delta
                explicit=stationary_formula(s,y0,y)
                renewal=stationary_renewal(s,y0,y)
                err=abs(explicit-renewal)/max(1e-12,renewal)
                max_rel=max(max_rel,err)
                assert err<8e-7,(s,y0,y,explicit,renewal,err)
                cases+=1
    # Pinning threshold, uniqueness and independence of remote reset point.
    previous=0
    for s in (0.1,0.25,0.5,0.75,0.9,0.99):
        y=free_mode(s)
        assert y>previous
        assert ratio(s,y-0.01)>y-0.01
        assert ratio(s,y+0.01)<y+0.01
        for y0 in (y+0.1,y+0.7):
            assert ratio(s,y0)-y0<0
        previous=y
    previous=0
    for y0 in (0.2,0.5,1.0,2.0,3.0,4.0):
        s=s_critical(y0)
        assert 0<s<1 and s>previous
        assert ratio(s-0.01 if s>0.01 else s/2,y0)<y0
        assert ratio((s+1)/2,y0)>y0
        previous=s
    # Special identity U_1'/U_1-y = 1/U_1 >0, using integral.
    for y in (0,0.4,1.0,2.0):
        u1=math.exp(y*y/2)*math.sqrt(2*math.pi)*0.5*(1+math.erf(y/math.sqrt(2)))
        assert abs((ratio(1,y)-y)-1/u1)<1e-12
    print('PASS independent renewal comparisons:',cases)
    print('max relative error:',max_rel)
    print('free mode at s=0.5:',free_mode(0.5))
    print('critical rate at y0=1:',s_critical(1))
    print('PASS monotonicity/brackets, special identity and mode saturation checks')

if __name__=='__main__': run()
