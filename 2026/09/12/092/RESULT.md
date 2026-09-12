# Corrected 6-torsion elliptic-dilogarithm ratio on the CM curve y^2 = x^3 + 1 (Cremona 36a1)

## Context

Let E be the elliptic curve over Q defined by y^2 = x^3 + 1. This is Cremona
label 36a1, LMFDB isogeny-class member 36.a4 (minimal model [0,0,0,0,1]),
j = 0, with complex multiplication by the Eisenstein order of discriminant -3
and conductor 36. (Note on labels: LMFDB 36.a1 denotes a different model
y^2 = x^3 - 135x - 594 with j = 54000 and torsion Z/2; the object studied here
is unambiguously y^2 = x^3 + 1, i.e. Cremona 36a1 = LMFDB 36.a4, torsion Z/6.)

The admitted target asked whether, with E(C) = C*/qZ Tate uniformization, D
the Bloch-Wigner dilogarithm, D_q(z) = sum_{n in Z} D(q^n z) extended linearly,
U = (2,3) of order 6, V = 3U = (-1,0) of order 2, and
xi = 3[(U)-(O)] - [(V)-(O)], the identity L(E,2)/pi = (1/12) D_q(xi) holds
exactly, with both proof and disproof counting as new exact invariants and
neither reducing to 2-torsion vanishing or antisymmetric cancellation.

## Definitions

- Bloch-Wigner dilogarithm: D(z) = Im Li_2(z) + arg(1-z) log|z|, D(0)=D(1)=0,
  D(1/z) = -D(z), evaluated with inversion for |z| > 1.
- Elliptic dilogarithm: D_q(z) = sum_{n in Z} D(q^n z), truncated at |n| <= M.
- Tate data: q = -exp(-pi sqrt(3)) ≈ -0.0043334205099831292192, from periods
  with tau = (-1 + i sqrt(3))/2; lifts z_U = i exp(-5 pi sqrt(3)/6),
  z_V = -i exp(-pi sqrt(3)/2), fixing the branch of the regulator sum.
- L-value: L(E,s) via modularity (modular form 36.2.a.a), root number +1.
- Divisor: xi = 3[(U)-(O)] - [(V)-(O)], degree 0, with 3U - V = O in E(Q).

## Result

Claim route: EMERGENT_FINDING arising solely from pursuit of the target.

1. The stated identity L(E,2)/pi = (1/12) D_q(xi) is FALSE as a numerical
   identity under the stated conventions, by a large margin:
   L(E,2) = 0.9400130073882257815, L(E,2)/pi = 0.29921543339302892813;
   D_q(U) = -0.67323472513431508824 (nonzero),
   D_q(V) = 0 to ~5e-20, D_q(xi) = 3 D_q(U) - D_q(V) = -2.01970417540294526467;
   (1/12) D_q(xi) = -0.16830868128357877206;
   gap L/pi - (1/12) D_q(xi) = 0.46752411467660770019 (wrong sign and magnitude).
2. The data instead identify a sharp corrected conjecture:
   (L(E,2)/pi) / D_q(xi) = -0.14814814814814814816 = -4/27 to ~2e-20, i.e.
   L(E,2)/pi = -(4/27) D_q(xi) at computed-evidence level.
3. Exactly proved by finite arithmetic: U, V lie on E; 2U = (0,1), 3U = V,
   6U = O so U has exact order 6; 2V = O so V has exact order 2; xi is
   degree-zero with 3U - V = O. Conductor 36 and torsion Z/6 confirmed via
   PARI elltors/ellglobalred as reported.

Status: items 1-2 at the level of high-precision computed evidence
(80-digit mpmath, M = 10/30/60/90 convergence to ~1e-20, PARI L-value stable
across 64-512 bits, Euler partial-sum bracketing); item 3 rigorous. The -4/27
equality is offered as a calibration conjecture, not a theorem.

## Proof / evidence

- Exact group law over Q with fractions verifies all torsion claims.
- Regulator: mpmath polylog at 80 digits; per-term profile for z_U:
  n=-1: -0.74488, n=0: +0.05940, n=-2: +0.01286, tails geometric with
  ratio |q| ≈ 0.00433. Controls: D_q(-U) = -D_q(U) (oddness),
  D_q(V) ≈ -5.1e-20 ≈ 0, D_q((0,1)) ≈ -1.3e-19 ≈ 0 (2-torsion vanishing).
  Hence the signal comes entirely from the 6-torsion point U.
- Tate data: tau matches (-1+i sqrt(3))/2 to 1.4e-20, q matches
  -exp(-pi sqrt(3)) to ~1e-21, lifts match stated exponentials to ~1e-20.
- L-side: PARI lfun value identical at 64/128/256/512 bits; Dirichlet
  coefficients from LMFDB class 36.a (a7=-4, a13=2, a19=8) give partial sums
  0.94097 (N=50), 0.93917 (N=100), 0.94025 (N=199), bracketing 0.94001.
- Ratio: (L/pi)/D(xi) = -0.14814814814814814816 differs from -4/27 by ~1.3e-20;
  equivalently D(xi)/(L/pi) = -6.75 = -27/4 and (L/pi)/D(U) = -4/9.

## Limitations

- No interval-arithmetic enclosure of Li_2 sums, lattice tails, or L-value was
  produced; conversion to a fully rigorous interval disproof is left open.
- The PARI L-value and period routines were not re-executed in this audit
  environment (no cypari); cross-checks above bound the L-side adequately for
  the 0.4675 gap but do not replace certification.
- The -4/27 identity is conjectural at 2e-20 computed support.

## Reproducibility

Run from the lane root: python3 output/artifacts/compute_ratio.py (regulator +
L-value + ratio); python3 output/artifacts/closedform_check.py (CM closed forms
+ Euler partials). Environment: Python 3.12, mpmath 1.2.1 at 80 digits,
cypari/PARI 2.15.4 at 120-bit real precision (512-bit L-value recheck).

## References

- LMFDB isogeny class 36.a and L-function 2-6e2-1.1-c1-0-0 (conductor 36,
  Euler factors, L(E,1) = 0.7010910526).
- Zagier-Gangl, Classical and elliptic polylogarithms and special values of
  L-series; Goncharov-Levin elliptic Bloch complex / Zagier conjecture for
  modular curves over Q; Bloch formula for CM L(E,2); Bloch-Vanhove sunset
  elliptic dilogarithm; Nemoto Hesse-cubic regulators; Mellit elliptic
  dilogarithms and parallel lines (conductor 14).
- Scripts: output/artifacts/compute_ratio.py, closedform_check.py.
