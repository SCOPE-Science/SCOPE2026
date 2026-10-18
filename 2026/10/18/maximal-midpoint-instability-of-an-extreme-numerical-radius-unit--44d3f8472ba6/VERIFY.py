#!/usr/bin/env python3
"""Independent finite-dimensional sanity checks for the explicit numerical-radius construction.
The infinite-dimensional statements are established analytically in RESULT.md.
"""
import math
import numpy as np

def num_radius(a, samples=1536):
    n = a.shape[0]
    ts = np.arange(samples) * (2*math.pi/samples)
    return max(np.linalg.eigvalsh((np.exp(-1j*t)*a+np.exp(1j*t)*a.conj().T)/2)[-1] for t in ts)

j=np.array([[0,1j],[1j,0]], dtype=np.complex128)
d0=np.diag([1.,-1.]).astype(np.complex128)
checks=0
assert np.allclose(j.conj().T,-j)
assert np.allclose(j@j,-np.eye(2))
checks+=2
for s in (-1,1):
    b=d0+s*j
    assert np.allclose(b@b,np.zeros((2,2)))
    assert np.allclose(b.conj().T@b@b.conj().T@b, 4*b.conj().T@b)
    assert abs(np.linalg.norm(b,ord=2)-2)<1e-12
    assert abs(num_radius(b)-1)<1e-12
    checks+=4
for n in range(1,31):
    angle=1/(n+2)
    eigen2=-np.exp(1j*angle)
    delta=abs(1+eigen2)
    d=np.diag([1.,eigen2]).astype(np.complex128)
    xp=(d+j)/(1+delta)
    xm=(d-j)/(1+delta)
    assert np.linalg.norm(d-d0,ord=2) <= delta+1e-12
    assert num_radius(xp) <= 1+1e-10
    assert num_radius(xm) <= 1+1e-10
    assert abs(num_radius((xp+xm)/2-d)-delta/(1+delta))<1e-10
    assert abs(num_radius(xp-xm)-2/(1+delta))<1e-10
    assert delta>0 and delta<1/(n+2)
    checks+=6
# This is a finite block test, not an exhaustion of all perturbations.
print('PASS', checks, 'matrix identities and numerical checks')
