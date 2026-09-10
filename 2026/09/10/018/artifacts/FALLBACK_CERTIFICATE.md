# Flat-line transfer obstruction at p0 = 7/2 — fallback certificate (lane-527)

Target status: the full TARGET (sharp range p>4) is not viable — its upper-bound
half is refuted on (4, 22/5) by the anisotropic Knapp family below (WORKLOG §2–3).
Route decision: PRESET_FALLBACK (exact fallback_claim), which is fully proved with
explicit constants far above the qualification threshold.

## 1. Objects (exact, replayable)

- Phase: phi(xi1,xi2) = xi1^2 - xi2^2 + xi1^3 on B^2(0,1/2).
- Surface: S_* = graph of phi. Extension: E f(x) = int e^{i(x1 xi1+x2 xi2+x3 phi)} f d xi.
- Fold: det Hess phi = -4(1+3 xi1); K = 0 <=> xi1 = -1/3, simple zero (slope -12).
- Recenter u = xi1+1/3, v = xi2: phi = u^3 - u/3 + 2/27 - v^2; fold point xi* = (-1/3,0).
- Radius: R = 2^24. Widths: d = R^{-1/3} = 2^{-8}, s = R^{-1/2} = 2^{-12}.
- Datum: f = 1_Q, Q = {|u| <= d, |v| <= s} (axis-aligned rectangle at xi*).
- Support: center distance 1/3 + d < 1/2 from origin, so Q ⊂ B^2(0,1/2); and
  |u| <= d = R^{-1/3}, so Q lies in the R^{-1/3}-neighbourhood of the fold line.
- Normalization: ||f||_2 = sqrt(4ds) = sqrt(2^{-18}) = 2^{-9} = 0.001953125.

## 2. Coherence box

- Shear y1 = x1 - x3/3, y2 = x2, y3 = x3 (Jacobian 1; removes the -u/3 tilt and the
  constant phase 2/27, which is unimodular).
- Then E f(x) = e^{i tilt phases} I(y), I(y) = ∫_{|u|≤d,|v|≤s} e^{i(y1 u + y2 v + y3 u^3 - y3 v^2)} du dv.
- Box T_y = {|y1| ≤ 0.1/d, |y2| ≤ 0.1/s, |y3| ≤ 0.1 R} = {|y1|≤25.6, |y2|≤409.6, |y3|≤1677721.6}.
- On T_y the total phase is at most 0.1+0.1+0.1+0.1 = 0.4 rad
  (|y1 u|≤0.1, |y2 v|≤0.1, |y3||u|^3≤0.1R·R^{-1}=0.1,
  |y3|v^2≤0.1R·R^{-1}=0.1), hence |I(y)| ≥ cos(0.4)·4ds = Emin = 3.51356886×10^{-6}.
- Physical box T_x = shear^{-1}(T_y): Vol(T_x) = 8·0.1^3·d^{-1}s^{-1}R = 0.008 R^{11/6}
  = 140737488355.33; corner |x| ≤ 0.1R·sqrt((R^{-2/3}+1/3)^2+R^{-1}+1) ≈ 0.1054R < R,
  so T_x ⊂ B_R (checked analytically for all R≥1 and numerically in verify_fold.py).

## 3. Ratio at p0 = 7/2 (binary test)

- ||E f||_{L^{7/2}(B_R)} ≥ Emin · Vol^{2/7} = 0.00538280....
- ||f||_2 = 0.001953125.
- Ratio ≥ 2.75599... ≥ 10^{-3}·R^{1/24} = 10^{-3}·2 = 0.002. HOLDS with margin ×1378.
- L^2-normalized data g = f/||f||_2 gives the same ratio (homogeneous).
- Dyadic form: R = 2^24 = 2^{6·4} = R_4 with k=4 ≥ ... ≥ 2^24. ✓
- Sequence form: same construction at R_k = 2^{6k} (k ≥ 4) gives ratio ≥ 0.463·R_k^{3/28}
  ≥ 10^{-3} R_k^{1/24} for all k ≥ 4 (exponent 3/28 > 1/24 absorbs the constant).

## 4. Why this refutes elliptic transfer

- Elliptic (Demeter–Wu / Guo–Liu–Xi) transfer range p > 22/7 ≈ 3.143 would imply
  boundedness (up to R^eps) at p0 = 7/2 = 3.5 on every admissible surface; the
  polynomial blowup R^{1/24} (in fact R^{3/28}) with absolute constant is incompatible
  with any C·R^eps bound. Hence the range does not transfer to S_*.
- Prior Knapp boxes (elliptic paraboloid, cone, nondegenerate saddle) are all bounded
  at p = 7/2, so none implies this blowup; the cubic-fold degeneracy (K vanishing
  simply along a line, transverse scalings R^{-1/3} × R^{-1/2}) changes the
  volume-overlap scaling. BMV's upper bound p > 10/3 is consistent with boundedness
  at 7/2 and does not imply it.

## 5. Replay

- python3 output/artifacts/verify_fold.py        → geometry, constants, containment, ratios (VERIFY_OK)
- python3 output/artifacts/verify_knapp_quad.py  → direct quadrature of I(y) at R=256 (QUAD_CHECK: PASS)
- python3 output/artifacts/verify_bilinear.py    → transverse bilinear constant chain (VERIFY_OK)
- python3 output/artifacts/knapp_optimality.py   → rectangle-threshold scan, max 22/5 (VERIFY_OK)
- This file's §3 numbers recompute by hand from d = 2^{-8}, s = 2^{-12} (see WORKLOG).
