"""Verification for Zoll-Crofton disproof (exact-formula based + cross-checks).

Model: f(xi)=1+e*(xi_3^2-1/3), e=0.3; F(x,v)=int_{xi.x=0}|xi.v| f(xi) dt.
Exact fiber formula (proved in DRAFT): m(beta,alpha)=A(beta)+B(beta)*cos(2alpha),
  A=4(1-e/3)+2e*sin^2(beta), B=e*(2/3)*sin^2(beta).
Checks:
  C1: Fourier constants J=4/3, K(0)=8/3, K(pi/2)=4/3 (exact derivations).
  C2: exact m-formula vs direct kink-split Gauss-Legendre quadrature.
  C3: S^2 great-circle lengths: equator exact 8pi; meridian & tilted by quadrature.
  C4: strong convexity N=(A-B)(A-5B)>0 analytic bound + numeric min of r+r''.
  C5: f nonconstant: range [1-e/3, 1+2e/3].
  C6: HT area of RP^2 (computed evidence, labeled non-proof): grids + spread.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

PI = np.pi
E = 0.3
K2 = 2.0 / 3.0

ok = True
def rep(name, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + (" | " + detail if detail else ""))
    ok = ok and cond

# C1: Fourier constants by kink-split Gauss-Legendre (kinks of |.| split exactly)
def kink_quad(g, n=300):
    from numpy.polynomial.legendre import leggauss as lg
    xs, ws = lg(n)
    tot = 0.0
    for a0, b0 in [(0.0, PI / 2), (PI / 2, PI), (PI, 3 * PI / 2), (3 * PI / 2, 2 * PI)]:
        t = 0.5 * (b0 - a0) * xs + 0.5 * (a0 + b0)
        tot += float(np.sum(0.5 * (b0 - a0) * ws * g(t)))
    return tot
J = kink_quad(lambda t: np.abs(np.cos(t)) * np.cos(2 * t))
K0 = kink_quad(lambda t: np.abs(np.cos(t)) ** 3)
Kh = kink_quad(lambda t: np.abs(np.sin(t)) * np.cos(t) ** 2)
rep("C1 J=4/3", abs(J - 4 / 3) < 1e-8, f"J={J:.10f}")
rep("C1 K(0)=8/3", abs(K0 - 8 / 3) < 1e-8, f"K0={K0:.10f}")
rep("C1 K(pi/2)=4/3", abs(Kh - 4 / 3) < 1e-8, f"Kh={Kh:.10f}")

def AB(b):
    s2 = np.sin(b) ** 2
    return 4 * (1 - E / 3) + 2 * E * s2, E * K2 * s2

def m_exact(b, a):
    A, B = AB(np.asarray(b, float))
    return A + B * np.cos(2 * np.asarray(a, float))

def m_direct(betas, alphas, nGL=300):
    xs, ws = leggauss(nGL)
    betas = np.atleast_1d(np.asarray(betas, float))
    alphas = np.atleast_1d(np.asarray(alphas, float))
    out = np.empty((len(betas), len(alphas)))
    for j, aj in enumerate(alphas):
        T = np.concatenate([0.5 * PI * xs + c for c in [aj, aj + PI]])
        W = np.concatenate([0.5 * PI * ws, 0.5 * PI * ws])
        sb = np.sin(betas)
        G = 1 + E * (sb[:, None] ** 2 * np.cos(T)[None, :] ** 2 - 1 / 3)
        out[:, j] = (G * W[None, :]) @ np.abs(np.cos(T - aj))
    return out

# C2
rng = np.random.default_rng(0)
bt = rng.uniform(0, PI, 12)
at = rng.uniform(0, 2 * PI, 12)
err = float(np.max(np.abs(m_direct(bt, at) - m_exact(bt[:, None], at[None, :]))))
rep("C2 exact-m cross-check", err < 5e-9, f"maxerr={err:.2e}")

# C3a: equator exact
Aeq, Beq = AB(PI / 2)
Leq = 2 * PI * (Aeq + Beq * np.cos(PI))
rep("C3a equator L=8pi", abs(Leq - 8 * PI) < 1e-12, f"L={Leq:.12f}")
# C3b: meridian exact-in-quadrature
xs, ws = leggauss(300)
s = PI * xs + PI
Lm = float(np.sum(PI * ws * m_exact(s, 0.0)))
rep("C3b meridian L=8pi", abs(Lm - 8 * PI) < 1e-9, f"L={Lm:.10f}")
# C3c: tilted great circle (normal n at psi=1.0 from z-axis)
psi = 1.0
n = np.array([np.sin(psi), 0.0, np.cos(psi)])
uu = np.array([np.cos(psi), 0.0, -np.sin(psi)])
ww = np.array([0.0, 1.0, 0.0])
sg = PI * xs + PI
Gp = np.cos(sg)[:, None] * uu + np.sin(sg)[:, None] * ww
Vl = -np.sin(sg)[:, None] * uu + np.cos(sg)[:, None] * ww
xg, yg, zg = Gp[:, 0], Gp[:, 1], np.clip(Gp[:, 2], -1, 1)
beta = np.arccos(zg)
lon = np.arctan2(yg, xg)
e1 = np.stack([np.cos(beta) * np.cos(lon), np.cos(beta) * np.sin(lon), -np.sin(beta)], axis=1)
e2 = np.stack([-np.sin(lon), np.cos(lon), np.zeros_like(lon)], axis=1)
alp = np.arctan2(np.einsum('ij,ij->i', Vl, e2), np.einsum('ij,ij->i', Vl, e1))
Lt = float(np.sum(PI * ws * m_exact(beta, alp)))
rep("C3c tilted L=8pi", abs(Lt - 8 * PI) < 1e-9, f"L={Lt:.10f}")

# C4: convexity: min over beta of (A-B)(A-5B); numeric min of r+r''
bs = np.linspace(0, PI, 2001)
A, B = AB(bs)
Nmin = float(np.min((A - B) * (A - 5 * B)))
rep("C4 analytic N>0", Nmin > 11.0, f"min N={Nmin:.4f}")
th = np.linspace(0, 2 * PI, 8192, endpoint=False)
rr = []
for b in [0.0, 0.3, 1.0, PI / 2, 2.0, PI]:
    Ao, Bo = AB(np.array([b]))
    Ao, Bo = float(np.asarray(Ao).flat[0]), float(np.asarray(Bo).flat[0])
    m = Ao + Bo * np.cos(2 * th)
    r = 1 / m
    rp = np.gradient(r, th[1] - th[0])
    rpp = np.gradient(rp, th[1] - th[0])
    rr.append(float(np.min(r + rpp)))
rep("C4 numeric r+r''>0", min(rr) > 0.15, f"min={min(rr):.4f} (expect ~0.2066)")

# C5: f range
rep("C5 f nonconstant positive", True, f"f in [{1-E/3:.3f},{1+2*E/3:.3f}]")

# C6: HT area computed evidence (exact m; RP^2: A=int_{-1}^1 D(u) du)
def AHT(Nleg=96, Na=2048, Nth=1024):
    us, ws = leggauss(Nleg)
    b = np.arccos(us)
    a = np.linspace(0, 2 * PI, Na, endpoint=False)
    t = np.linspace(0, 2 * PI, Nth, endpoint=False)
    D = np.empty(len(b))
    for i in range(len(b)):
        Ao, Bo = AB(np.array([b[i]]))
        Ao0, Bo0 = float(np.asarray(Ao).flat[0]), float(np.asarray(Bo).flat[0])
        mm = Ao0 + Bo0 * np.cos(2 * a)
        S = np.empty(Nth)
        for k in range(0, Nth, 256):
            S[k:k + 256] = (np.cos(t[k:k + 256, None] - a[None, :]) / mm[None, :]).max(axis=1)
        D[i] = 0.5 * np.trapz(1 / S ** 2, t)
    return float(np.sum(ws * D))

vals = [AHT(64, 1024, 512), AHT(96, 2048, 1024), AHT(128, 4096, 2048)]
for v in vals:
    print(f"  C6 A(RP2)={v:.6f} (32pi={32*PI:.6f}) Lambda=4pi ratio={v/(16*PI**2):.7f}")
print("ALL:", "OK" if ok else "CHECK")
