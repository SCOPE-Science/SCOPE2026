#!/usr/bin/env python3
"""Independent finite sanity checks for the four-oval chemical oscillator.

Python 3.9+ standard library only. Run: python verify.py
These checks supplement but do not substitute for the analytic proof.
"""
from fractions import Fraction as Q
from math import asin, atan, cos, exp, isfinite, log, pi, sin, sqrt

MU_C = 337.0 / 9.0

def simpson(f, lo, hi, n=8000):
    assert n > 0 and n % 2 == 0
    h = (hi - lo) / n
    v = f(lo) + f(hi)
    for j in range(1, n):
        v += (4 if j % 2 else 2) * f(lo + j * h)
    return v * h / 3

def quadratures(mu, eps=1):
    assert mu > MU_C and eps > 0
    k = 7 / (3 * sqrt(mu - 32))
    def samples(phi):
        theta = asin(k * sin(phi)) / 2
        A = 16 + (mu - 32) * sin(2 * theta)**2 / 4
        D = 7 * max(0.0, cos(phi))
        rp = sqrt((25 + D) / (2 * A))
        rm = sqrt((25 - D) / (2 * A))
        return theta, rp, rm
    def time_integrand(phi, left):
        theta, rp, rm = samples(phi)
        v1, v2 = rp * sin(theta), rm * sin(theta)
        u1, u2 = rp * cos(theta), rm * cos(theta)
        sign = -1 if left else +1
        w1 = (2 + sign * u1) * (2 + v1)
        w2 = (2 + sign * u2) * (2 + v2)
        return (1 / w1 + 1 / w2) / sqrt(1 - k*k*sin(phi)**2)
    tr = k/(28*eps)*simpson(lambda p:time_integrand(p,False),-pi/2,pi/2)
    tl = k/(28*eps)*simpson(lambda p:time_integrand(p,True),-pi/2,pi/2)
    def geometric_integrand(phi):
        theta, rp, rm = samples(phi)
        A = 16 + (mu - 32) * sin(2*theta)**2 / 4
        D = 7*max(0.0,cos(phi))
        # Radial integral of the Laplacian, independent of period formula.
        radial = (48 + mu/2)*(25*D/A**2) - 50*(D/A)
        dtheta = k*cos(phi)/(2*sqrt(1-k*k*sin(phi)**2))
        return radial*dtheta
    geom = simpson(geometric_integrand,-pi/2,pi/2)
    return tr,tl,geom

def independent_return(mu=39.0, eps=1.0):
    # Fourth-order Runge-Kutta at fixed timestep, without integrating any polar formula.
    def rhs(x,y):
        u,v=x-2,y-2
        h=16*(u**4+v**4)-25*(u*u+v*v)+mu*u*u*v*v+9
        hx=64*u**3-50*u+2*mu*u*v*v
        hy=64*v**3-50*v+2*mu*u*u*v
        return x*y*(-h*hx-eps*hy), x*y*(-h*hy+eps*hx)
    n=20000
    t_target=quadratures(mu,eps)[0]
    step=t_target/n
    x,y=3.0,2.0
    for _ in range(n):
        a,b=rhs(x,y)
        c,d=rhs(x+step*a/2,y+step*b/2)
        e,f=rhs(x+step*c/2,y+step*d/2)
        g,h=rhs(x+step*e,y+step*f)
        x+=step*(a+2*c+2*e+g)/6
        y+=step*(b+2*d+2*f+h)/6
    return abs(x-3), abs(y-2)

def main():
    # The rational saddle clocks, computed independently from chemical weights.
    wpp,wpm,wmm=Q(169,25),Q(91,25),Q(49,25)
    cr=Q(1,28)*(1/wpp+1/wpm)
    cl=Q(1,28)*(1/wpm+1/wmm)
    assert cr==Q(125,8281) and cl==Q(125,4459)
    assert cl/cr==Q(13,7)
    ic=Q(8407,400)+float(Q(1225,384))*atan(7/24)
    ic_float=float(ic)
    ic_integral=simpson(lambda z:12600*(625-49*z*z)/(576+49*z*z)**2,0,1)
    assert abs(ic_integral-ic_float)<1e-9
    for mu in (39.0,40.0,100.0):
        r,l,g=quadratures(mu)
        assert 0<r<l and g>0 and all(isfinite(v) for v in (r,l,g))
        half=quadratures(mu,2.0)
        assert abs(half[0]-r/2)<1e-11 and abs(half[1]-l/2)<1e-11
        assert abs(half[2]-g)<1e-10
        assert 0<exp(-g)<1
    for delta in (0.01,0.001):
        r,l,g=quadratures(MU_C+delta)
        assert abs(g-ic_float)<0.5
        assert r>0 and l>r
    errx,erry=independent_return()
    assert max(errx,erry)<2e-6,(errx,erry)
    print('CHECK_OK')

if __name__=='__main__': main()
