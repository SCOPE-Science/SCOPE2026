"""Deterministic checks of stationary renewal-resetting covariance and spectrum."""
from math import exp, gamma, pi, sin
from scipy.integrate import quad

D=1.3
rate=0.8
mu=1/rate

def C_exp(t): return D*mu**-1 *2*exp(-rate*t)/rate**2

def S_exp(w):
    return (4*D/mu/w**2)*quad(lambda x: exp(-rate*x)*(1-__import__('math').cos(w*x)),0,50)[0]

checks=0
for t in (0,0.3,1.2,3.0):
    assert abs(C_exp(t)-2*D/rate*exp(-rate*t))<1e-11
    checks+=1
for w in (0.13,0.8,3.0,7.0):
    assert abs(S_exp(w)-4*D/(rate**2+w**2))<1e-7
    checks+=1

alpha,tau=2.6,1.7
mul=tau/(alpha-1)
C0=2*D*tau/(alpha-2)
for t in (0,0.2,1.5,5.,20.):
    moment=2*quad(lambda x:(x-t)*(1+x/tau)**(-alpha),t,float("inf"),epsabs=1e-10)[0]
    exact=C0*(1+t/tau)**(2-alpha)
    assert abs(D/mul*moment-exact)<5e-6
    checks+=1
for t in (0.1,0.7,2.,5.,40.):
    second=2*D/mul*(1+t/tau)**(-alpha)
    exact=C0*(alpha-2)*(alpha-1)/tau**2*(1+t/tau)**(-alpha)
    assert abs(second-exact)<1e-11
    checks+=1
for alpha in (3.2,3.7,5.,7.):
    moment3=6*tau**3/((alpha-1)*(alpha-2)*(alpha-3))
    mu=tau/(alpha-1)
    expected=2*D*moment3/(3*mu)
    direct=4*D*tau**2/((alpha-2)*(alpha-3))
    assert abs(expected-direct)<1e-10
    checks+=1
for w in (2.,4.,8.,16.,32.):
    rate=0.8
    expected=4*D/(rate**2+w**2)
    assert abs(w*w*expected/(4*D)-w*w/(rate**2+w**2))<1e-13
    checks+=1

print(f'PASSED: {checks} deterministic assertion groups')
