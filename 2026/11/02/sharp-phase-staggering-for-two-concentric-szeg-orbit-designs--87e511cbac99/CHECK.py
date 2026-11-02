"""Finite consistency checks for the two-circle Szego determinant identity.
Run with Python 3 and NumPy. These checks do not replace the analytic proof.
"""
from math import gcd, lcm, pi, cos, log
import numpy as np


def formula(m, n, r, s, theta):
    L, g = lcm(m, n), gcd(m, n)
    a, b = r**L, s**L
    c = ((m*(1-r*r)/(1-r**(2*m)))**m * r**(m*(m-1))
         * (n*(1-s*s)/(1-s**(2*n)))**n * s**(n*(n-1)))
    v = (a*a + b*b - 2*a*b*cos(L*theta))/(1+a*a*b*b-2*a*b*cos(L*theta))
    return c*v**g


def direct(m, n, r, s, theta):
    z = np.r_[r*np.exp(2j*pi*np.arange(m)/m),
              s*np.exp(1j*(theta+2*pi*np.arange(n)/n))]
    gram = np.sqrt(1-abs(z[:, None])**2) * np.sqrt(1-abs(z[None, :])**2) / (1-z[:, None]*z[None,:].conj())
    assert np.allclose(gram,gram.conj().T,rtol=0,atol=1e-13)
    return np.linalg.det(gram).real


def defect(m,n,r,s,theta):
    L,g=lcm(m,n),gcd(m,n)
    a,b=r**L,s**L
    alpha=2*a*b/(a+b)**2
    beta=2*a*b/(1+a*b)**2
    t=1+cos(L*theta)
    if alpha*t>=1: return float('inf'), g*(alpha-beta)*t
    return g*log((1-beta*t)/(1-alpha*t)),g*(alpha-beta)*t

cases=0
for m,n in [(1,1),(1,6),(2,3),(2,4),(3,3),(3,5),(4,6),(5,7)]:
    for r,s in [(0.14,0.39),(0.35,0.35),(0.48,0.71),(0.7,0.83)]:
        L=lcm(m,n)
        for theta in [0.0,0.127,pi/L,2*pi/L,2*pi/L+0.22]:
            exp=formula(m,n,r,s,theta)
            act=direct(m,n,r,s,theta)
            assert abs(act-exp) <= 1e-8*max(exp,1e-12), (m,n,r,s,theta,act,exp)
            d,lower=defect(m,n,r,s,theta)
            assert d+2e-13>=lower, (m,n,r,s,theta,d,lower)
            if theta==pi/L:
                assert np.isclose(exp,formula(m,n,r,s,-pi/L),rtol=1e-11)
            cases+=1
# Strict inequality and sharp second-order matching in a nontrivial gcd case
m,n,r,s=4,6,0.61,0.77
L,g=lcm(m,n),gcd(m,n)
a,b=r**L,s**L
alpha=2*a*b/(a+b)**2;beta=2*a*b/(1+a*b)**2
for delta in [0.005,0.002,0.001]:
    d,lower=defect(m,n,r,s,pi/L+delta)
    assert d>lower>0 and abs(d/lower-1)<0.005
print(f'PASS: {cases} direct determinant and sharp-stability comparisons, 3 local-limit checks')
