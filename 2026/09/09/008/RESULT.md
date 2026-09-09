# Certified finite-horizon transient-peak intervals for T_n = -I_n + 2 N_n (n = 8, 10, 12, 14, 16)

## Context
Finite-horizon peak transient amplification Mmax(A) = max_{t>=0} ||exp(tA)||_2 for
Hurwitz-stable nonnormal matrices is the well-posed transient quantity behind
hydrodynamic-stability transient growth, Kreiss-matrix-theorem sharpness for stable
matrices, and eigenvalue-misleading (Greenbaum/Elman/GMRES) bounding programs, where
eigenvalues underpredict observed behavior. General Kreiss solvers, Lyapunov-extended
Elman bounds, GMRES curve-prescription existence theorems, and pseudospectra plot
galleries do not supply certified two-sided peak values for any concrete small stable
sequence.

## Definitions
- N_n: n x n superdiagonal-ones nilpotent shift (ones on first superdiagonal, zeros
  elsewhere). T_n = -I_n + 2 N_n: upper triangular with diagonal -1, hence eigenvalues
  {-1}^n, Hurwitz-stable.
- exp(t T_n) is exactly upper-triangular Toeplitz with entries
  E(t)[i,i+k] = e^{-t} (2t)^k / k!, k = 0..n-1 (finite nilpotent sum; no truncation).
- Mmax(T_n) = max_{t>=0} ||exp(t T_n)||_2 (spectral norm). Continuous in t, equals 1
  at t = 0, tends to 0 as t -> infinity, so the maximum is attained and finite (>= 1).
- Rational time maximizers t*: 6.388 (n=8), 8.379 (n=10), 10.373 (n=12),
  12.368 (n=14), 14.365 (n=16). Rational test vectors v (denominator 10^6, rounded
  numpy top singular vectors) stored in vectors.json.

## Result
For Mmax(T_n) = max_{t>=0} ||exp(t T_n)||_2:

| n  | t*     | certified interval [Lm, Um] | width/mid |
|----|--------|-----------------------------|-----------|
| 8  | 6.388  | [25.11, 26.00]              | 3.5%      |
| 10 | 8.379  | [89.00, 92.50]              | 3.9%      |
| 12 | 10.373 | [323.05, 336.60]            | 4.1%      |
| 14 | 12.368 | [1191.25, 1246.00]          | 4.5%      |
| 16 | 14.365 | [4443.28, 4657.00]          | 4.7%      |

All widths <= 4.7% (gate <= 20%). Replayed verifier values: Lm_replay = (25.11997,
89.01695, 323.05393, 1191.25688, 4443.28297); Um_replay = (25.98426, 92.40664,
336.48800, 1244.73972, 4656.70242). The enclosed ratio R = Mmax(T_16)/Mmax(T_8) lies
in [4443.28/26.00, 4657.00/25.11] = [170.9, 185.5], hence R >= 1.5: strictly
super-constant dimension growth of the finite-horizon transient peak.

## Proof / evidence
- Lower bound: at each rational t*, E(t*) entries enclosed as exact Fractions
  (2t*)^k/k! times a rigorous Decimal enclosure of e^{-t*} (Taylor sum plus
  alternating-tail remainder, 80-digit context). Stored rational test vector v gives
  interval w = E v; Lm = sqrt_lower(||w||^2)/||v||_hi * (1-0.001) - 1e-9. Since
  ||E||_2 >= ||Ev||/||v||, Lm <= Mmax rigorously.
- Upper bound: time grid h = 0.01 over [0, 30]. At each grid point tau the Frobenius
  norm is upper-bounded from entry intervals. With a = ||T||_F = sqrt(5n-4) exactly,
  |dF/dt| <= aF, so within delta = h/2 of a grid point, F(t) <= F(tau)/(1-a*delta)
  (using e^x <= 1/(1-x) for a*delta < 1; here a*delta <= 0.0436). Max over grid gives
  G_hi and Um = G_hi/(1-a*delta)*1.001+1e-9 >= every ||E(t)||_2 on [0,30].
- Tail: for t >= 30 > n-1 >= k, dv_k/dt = v_k(k/t-1) <= 0 entrywise, so
  F(t) <= F(30) termwise. Rigorous F_hi(30) = (5.3e-5, 2.7e-3, 0.088, 2.06, 35.86)
  is far below each Lm, so the global max lies in [0,30] and Um is global.
- Ratio by interval division as above.
- Independent audit: re-ran stdlib verifier -> VERIFY_OK; numpy cross-check gives
  spectral norms (25.145, 89.106, 323.377, 1192.449, 4447.731) strictly inside the
  claimed intervals; Frobenius/spectral ratio 1.0003-1.0014.

## Limitations
- Proven: the five intervals, R >= 1.5, stability, tail exclusion.
- Computed, not certified (excluded from certificate): numpy peak locations/test
  vectors used only as certificate inputs; Lyapunov sqrt(kappa(P)) comparison table
  (132.8, 503.4, 1925, 7409, 2.866e4) is an uncertified numpy tally.
- Open / not claimed: growth-law exponent fit (~3.6x per +2 dims is descriptive only);
  asymptotic law and Kreiss-constant comparison are conjectural follow-ups.
- Object caveat: T_n is a single-Jordan-block nonnormal toy benchmark, not a full
  Orr-Sommerfeld discretization (N ~ 99-100); rigor relies on slop factors
  (0.999/1.001/1e-9/1e-60) dominating ~1e-78 Decimal rounding rather than fully
  formal interval arithmetic.

## Reproducibility
Stdlib-only (no third-party imports): run `python3 verify.py` in output/artifacts/
with vectors.json present -> `VERIFY_OK` (replays exp enclosures, lower bounds, full
3001-point grid upper bounds, tails, widths, ratio; takes minutes). Numpy was used
only to discover t* and v (inputs to the certificate), never as proof.

## References
- Mitchell, Computing the Kreiss Constant of a Matrix (arXiv:1907.06537).
- Embree, Extending Elman's Bound for GMRES (arXiv:2312.15022).
- Matalon & Spillane, Any nonincreasing convergence curves are simultaneously possible
  for GMRES and weighted GMRES (arXiv:2506.17193).
- Pseudospectra Gateway: Orr-Sommerfeld Operator Example + EigTool,
  https://www.cs.ox.ac.uk/pseudospectra/thumbnails/orrsomm.html
