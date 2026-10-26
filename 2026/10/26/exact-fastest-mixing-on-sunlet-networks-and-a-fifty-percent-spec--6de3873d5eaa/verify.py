"""Standalone checks for the closed-form sunlet fastest-mixing theorem.

Requires Python 3, SymPy, and NumPy. Run: python verify.py.
This is a check of symbolic identities and finite examples; the universal proof is in RESULT.md.
"""
import math
import random
import numpy as np
import sympy as sp

u = sp.symbols('u', real=True, positive=True)
r = u**2
H = u**2+2*u+2
a = (u+2)/(2*H)
b = u*(u+1)/H
f = 2*(u+1)/H
assert sp.simplify(2*a+b-1) == 0
assert sp.simplify(b*b+(a*r)**2-r/4) == 0
assert sp.simplify(f-(1-b-a*r+u/2)) == 0
assert sp.simplify(f*f-(b*b+(1-b)**2)-u*(u+2)*(2-u*u)/H**2) == 0
assert sp.simplify(1-f-r/H) == 0
assert sp.simplify(f-(1-2*b)-u*(u+2)/H) == 0
assert sp.simplify(f-(1-b)-u/H) == 0

def transition(n, rim, spoke):
    P = np.zeros((2*n, 2*n))
    for i in range(n):
        j = (i+1) % n
        P[i,j] += rim
        P[j,i] += rim
        P[i,n+i] = P[n+i,i] = spoke
    for i in range(2*n):
        P[i,i] = 1.0 - P[i].sum()
    return P

def modal_eigenvalues(n, rim, spoke):
    spectrum = []
    for j in range(n):
        d = 1.0 - math.cos(2*math.pi*j/n)
        t = math.hypot(spoke, rim*d)
        spectrum += [1-spoke-rim*d-t, 1-spoke-rim*d+t]
    return np.sort(spectrum)

def slem(P):
    eigen = np.linalg.eigvalsh(P)
    return float(max(abs(eigen[0]),abs(eigen[-2])))

checks = {'spectral':0,'optimizer':0,'heuristic':0,'competitors':0}
rng = random.Random(20260717)
for n in range(3,51):
    u0 = math.sqrt(1.0-math.cos(2*math.pi/n))
    H0 = u0*u0+2*u0+2
    a0 = (u0+2)/(2*H0)
    b0 = u0*(u0+1)/H0
    mu0 = 2*(u0+1)/H0
    P = transition(n,a0,b0)
    assert np.min(P) >= -1e-13
    assert np.max(abs(P.sum(axis=1)-1)) < 2e-14
    assert np.max(abs(P-P.T)) < 1e-14
    assert np.max(abs(np.linalg.eigvalsh(P)-modal_eigenvalues(n,a0,b0))) < 2e-12
    checks['spectral'] += 1
    assert abs(slem(P)-mu0)<2e-12
    checks['optimizer'] += 1
    md = transition(n,1/3,1/3)
    r0 = u0*u0
    md_pred = (2-r0+math.sqrt(1+r0*r0))/3
    assert abs(slem(md)-md_pred)<2e-12
    checks['heuristic'] += 1
    if n in (3,4,5,7,10,14):
        for _ in range(120):
            a1 = rng.random()*.5
            b1 = rng.random()*(1-2*a1)
            trial=transition(n,a1,b1)
            assert slem(trial) >= mu0-3e-12
            checks['competitors'] += 1
        # Unrestricted, feasible non-rotation-invariant edge perturbations.
        for _ in range(60):
            eps = 0.02+0.09*rng.random()
            edge_a = [(1-eps)*a0*(0.7+0.3*rng.random()) for i in range(n)]
            edge_b = [(1-eps)*b0*(0.7+0.3*rng.random()) for i in range(n)]
            R = np.zeros((2*n,2*n))
            for i in range(n):
                j=(i+1)%n
                R[i,j]=R[j,i]=edge_a[i]
                R[i,n+i]=R[n+i,i]=edge_b[i]
            for i in range(2*n): R[i,i]=1-R[i].sum()
            assert np.min(R)>-1e-13
            assert slem(R)>=mu0-3e-12
            checks['competitors'] += 1

# The asymptotic spectral-gap ratio is three-halves by symbolic expansion.
t = sp.symbols('t',positive=True)
g_opt = t*t/(t*t+2*t+2)
g_md = (1+t*t-sp.sqrt(1+t**4))/3
assert sp.limit(g_opt/g_md,t,0,dir='+')==sp.Rational(3,2)
print('VERIFY_OK symbolic identities, spectral blocks and exact closed forms;',
      checks['spectral'], 'graph sizes;', checks['optimizer'], 'optimum checks;',
      checks['heuristic'], 'heuristic checks;', checks['competitors'],
      'feasible comparisons; asymptotic gap ratio 3/2')
