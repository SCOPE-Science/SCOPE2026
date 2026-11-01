"""Numerical checks for a radial Gaussian-Fock concentration theorem.

Requires NumPy and SciPy. These checks are finite corroboration, not proof
of the arbitrary-dimension or arbitrary-shell statements.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gammainc, gammaln

checks = 0

def check(condition, explanation):
    global checks
    if not condition:
        raise AssertionError(explanation)
    checks += 1


def mass(n, d, intervals):
    k = n + d
    return sum(float(gammainc(k, b) - gammainc(k, a)) for a, b in intervals)


def difference_boundary(n, d, intervals):
    k = n + d
    return sum((math.exp(k*math.log(a) - a - math.lgamma(k+1))
                - math.exp(k*math.log(b) - b - math.lgamma(k+1)))
               for a,b in intervals)


for d in (1,2,5):
    intervals = [(0.15,0.5),(1.2,1.8),(4.1,5.2)]
    for n in range(0,15):
        v = mass(n,d,intervals)
        direct = sum(quad(lambda t: math.exp(-t+n*math.log(t)+(d-1)*math.log(t)-math.lgamma(n+d)),a,b,
                          epsabs=1e-13)[0] for a,b in intervals)
        check(abs(v-direct)<3e-12,(d,n,'Gamma integral'))
        delta = mass(n+1,d,intervals) - v
        check(abs(delta-difference_boundary(n,d,intervals))<3e-12,(d,n,'boundary identity'))

# The one-shell sign-change threshold is the logarithmic mean.
for d in (1,2,4):
    for a,b in ((.2,.7),(1.,3.),(4.,8.),(15.,27.)):
        lm = (b-a)/math.log(b/a)
        for n in range(0,35):
            exact = difference_boundary(n,d,[(a,b)])
            if abs(n+d-lm)>1e-7 and abs(exact)>1e-13:
                check((exact>0)==(n+d<lm),(d,n,a,b,'log mean'))

# Fixed total Gaussian mass, prescribed dimensions, three annuli.
for d in (1,3,8):
    for p in (.2,.4,.85,.99):
        R=(100,1000)
        far=[(float(r-np.sqrt(r)),float(r+np.sqrt(r))) for r in R]
        tail=sum(mass(0,d,[interval]) for interval in far)
        a=.000001
        b=brentq(lambda t:mass(0,d,[(a,t)])+tail-p,a,150)
        intervals=[(a,b)]+far
        check(abs(mass(0,d,intervals)-p)<2e-12,(d,p,'prescribed mass'))
        ns=np.arange(1100,dtype=int)
        spectral=np.zeros(len(ns))
        for low,high in intervals:
            spectral+=gammainc(ns+d,high)-gammainc(ns+d,low)
        maxima=np.where((spectral[1:-1]>spectral[:-2]) & (spectral[1:-1]>spectral[2:]))[0]+1
        maxima=list(([0] if spectral[0]>spectral[1] else []))+list(maxima)
        check(maxima==[0,100-d,1000-d],(d,p,'strict spectral peaks',maxima))

print(f'PASS: {checks} numerical identities, thresholds and prescribed-mass peak checks')
