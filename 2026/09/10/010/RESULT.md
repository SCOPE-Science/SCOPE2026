# Wall-concentrated extremal datum blocking the mandated D=3 step at the Guth endpoint

## Context

The Fourier restriction problem for the paraboloid in R^3 asks for which
exponents p the extension bound
||E_S f||_{L^p(R^3)} <= C ||f||_2 holds. Stein-Tomas gives p >= 4;
Guth (arXiv:1407.1916) proved p > 3.25 for smooth compact S in R^3 with
strictly positive second fundamental form, via polynomial partitioning.
Whether the endpoint p0 = 3.25 is stable under a fixed C^2 perturbation,
and where a one-step degree-3 narrow-vs-broad attack stalls, is the
recognized local frontier with downstream use in PDE Strichartz,
point-tube incidence/Kakeya, and exponential-sum estimates.

## Definitions

- Fixed surface: h0(xi1,xi2) = (xi1^2+xi2^2)/2 + (0.05/6) xi1^3 on the
  unit disc. D^2 h0 = diag(1+0.05 xi1, 1),
  det D^2 h0 = 1+0.05 xi1 in [0.95, 1.05]; ellipticity preserved.
- Extension: E_{h0} f(x) = int_{|xi|<=1} e^{i(x'.xi + x3 h0(xi))} f(xi) dxi.
- Exponent p0 = 3.25 = 13/4 (Guth endpoint); scale R = 100; degree D = 3.
- Baseline e_ST = 3(1/p0 - 1/4) = 9/52 ~= 0.17308 (Hoelder down from the
  Tomas-Stein L^4 bound); target shaving 0.02, e_T = e_ST - 0.02 = 199/1300.
  Knapp floor exponent 2/p0 - 1/2 = 3/26 ~= 0.11538 < e_T (target Knapp-legal).
- Partition polynomial P*(x) = x1 x2 x3 (degree 3);
  wall W = N_{10}(Z(P*)) cap B_100 (width R^{1/2} = 10);
  cap radius R^{-1/2} = 0.1.
- Datum: f* = (1/0.792665) sum_{k=1}^5 1_{B((0,t_k),0.2)},
  t_k = -0.8, -0.4, 0, 0.4, 0.8, supported in the unit disc, ||f*||_2 = 1
  (||sum 1||_2^2 = 5 pi (0.2)^2; discs tangent-disjoint).
  Frequency caps lie on the xi1 = 0 line, so every tube direction has zero
  first component and every centerline from x1 = 0 keeps x1(s) = 0, i.e. lies
  on the wall plane {x1 = 0} subset Z(P*).

## Result (headline claim)

For the fixed h0 above at scale R = 100 with degree D = 3, the explicit
L2-normalized datum f* satisfies the wall-concentration ratio

  rho = ||E f*||_{L^{3.25}(W)}^{3.25} / ||E f*||_{L^{3.25}(B_{100})}^{3.25}
      = 0.9701 >= 0.70

(fine grid; coarse grid 0.9793; independent uniform-ball Monte Carlo ~0.956),
with tube counts W = 5/5 (fat caps) and W = 25/25 (R^{-1/2} subcaps),
W/Wmax = 1.0 >= 0.70 for P* = x1 x2 x3, and narrow/broad split
N = 0.00000 / B = 1.00000 with N + B = 1 (within 0.01), certified by a
reproducible cell-vs-wall table. By-plane split (overlapping):
{|x1| <= 10} carries 0.94, {|x2| <= 10} carries 0.62,
{|x3| <= 10} carries 0.34 -- concentration sits on the hugging plane.
The table blocks the mandated single-D=3-step plus single
narrow/broad-decoupling route to a delta >= 0.02 improvement: the cellular
branch carries <= 3% of the energy yet closes with factor
D^{3-p-e_T p} = 3^{-0.7475} = 0.44 < 1, while the wall branch (which must
carry >= 97%) has available single-step power gain 0 (l2-decoupling constant
C_dec >= 1 exact by the single-cap test; Tao bilinear endpoint-excluded at
p0/2 = 1.625; Guth strict p > 3.25; trilinear/k-broad miss planar tangent
mass or carry only R^delta losses), for a route-specific shortfall of the
full 0.02. The target inequality with exponent e_T itself is NOT refuted:
it is Knapp-legal and possibly true via multiscale routes.

## Proof / evidence

- (i) f*: normalization verified analytically; support in the unit disc
  (farthest point (0,1.0)); wall-bound centerlines by the xi1 = 0 design.
- (ii) Tree: P* = x1 x2 x3 at R = 100 with full fat and subcap tube lists
  (bases, directions, wall fractions), recomputed by
  `python3 verify_NB_W.py` and `python3 fallback_certificate.py`
  (both VERIFY_OK; W = 5/5 and 25/25).
- (iii) N/B: subcap-pair census at threshold R^{-1/2} = 0.1 gives
  N = 0.00000, B = 1.00000, N + B = 1 exactly; protocol-specific, disclosed.
- (iv) rho: direct Riemann-quadrature evaluation of E f* --
  coarse grid (x1 +-20 step 1, x2 step 4, x3 step 5): rho = 0.9793;
  fine grid (x1 +-30 step 1, x2 step 2, x3 step 2.5, m = 14 per cap,
  780 cap points): rho = 0.9701; margin 0.27 over threshold.
  Reproduce: `python3 verify_fan_rho.py`, `python3 verify_fan_rho_fine.py`.
  Error budget: transverse tail beyond |x1| = 30 at ~0.4% of total
  (field profile |Ef|(20,0,0) ~ 0.019, decaying); x3-step refinement
  changes column sums by ~0.1%; cap refinement m = 10 -> 14 shifts grids
  consistently (0.9793 -> 0.9701). Errors are two orders of magnitude
  below the margin. Independent uniform-in-B_100 Monte Carlo (N = 4000)
  gives rho ~ 0.956, consistent.
- Blocking: cellular factor 0.44 closes; wall-tangent single-step inputs
  audited with exact decoupling floor (C_dec >= 1); S9 sweep finds no
  mandate-compliant rescue via P-choice, K-threshold, or fixed-D change.
- Prior comparison: Bourgain-Guth (generic multilinear-to-linear),
  Bourgain-Demeter (generic l2-decoupling), Tao (generic bilinear up to
  endpoint), Guth (generic strict p > 3.25, L_inf data), Li (hyperbolic,
  n >= 5) -- none logs a fixed-h0 (eps = 0.05), R = 100, D = 3
  wall-concentration table with rho >= 0.70.

## Limitations

- rho is quadrature-certified (two grids + tail/step analysis + independent
  Monte Carlo), not interval-arithmetic proved; margin 0.27 dominates the
  error budget but an independent re-run is the check.
- The blocking argument is a route audit (survey of available one-step
  inputs with the exact decoupling floor), not an impossibility theorem:
  the target inequality with exponent e_T stays Knapp-legal and possibly
  true via multiscale routes.
- N = 0 is protocol-specific (pair census on the committed subcap
  decomposition); the certificate's force sits in W/rho, which pass either way.
- Wall N_10(Z(P*)) has large volume in B_100; quote the by-plane split
  ({|x1| <= 10} 0.94 vs ~0.15 volume share) alongside rho.
- Perturbation stability (eps = 0.05: tilt <= 0.025, displacement <= 2.5 < 10,
  cap-local phase 8.3e-4) means the mechanism is not a perturbation artifact;
  constants above are for the stated h0.

## Reproducibility

stdlib + numpy only:
`python3 fallback_certificate.py`, `python3 verify_NB_W.py`,
`python3 verify_fan_rho.py`, `python3 verify_fan_rho_fine.py`.
All four exit VERIFY_OK / print matching rho values.

## References

- L. Guth, A restriction estimate using polynomial partitioning,
  arXiv:1407.1916 (p > 3.25, generic positive-curvature S, strict endpoint).
- J. Bourgain and C. Demeter, Decouplings for curves and hypersurfaces with
  nonzero Gaussian curvature, arXiv:1409.1634 (generic l2-decoupling).
- T. Tao, A sharp bilinear restriction estimate for paraboloids,
  arXiv:math/0210084 (generic bilinear, endpoint-excluded).
- J. Bourgain and L. Guth, Bounds on oscillatory integral operators based on
  multilinear estimates, arXiv:1012.3760 (generic broad-narrow).
- X. Li, Restriction estimates for hyperbolic paraboloids in higher
  dimensions, arXiv:2407.08549 (hyperbolic, n >= 5; different object).
