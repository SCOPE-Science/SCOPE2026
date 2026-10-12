#!/usr/bin/env python3
"""Independent numerical checks of a one-leaf clique spectral comparison.
Requires numpy and sympy; finite tests corroborate but do not prove the theorem.
"""
import math
import cmath
import numpy as np
import sympy as sp

x, m = sp.symbols('x m')
q = sp.sqrt(m - 1)
B = sp.Matrix([[0, q, 1], [q, m - 2, 0], [1, 0, 0]])
f = sp.expand((x * sp.eye(3) - B).det())
target = x**3 - (m - 2)*x**2 - m*x + (m - 2)
assert sp.simplify(f - target) == 0
cofactor = sp.expand((x * sp.eye(3) - B).minor_submatrix(0, 0).det())
assert sp.simplify(cofactor - x*(x-m+2)) == 0
exact_checks = 2

families = [3, 4, 5, 6, 8, 10, 16, 25, 40, 70, 100, 300, 1000]
times = [0, math.pi/19, math.pi/5, math.pi/math.sqrt(5), math.pi, 3*math.pi, 17.123]
full_checks = 0
for N in families[:8]:
    size = N + 1
    az = np.zeros((size, size))
    az[:N,:N] = np.ones((N, N)) - np.eye(N)
    az[0,N] = az[N,0] = 1
    ak = np.ones((N, N)) - np.eye(N)
    ez, vz = np.linalg.eigh(az)
    ek, vk = np.linalg.eigh(ak)
    br = np.array([[0, math.sqrt(N-1), 1], [math.sqrt(N-1), N-2, 0], [1, 0, 0]], dtype=float)
    eb, vb = np.linalg.eigh(br)
    for t in times:
        uz = (vz*np.exp(1j*t*ez))@vz.T
        uk = (vk*np.exp(1j*t*ek))@vk.T
        ub = (vb*np.exp(1j*t*eb))@vb.T
        hh = np.sum(vb[0,:]**2*np.exp(1j*t*eb))
        assert abs(uz[0,0]-hh) < 8e-12
        assert abs(ub[0,0]-hh) < 8e-12
        assert abs(uk[0,0] - (np.exp(1j*(N-1)*t)/N+(1-1/N)*np.exp(-1j*t))) < 8e-12
        assert np.max(np.abs(uz[1:N,1:N]-uk[1:N,1:N])) < 3/N
        assert np.max(np.abs(uz[0,1:N]-uk[0,1:N])) < 1/math.sqrt(N-1)+2/N+1e-12
        full_checks += 5

root_checks=0
for N in families:
    br = np.array([[0, math.sqrt(N-1), 1], [math.sqrt(N-1), N-2, 0], [1, 0, 0]], dtype=float)
    eig, v = np.linalg.eigh(br)
    weights = np.abs(v[0,:])**2
    assert abs(sum(weights)-1) < 1e-12
    for lam, a in zip(eig, weights):
        poly = lam**3 - (N-2)*lam**2 - N*lam+(N-2)
        deriv=3*lam*lam-2*(N-2)*lam-N
        aa=lam*(lam-N+2)/deriv
        assert abs(poly) < 1e-4 if N >= 1000 else abs(poly) < 1e-7
        assert abs(aa-a)<1e-8
        root_checks += 2
    assert max(weights)>0.5
    assert abs(np.sum(weights*np.exp(1j*math.pi/math.sqrt(5)*eig)))+1e-13 >= 2*max(weights)-1
    root_checks+=2

minus = (-1-math.sqrt(5))/2
plus = (-1+math.sqrt(5))/2
alpha=minus/(2*minus+1)
beta=plus/(2*plus+1)
assert abs(alpha-(1+1/math.sqrt(5))/2)<1e-14
assert abs(beta-(1-1/math.sqrt(5))/2)<1e-14
assert abs(alpha-beta-1/math.sqrt(5))<1e-14
for N in [100,1000,10000]:
    # High precision via 3x3 numerics at large N. Bounds display convergence.
    b=np.array([[0,math.sqrt(N-1),1],[math.sqrt(N-1),N-2,0],[1,0,0.]])
    e,v=np.linalg.eigh(b)
    w=v[0,:]**2
    if N==10000:
        assert abs(w[0]-alpha)<.0001
        assert abs(w[1]-beta)<.0001
        assert abs(w[2])<.0002
        ret=abs(sum(w*np.exp(1j*e*math.pi/math.sqrt(5))))
        assert abs(ret-1/math.sqrt(5))<.0002
print('VERIFY_OK symbolic_identities=%d full_matrix_checks=%d spectral_checks=%d family_orders=%s' % (exact_checks,full_checks,root_checks,len(families)))
