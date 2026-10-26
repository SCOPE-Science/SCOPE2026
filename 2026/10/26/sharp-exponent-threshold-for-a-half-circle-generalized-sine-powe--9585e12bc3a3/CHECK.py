"""Independent arithmetic and quadrature checks for the half-circle sine-power Fourier result.

Usage: python CHECK.py
The published infinite-frequency argument is analytic; this program tests its exact
identities and illustrative Fourier and finite-matrix consequences.
"""
from __future__ import annotations

import math
import sympy as sp
from scipy.integrate import quad
import numpy as np

A = sp.symbols('A', positive=True)
D = {}
D[1] = A/(A+1)
for n in (3, 5, 7, 9, 11):
    eps = (-1)**((n-1)//2)
    D[n] = sp.factor(((n-2-A)*D[n-2]-2*A*eps/(n*(n-2)))/(n+A))
assert sp.simplify(D[3] - A*(5-A)/(3*(A+1)*(A+3))) == 0
assert sp.simplify(D[5] - A*(A*A-16*A+23)/(5*(A+1)*(A+3)*(A+5))) == 0
critical = 8-sp.sqrt(41)
assert sp.simplify(D[5].subs(A, critical)) == 0
assert sp.simplify((critical**2-16*critical+23)) == 0

# Derive and verify the crucial positive lower bound in the odd induction.
m = sp.symbols('m', positive=True)
bound = sp.factor((m+2-A)/(m*(m+2+A))-1/(m+4))
assert sp.simplify(bound-(m+2)*(4-2*A)/(m*(m+2+A)*(m+4))) == 0

# The cosine-integral tests are independent of the symbolic Fourier recurrence.
trial_parameters = [0.5, 1.0, 1.5, float(critical.evalf(17)), 1.7, 2.5]
comparisons = 0
worst = 0.0
for alpha in trial_parameters:
    # Use direct quadrature. Endpoint behavior is integrable for alpha>0.
    f = lambda t: 1.0-math.sin(t)**alpha
    def actual(n):
        return quad(lambda t: f(t)*math.cos(n*t), 0, math.pi/2,
                    epsabs=4e-12, epsrel=4e-12, limit=250)[0]
    n0 = actual(0)
    I0 = math.pi/2-n0
    predicted = {}
    predicted[1] = alpha/(alpha+1)
    Ie = {0: I0}
    for n in range(2, 65, 2):
        Ie[n] = (n-2-alpha)/(n+alpha)*Ie[n-2]
        predicted[n] = -Ie[n]
    for n in range(3, 65, 2):
        eps = (-1)**((n-1)//2)
        predicted[n] = ((n-2-alpha)*predicted[n-2]-2*alpha*eps/(n*(n-2)))/(n+alpha)
    for n in range(1,65):
        computed = actual(n)
        err = abs(predicted[n]-computed)
        worst = max(worst,err)
        assert err < 3e-10, (alpha,n,computed,predicted[n],err)
        comparisons += 1

# Outside alpha_star, the fifth harmonic is negative; beyond 2 fourth is negative.
assert float(D[5].subs(A,sp.Rational(17,10))) < 0
for a in (2.2, 2.5, 5.0):
    i0 = quad(lambda t: math.sin(t)**a,0,math.pi/2)[0]
    a4 = -a*(a-2)*i0/((a+2)*(a+4))
    assert a4 < 0

# A discrete witness at alpha=1.7 for a sufficiently fine cyclic grid.
alpha = 1.7
for N in (32,64,128):
    angles = 2*math.pi*np.arange(N)/N
    distances = np.minimum(angles,2*math.pi-angles)
    values = np.where(distances < math.pi/2,
                      1-np.sin(np.minimum(distances,math.pi/2))**alpha,0.0)
    eigenvalues = np.fft.fft(values).real
    if eigenvalues[5] < -1e-8:
        print(f'finite witness: N={N}, alpha={alpha}, Fourier eigenvalue at n=5: {eigenvalues[5]:.12g}')
        break
else:
    raise AssertionError('Expected negative discrete n=5 witness absent')

print('symbolic identities: PASS (A_3, A_5, critical root, induction factor)')
print(f'independent integral comparisons: {comparisons}; max absolute discrepancy {worst:.4g}')
print(f'critical exponent: {float(critical):.15f}')
print('sample inadmissible Fourier coefficients: PASS')
print('Analytic all-frequency induction and Bochner argument require the accompanying proof.')
