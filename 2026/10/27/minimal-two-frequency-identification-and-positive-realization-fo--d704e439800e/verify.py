"""Independent numerical and exact-rational reconstruction tests for the two-box harmonic inverse."""
from fractions import Fraction as F
import random
import math


def inverse(freq1, freq2, H1, H2):
    assert 0 < freq1 < freq2
    z1, z2 = 1 / H1, 1 / H2
    r1, r2 = z1.real, z2.real
    j1, j2 = z1.imag/freq1, z2.imag/freq2
    a, b = r2-r1, j1-j2
    if not (a>0 and b>0):
        return None
    tau=b/a
    d=freq2**2-freq1**2
    gamma=a*(1+freq1**2*tau**2)*(1+freq2**2*tau**2)/(tau**2*d)
    cdeep=gamma*tau
    c=j1-cdeep/(1+freq1**2*tau**2)
    lam=r1-gamma*freq1**2*tau**2/(1+freq1**2*tau**2)
    if not (c>0 and lam>0):
        return None
    return c,cdeep,lam,gamma

def transfer(freq, c, cdeep, lam, gamma):
    z=1j*freq
    return 1/(lam+c*z+(gamma*cdeep*z)/(gamma+cdeep*z))

# Rational demonstration: known exact impedances from lambda=1,C=2,Cdeep=6,gamma=3.
z1=complex(F(17,5),F(16,5))
z2=complex(F(65,17),F(80,17))
assert abs(1/transfer(1,2,6,1,3)-z1)<1e-13
assert abs(1/transfer(2,2,6,1,3)-z2)<1e-13
x=inverse(1,2,1/z1,1/z2)
assert all(abs(a-b)<1e-11 for a,b in zip(x,(2,6,1,3))),x

random.seed(442221)
for trial in range(12000):
    c=10**random.uniform(-0.5,0.5)
    lam=10**random.uniform(-0.5,0.5)
    gamma=10**random.uniform(-0.5,0.5)
    tau=10**random.uniform(-0.5,0.5)
    cdeep=gamma*tau
    f1=random.uniform(0.3,2.0)/tau
    f2=f1*random.uniform(1.5,4.0)
    h1,h2=(transfer(w,c,cdeep,lam,gamma) for w in (f1,f2))
    params=inverse(f1,f2,h1,h2)
    assert params is not None, (trial,c,cdeep,lam,gamma,f1,f2)
    for target, got in zip((c,cdeep,lam,gamma),params):
        assert math.isclose(target,got,rel_tol=5e-7,abs_tol=3e-9),(trial,target,got)
    assert abs(transfer(f1,*params)-h1) <= 1e-7*abs(h1)
    assert abs(transfer(f2,*params)-h2) <= 1e-7*abs(h2)

# One frequency: freely perturb two parameters while keeping its exact impedance.
c, deep, lam, gamma=2.,6.,1.,3.
f=1.
z=1/transfer(f,c,deep,lam,gamma)
R=z.real; J=z.imag/f
for dt in (-0.1,-0.05,0.05,0.1):
  for dg in (-0.1,0,0.1):
    tau=2+dt; gam=3+dg
    de=gam*tau
    ci=J-de/(1+f*f*tau*tau)
    la=R-gam*f*f*tau*tau/(1+f*f*tau*tau)
    assert min(ci,la,de,gam)>0
    assert abs(transfer(f,ci,de,la,gam)-1/z)<1e-13

# Nearby data may violate physical positivity despite a>0,b>0.
H1=transfer(1,2,6,1,3)
H2=transfer(2,2,6,1,3)
assert inverse(1,2,H1,H2) is not None
print('PASS: 12,000 randomized exact-model inversions; rational example; one-frequency nonidentifiability family; two-frequency forward replay.')
