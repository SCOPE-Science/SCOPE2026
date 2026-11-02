"""Reproducibility checks for a two-level renewal-probing timing frontier.

Requires numpy, scipy, and mpmath. Computations corroborate but do not
replace the analytic concave-majorant proof.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq, linprog
from mpmath import mp

mp.dps = 55
x0 = mp.findroot(lambda x: mp.tan(x)-2*x, (mp.mpf('1.1'),mp.mpf('1.3')))
k = mp.sin(x0)**2 / x0
assert mp.mpf('0.7853981633974483') < x0 < mp.pi/2
assert abs(2*x0*mp.sin(x0)*mp.cos(x0)-mp.sin(x0)**2) < mp.mpf('1e-48')
assert abs(mp.sin(x0)**2/x0 - 2*mp.sin(x0)*mp.cos(x0)) < mp.mpf('1e-48')

def phi(x):
    x = float(x)
    if x <= float(x0):
        return float(k)*x
    if x <= math.pi/2:
        return math.sin(x)**2
    return 1.0

# Direct 2x2 Hamiltonian check, including nonzero detuning and complex coupling.
for delta, g, imag in [(0,1,0),(0.7,1.1,0),(-0.25,1.4,0.4),(3.0,0.4,-0.6)]:
    H = np.array([[delta,complex(g,imag)],[complex(g,-imag),-delta]], complex)
    Omega = math.sqrt(delta**2+g**2+imag**2)
    beta=(g**2+imag**2)/Omega**2
    for x in [0.09, 0.2, 0.75, 1.2, 1.57, 3.1, 5.0]:
        amp = expm(-1j*H*x/Omega)[1,0]
        assert abs(abs(amp)**2-beta*math.sin(x)**2) < 3e-14

# Explicit optimal distributions (dimensionless waiting times);
# compute mean and one-attempt probability directly from atoms.
def trial(law):
    z=sum(w*x for w,x in law)
    sf=sum(w*math.sin(x)**2 for w,x in law)
    return z, sf

def opt_law(z):
    v=float(x0)
    if z <= v:
        return [(1-z/v,0),(z/v,v)]
    if z <= math.pi/2:
        return [(1,z)]
    j=max(0, math.floor((z-math.pi/2)/math.pi))
    L=math.pi/2+j*math.pi
    R=L+math.pi
    return [((R-z)/(R-L),L),((z-L)/(R-L),R)]

for z in [0.02, 0.2, 1, float(x0), 1.3, math.pi/2, 2, math.pi, 4.1, 10.2]:
    zz,ss=trial(opt_law(z))
    assert abs(zz-z)<1e-12
    assert abs(ss-phi(z))<1e-12

# Global majorization and concavity sampling over a wide window,
# including many recurrent Rabi peaks.
grid=np.linspace(0, 48*math.pi, 30001)
assert np.max(np.sin(grid)**2-np.array([phi(t) for t in grid]))<2e-12
bpts=np.concatenate(([0,float(x0)],np.linspace(0,5*math.pi,251),[math.pi/2]))
bpts=np.unique(np.sort(bpts))
for z in [0.1,0.4,0.9,1.15,1.3,1.5,2.0,3.2,5.8,9.0]:
    A=np.vstack([np.ones(len(bpts)),bpts])
    res=linprog(-np.sin(bpts)**2,A_eq=A,b_eq=[1,z],bounds=(0,None),method='highs')
    assert res.success,res.message
    assert -res.fun <= phi(z)+1e-8
    assert -res.fun > phi(z)-0.002 # discretized grid converges from below

# Randomized tests for concave-majorant bound, arbitrary finite-support laws.
rng=np.random.default_rng(8215)
for j in range(800):
    points=rng.uniform(0,15*math.pi,rng.integers(2,12))
    weights=rng.dirichlet(np.ones(len(points)))
    z=float(weights@points)
    sf=float(weights@(np.sin(points)**2))
    assert sf<=phi(z)+4e-14

print('PASS: qubit transitions, tangency, optimal phase laws, majorization,')
print('      LP crosschecks and 800 random-protocol comparisons')
print('x0=',mp.nstr(x0,50))
print('k=',mp.nstr(k,50))
print('best global time coefficient=',mp.nstr(1/k,50))
