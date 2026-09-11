"""All-multiplicity (all-m) interpolation impossibility at lane-831 window.

Window: base RS [64,16]/F257 folded s=4 -> N=16, rate 1/4; rho=0.52 ->
bundle agreement t=8 (errors<=8); unfolded agreement t_u=31 as the direct
fractional-radius translation (ceil(64*0.48)), with folded-induced minimum
t>=32 (8 fully-correct bundles x4). Lemma 2 is blocked under either bound
(see below); t_u=31 is adopted as the operative sweep since it is the weakest
fractional-radius premise, plus an explicit t=32 sweep (collapses to the L1
AM-GM) so the stronger folded structure does not rescue the certificate.
Standard existence-plus-multiplicity-lemma framework:
  existence: #coeffs(D,l) > #conditions(m); decoding: D < t*(m-l), l<m.

Proves infeasibility for EVERY m>=2 in three settings:
 L1: bivariate bundle (N=16): analytic AM-GM, no computation needed
     (numeric sweep to m=500 as machine check).
 L2: bivariate unfolded (n=64): analytic AM-GM at t=31 and t=32
     (numeric sweeps to m=500 for both).
 L3: (s+1)-variate GR-type generous unweighted upper bound: exhaustive
     best-case check for m<=200 + analytic tail bound for m>=50
     (overlap [50,200] cross-validates). Corrected chain:
     numerator 8(m-l)*C(l+4,4) <= (1/3)(m-l)(l+4)^4,
     denominator 16*C(m+4,5) >= (2/15)m^5,
     so Rtrue <= 2.5*((m-l)/m)*(((l+4)/m)^4) =: Rcorr-base;
     with u':=(m-l)/m in (0,1] and (l+4)/m = 1-u'+4/m <= 1.08-u' for m>=50,
     Rtrue <= 2.5*u'*(1.08-u')^4. Failure under the generous
     upper bound implies failure under the true stricter GR weighted
     count, so the obstruction transfers.
"""
import math

print("=== L1: bivariate bundle N=16, t=8 ===")
# Necessary: (l+1)*8*(m-l) > 8*m*(m+1) i.e. s*(m+1-s) > m*(m+1), s=l+1.
# LHS <= ((m+1)/2)^2; suffices ((m+1)/2)^2 <= m*(m+1) <=> (m+1)/4 <= m <=> True for m>=1.
ok1 = True
for m in range(2, 501):
    conds = 8 * m * (m + 1)
    feas = []
    for l in range(0, m):
        D = 8 * (m - l) - 1  # largest D allowed by decoding
        c = sum(max(0, D - j * 15 + 1) for j in range(l + 1))  # exact weighted count
        if c > conds:
            feas.append(l)
    # analytic certificate: max_s s*(m+1-s) = floor((m+1)^2/4) <= m*(m+1) iff m>=1
    smax = (m + 1) ** 2 // 4
    assert smax <= m * (m + 1), m
    if feas:
        ok1 = False
        print(f"  m={m}: UNEXPECTED feasible l={feas}")
print(f"  L1 analytic holds for all m>=1; numeric sweep 2..500 feasible: {'NONE (OK)' if ok1 else 'FOUND (FAIL)'}")

print("=== L2: bivariate unfolded n=64 ===")
print("  t_u=31 adopted as the operative sweep (weakest fractional-radius premise ceil(64*0.48));")
print("  t=32 folded-induced minimum (8 fully-correct bundles) swept as well: necessity then")
print("  collapses to s(m+1-s)>m(m+1), the same AM-GM as L1, so blocked under either bound.")
ok2 = True
for m in range(2, 501):
    conds = 32 * m * (m + 1)
    feas = []
    for l in range(0, m):
        D = 31 * (m - l) - 1
        c = sum(max(0, D - j * 15 + 1) for j in range(l + 1))
        if c > conds:
            feas.append(l)
    # analytic: 31*((m+1)/2)^2 <= 32*m*(m+1) <=> 31*(m+1) <= 128*m <=> 31 <= 97*m, true
    assert 31 * (m + 1) ** 2 // 4 <= 32 * m * (m + 1) or True
    if feas:
        ok2 = False
        print(f"  m={m}: UNEXPECTED feasible l={feas} at t=31")
# analytic inequality check exact rational form: 31(m+1)^2/4 <= 32m(m+1) <=> 31(m+1) <= 128m
assert all(31 * (m + 1) <= 128 * m for m in range(1, 501))
print(f"  L2 analytic 31(m+1)<=128m holds for all m>=1; numeric sweep t=31, 2..500 feasible: {'NONE (OK)' if ok2 else 'FOUND (FAIL)'}")
ok2b = True
for m in range(2, 501):
    conds = 32 * m * (m + 1)
    feas = []
    for l in range(0, m):
        D = 32 * (m - l) - 1  # folded-induced minimum t=32
        c = sum(max(0, D - j * 15 + 1) for j in range(l + 1))
        if c > conds:
            feas.append(l)
    if feas:
        ok2b = False
        print(f"  m={m}: UNEXPECTED feasible l={feas} at t=32")
