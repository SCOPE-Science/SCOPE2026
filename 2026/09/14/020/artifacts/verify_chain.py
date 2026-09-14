"""Verify one-way 3-chain SEIR source-endemic boundary classification (numpy only)."""
import json
import numpy as np

SIG, GAM, D = 0.5, 0.2, 0.1
LAM = np.array([10.0, 10.0, 10.0])

def params(b1, b2, b3, mS, mE, mI, mR):
    beta = np.array([b1, b2, b3])
    muS = np.array([D + mS, D + mS, D])
    a = np.array([SIG + D + mE, SIG + D + mE, SIG + D])
    b = np.array([GAM + D + mI, GAM + D + mI, GAM + D])
    muR = np.array([D + mR, D + mR, D])
    m = dict(mS=mS, mE=mE, mI=mI, mR=mR)
    return dict(beta=beta, muS=muS, a=a, b=b, muR=muR, m=m)

def dfe(p):
    muS, mS = p['muS'], p['m']['mS']
    S0 = np.zeros(3)
    S0[0] = LAM[0] / muS[0]
    S0[1] = (LAM[1] + mS * S0[0]) / muS[1]
    S0[2] = (LAM[2] + mS * S0[1]) / muS[2]
    R0 = p['beta'] * S0 * SIG / (p['a'] * p['b'])
    z = np.zeros(12)
    z[0], z[4], z[8] = S0
    return z, S0, R0

def source_endemic(p):
    """Constructive equilibrium: patch-1 closed form, patches 2,3 quadratic roots."""
    beta, muS, a, b, muR = p['beta'], p['muS'], p['a'], p['b'], p['muR']
    mS, mE, mI, mR = p['m']['mS'], p['m']['mE'], p['m']['mI'], p['m']['mR']
    S = np.zeros(3); E = np.zeros(3); I = np.zeros(3); R = np.zeros(3)
    S[0] = a[0] * b[0] / (beta[0] * SIG)
    E[0] = (LAM[0] - muS[0] * S[0]) / a[0]
    I[0] = SIG * E[0] / b[0]
    R[0] = GAM * I[0] / muR[0]
    info = {}
    for j in (1, 2):
        mmS, mmE, mmI, mmR = (mS, mE, mI, mR)
        T = LAM[j] + mmS * S[j - 1]
        PE = mmE * E[j - 1]
        PI = mmI * I[j - 1]
        Dd = a[j] * PI + SIG * PE
        Aq = a[j] * b[j] * beta[j]
        Bq = a[j] * b[j] * muS[j] - beta[j] * (T * SIG + Dd)
        Cq = -muS[j] * Dd
        disc = Bq * Bq - 4 * Aq * Cq
        assert disc >= 0, f"patch {j}: negative discriminant"
        I[j] = (-Bq + np.sqrt(disc)) / (2 * Aq) if Aq > 0 else 0.0
        if Dd == 0:
            I[j] = max(0.0, I[j])
        S[j] = T / (muS[j] + beta[j] * I[j])
        E[j] = (beta[j] * S[j] * I[j] + PE) / a[j]
        R[j] = (GAM * I[j] + mmR * R[j - 1]) / muR[j]
        info[j] = dict(T=T, D=Dd, Aq=Aq, Bq=Bq, Cq=Cq, disc=disc,
                       Stilde=T / muS[j], Rtilde=beta[j] * (T / muS[j]) * SIG / (a[j] * b[j]))
    z = np.zeros(12)
    for j in range(3):
        z[4 * j:4 * j + 4] = (S[j], E[j], I[j], R[j])
    return z, dict(S=S, E=E, I=I, R=R), info

def resid(p, z):
    beta, muS, a, b, muR = p['beta'], p['muS'], p['a'], p['b'], p['muR']
    mS, mE, mI, mR = p['m']['mS'], p['m']['mE'], p['m']['mI'], p['m']['mR']
    F = np.zeros(12)
    for j in range(3):
        S, E, I, R = z[4 * j:4 * j + 4]
        o = 4 * j
        infl = np.zeros(4) if j == 0 else np.array(
            [mS * z[4 * (j - 1)], mE * z[4 * (j - 1) + 1],
             mI * z[4 * (j - 1) + 2], mR * z[4 * (j - 1) + 3]])
        F[o] = LAM[j] + infl[0] - beta[j] * S * I - muS[j] * S
        F[o + 1] = beta[j] * S * I + infl[1] - a[j] * E
        F[o + 2] = SIG * E + infl[2] - b[j] * I
        F[o + 3] = GAM * I + infl[3] - muR[j] * R
    return F

def jac(p, z):
    beta, muS, a, b, muR = p['beta'], p['muS'], p['a'], p['b'], p['muR']
    mS, mE, mI, mR = p['m']['mS'], p['m']['mE'], p['m']['mI'], p['m']['mR']
    J = np.zeros((12, 12))
    for j in range(3):
        S, E, I, R = z[4 * j:4 * j + 4]
        o = 4 * j
        J[o, o] = -beta[j] * I - muS[j]
        J[o, o + 2] = -beta[j] * S
        J[o + 1, o] = beta[j] * I
        J[o + 1, o + 1] = -a[j]
        J[o + 1, o + 2] = beta[j] * S
        J[o + 2, o + 1] = SIG
        J[o + 2, o + 2] = -b[j]
        J[o + 3, o + 2] = GAM
        J[o + 3, o + 3] = -muR[j]
        if j > 0:
            J[o, o - 4] = mS
            J[o + 1, o - 3] = mE
            J[o + 2, o - 2] = mI
            J[o + 3, o - 1] = mR
    return J

