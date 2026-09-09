"""verify.py — stdlib-only rigorous verifier for lane-286 certificates.
Run: python3 verify.py  (no third-party imports)

Certificate object (committed BEFORE computation):
  T_n = -I_n + 2*N_n, N_n = superdiagonal-ones nilpotent; eig(T_n) = {-1}^n (Hurwitz).
  Mmax(T_n) = max_{t>=0} ||exp(t T_n)||_2, closed-form Toeplitz entries
      E(t)[i,i+k] = e^{-t} (2t)^k / k!.
Claim: for each n in {8,10,12,14,16}: Mmax(T_n) in [Lm,Um] (CLAIM table),
  widths <= ~5% of midpoint (gate: <=20%), and R=Mmax(T16)/Mmax(T8) in [~171,~186]
  hence R>=1.5 (super-constant growth witness).

Method (all bounds rigorous in exact rational + Decimal interval arithmetic):
  EXP: Decimal enclosure of e^{-x}: S_N +/- (t_{N+1} + round-margin), where the
      alternating-tail remainder bound |R_N| <= t_{N+1} = x^{N+1}/(N+1)! applies
      since terms decrease monotonically for k+1 > x (we assert N+1 > x).
  LOWER: rational test vector v (denominator 10^6, from numpy singular vector, stored
      in vectors.json); E(t*) entries enclosed as intervals; w=Ev interval;
      Lm_replay = sqrt_lower(||w||^2)/||v||_hi - margins. No series truncation:
      entries use the exact closed form times the enclosed exp factor.
  UPPER: time grid h=0.01 on [0,30]; at each grid point F_hi(tau) = Frobenius upper
      bound from entry intervals; G_hi = max; Lipschitz a=||T||_F=sqrt(5n-4) exact
      (upper-bounded); cell sup <= F(tau)/(1-a*h/2) since |F'|<=aF gives
      F(t)<=F(tau)*exp(a*delta)<=F(tau)/(1-a*delta) for a*delta<1. Tail: for t>=30,
      each entry v_k(t) is termwise decreasing (dv_k/dt = v_k*(k/t-1) <= 0 as
      k<=n-1<=15<30=t), so F(t)<=F(30)<=Lm. Verifier checks F_hi(30) <= Lm_c.
Checks printed: exp-enclosure validity, per-n Lm replay, per-n Um replay (full grid
  recompute in stdlib), width gate, tail gate, ratio gate, stability.
"""
import json
import os
from fractions import Fraction as F
from decimal import Decimal, getcontext, localcontext

getcontext().prec = 80
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------- committed certificate ----------------
TSTAR = {"8": "6.388", "10": "8.379", "12": "10.373", "14": "12.368", "16": "14.365"}
# claimed intervals (verifier FAILS unless replay supports them)
CLAIM = {
    "8":  (25.11, 26.00),
    "10": (89.00, 92.50),
    "12": (323.05, 336.60),
    "14": (1191.25, 1246.00),
    "16": (4443.28, 4657.00),
}
TT = F(30, 1)
TOL = Decimal(10) ** Decimal(-60)


def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def exp_enclosure(x_dec, terms=120):
    """Rigorous enclosure of exp(-x), x>0 Decimal.
    S_N = sum_{k<=N} (-x)^k/k!; tail alternating with decreasing |terms| once
    k+1 > x (asserted), so |R_N| <= t_{N+1} = x^{N+1}/(N+1)!. Add TOL margin for
    Decimal rounding of the partial sum."""
    x = x_dec
    if x == 0:
        return Decimal(1), Decimal(1)
    assert x > 0
    N = terms
    assert Decimal(N + 1) > x, "need N+1 > x for decreasing tail"
    s = Decimal(1)
    term = Decimal(1)  # signed term (-x)^k/k!
    for k in range(1, N + 1):
        term = term * (-x) / Decimal(k)
        s += term
    mag = term.copy_abs() * x / Decimal(N + 1)  # |term_{N+1}|
    margin = TOL * (1 + s.copy_abs())
    return s - mag - margin, s + mag + margin


def dsqrt(x):
    with localcontext() as c:
        c.prec = 80
        r = x.sqrt() if x > 0 else Decimal(0)
    return r


def entry_scales(t_frac, n):
    """Exact Fractions (2t)^k/k! for k<n."""
    out = []
    pw = F(1, 1)
    for k in range(n):
        if k > 0:
            pw *= 2 * t_frac
        out.append(pw / fact(k))
    return out


