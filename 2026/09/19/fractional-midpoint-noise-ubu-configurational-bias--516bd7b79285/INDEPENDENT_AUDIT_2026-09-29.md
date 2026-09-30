# Independent Audit — 2026/09/19/fractional-midpoint-noise-ubu-configurational-bias--516bd7b79285

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `7ddf8ebc51ba4e6605f34401e25d9ab9f9185d93`
- Disposition: **PASSED**

## Correctness

**PASS** — The quadratic-target calculation is internally consistent and was independently recomputed from the displayed deterministic transition and one-step covariance. Because the transition matrix is theta-independent while the noise covariance is exactly quadratic in theta, the discrete Lyapunov solution is exactly quadratic in theta throughout the stable regime. A fresh direct Lyapunov solve for gamma=3, alpha=lambda=1 gives, as h decreases from 0.05 to 0.0125, LC error/h^2 0.07728→0.08178 toward 1/12, theta=1/3 error/h^3 -0.08051→-0.08263 toward -1/12, UBU error/h^2 -0.16658→-0.16666 toward -1/6, and the friction-corrected error/h^4 0.01580→0.01497 toward 127/8640. The implicit-function argument for a unique scalar exact-zero-bias branch near theta=1/3 is valid because the normalized bias derivative at (1/3,0) is -k/4≠0. The claims are correctly limited to stationary configurational covariance for Gaussian targets rather than nonlinear weak/strong trajectory order.

## Originality

**PASS** — The September 2026 Lyu-Wang-Yang preprint introduces the low-cost UBU family and a universal predictor-corrector framework, but its stated results are Wasserstein convergence bounds and cost reductions; no theta-fractional midpoint-noise covariance interpolation, one-third cancellation law, or friction-only fourth-order Gaussian covariance correction was located. Configurational superconvergence and harmonic covariance analysis are established prior art, so novelty is not assigned to those general ideas. Targeted searches of the new LC-UBU source and older UBU/configurational-sampling literature did not locate the source-specific exact quadratic-in-theta stationary covariance law or the universal theta=1/3 cancellation. Given the motivating preprint's recency, contemporaneous unindexed work remains a residual risk, but the submitted claim is sufficiently narrow and distinct.

## Scientific value

**PASS** — The result explains a concrete bias tradeoff created by removing the stochastic midpoint in LC-UBU: the leading covariance error changes sign and magnitude, and a universal partial-noise choice cancels the O(h^2) term for every Gaussian Hessian. The h-dependent correction further shows precisely how far a spectrum-independent scalar tuning can go before Hessian dependence enters. This is useful for algorithm design and diagnostic comparison even though any nonzero theta forfeits the reduced Gaussian count that motivated LC-UBU.

## Sources

- A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New (Wanjie Lyu; Xiaojie Wang; Bin Yang): https://arxiv.org/abs/2609.20713 — Primary 2026 source introducing LC-UBU and the universal predictor-corrector framework; its abstract emphasizes cost and W1/W2 convergence rates rather than the audited stationary-covariance interpolation.
- Wasserstein distance estimates for the distributions of numerical approximations to ergodic stochastic differential equations (J. M. Sanz-Serna; K. C. Zygalakis): https://www.jmlr.org/papers/v22/21-0453.html — Prior UBU/Langevin numerical-analysis background; not a source for the audited theta-interpolation formulas.
- Robust and efficient configurational molecular sampling via Langevin dynamics (Benedict Leimkuhler; Charles Matthews): https://doi.org/10.1063/1.4802990 — Classical configurational-superconvergence background, establishing that the general phenomenon itself is prior art.

## Limitations

- Only quadratic Gaussian targets and stationary position covariance are covered.
- Nonzero theta requires the midpoint Gaussian and therefore loses LC-UBU's reduced random-number count.
- The exact finite-step zero-bias choice is mode-dependent beyond the displayed universal orders.
- The motivating LC-UBU source is very recent, leaving a residual priority risk for unindexed follow-up work.

## Independent checks

```json
{
  "direct_lyapunov_recomputation": true,
  "h_values": [
    0.05,
    0.025,
    0.0125
  ],
  "theta_quadratic_structure_checked": true,
  "source_tree_unchanged": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked first. The scientific conclusions above are independent of the record's same-model review.