def newton(p, z0):
    z = z0.copy()
    r = np.linalg.norm(resid(p, z))
    for _ in range(300):
        F = resid(p, z)
        nF = np.linalg.norm(F)
        if nF < 1e-13:
            return z, True
        try:
            d = np.linalg.solve(jac(p, z), -F)
        except np.linalg.LinAlgError:
            return z, False
        step = 1.0
        for _ in range(40):
            zn = z + step * d
            if np.linalg.norm(resid(p, zn)) < nF:
                z = zn
                break
            step *= 0.5
        else:
            return z, False
    return z, np.linalg.norm(resid(p, z)) < 1e-9

def scan(p, seed):
    rng = np.random.default_rng(seed)
    found = []
    ok = 0
    for _ in range(24):
        z0 = np.zeros(12)
        for j in range(3):
            z0[4 * j] = rng.uniform(1, 130)
            z0[4 * j + 1] = rng.uniform(0, 25)
            z0[4 * j + 2] = rng.uniform(0, 25)
            z0[4 * j + 3] = rng.uniform(0, 60)
        z, conv = newton(p, z0)
        if conv and np.all(z > -1e-9):
            z = np.maximum(z, 0.0)
            ok += 1
            key = tuple(np.round(z, 6))
            if not any(np.linalg.norm(np.array(k) - z) < 1e-4 for k in found):
                found.append(key)
    return found, ok

def eigs(p, z):
    return np.linalg.eigvals(jac(p, z))

out = {}

# ---- Scenario A: driven source-endemic (R0 = (3, .5, .5)) ----
pA = params(0.0204732, 0.00255915, 0.00236229, 0.05, 0.05, 0.05, 0.05)
zD, S0, R0 = dfe(pA)
zE, comp, info = source_endemic(pA)
eD, eE = eigs(pA, zD), eigs(pA, zE)
fA = dict(R0=R0.tolist(), S0=S0.tolist(),
          endemic=dict(S=comp['S'].tolist(), E=comp['E'].tolist(),
                       I=comp['I'].tolist(), R=comp['R'].tolist()),
          res_dfe=float(np.linalg.norm(resid(pA, zD))),
          res_end=float(np.linalg.norm(resid(pA, zE))),
          maxreal_dfe=float(np.max(eD.real)), maxreal_end=float(np.max(eE.real)),
          eig_end_sorted=np.sort(eE.real).tolist(),
          patch2=info[1], patch3=info[2])
foundA, okA = scan(pA, 7)
fA['newton_converged'] = okA
fA['newton_distinct'] = [list(k) for k in foundA]
out['A_driven'] = fA

# ---- Scenario B: stable DFE (all R0 = .5) ----
pB = params(0.0034122, 0.00255915, 0.00236229, 0.05, 0.05, 0.05, 0.05)
zDB, S0B, R0B = dfe(pB)
eDB = eigs(pB, zDB)
out['B_stable_dfe'] = dict(R0=R0B.tolist(),
                           res_dfe=float(np.linalg.norm(resid(pB, zDB))),
                           maxreal_dfe=float(np.max(eDB.real)),
                           eig_dfe_sorted=np.sort(eDB.real).tolist())

# ---- Scenario C: zero infected driving edge (mE=mI=0) ----
pC = params(0.0204732, 0.00255915, 0.00236229, 0.05, 0.0, 0.0, 0.05)
zDC, S0C, R0C = dfe(pC)
zEC, compC, infoC = source_endemic(pC)
eEC = eigs(pC, zEC)
fC = dict(R0=R0C.tolist(),
          endemic=dict(S=compC['S'].tolist(), E=compC['E'].tolist(),
                       I=compC['I'].tolist(), R=compC['R'].tolist()),
          res_end=float(np.linalg.norm(resid(pC, zEC))),
          maxreal_end=float(np.max(eEC.real)),
          eig_end_sorted=np.sort(eEC.real).tolist(),
          patch2=infoC[1], patch3=infoC[2])
foundC, okC = scan(pC, 11)
fC['newton_converged'] = okC
fC['newton_distinct'] = [list(k) for k in foundC]
out['C_zero_driving'] = fC

with open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1878/output/artifacts/verify_results.json', 'w') as f:
    json.dump(out, f, indent=1)

print("A R0:", fA['R0'])
print("A endemic E:", comp['E'], "I:", comp['I'])
print("A res:", fA['res_dfe'], fA['res_end'])
print("A maxreal dfe/end:", fA['maxreal_dfe'], fA['maxreal_end'])
print("A newton converged:", okA, "distinct:", len(foundA))
for k in foundA:
    a = np.array(k)
    print("   sol E+I per patch:", [(a[4*j+1]+a[4*j+2]) for j in range(3)])
print("B R0:", out['B_stable_dfe']['R0'], "maxreal:", out['B_stable_dfe']['maxreal_dfe'])
print("C R0:", fC['R0'])
print("C endemic E:", compC['E'], "I:", compC['I'])
print("C maxreal end:", fC['maxreal_end'])
print("C newton converged:", okC, "distinct:", len(foundC))
for k in foundC:
    a = np.array(k)
    print("   sol E+I per patch:", [(a[4*j+1]+a[4*j+2]) for j in range(3)])
print("A patch2 Rtilde:", info[1]['Rtilde'], "D:", info[1]['D'])
print("A patch3 Rtilde:", info[2]['Rtilde'], "D:", info[2]['D'])
print("C patch2 Rtilde:", infoC[1]['Rtilde'], "D:", infoC[1]['D'])
