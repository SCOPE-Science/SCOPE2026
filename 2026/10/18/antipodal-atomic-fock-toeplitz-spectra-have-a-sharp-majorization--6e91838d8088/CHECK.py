"""Finite diagnostics for the antipodal two-atom Fock Toeplitz spectral theorem.

These checks are not a substitute for the analytic proof.
"""
import math
import random

import numpy as np
import sympy as sp

u = sp.symbols('u', positive=True)
D = 2-u
q = u*(2*u-1)
assert sp.simplify((q**2/D**2-u**4) -
    u**2*(1-u**2)*(u**2-4*u+1)/D**2) == 0
assert sp.simplify((D-q)-2*(1-u**2)) == 0
assert sp.simplify((D+q)-2*(1-u+u**2)) == 0
print('Exact symbolic identities: 3 passed')

rng = random.Random(20261015)
threshold = math.log(2+math.sqrt(3))
powers = [0.2, 0.5, 0.9, 1.0, 1.1, 1.6, 2.0, 3.0, 8.0]
checked=0
for t in [0.08,0.3,0.69,0.7,1.0,1.3,threshold,1.4,1.7,2,3.0,5.0]:
    u0=math.exp(-t)
    d=2-u0
    k=u0*(2*u0-1)
    for j in range(12):
        a=10**rng.uniform(-2,2)
        b=10**rng.uniform(-2,2)
        H=np.array([[a,math.sqrt(a*b)*u0*u0],
                    [math.sqrt(a*b)*u0*u0,b]],dtype=float)
        P=np.array([[d*a,math.sqrt(a*b)*k],
                    [math.sqrt(a*b)*k,d*b]],dtype=float)
        eh=np.linalg.eigvalsh(H)
        ep=np.linalg.eigvalsh(P/d)
        assert min(eh)>0 and min(ep)>0
        expected=0 if abs(t-threshold)<1e-10 else (1 if t>threshold else -1)
        largest_difference=ep[-1]-eh[-1]
        if expected:
            assert expected*largest_difference>1e-14, (t,a,b,largest_difference)
        else:
            assert abs(largest_difference)<1e-10
        for power in powers:
            rh=sum(x**power for x in eh)
            rp=sum(x**power for x in ep)
            if power==1.0 or expected==0:
                assert abs(rh-rp)<1e-8*max(rh,rp)
            else:
                sign=expected*(1 if power>1 else -1)
                assert sign*(rp-rh)>-1e-12*max(rp,rh), (t,a,b,power,rp-rh)
            checked+=1
print(f'Gram spectra and Schatten comparisons: {checked} diagnostics passed')
