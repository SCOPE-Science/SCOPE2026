#!/usr/bin/env python3
"""Reproduce spectral admissibility and local-channel boundary checks."""
import math
import numpy as np

rng = np.random.default_rng(22041)
checks = 0

def test(ok, message):
    global checks
    assert bool(ok), message
    checks += 1

def haar(n):
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    return q @ np.diag(np.diag(r).conj() / np.abs(np.diag(r)))

def admissible(x, tol=2e-10):
    spectrum = np.linalg.eigvalsh(x)
    return spectrum[0] >= -tol and spectrum[-1] <= 1 + tol

def reset(gamma, target, eta):
    d = target.shape[0]
    result = np.zeros((d+1, d+1), complex)
    result[0, 0] = gamma[0, 0]
    result[0, 1:] = eta * gamma[0, 1:]
    result[1:, 0] = eta * gamma[1:, 0]
    result[1:, 1:] = target
    return result

def pure_witness(p, direction):
    vec = np.r_[np.sqrt(p), np.sqrt(1-p)*direction]
    return np.outer(vec, vec.conj())

for d in [1,2,3,5,8]:
    for k in range(65):
        qb = haar(d)
        spec = rng.uniform(.008, .992, d)
        target = (qb * spec) @ qb.conj().T
        ev, vec = np.linalg.eigh(target)
        safe = min(ev[0], 1 - ev[-1])
        eta_critical = math.sqrt(safe)
        q = haar(d+1)
        vals = rng.uniform(0, 1, d+1)
        gamma = (q * vals) @ q.conj().T
        test(admissible(gamma), 'input covariance')
        test(admissible(reset(gamma,target,eta_critical)), 'sharp global safe edge')
        test(admissible(reset(gamma,target,eta_critical*rng.random())), 'safe interior')
        eta_bad = (eta_critical + 1)/2
        if ev[0] <= 1-ev[-1]:
            p = (1-ev[0]/(eta_bad**2))/2
            witness = pure_witness(p, vec[:, 0])
        else:
            p = (1+(1-ev[-1])/(eta_bad**2))/2
            witness = pure_witness(p, vec[:, -1])
        test(admissible(witness), 'pure fermionic input')
        test(not admissible(reset(witness,target,eta_bad)), 'strict sharpness')
        x = gamma[0,1:]
        p = gamma[0,0].real
        a = np.vdot(x.conj(), np.linalg.solve(target, x.conj()))
        b = np.vdot(x.conj(), np.linalg.solve(np.eye(d)-target, x.conj()))
        if abs(a)>1e-13 and abs(b)>1e-13:
            eta_state_sq = min(p/a.real,(1-p)/b.real)
            test(admissible(reset(gamma,target,min(1,math.sqrt(eta_state_sq)))), 'statewise Schur edge')
            if eta_state_sq < .97:
                eta_over = min(1.0, math.sqrt(eta_state_sq)*1.025)
                test(not admissible(reset(gamma,target,eta_over)), 'statewise Schur sharpness')

for c in [.001,.12,.5,.74,.99]:
    bound = math.sqrt(c*(1-c))
    # Choi matrix of the local number-reset, coherence-attenuation qubit map.
    def choi(eta):
        z = np.diag([1-c,1-c,c,c]).astype(complex)
        z[0,3]=z[3,0]=eta
        return z
    test(np.linalg.eigvalsh(choi(bound))[0]>-1e-12, 'CPTP boundary')
    test(np.linalg.eigvalsh(choi((bound+1)/2))[0]<-1e-10, 'CPTP sharpness')
    test(bound <= math.sqrt(min(c,1-c))+1e-12, 'hierarchy')

for beta, bandwidth, mu in [(1,2,0),(3,2,0),(5,1.1,.7),(0.2,4,-.3)]:
    energies=np.linspace(-bandwidth,bandwidth,3001)
    occupations=1/(1+np.exp(beta*(energies-mu)))
    actual=min(float(occupations.min()),float((1-occupations).min()))
    expected=1/(1+math.exp(beta*(bandwidth+abs(mu))))
    test(abs(actual-expected)<1e-12, 'symmetric thermal-band formula')

print(f'PASS: {checks} explicit spectral and channel assertions')
print('thermal example eta_max =', (1+math.exp(6))**-.5)
