"""Numeric check of Koranyi spherical decay for n=1 (target leg D).

R_k(lam) = (1/pi) * int_{-pi/2}^{pi/2} L_k^0(lam*cos(t)/2) * exp(-lam*cos(t)/4)
           * cos(lam*sin(t)/4) dtheta   (lam>0, real by symmetry)
Verifies: (i) R_k(0)=1; (ii) low-freq R_k~1 for mu*lam<<1;
(iii) high-freq envelope |R_k| <= C (lam*mu)^(-1/4), mu=2(2k+1).
Laguerre via stable 3-term recurrence (alpha=0), mpmath only for quadrature.
"""
import mpmath as mp

mp.mp.dps = 25

def laguerre0(k, x):
    x = mp.mpf(x)
    if k == 0:
        return mp.mpf(1)
    if k == 1:
        return 1 - x
    L0, L1 = mp.mpf(1), 1 - x
    for j in range(1, k):
        # (j+1) L_{j+1} = (2j+1-x) L_j - j L_{j-1}
        L2 = ((2 * j + 1 - x) * L1 - j * L0) / (j + 1)
        L0, L1 = L1, L2
    return L1

def Rk(k, lam):
    lam = mp.mpf(lam)
    def f(th):
        c = mp.cos(th)
        x = lam * c / 2
        L = laguerre0(k, x)
        return L * mp.e**(-lam * c / 4) * mp.cos(lam * mp.sin(th) / 4)
    val = mp.quad(f, [-mp.pi / 2, mp.pi / 2], maxdegree=12)
    return val / mp.pi

def main():
    print("=== R_k(0) check (expect 1) ===")
    for k in [0, 1, 2, 5]:
        print(f"k={k} R(0)={float(Rk(k, 0)):.10f}")
    print("=== low frequency (mu*lam<<1, expect ~1) ===")
    for k in [0, 3, 8]:
        mu = 2 * (2 * k + 1)
        lam = 0.01 / mu
        print(f"k={k} mu={mu} lam={float(lam):.3e} R={float(Rk(k, lam)):.8f}")
    print("=== high frequency envelope ===")
    print(f"{'k':>3} {'lam':>6} {'rho=lam*mu':>12} {'R':>14} {'rho^-1/4':>12} {'ratio':>9}")
    worst = 0.0
    for k in [0, 1, 2, 3, 5, 8, 12]:
        mu = 2 * (2 * k + 1)
        for lam in [2.0, 5.0, 10.0, 20.0]:
            rho = lam * mu
            r = float(Rk(k, lam))
            pred = rho ** (-0.25)
            ratio = abs(r) / pred
            print(f"{k:>3} {lam:>6} {rho:>12.2f} {r:>14.6f} {pred:>12.6f} {ratio:>9.3f}")
            worst = max(worst, ratio)
    print(f"worst |R|/rho^-1/4 = {worst:.3f} (bounded => decay holds with C>={worst:.3f})")
    k, lam, r = 3, 5.0, 0.5
    mu = 2 * (2 * k + 1)
    print(f"scaling: R_{k}({lam}*{r}^2={lam*r*r})={float(Rk(k, lam*r*r)):.6f}, rho'={lam*r*r*mu}")

if __name__ == "__main__":
    main()
