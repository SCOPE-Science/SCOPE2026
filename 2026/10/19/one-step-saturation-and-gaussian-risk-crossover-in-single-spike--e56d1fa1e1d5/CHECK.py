"""Reproducible checks for the Gaussian single-spike sketch-power limit.
Run: python3 CHECK.py (NumPy required). These finite checks do not prove asymptotic statements.
"""
import numpy as np
from math import sqrt

rng = np.random.default_rng(20261013)
counts = {"schur": 0, "power": 0, "risk": 0, "asymptotic": 0}

def sample(n, ell, c):
    phi = rng.standard_normal((n, ell))
    omega = rng.standard_normal(n)
    z = phi.copy()
    y = omega.copy()
    z[0, :] *= sqrt(c*n)
    y[0] *= sqrt(c*n)
    return phi, y, z, omega

for n in (9, 16, 43, 102):
    for ell in (2, 3, 4, 6):
        if ell >= n: continue
        for _ in range(15):
            c = .2 + 3*rng.random()
            phi, y, z, omega = sample(n, ell, c)
            gram = z.T @ z
            pin = z @ np.linalg.solve(gram,z[0])
            p_direct = pin[0]
            g = phi[0]
            h = phi[1:]
            tau = g @ np.linalg.solve(h.T@h,g)
            p_schur = c*n*tau/(1+c*n*tau)
            assert np.isclose(p_direct,p_schur,atol=2e-10,rtol=3e-10)
            assert -1e-12 <= p_direct <= 1+1e-12
            counts["schur"] += 1
            coef = z.T@y
            for q in (1, 2, 3, 4):
                v_iter = z @ np.linalg.matrix_power(gram,q-1) @ coef
                v_iter /= np.linalg.norm(v_iter)
                v_ref = y.copy()
                for k in range(q): v_ref = z@(z.T@v_ref)
                v_ref /= np.linalg.norm(v_ref)
                assert np.allclose(abs(v_iter @ v_ref),1,atol=3e-8,rtol=1e-8)
                cap = float(v_iter[0]**2)
                background = np.eye(n);background[0,0]=sqrt(c*n)
                loss = np.linalg.norm((np.eye(n)-np.outer(v_iter,v_iter))@background,ord=2)**2/(c*n)
                assert 1-cap-2e-10 <= loss <= 1-cap+1/(c*n)+2e-10
                counts["power"] += 1
                counts["risk"] += 1

for n in (160, 640):
    ell=3;c=.7; diffs=[]; gains=[]; horizon=[]
    for rep in range(140):
        phi,y,z,omega=sample(n,ell,c)
        gram=z.T@z/n
        u=z.T@y/n
        limiting=c*(phi[0]@phi[0])/(1+c*(phi[0]@phi[0]))
        vals=[]
        for q in (1,2,4,8):
            w=z@np.linalg.matrix_power(gram,q-1)@u
            vals.append(w[0]**2/(w@w))
        diffs.append(abs(vals[0]-limiting))
        horizon.append(max(abs(a-limiting) for a in vals))
        gains.append(vals[0]-(y[0]**2/(y@y)))
        counts["asymptotic"] += 1
    print(f"n={n} ell={ell}: mean |capture(q=1)-limit|={np.mean(diffs):.5f}; max across powers mean={np.mean(horizon):.5f}; Pr(gain>0) estimate={np.mean(np.array(gains)>0):.3f}")

print("Checks passed:", counts)
print("Limiting improvement probability for ell=2 is 1/sqrt(2) =",1/sqrt(2))
