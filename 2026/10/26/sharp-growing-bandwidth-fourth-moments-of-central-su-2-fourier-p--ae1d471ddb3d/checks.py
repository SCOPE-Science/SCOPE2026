"""Reproduce finite SU(2) Clebsch-Gordan fourth moments and continuum checks.
All computations concern the explicitly defined mathematical quantities in RESULT.md.
"""
from fractions import Fraction
from math import sin, pi, sqrt
import numpy as np


def fusion_moment(a):
    n = len(a)
    b = np.zeros(2*n - 1, dtype=complex)
    for i in range(n):
        for j in range(n):
            b[abs(i-j):i+j+1:2] += a[i]*a[j]
    return float(np.vdot(b, b).real)


def angular_moment(a, nodes=6000):
    # Explicit SU(2) Haar class integral, using midpoint quadrature.
    th = (np.arange(nodes)+0.5)*pi/nodes
    S = np.zeros(nodes,dtype=complex)
    for j, aj in enumerate(a):
        S += aj*np.sin((j+1)*th)
    return float(2/pi*np.mean(np.abs(S)**4/np.sin(th)**2)*pi)


def profile(n, kind):
    j=np.arange(n,dtype=float)
    a = np.ones(n) if kind == 'flat' else (j+1)/n
    return a/np.linalg.norm(a)

for n in [2,3,4,7]:
    z=np.array([(j+1)*np.exp(1j*j/3) for j in range(n)],dtype=complex)
    z=z/np.linalg.norm(z)
    exact=fusion_moment(z)
    integ=angular_moment(z)
    assert abs(exact-integ)<1e-8,(n,exact,integ)
    print('SU2 fourth-moment identity n=%d %.12f' %(n,exact))

for kind,expected in [('flat',1/12),('ramp',34/315)]:
    for n in [40,100,200]:
        value=fusion_moment(profile(n,kind))/n**3
        print('asymptotic',kind,'N',n,'value',round(value,10),'limit',round(expected,10))
    assert abs(fusion_moment(profile(200,kind))/200**3-expected)<0.003

# Algebraically computed example values: for g=1, F=1/3;
# for g=sqrt(3)*x, F=136/315.
assert Fraction(1,3)/4 == Fraction(1,12)
assert Fraction(136,315)/4 == Fraction(34,315)
print('finite and asymptotic normalization checks passed')
