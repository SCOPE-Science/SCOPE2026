"""Finite consistency tests for the sharp even-jet Fock kernel profile.

This script checks the coefficient formula and numerical boundary equalities.
The proof for all complex variables and all even orders is analytic; finite
sampling alone does not establish the theorem.
"""
from math import factorial, exp
from cmath import exp as cexp
from itertools import product
import mpmath as mp
mp.mp.dps = 60
for m,tau in product((2,4,6,10),(0.1,1,10,100)):
    q=mp.mpf(str(tau))/(1+mp.mpf(str(tau))*factorial(m))
    R=m*mp.lambertw(1/(m*mp.root(q,m)))
    assert abs(mp.exp(-R)-q*R**m)<mp.mpf('1e-48')
    for r in [mp.mpf('0.1')*R,mp.mpf('0.9')*R, R, mp.mpf('1.1')*R]:
        bound=max(mp.mpf(0),mp.exp(-r)-q*r**m)
        if r<R:
            assert abs(abs(mp.exp(-r)-q*(-r)**m)-bound)<mp.mpf('1e-48')
        for ir in range(17):
            t_abs=r*ir/16
            for ia in range(40):
                theta=2*mp.pi*ia/40
                z=t_abs*mp.exp(1j*theta)
                val=abs(mp.exp(z)-q*z**m)
                assert val+mp.mpf('1e-43')>=bound
    assert abs(mp.exp(-R)-q*(-R)**m)<mp.mpf('1e-48')
    derivative=mp.exp(-R)-q*m*(-R)**(m-1)
    assert derivative>0
for m in (2,4,6,10,40,200):
    q_limit=mp.mpf(1)/factorial(m)
    r_limit=m*mp.lambertw(1/(m*mp.root(q_limit,m)))
    assert abs(mp.exp(-r_limit)-q_limit*r_limit**m)<mp.mpf('1e-40')
    assert r_limit>0
print('OK: 16 finite-penalty profiles and 6 infinite-penalty limits; analytic proof required.')
