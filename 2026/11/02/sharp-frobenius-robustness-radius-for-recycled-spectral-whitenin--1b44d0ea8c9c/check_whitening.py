"""Reproducible finite checks for an exact perturbation theorem.

Run: python check_whitening.py
Requires: Python 3, numpy; seeded finite checks corroborate, not prove, the theorem.
"""
from fractions import Fraction
import math
import numpy as np

rng = np.random.default_rng(261028808)
checks = 0

def check(ok, message):
    global checks
    if not ok:
        raise AssertionError(message)
    checks += 1

# Exact rational examples with diagonal A and K=2.
# For A=diag(1,2), the sharp radius is 2/sqrt(17),
# attained with E=diag(-4/sqrt(17),1/sqrt(17)).
# The preconditioned diagonal is (1-8/17, 1+1/17)=(9/17,18/17).
check(Fraction(18,17)/Fraction(9,17)==2, 'exact scalar ratio')
check(Fraction(16,17)+Fraction(1,17)==1, 'exact Frobenius radius')

for n in range(2,9):
    for trial in range(110):
        eig = np.sort(rng.uniform(0.4,5.0,size=n))
        if trial % 11 == 0:
            eig[1] = eig[0]  # repeated minimal eigenvalue
        q, _ = np.linalg.qr(rng.normal(size=(n,n)))
        a = (q * eig) @ q.T
        invroot = (q * (1 / np.sqrt(eig))) @ q.T
        K = float(rng.uniform(1.01,9.0))
        h1, h2 = 1/eig[0], 1/eig[1]
        L = math.hypot(K*h1,h2)
        t = (K-1)/L
        check(t > 0 and t < eig[0], 'positive definite threshold')
        E = ((-K*h1/L)*np.outer(q[:,0],q[:,0]) +
             (h2/L)*np.outer(q[:,1],q[:,1]))
        check(abs(np.linalg.norm(E,'fro')-1)<1e-11,'extremizer norm')
        B = np.eye(n)+t*(invroot@E@invroot)
        spectrum = np.linalg.eigvalsh((B+B.T)/2)
        check(spectrum[0]>0,'positive extremal B')
        check(abs(spectrum[-1]/spectrum[0]-K)<1e-10,'attained K boundary')
        # All sampled symmetric Frobenius perturbations must stay below cap.
        for j in range(6):
            G = rng.normal(size=(n,n))
            G = (G+G.T)/2
            G /= np.linalg.norm(G,'fro')
            B = np.eye(n)+t*(invroot@G@invroot)
            vals = np.linalg.eigvalsh((B+B.T)/2)
            check(vals[0] > 0 and vals[-1]/vals[0] < K+2e-10, 'robust random error')
        # Slightly beyond the boundary, the same extremizer violates cap
        # for sufficiently small step to preserve SPD.
        tnew = t + min(1e-3*t, (eig[0]-t)/100)
        B = np.eye(n)+tnew*(invroot@E@invroot)
        vals = np.linalg.eigvalsh((B+B.T)/2)
        check(vals[0] > 0 and vals[-1]/vals[0] > K+1e-10,
              'strict failure beyond boundary')
print(f'PASS: {checks} reproducible exact/rational and seeded numerical checks')
