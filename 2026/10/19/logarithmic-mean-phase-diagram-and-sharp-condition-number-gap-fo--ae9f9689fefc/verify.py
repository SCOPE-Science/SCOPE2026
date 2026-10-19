"""Finite independent checks for rank-one Bregman preconditioning theorem.

Run: python verify.py   (requires NumPy).  Tests support but do not replace proof.
"""
import math
import numpy as np

rng = np.random.default_rng(931709)
checks = 0

def verify(test, detail):
    global checks
    if not test:
        raise AssertionError(detail)
    checks += 1

for K in (1.01, 1.1, 2, 4, 10, 100, 10000):
    LF = (K-1)/math.log(K)
    TF, TC, TR = K/LF, math.sqrt(K), LF
    verify(1 < TF < TC < TR < K, (K,TF,TC,TR))
    competitive = (K-1)**2/(K*math.log(K)**2)
    verify(abs(competitive - K/TF**2) < 1e-9, 'forward limit')
    verify(abs(competitive - TR**2/K) < 1e-9, 'reverse limit')
    for t in (math.sqrt(TF), (TF+TC)/2, math.sqrt(K), (TC+TR)/2,
              (TR+K)/2, K*0.99+0.01):
        if not 1 < t < K:
            continue
        delta = t/K
        af = t-1-math.log(t)
        bf = 1/t-1+math.log(t)
        am = delta-1-math.log(delta)
        bm = 1/delta-1+math.log(delta)
        forward = 'plus' if af > am else 'minus'
        reverse = 'plus' if bf > bm else 'minus'
        verify(forward == ('plus' if t > TF else 'minus'), (K,t,'forward'))
        verify(reverse == ('plus' if t > TR else 'minus'), (K,t,'reverse'))
        verify(abs((af-am) - ((1-1/K)*t-math.log(K))) < 5e-12, 'score F')
        verify(abs((bf-bm) - (math.log(K)-(K-1)/t)) < 5e-12, 'score R')
        n = 5
        spectrum = np.array([delta,1,1,1,t])
        Ssqrt = np.diag(np.sqrt(spectrum))
        S = np.diag(spectrum)
        opt = min(t,K/t)
        for sign in ('minus','plus'):
            P = np.eye(n)
            if sign == 'minus': P[0,0] = delta
            else: P[-1,-1] = t
            H = Ssqrt @ np.linalg.inv(P) @ Ssqrt
            cond = np.linalg.cond(H)
            target = t if sign == 'minus' else K/t
            verify(abs(cond-target) <= 1e-8 * target, (K,t,sign,cond,target))
        for trial in range(70):
            u = rng.normal(size=n)
            u /= np.linalg.norm(u)
            # Positive and negative perturbations, including near singularity.
            alpha = (math.exp(rng.uniform(-12,9)) - 1)
            invP = np.eye(n) - alpha/(1+alpha)*np.outer(u,u)
            H = Ssqrt @ invP @ Ssqrt
            eig = np.linalg.eigvalsh(H)
            observed = eig[-1]/eig[0]
            verify(observed + 1e-8*max(1,observed) >= opt, (K,t,alpha,observed,opt))
            # Compare divergences to the best spectral-mode update.
            logdetS = math.log(delta)+math.log(t)
            Dforward = (np.trace(S@invP) - logdetS + math.log1p(alpha) - n)
            Dreverse = (np.trace(S) * 0) + sum(1/spectrum) + alpha*sum(u*u/spectrum) - math.log1p(alpha) + logdetS - n
            optimum_forward = af + am - max(af,am)
            optimum_reverse = bf + bm - max(bf,bm)
            verify(Dforward >= optimum_forward-2e-8, ('forward optimality', K,t,Dforward,optimum_forward))
            verify(Dreverse >= optimum_reverse-2e-8, ('reverse optimality', K,t,Dreverse,optimum_reverse))

print(f'PASS: {checks} deterministic / seeded numerical checks')
print('The all-rank-one optimality, exact thresholds and limiting sharp constants are established by proof, not enumeration.')