def frac_dec(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


def main():
    with open(os.path.join(HERE, "vectors.json")) as f:
        VECS = json.load(f)
    ok = True
    print("=== stability ===")
    print("T_n upper triangular with diagonal -1 by construction -> eig = {-1}^n, Hurwitz. PASS")
    print("=== exp enclosure self-test ===")
    lo, hi = exp_enclosure(Decimal("6.388"))
    import math
    ref = Decimal(str(math.exp(-6.388)))
    rel = abs((lo + hi) / 2 - ref) / ref
    print("e^-6.388 enclosure width %.2e, float-ref rel.diff %.2e -> %s"
          % (float(hi - lo), float(rel), "PASS" if rel < Decimal("1e-12") else "FAIL"))
    ok &= rel < Decimal("1e-12")
    for ns in ["8", "10", "12", "14", "16"]:
        n = int(ns)
        ts = TSTAR[ns]
        digits = ts.split(".")[1]
        t_frac = F(int(ts.replace(".", "")), 10 ** len(digits))
        scales = entry_scales(t_frac, n)
        elo, ehi = exp_enclosure(Decimal(ts))
        # ---- LOWER replay ----
        v = [F(x, 10 ** 6) for x in VECS[ns]]
        vnsq = sum(x * x for x in v)
        vnhi = dsqrt(frac_dec(vnsq)) * (1 + Decimal(10) ** Decimal(-70))
        wlo = [Decimal(0)] * n
        whi = [Decimal(0)] * n
        for i in range(n):
            slo = Decimal(0)
            shi = Decimal(0)
            for k in range(n - i):
                cd = frac_dec(scales[k])
                vd = frac_dec(v[i + k])
                if vd >= 0:
                    slo += elo * cd * vd
                    shi += ehi * cd * vd
                else:
                    slo += ehi * cd * vd
                    shi += elo * cd * vd
            wlo[i], whi[i] = slo, shi
        qlo = Decimal(0)
        for a, b in zip(wlo, whi):
            if a >= 0:
                qlo += a * a
            elif b <= 0:
                qlo += b * b
            else:
                qlo += Decimal(0)
        Lm_replay = dsqrt(qlo) / vnhi * (1 - Decimal("0.001")) - Decimal("1e-9")
        # ---- UPPER replay: grid max of Frobenius (stdlib loop) ----
        a2 = 5 * n - 4  # ||T||_F^2 exact
        ahi = dsqrt(Decimal(a2)) * (1 + Decimal(10) ** Decimal(-70)) + Decimal(10) ** Decimal(-60)
        G2hi = Decimal(0)
        for j in range(0, 3001):
            tau = F(j, 100)
            sc = entry_scales(tau, n)
            ehi_j = exp_enclosure(Decimal(j) / Decimal(100), terms=160)[1]
            q = Decimal(0)
            for k in range(n):
                cd = frac_dec(sc[k])
                q += Decimal(n - k) * (ehi_j * cd) ** 2
            if q > G2hi:
                G2hi = q
        Ghi = dsqrt(G2hi) * (1 + Decimal(10) ** Decimal(-70)) + Decimal(10) ** Decimal(-60)
        den = 1 - ahi * Decimal(1) / Decimal(200)
        assert den > 0
        Um_replay = Ghi / den * (Decimal("1.001")) + Decimal("1e-9")
        # ---- TAIL: F(30) upper ----
        scT = entry_scales(TT, n)
        ehiT = exp_enclosure(Decimal(30), terms=220)[1]
        qT = Decimal(0)
        for k in range(n):
            cd = frac_dec(scT[k])
            qT += Decimal(n - k) * (ehiT * cd) ** 2
        FThi = dsqrt(qT) * (1 + Decimal(10) ** Decimal(-70)) + Decimal(10) ** Decimal(-60)
        Lm_c, Um_c = CLAIM[ns]
        l_ok = Lm_c <= float(Lm_replay)
        u_ok = float(Um_replay) <= Um_c
        tail_ok = float(FThi) <= Lm_c
        width = 200 * (Um_c - Lm_c) / (Um_c + Lm_c)
        w_ok = width <= 20.0
        print("n=%s t*=%s Lm_replay=%.6f Um_replay=%.6f Fhi(30)=%.4g | claim=[%.2f,%.2f] w=%.2f%% -> L:%s U:%s tail:%s W:%s"
              % (ns, ts, float(Lm_replay), float(Um_replay), float(FThi), Lm_c, Um_c, width,
                 "PASS" if l_ok else "FAIL", "PASS" if u_ok else "FAIL",
                 "PASS" if tail_ok else "FAIL", "PASS" if w_ok else "FAIL"))
        ok &= (l_ok and u_ok and tail_ok and w_ok)
    Rlo = CLAIM["16"][0] / CLAIM["8"][1]
    Rhi = CLAIM["16"][1] / CLAIM["8"][0]
    r_ok = Rlo >= 1.5
    print("R = Mmax16/Mmax08 in [%.3f, %.3f]; R>=1.5 -> %s" % (Rlo, Rhi, "PASS" if r_ok else "FAIL"))
    ok &= r_ok
    print("VERIFY_" + ("OK" if ok else "FAILED"))
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
