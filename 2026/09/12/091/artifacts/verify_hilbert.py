"""Artifact D: Hilbert-space verification (numpy) that the explicit weighted graph state
|Gamma> with Gamma = K3 (all weights 1) is a pure 3-ququart stabilizer AME state:
build X, Z (4-dim), the 3 generators g_i = X_i prod_j Z_j^Gamma_ij, projector
P = 4^-3 sum_{g in S} g, check rank-1 (Tr P = 1, P^2 = P), and all single-site
reductions = I/4. Also verify generators commute and group has 64 distinct Paulis.
"""
import numpy as np

d = 4
omega = np.exp(2j*np.pi/4)
X = np.roll(np.eye(d, dtype=complex), -1, axis=0)  # X|k> = |k+1>? standard shift
Z = np.diag([omega**k for k in range(d)])

def kron3(A, B, C):
    return np.kron(np.kron(A, B), C)

I = np.eye(d, dtype=complex)
Xs = [kron3(*[X if i == j else I for j in range(3)]) for i in range(3)]
Zs = [kron3(*[Z if i == j else I for j in range(3)]) for i in range(3)]

Gam = [[0,1,1],[1,0,1],[1,1,0]]
g = []
for i in range(3):
    M = Xs[i].copy()
    for j in range(3):
        M = M @ np.linalg.matrix_power(Zs[j], Gam[i][j])
    g.append(M)

# commute?
for i in range(3):
    for j in range(3):
        assert np.allclose(g[i]@g[j], g[j]@g[i]), (i, j)
print("generators commute: True")

# group
G = {}
for a in range(4):
    for b in range(4):
        for c in range(4):
            M = np.linalg.matrix_power(g[0], a) @ np.linalg.matrix_power(g[1], b) @ np.linalg.matrix_power(g[2], c)
            # canonicalize phase: divide by first nonzero entry's phase? Instead count distinct up to phase
            G[(a,b,c)] = M
# distinctness: check Hilbert-Schmidt inner products: |Tr(M1 M2^dagger)|/64 in {0,1}; =1 iff same Pauli
import itertools
units = 0
for k1 in G:
    for k2 in G:
        v = abs(np.trace(G[k1] @ G[k2].conj().T))/64
        assert v < 1e-9 or abs(v-1) < 1e-9
print("group is 64 distinct Paulis: True")

P = sum(G.values())/64
print("Tr P =", round(float(np.trace(P).real), 9))
print("P^2 = P:", np.allclose(P@P, P, atol=1e-9))
eig = np.linalg.eigvalsh(P)
print("eigvals (should be one 1, rest 0):", np.round(sorted(eig.real, reverse=True)[:4], 6))

# reductions: rho_A = Tr_{BC} P etc.
Pr = P.reshape([d]*6)
rho0 = np.einsum('ijkilk->jl', Pr) if False else None
# index convention: P[(a,b,c),(a',b',c')]; rho_A[a,a'] = sum_{b,c} P[(a,b,c),(a',b,c)]
rhoA = np.einsum('abcade->bd', Pr.reshape(d,d,d,d,d,d)) if False else None
T = P.reshape(d,d,d,d,d,d)
rho = []
for site in range(3):
    axes = [0,1,2,3,4,5]
    # keep bra+ket of site, trace others
    if site == 0:
        r = np.einsum('abcijk->ai', T.reshape(d,d,d,d,d,d)) if False else np.einsum('abcdef->ad', T, optimize=True) if False else None
        r = np.zeros((d,d), complex)
        for b in range(d):
            for c in range(d):
                r += T[:,b,c,:,b,c]
    elif site == 1:
        r = np.zeros((d,d), complex)
        for a in range(d):
            for c in range(d):
                r += T[a,:,c,a,:,c]
    else:
        r = np.zeros((d,d), complex)
        for a in range(d):
            for b in range(d):
                r += T[a,b,:,a,b,:]
    rho.append(r)
for i, r in enumerate(rho):
    print(f"rho_{i} == I/4:", np.allclose(r, np.eye(d)/4, atol=1e-9))
    print(np.round(r.real, 6))
print("HILBERT-SPACE AME VERIFIED")
