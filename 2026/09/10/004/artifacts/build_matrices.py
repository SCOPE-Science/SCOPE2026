"""Canonical certificate computation for lane-498 target.
Rebuilds genus-2 Fuchsian double, Sym^2, Goldman bulge rho_t,
Labourie cross-ratio B(Q0), length-stretch table, dominated-splitting check.
Deterministic; prints all numbers; saves artifacts.
"""
import numpy as np

ART = "output/artifacts"

# ---------- base block (solved tr=3.2 triple) ----------
A = np.array([[0.54951023, 0.08931767], [5.11064855, 2.65048977]])
B = np.array([[3.56576266, 0.51121035], [-4.5073869, -0.36576267]])
A /= np.sqrt(np.linalg.det(A)); B /= np.sqrt(np.linalg.det(B))
C = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
C = (C + C.T) / 2; C /= np.sqrt(np.linalg.det(C))
w, Q = np.linalg.eigh(C)
j = Q @ np.array([[0., 1.], [1., 0.]]) @ Q.T
A2 = j @ A @ j; B2 = j @ B @ j
gens2 = [A, B, A2, B2]
names = ["A1", "B1", "A2", "B2"]
C1 = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
C2 = A2 @ B2 @ np.linalg.inv(A2) @ np.linalg.inv(B2)
print("relation |C1C2-I| =", np.linalg.norm(C1 @ C2 - np.eye(2)))

def sym2(M):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]; s = np.sqrt(2.)
    return np.array([[a*a, s*a*b, b*b], [s*a*c, a*d+b*c, s*b*d],
                     [c*c, s*c*d, d*d]])
G = [sym2(g) for g in gens2]
gam = G[0] @ G[1] @ np.linalg.inv(G[0]) @ np.linalg.inv(G[1])
gev, GeV = np.linalg.eig(gam); oi = np.argsort(gev.real)[::-1]
Vf = np.real(GeV[:, oi]); Vfi = np.linalg.inv(Vf)

def bulge(t):
    D = np.diag([np.exp(t), 1., np.exp(-t)])
    M = np.real(Vf @ D @ Vfi); return M / (np.linalg.det(M) ** (1/3))
def rho(t):
    Bt = bulge(t); Bi = np.linalg.inv(Bt)
    return [G[0], G[1], Bt @ G[2] @ Bi, Bt @ G[3] @ Bi]
def flags(M):
    ev, Vv = np.linalg.eig(M); r = ev.real
    i1 = int(np.argmax(r)); W = np.linalg.inv(Vv).T
    return {"pa": np.real(Vv[:, i1]), "na": np.real(W[:, i1])}
def CR(Fx, Fy, Fz, Fw):
    p = lambda A, Bc: float(np.dot(Bc["na"], A["pa"]))
    return p(Fx, Fz) * p(Fy, Fw) / (p(Fx, Fw) * p(Fy, Fz))
def lenses(M):
    ev = np.linalg.eig(M)[0]
    if np.max(np.abs(ev.imag)) > 1e-5: return None
    r = np.sort(ev.real)[::-1]
    if r[2] <= 1e-9 or r[0]/r[1] < 1+1e-9 or r[1]/r[2] < 1+1e-9: return None
    return float(np.log(r[0]/r[1])), float(np.log(r[1]/r[2])), float(np.log(r[0]/r[2]))

print("\n== (i) Labourie cross-ratio B(Q0), Q0=(A1+,B2+,B1+,A2+) ==")
for t in [0.0, 0.15, 0.2, 0.25, 0.3, 0.35]:
    R = rho(t); Fa = {n: flags(g) for n, g in zip(names, R)}
    print(f"t={t:.2f} B={CR(Fa['A1'], Fa['B2'], Fa['B1'], Fa['A2']):.6f}")

print("\n== length stretch: short crossing words (a1-length) ==")
idx = {n: i for i, n in enumerate(names)}
tests = ["A1A2", "A1B2", "B1A2", "B1B2", "A1a2", "A1B1A2", "B1B1A2B2"]
for word in tests:
    row = []
    for t in [0.0, 0.25]:
        R = rho(t); Ri = {n: np.linalg.inv(g) for n, g in zip(names, R)}
        M = np.eye(3)
        for ch in [word[i:i+2] if word[i:i+2] in idx else word[i]
                   for i in range(len(word))]:
            pass
        # parse: tokens like 'A1','B2','a2'(=A2^-1)
        toks = []; i = 0
        while i < len(word):
            c = word[i]
            if i+1 < len(word) and word[i+1] in "12":
                toks.append(c + word[i+1]); i += 2
            else:
                toks.append(c + "1"); i += 1
        M = np.eye(3)
        for tk in toks:
            base = tk[0].upper() + tk[1]
            g = R[idx[base]] if tk[0].isupper() else Ri[base]
            M = M @ g
        e = lenses(M)
        row.append(e[0] if e else float("nan"))
    print(f"{word:10s} l0={row[0]:.4f} l.25={row[1]:.4f} ratio={row[1]/row[0]:.4f}")

print("\n== dominated splitting: min eig-gap over words |w|<=3 at t=0.25 ==")
R = rho(0.25); S = R + [np.linalg.inv(g) for g in R]
inv = {0: 4, 1: 5, 2: 6, 3: 7, 4: 0, 5: 1, 6: 2, 7: 3}
cur = {(i,): S[i] for i in range(8)}
mingap = 1e9; nonhyp = 0
for N in range(1, 4):
    for wM, M in cur.items():
        e = lenses(M)
        if e is None: nonhyp += 1
        else: mingap = min(mingap, e[0], e[1])
    nxt = {}
    for wM, M in cur.items():
        for i in range(8):
            if inv[i] != wM[-1]: nxt[wM + (i,)] = M @ S[i]
    cur = nxt
print("nonhyperbolic:", nonhyp, "min gap:", mingap)

np.save(f"{ART}/genus2_SL3.npy", np.array(G))
np.save(f"{ART}/genus2_SL2.npy", np.array(gens2))
np.save(f"{ART}/rho_t025.npy", np.array(rho(0.25)))
print("\nartifacts saved")
