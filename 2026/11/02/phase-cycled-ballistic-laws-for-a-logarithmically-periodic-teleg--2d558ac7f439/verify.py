"""Reproducible numerical checks for periodic-hazard telegraph scaling.

These are finite consistency tests, not an infinite-time proof.
"""
from math import cos, pi, exp, sqrt, log
import numpy as np
from scipy.integrate import solve_ivp, quad


def periodic_moments(c, epsilon, omega, periods=80, n=2001):
    assert 0 <= abs(epsilon) < c and c > 0 and omega > 0
    T = 2*pi/omega
    def rhs(s, v):
        r = c + epsilon*cos(omega*s)
        a, q = v
        return [1 - (1+2*r)*a, 2*a - 2*q]
    sol=solve_ivp(rhs, (0, periods*T), [0.,0.],
                  rtol=1e-11, atol=1e-13, dense_output=True,
                  max_step=T/200)
    assert sol.success
    theta=np.linspace(0,T,n)
    vals=sol.sol(theta+(periods-1)*T)
    return theta, vals[0],vals[1]


def main():
    checks=0
    for c in (0.2,0.5,1.0,3.0):
        th,a,q=periodic_moments(c,0.0,1.3,periods=25,n=17)
        expected=1/(1+2*c)
        assert max(abs(a-expected))<3e-9
        assert max(abs(q-expected))<3e-9
        checks+=2
    for (c,eps,om) in ((.3,.14,.7),(1.,.4,2.),(2.,1.,.31)):
        th,a,q=periodic_moments(c,eps,om,periods=60,n=721)
        assert np.max(q)-np.min(q)>1e-4
        assert np.min(q)>0 and np.max(q)<1
        assert abs(q[0]-q[-1])<5e-8
        assert abs(a[0]-a[-1])<5e-8
        # Direct Feynman--Kac formula at different logarithmic phases.
        for idx in (0,97,266,514):
            s=float(th[idx]);
            def integral_rate(u):
                return c*u + (eps/om)*(np.sin(om*s)-np.sin(om*(s-u)))
            adirect=quad(lambda u: exp(-u-2*integral_rate(u)),0,150,
                         epsabs=3e-12)[0]
            assert abs(adirect-a[idx])<7e-8,(c,eps,om,s,adirect,a[idx])
            checks+=1
        checks+=4
    # Uniform linear response q1(s) for sufficiently small harmonic modulation.
    for (c,om) in ((.4,.7),(1.5,2.2),(2.8,.3)):
        th,a,q=periodic_moments(c,0.001,om,periods=65,n=501)
        k=1+2*c
        first=(1/k)-(.004/k)*np.real(np.exp(1j*om*th)/((k+1j*om)*(2+1j*om)))
        assert np.max(abs(q-first))<1.5e-6
        checks+=1
    print(f'{checks} independently sampled assertions passed: periodicity, direct moment integral, nonconstant variance, harmonic response.')


if __name__=='__main__':
    main()
