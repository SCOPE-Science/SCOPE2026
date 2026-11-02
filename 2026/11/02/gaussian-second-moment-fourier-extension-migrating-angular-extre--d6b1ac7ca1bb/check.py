"""Finite numerical cross-checks for the Gaussian second-moment extension spectrum.

Requires Python >=3.9 and SciPy. It neither proves uniformity nor certifies priority.
"""
from math import sqrt, pi, exp
import numpy as np
from scipy.integrate import quad
from scipy.special import jv, ive

checks = 0

def verify(test, label):
    global checks
    assert bool(test), label
    checks += 1

def eigen(z, n):
    # Stable positive integral formula, by the exact modified-Bessel identity.
    return 2*z*z*((n+1-z)*ive(n,z)+z*ive(n+1,z))

for z in (0.15, 0.25, 0.7, 1.0, 2.0, 7.0):
    for n in range(9):
        t=1/(2*z)
        integral = quad(lambda r:r**3*exp(-t*r*r)*jv(n,r)**2,
                        0, max(28, 11/sqrt(t)), epsabs=2e-11)[0]
        value=eigen(z,n)
        verify(abs(integral-value)<2e-8*max(1,value),f'Weber derivative z={z},n={n}')

for z in (0.01,0.1,0.25):
    vals=[eigen(z,n) for n in range(31)]
    verify(vals[0]>max(vals[1:]),f'constant symmetry z={z}')
verify(eigen(1,1)>eigen(1,0),'broken symmetry at z=1')

for z in (0.5, 1., 5., 15., 40.):
    trunc=max(150,int(6*z+150))
    summed=eigen(z,0)+2*sum(eigen(z,n) for n in range(1,trunc))
    verify(abs(summed-2*z*z)<2e-7*max(1,2*z*z),f'trace z={z}')

for z in (40.,100.,300.,800.):
    ns=np.arange(0,int(6*sqrt(z))+1)
    vals=np.asarray([eigen(z,int(n))/z**1.5 for n in ns])
    profile=(1+(ns/np.sqrt(z))**2)*np.exp(-(ns**2)/(2*z))/sqrt(2*pi)
    verify(np.max(np.abs(vals-profile)) < 1.0/z+0.006,f'profile z={z}')
    nmax=int(np.argmax(vals))
    verify(abs(nmax/sqrt(z)-1)<2/sqrt(z)+0.04,f'optimizer z={z}')

print(f'PASS {checks} finite numerical assertions')
