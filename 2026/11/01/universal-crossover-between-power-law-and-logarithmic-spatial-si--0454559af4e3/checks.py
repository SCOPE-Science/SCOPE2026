"""Numerical consistency checks for Gaussian-velocity reset crossover."""
from math import sqrt, pi, exp, log, isfinite
from scipy.integrate import quad
from scipy.special import gamma
from numpy import euler_gamma


def response(t, damping):
    return -__import__('math').expm1(-damping*t)/damping


def integrated_response_square(t, damping):
    z = damping*t
    if z < 0.02:
        return t**3 * (1/3-z/4+7*z*z/60-z**3/24+31*z**4/2520)
    h = response(t,damping)
    return (t-2*h-__import__('math').expm1(-2*z)/(2*damping))/damping**2


def variance(t,eps,damping,dv):
    h=response(t,damping)
    return eps**2*h*h+2*dv*integrated_response_square(t,damping)


def universal(y):
    assert y != 0
    def integrand(u):
        if u == 0: return 0.
        return exp(-y*y/(2*u*u*(1+u)))/(sqrt(2*pi)*u*sqrt(1+u))
    return quad(integrand,0,1,epsabs=1e-11,limit=250)[0]+quad(integrand,1,__import__('math').inf,epsabs=1e-11,limit=250)[0]


def scaled_exact(eps,y,r,damping,dv):
    c=2*dv/3
    x=eps**3*y/c
    def integrand(u):
        if u==0:return 0.
        t=eps*eps*u/c
        w=variance(t,eps,damping,dv)
        if w<=0:return 0.
        return eps**3/c*exp(-r*t-x*x/(2*w))/sqrt(2*pi*w)
    return quad(integrand,0,1,epsabs=2e-10,limit=250)[0]+quad(integrand,1,__import__('math').inf,epsabs=2e-10,limit=250)[0]


def run_checks():
    n=0
    small_const=log(4)+(log(2)-float(euler_gamma))/2
    large_const=2**(1/6)*gamma(1/6)/(3*sqrt(2*pi))
    for y in [.0001,.00001,.001]:
        diff=sqrt(2*pi)*universal(y)-log(1/y)
        assert abs(diff-small_const)<.004,(y,diff,small_const)
        n+=1
    for y in [30.,100.,1000.]:
        ratio=universal(y)*y**(1/3)/large_const
        assert abs(ratio-1)<.002,(y,ratio)
        n+=1
    for y in [.2, .7, 1., 3., 8.]:
        assert abs(universal(y)-universal(-y))<1e-11
        n+=1
    for damping,dv,r in [(.7,1.4,1.2),(.2,.4,2.),(1.3,2.2,.3)]:
        for y in [.3,1.,3.]:
            errors=[]
            for eps in [.12,.06,.03]:
                got=scaled_exact(eps,y,r,damping,dv)
                target=universal(y)
                errors.append(abs(got-target)/target)
                assert isfinite(got) and got>0
                n+=1
            assert errors[-1]<errors[0] and errors[-1]<.22,(damping,y,errors)
            n+=1
    print(f'PASS: {n} quadrature, symmetry, and crossover consistency checks')

if __name__=='__main__':run_checks()