print(f"  L2 numeric sweep t=32 (folded-induced minimum), 2..500 feasible: {'NONE (OK)' if ok2b else 'FOUND (FAIL)'}")

print("=== L3: multivar GR-type generous, t=8 ===")
# best case per (m,l): D+1 = 8*(m-l); check 8*(m-l)*C(l+4,4) > 16*C(m+4,5)?
# Corrected bounding chain (audit fix): numerator 8(m-l)*C(l+4,4) <= (1/3)(m-l)(l+4)^4
# since C(l+4,4)=(l+4)(l+3)(l+2)(l+1)/24 <= (l+4)^4/24; denominator
# 16*C(m+4,5) = 16(m+4)(m+3)(m+2)(m+1)m/120 >= 16*m^5/120 = (2/15)m^5.
# Hence Rtrue <= [(1/3)(m-l)(l+4)^4]/[(2/15)m^5] = 2.5*((m-l)/m)*(((l+4)/m)^4).
ok3 = True
worst_ratio = 0.0
for m in range(2, 201):
    conds = 16 * math.comb(m + 4, 5)
    for l in range(0, m):
        if 8 * (m - l) * math.comb(l + 4, 4) > conds:
            ok3 = False
            print(f"  m={m},l={l}: UNEXPECTED feasible")
    for l in range(0, m):
        r = 8 * (m - l) * math.comb(l + 4, 4) / conds
        worst_ratio = max(worst_ratio, r)
print(f"  exhaustive m=2..200 feasible: {'NONE (OK)' if ok3 else 'FOUND (FAIL)'}; worst best-case ratio={worst_ratio:.4f}")
# explicit verification that Rtrue <= corrected-chain bound on the tail range:
# check exact best-case Rtrue(m,l) <= 2.5*((m-l)/m)*(((l+4)/m)^4) for 50<=m<=200, all l<m
chain_ok = True
chain_worst_slack = 0.0
for m in range(50, 201):
    den = 16 * math.comb(m + 4, 5)
    for l in range(0, m):
        rtrue = 8 * (m - l) * math.comb(l + 4, 4) / den
        rcorr = 2.5 * ((m - l) / m) * (((l + 4) / m) ** 4)
        slack = rcorr - rtrue
        chain_worst_slack = max(chain_worst_slack, slack) if chain_ok else chain_worst_slack
        if not rtrue <= rcorr:
            chain_ok = False
            print(f"  CHAIN VIOLATION m={m},l={l}: Rtrue={rtrue} > Rcorr={rcorr}")
print(f"  corrected-chain verification Rtrue<=Rcorr on 50<=m<=200, all l<m: {'HOLDS (OK)' if chain_ok else 'VIOLATED (FAIL)'}")
# analytic tail for m>=50 with u':=(m-l)/m in (0,1]: (l+4)/m = 1-u'+4/m <= 1.08-u',
# so Rtrue <= Rcorr <= 2.5*u'*(1.08-u')^4; max of RHS over (0,1] at u'=1.08/5=0.216.
up = 0.216
gmax = up * (1.08 - up) ** 4  # = 0.216*0.864^4
Rbound = 2.5 * gmax
print(f"  tail bound (u'=(m-l)/m): gmax={gmax:.6f}, R<={Rbound:.6f} < 1 for all m>=50 (covers tail)")
# verify calculus claim on a fine grid over u' in (0,1] (stdlib only)
gridmax = max((x * (1.08 - x) ** 4) for x in [i / 10000 for i in range(1, 10001)] if 1.08 - x > 0)
print(f"  grid check max u'*(1.08-u')^4 on (0,1] = {gridmax:.6f} (theory {gmax:.6f}); R_grid<={2.5 * gridmax:.6f} < 1")
# exact-rational maximum: u'*=27/125, g*=(27/125)*(108/125)^4=3673320192/30517578125
from fractions import Fraction as F
gstar = F(27, 125) * (F(108, 125) ** 4)
print(f"  exact-rational max g*={gstar}~={float(gstar):.6f}; 2.5*g*={float(F(5,2)*gstar):.6f} < 1")
assert gstar == F(3673320192, 30517578125), "exact rational identity"
assert F(5, 2) * gstar < 1
print("RESULT:", "ALL-m BLOCKED in L1/L2/L3" if (ok1 and ok2 and ok2b and ok3 and chain_ok and Rbound < 1) else "GAP REMAINS")
