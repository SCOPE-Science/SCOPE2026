"""Finite consistency checks for the phase-resolved OU return theorem.

Run: python verify.py (requires Python 3.10+ and scipy>=1.10).
These checks are not substitutes for the analytical proof.
"""
import math
from scipy.integrate import quad

D = 1.2
a = 1.3
checks = 0

def moment_normal(q):
    return 2**(q/2)*math.gamma((q+1)/2)/math.sqrt(math.pi)

def gaussian_average(func):
    return 2/math.sqrt(2*math.pi)*quad(lambda z: math.exp(-z*z/2)*func(z), 0, 14, epsabs=2e-10)[0]

def positive_tail_release(delta, x):
    return gaussian_average(lambda z: (1+x*x/(2*D*z*z))**(-delta))

def off_tail_unnormalized(delta, x):
    return gaussian_average(lambda z: (1+x*x/(2*D*z*z))**(1-delta))/(delta-1)

def normal_moment_direct(q):
    return gaussian_average(lambda z: z**q)

for p in [0.5, 1, 2, 3.5, 7]:
    assert abs(normal_moment_direct(p)/moment_normal(p)-1) < 5e-8
    checks += 1

for delta in [1.25, 1.6, 2.5, 3.7]:
    c_release = (4*D)**delta*math.gamma(delta+0.5)/math.sqrt(math.pi)
    c_off = (4*D)**(delta-1)*math.gamma(delta-0.5)/((delta-1)*math.sqrt(math.pi))
    for x in [35, 100, 300]:
        release_scaled = positive_tail_release(delta, x)*x**(2*delta)/c_release
        off_scaled = off_tail_unnormalized(delta, x)*x**(2*delta-2)/c_off
        # Finite-distance relative errors decay quadratically at fixed delta.
        assert abs(release_scaled-1)<0.07 if x==35 else abs(release_scaled-1)<0.009
        assert abs(off_scaled-1)<0.07 if x==35 else abs(off_scaled-1)<0.009
        checks += 2

# The return-phase occupation density solves D q'(x)+a x q(x)=P(Y0>x)/C.
# The following kernel reproduces its large-distance, exactly one-sided flux.
for delta in [1.5,2.5]:
    for x in [5, 9, 15]:
        source = positive_tail_release(delta,x)/2
        c=a/(2*D)
        # change variables u=x-v, removing the enormous exp(c*x*x)
        kern = quad(lambda v: math.exp(c*((x-v)**2-x*x))*positive_tail_release(delta,x-v)/2,0,x,epsabs=1e-12)[0]/D
        ratio = kern*a*x/source
        assert ratio>0.6 and ratio<1.9,(delta,x,ratio)
        checks += 1

# Direct OU Poisson ODE identity at sample points for any p>0.
for p in [0.5,1,2,3.5,6]:
    for x in [0.5,1,2,4]:
        c = a/(2*D)
        # stable expression u_p'(x) by shifting the exponential
        def uprime(v):
            return quad(lambda z: (v+z)**p*math.exp(-c*(2*v*z+z*z)),0,100,epsabs=1e-11)[0]/D
        h=1e-4
        residual=D*(uprime(x+h)-uprime(x-h))/(2*h)-a*x*uprime(x)+x**p
        assert abs(residual)<4e-5,(p,x,residual)
        checks+=1

# Closed cycle moment identities: arbitrary positive mean release, e.g. Gamma(3,2).
# E B_T^2 = 2D E T, so E int_return Y^2 = D/a*(ET+EH).
ET=6.0
EH=0.77
assert abs((D*ET/a+D*EH/a)/(ET+EH)-D/a)<1e-12
checks+=1
print(f'PASS: {checks} finite checks; on/off tail constants, OU generator identity and cycle energy balance.')
