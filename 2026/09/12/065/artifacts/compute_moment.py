"""Self-contained reproduction of the two-point coverage moment computation
(Propositions 1-2, envelopes, tail bound, Euclidean-limit model). numpy only.
Run: python3 compute_moment.py  (~40 s; production trio + convergence check)
"""
import numpy as np, math, time

def r_of_v(v):
    return np.arccosh(1.0 + np.maximum(np.asarray(v), 0.0) / (2 * np.pi))

def inner_I(r1, r2, ds, M):
    c2 = np.cosh(r2)
    I = np.zeros_like(ds)
    if r1 <= 0 or r2 <= 0:
        return I
    disj = ds >= r1 + r2
    cont = (ds <= abs(r1 - r2)) | (ds < 1e-300)
    I[cont] = 2 * np.pi * (np.cosh(min(r1, r2)) - 1.0)
    m = ~(disj | cont)
    if np.any(m):
        dsm = ds[m]
        rhos = np.linspace(0, r1, M + 1)
        shr, chr_ = np.sinh(rhos), np.cosh(rhos)
        shd, chd = np.sinh(dsm), np.cosh(dsm)
        num = chr_[:, None] * chd[None, :] - c2
        den = shr[:, None] * shd[None, :]
        with np.errstate(invalid='ignore', divide='ignore'):
            cosb = np.divide(num, den, out=np.zeros_like(num), where=np.abs(den) > 1e-300)
        tiny = np.abs(den) <= 1e-300
        cosb[tiny & (num < 0)] = -1.0
        beta = np.arccos(np.clip(cosb, -1, 1))
        I[m] = np.trapz(2 * beta * shr[:, None], rhos, axis=0)
    return I

def M_hyp(lam, Nw=120, Nth=96, M=350, Wmax=18.0):
    ws = np.linspace(0, Wmax, Nw + 1); ths = np.linspace(0, np.pi, Nth + 1)
    rs = r_of_v(np.asarray(ws) / lam); vs = np.asarray(ws) / lam
    def simp(n, h):
        w = np.ones(n + 1); w[1:n:2] = 4; w[2:n-1:2] = 2; return w * (h / 3.0)
    ww, wt = simp(Nw, Wmax / Nw), simp(Nth, np.pi / Nth)
    E = 0.0
    for i in range(Nw + 1):
        for j in range(Nw + 1):
            r1, r2 = float(rs[i]), float(rs[j])
            cc = np.cosh(r1) * np.cosh(r2) - np.sinh(r1) * np.sinh(r2) * np.cos(ths)
            ds = np.arccosh(np.maximum(cc, 1.0))
            U = vs[i] + vs[j] - inner_I(r1, r2, ds, M)
            E += ww[i] * ww[j] * np.sum(wt * np.exp(-lam * U))
    return E / (2 * np.pi) * 2.0

def tail_bound(W):
    return 2 * (W + 2) * math.exp(-W)  # exact integral of e^{-max} over box complement

def eucl_inter(w1, w2, th):
    if w1 <= 0 or w2 <= 0:
        return 0.0
    a1, a2 = math.sqrt(w1 / math.pi), math.sqrt(w2 / math.pi)
    d = math.sqrt(a1 * a1 + a2 * a2 - 2 * a1 * a2 * math.cos(th))
    if d >= a1 + a2:
        return 0.0
    if d <= abs(a1 - a2) or d < 1e-14:
        return min(w1, w2)
    t1 = math.acos(max(-1, min(1, (d * d + a1 * a1 - a2 * a2) / (2 * d * a1))))
    t2 = math.acos(max(-1, min(1, (d * d + a2 * a2 - a1 * a1) / (2 * d * a2))))
    return a1 * a1 * (t1 - 0.5 * math.sin(2 * t1)) + a2 * a2 * (t2 - 0.5 * math.sin(2 * t2))

def M_eucl(Nw=120, Nth=120, Wmax=18.0):
    ws = np.linspace(0, Wmax, Nw + 1); ths = np.linspace(0, np.pi, Nth + 1)
    def simp(n, h):
        w = np.ones(n + 1); w[1:n:2] = 4; w[2:n-1:2] = 2; return w * (h / 3.0)
    ww, wt = simp(Nw, Wmax / Nw), simp(Nth, np.pi / Nth)
    E = 0.0
    for i in range(Nw + 1):
        for j in range(Nw + 1):
            U = np.array([ws[i] + ws[j] - eucl_inter(ws[i], ws[j], t) for t in ths])
            E += ww[i] * ww[j] * np.sum(wt * np.exp(-U))
    return E / (2 * np.pi) * 2.0

if __name__ == "__main__":
    for cfg in [(80, 64, 256, 14.0), (100, 80, 300, 16.0), (120, 96, 350, 18.0)]:
        t = time.time(); v = M_hyp(1.0, *cfg)
        print(f"lam=1 {cfg}: M={v:.6f} V={v-1:.6f} t={time.time()-t:.0f}s", flush=True)
    for lam in [0.5, 1.0, 2.0]:
        t = time.time(); v = M_hyp(lam, 120, 96, 350, 18.0)
        print(f"lam={lam}: M={v:.6f} V={v-1:.6f} t={time.time()-t:.0f}s", flush=True)
    t = time.time(); ve = M_eucl()
    print(f"eucl: M={ve:.6f} V={ve-1:.6f} t={time.time()-t:.0f}s", flush=True)
    print("tail T(18) =", tail_bound(18.0))
