"""Finite-section checks for the numerical-radius smoothness phase law.

The mathematical statement concerns infinite operators; finite sections do not
prove the infinite limits or differentiability. Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal


def top_radius(weights, eigenvector=False):
    weights = np.asarray(weights, dtype=float)
    if eigenvector:
        eig, vec = eigh_tridiagonal(np.zeros(len(weights)+1), weights / 2.0,
                                    select='i', select_range=(len(weights),len(weights)))
        return float(eig[0]), vec[:,0]
    eig = eigh_tridiagonal(np.zeros(len(weights)+1), weights / 2.0,
                          eigvals_only=True, select='i',
                          select_range=(len(weights),len(weights)))
    return float(eig[0])


def exact_one_defect(t):
    return 1.0 if t <= math.sqrt(2.0) else 0.5 * (math.sqrt(t*t-1.0) + 1.0/math.sqrt(t*t-1.0))


def exact_first_coordinate_derivative(t):
    assert t > math.sqrt(2.0)
    return t*(t*t-2.0)/(2.0*(t*t-1.0)**1.5)

checks = 0
for t in [0.7,1.0,1.25,math.sqrt(2.0),1.5,2.0,3.0]:
    expected = exact_one_defect(t)
    prev = 0.0
    for n in [60, 240, 960]:
        observed = top_radius([t]+[1.0]*(n-1))
        assert prev <= observed + 1e-10
        assert observed <= expected + 1e-9
        prev = observed
        checks += 3
    assert abs(prev-expected) < 0.002
    checks += 1

for t in [1.5,2.0,3.0]:
    n=240
    w=np.array([t]+[1.0]*(n-1))
    r,u=top_radius(w,True)
    derivative = u[0]*u[1]
    predicted=exact_first_coordinate_derivative(t)
    assert abs(derivative-predicted)< 1e-5, (derivative,predicted)
    for eps in [1e-3,1e-4]:
        wp=w.copy(); wp[0]+=eps
        wm=w.copy(); wm[0]-=eps
        slope=(top_radius(wp)-top_radius(wm))/(2*eps)
        assert abs(slope-predicted)<1e-4
        checks+=1
    checks+=1

# A finite shadow of the non-Gateaux witness: long alternating sign blocks.
for n in [1024,4096]:
    h=np.array([1.0 if int(math.sqrt(k+1))%2==0 else -1.0 for k in range(n)])
    for sign in [-1,1]:
        pert=np.ones(n)+sign*0.125*h
        got=top_radius(pert)
        assert 1.11<got<=1.12500001, (n, sign,got)
        checks+=1

# Nonconstant convergent positive weights and isolated eigenvalue.
n=500
w=np.ones(n)+0.03/(1.0+np.arange(n))
w[0]=2.0
r,u=top_radius(w,True)
assert r>1.0
coef=u[:-1]*u[1:]
h=np.sin(np.arange(n)*0.371)
eps=1e-5
num=(top_radius(w+eps*h)-top_radius(w-eps*h))/(2*eps)
ana=float(np.dot(coef,h))
assert abs(num-ana)<1e-6,(num,ana)
checks+=3
print('VERIFY_OK finite_section_checks=%d one_defect_cases=7 Frechet_directional_cases=3 alternating_block_sizes=2 infinite_proof_required=True' % checks)
