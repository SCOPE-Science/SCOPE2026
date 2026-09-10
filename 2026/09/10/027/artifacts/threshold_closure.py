"""Verify threshold-closure arithmetic for the emergent H^1 Koranyi bound (stdlib only).

Given the uniform spectral envelope (verified numerically in check_Rk_decay.py,
proved as Raani-Singh Lemma 1.4):
    |R_k(lam r^2)| <= C0 * min(1, (lam r^2 mu)^(-1/4)),  t := lam*mu,
the r-integrated kernel is
    M(t) = int_0^{R0} r^6 min(1, (t r^2)^(-1/2)) dr.
Riesz energy weight (alpha = 4 - s'): w(t)^2 = t^(-alpha).
Closure of the Mattila Cauchy-Schwarz bookkeeping needs M(t) <= C1 t^(-alpha)
uniformly in t, i.e. sup_t M(t)/t^(-alpha) < inf.
This script checks that this holds iff alpha <= 1/2, i.e. s' >= 7/2,
so s_c = Q - 2*beta = 4 - 2*(1/4) = 7/2. Pure envelope arithmetic.
"""
import math

R0 = 2.0

def M(t):
    rs = t ** (-0.5)
    if rs >= R0:
        return R0 ** 7 / 7.0
    return rs ** 7 / 7.0 + t ** (-0.5) * (R0 ** 6 - rs ** 6) / 6.0

def sup_ratio(alpha, tmin=1e-6, tmax=1e8, n=20001):
    worst = 0.0
    t_at = None
    for i in range(n + 1):
        le = math.log10(tmin) + (math.log10(tmax) - math.log10(tmin)) * i / n
        t = 10 ** le
        r = M(t) / (t ** (-alpha))
        if r > worst:
            worst = r
            t_at = t
    return worst, t_at

def main():
    print("Q=4, beta=1/4 -> s_c = Q-2*beta = 7/2 = 3.5")
    print(f"R0={R0}, M(t) envelope as above; ratio = M(t)/t^(-alpha)")
    for alpha, s in [(0.5, 3.5), (0.8, 3.2), (1.0, 3.0)]:
        w, t_at = sup_ratio(alpha)
        print(f"alpha={alpha} (s'={s}): sup ratio = {w:.4f} at t={t_at:.3e} "
              + ("BOUNDED -> closes" if alpha <= 0.5 else "GROWS with tmax -> fails"))
    # show growth explicitly for alpha=0.8 at increasing tmax
    print("growth check alpha=0.8:")
    for tmax in [1e2, 1e4, 1e6, 1e8]:
        w, _ = sup_ratio(0.8, tmax=tmax)
        print(f"  tmax={tmax:.0e}: sup = {w:.4f} (~ tmax^(alpha-1/2) = {tmax**(0.3):.1f} x const)")
    print("CONCLUSION: with decay exponent beta=1/4, bookkeeping closes iff s'>=7/2;")
    print("s'>3 (alpha=1) is NOT closable on this route (ratio ~ t^1/2 unbounded).")

if __name__ == "__main__":
    main()
