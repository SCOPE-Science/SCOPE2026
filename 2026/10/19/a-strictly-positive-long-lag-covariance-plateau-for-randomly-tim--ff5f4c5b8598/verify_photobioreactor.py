"""Independent arithmetic illustrations for a randomly period-forced photosynthetic two-mode kinetic model.
The analytical limit theorem is proved separately; quadrature here is finite evidence only.
"""
import math
import numpy as np
from scipy.integrate import quad


def period_mean(h, a, b, c, r):
    u = a*r
    v = b*(1-r)
    q = (-np.expm1(-u*h))*(-np.expm1(-v*h))/(-np.expm1(-(u+v)*h))/h
    return c*(1-r) + c*(1/a-1/b)*q


def trajectory(t, h, a, b, c, r):
    phase = np.remainder(t, h)
    dark = r*h
    x0 = c*(-np.expm1(-b*(1-r)*h))/(-np.expm1(-(a*r+b*(1-r))*h))
    lower = x0*np.exp(-a*dark)
    return np.where(phase < dark, x0*np.exp(-a*phase),
                    c+(lower-c)*np.exp(-b*(phase-dark)))


def run():
    configs = [(1., 3., 1., .4),(.5,2.,1.5,.6),(2.,4.,.7,.25)]
    checks=0
    for a,b,c,r in configs:
        hs=np.linspace(.02,5.,80)
        averages=period_mean(hs,a,b,c,r)
        assert np.all(np.diff(averages)<0)
        checks+=1
        for h in hs[::7]:
            integration=quad(lambda t: float(trajectory(t,np.array(h),a,b,c,r)),0,h,
                             points=[r*h],epsabs=1e-12,epsrel=1e-12)[0]/h
            assert abs(integration-period_mean(h,a,b,c,r))<1e-11
            checks+=1
        # Formula for the first periodic point must close one full cycle.
        for h in hs[::7]:
            x0=c*(-math.expm1(-b*(1-r)*h))/(-math.expm1(-(a*r+b*(1-r))*h))
            x1=c+(x0*math.exp(-a*r*h)-c)*math.exp(-b*(1-r)*h)
            assert abs(x0-x1)<1e-13
            checks+=1
    a,b,c,r=1.,3.,1.,.4
    hs=np.linspace(.6,2.2,250001)
    avg=period_mean(hs,a,b,c,r)
    plateau=float(np.var(avg))
    assert plateau>0
    # Time-averaged conditional orbit variance is positive and bounded.
    orbit_variance=float(np.mean((trajectory(.37*hs,hs,a,b,c,r)-avg)**2))
    assert orbit_variance>0
    # Lag limits require t -> infinity first, then lag -> infinity.
    # Quadrature is only illustrative; the proof uses phase mixing.
    t=600.
    x=trajectory(t,hs,a,b,c,r)
    y=trajectory(t+1000,hs,a,b,c,r)
    empirical=float(np.mean((x-np.mean(x))*(y-np.mean(y))))
    assert abs(empirical-plateau)<.001
    print('PASS checks:',checks+3)
    print('quenched plateau =',plateau)
    print('finite-time long-lag covariance =',empirical)
    print('unconditioned cycle-variance witness =',orbit_variance)

if __name__=='__main__':run()
