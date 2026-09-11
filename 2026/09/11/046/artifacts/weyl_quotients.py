"""Weyl-sequence corroboration for lane-824 target refutation (numpy only).

Sine modes phi_m on upper semicircle Gamma+ (extended by zero), harmonic
extension to B1 via Fourier series, interior gradient energies over the
D* box and the C_out box, normalized by the H^{1/2}-equivalent norm.
Also assembles finite-section matrices (M^C, G) for the Fréchet-derivative
form P_C(f,g) = int_C grad u_f . grad u_g and reports smallest generalized
eigenvalues at increasing section size N (collapse toward 0).

Outputs: weyl_results.json + stdout table.
"""
import json
import numpy as np

S = np.sqrt(2.0 / np.pi)

def fourier_coeffs(m, ns):
    """Fourier coeffs of phi_m (extension by zero of sqrt(2/pi) sin(m theta))."""
    c = np.zeros(len(ns), dtype=complex)
    for i, n in enumerate(ns):
        tot = 0.0 + 0.0j
        for sgn, k in ((1.0, m - n), (-1.0, -m - n)):
            if k == 0:
                tot += sgn * np.pi
            else:
                tot += sgn * (np.exp(1j * k * np.pi) - 1.0) / (1j * k)
        c[i] = S / (2.0 * np.pi) * tot / (2.0j)
    return c

def run(NTR=50, NR=150, NT=288, MODES=(1, 2, 3, 4, 6, 8, 12, 16, 20, 24)):
    ns = np.arange(-NTR, NTR + 1)
    absn = np.abs(ns)
    # Fourier coefficients per mode
    C = {m: fourier_coeffs(m, ns) for m in MODES}
    # H^{1/2}-equivalent norms
    H2 = {m: 2 * np.pi * float(np.sum((1 + absn) * np.abs(C[m]) ** 2)) for m in MODES}
    # polar grid
    r = np.linspace(0.0, 1.0, NR)
    th = np.linspace(0.0, 2 * np.pi, NT, endpoint=False)
    dr = 1.0 / (NR - 1)
    dth = 2 * np.pi / NT
    R, TH = np.meshgrid(r, th, indexing="ij")
    X = R * np.cos(TH)
    Y = R * np.sin(TH)
    W = R * dr * dth
    Z = X + 1j * Y
    Zb = X - 1j * Y
    # boxes: D* and C_out
    mD = (np.abs(X) <= 0.15) & (Y >= 0.30) & (Y <= 0.60)
    mO = (np.abs(X) <= 0.15) & (Y >= -0.60) & (Y <= -0.30)
    Gx = {}
    Gy = {}
    for m in MODES:
        c = C[m]
        gx = np.zeros_like(X, dtype=complex)
        gy = np.zeros_like(X, dtype=complex)
        for j, n in enumerate(ns):
            cj = c[j]
            if abs(cj) == 0:
                continue
            if n > 0:
                d = cj * n * Z ** (n - 1)
                gx += d
                gy += 1j * d
            elif n < 0:
                k = -n
                d = cj * k * Zb ** (k - 1)
                gx += d
                gy += -1j * d
        Gx[m] = gx
        Gy[m] = gy
    rows = []
    for m in MODES:
        eD = float(np.sum((np.abs(Gx[m]) ** 2 + np.abs(Gy[m]) ** 2) * mD * W))
        eO = float(np.sum((np.abs(Gx[m]) ** 2 + np.abs(Gy[m]) ** 2) * mO * W))
        rows.append({"m": m, "H12sq": H2[m], "E_Dstar": eD, "E_Cout": eO,
                     "q_Dstar": eD / H2[m], "q_Cout": eO / H2[m]})
    # finite sections of P_{C_out}: Mjk, Gjk over mode prefix
    ms = sorted(MODES)
    out = {"rows": rows, "sections": {}}
    for N in (4, 8, 12):
        sub = ms[:N]
        M = np.zeros((N, N), dtype=complex)
        G = np.zeros((N, N), dtype=complex)
        for a, ja in enumerate(sub):
            for b, jb in enumerate(sub):
                M[a, b] = np.sum((Gx[ja] * np.conj(Gx[jb]) + Gy[ja] * np.conj(Gy[jb])) * mO * W)
                G[a, b] = 2 * np.pi * complex(np.sum((1 + absn) * C[ja] * np.conj(C[jb])))
        G = G.real
        M = M.real
        # Generalized eigenvalues of (M,G) via regularized solve (G near-singular
        # at high modes is itself a compactness signature). No Cholesky.
        eps = 1e-10 * max(1.0, float(np.trace(G)) / N)
        GiM = np.linalg.solve(G + eps * np.eye(N), M)
        ev = np.linalg.eigvals(GiM).real
        ev = np.sort(ev)
        out["sections"][str(N)] = [float(v) for v in ev]
    return out

if __name__ == "__main__":
    res = run()
    for row in res["rows"]:
        print("m=%3d  H12sq=%9.4f  E_Dstar=%10.4e  E_Cout=%10.4e  q_D=%9.3e  q_O=%9.3e" % (
            row["m"], row["H12sq"], row["E_Dstar"], row["E_Cout"], row["q_Dstar"], row["q_Cout"]))
    for N, ev in res["sections"].items():
        print(f"N={N} gen-eigs min={min(ev):.3e} max={max(ev):.3e}")
        print("   ", " ".join(f"{v:.3e}" for v in ev))
    with open("output/artifacts/weyl_results.json", "w") as f:
        json.dump(res, f, indent=1)
    print("wrote output/artifacts/weyl_results.json")
