"""Check the exact spectral kernel against proved logarithmic asymptotics.

Requires numpy and mpmath. This is numerical corroboration, not a proof.
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 42
nodes, weights = np.polynomial.legendre.leggauss(65)
z3 = mp.zeta(3)
gamma = mp.mpf(1)

def S(p, k):
    return mp.zeta(p) - mp.re(mp.polylog(p, mp.exp(1j * k)))

def velocity_square(d, k):
    return mp.im(mp.polylog(d - 1, mp.exp(1j * k)))**2 / (2*mp.zeta(d)*S(d,k))

def J(a, d, t):
    t = mp.mpf(t)
    scale = mp.sqrt(2*z3/(gamma*t*mp.log(t)))
    hi = mp.sqrt(12)
    total = mp.mpf(0)
    for xx, ww in zip(nodes, weights):
        u = (mp.mpf(float(xx)) + 1)*hi/2
        k = scale*u*u
        integrand = velocity_square(d,k)*mp.exp(-t*2*gamma*S(a,k)/mp.zeta(a))
        total += mp.mpf(float(ww))*hi*u*scale*integrand
    return total

def phi(q):
    return 2*(1-mp.exp(-mp.mpf(q)/2))/q if q else mp.mpf(1)

def asymptotic(d,t):
    t=mp.mpf(t)
    if d < 3:
        c=-2*mp.gamma(1-d)*mp.sin(mp.pi*d/2)/mp.zeta(d)
        z=c*((d-1)/2)**2
        p=(d-2)/2
        return z*mp.gamma(p)/2*(2*z3/(gamma*t*mp.log(t)))**p
    if d == 3:
        return mp.sqrt(mp.pi)/(2*mp.sqrt(2*gamma*z3))*mp.sqrt(mp.log(t)/t)
    return mp.zeta(d-2)/mp.zeta(d)*mp.sqrt(mp.pi*z3/(2*gamma*t*mp.log(t)))

for d in [mp.mpf('2.5'), mp.mpf(3), mp.mpf(4)]:
    observed=[]
    for t in [10**5, 10**10]:
        observed.append(float(J(3,d,t)/asymptotic(d,t)))
    print('fixed delta=',float(d),'ratios=',observed)
    assert abs(observed[1]-1) < abs(observed[0]-1)
    assert abs(observed[1]-1) < 0.34

T=mp.mpf(10**10)
for d in [mp.mpf('2.5'),mp.mpf(3)]:
    base=J(3,d,T)
    nu=d-2 if d<3 else mp.mpf(1)
    for s in [-2,2]:
        measured=J(3+mp.mpf(s)/mp.log(T),d,T)/base
        predicted=phi(s)**(-nu/2)
        print('collision crossover',float(d),s,float(measured),float(predicted))
        assert abs(float(measured/predicted)-1) < .12

base=J(3,3,T)
for r,s in [(2,2),(-2,2),(2,-2),(-2,-2)]:
    measured=J(3+mp.mpf(s)/mp.log(T),3+mp.mpf(r)/mp.log(T),T)/base
    predicted=phi(r)/mp.sqrt(phi(s))
    print('joint crossover',r,s,float(measured),float(predicted))
    assert abs(float(measured/predicted)-1) < .15
print('All finite spectral checks passed.')
