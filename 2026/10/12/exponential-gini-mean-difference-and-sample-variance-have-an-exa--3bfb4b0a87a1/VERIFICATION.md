---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The analytic proof uses the exact covariance formula for two normalized degree-two \(U\)-statistics, separating same-pair and one-index-overlap contributions.

The standalone checker reconstructs the conditional projection moments for standard exponential sampling using exact rational evaluation of exponential-polynomial integrals. In particular, it verifies
\[
\mathbb Ea(X)=1,
\qquad
\mathbb Eb(X)=1,
\qquad
\mathbb E[a(X)^2]=\frac43,
\qquad
\mathbb E[b(X)^2]=3,
\qquad
\mathbb E[a(X)b(X)]=\frac74.
\]
These values imply the mixed first-projection covariance \(3/4\), the Gini first-projection variance \(1/3\), and the variance-kernel first-projection variance \(2\).

The checker then validates the finite-\(n\) covariance and both marginal variances over a broad integer range using exact fractions.

A second route is independent of the conditional-projection calculation. It represents the ordered exponential sample by independent spacings, writes the Gini statistic as a linear form and the sample variance as a quadratic form, and evaluates their covariance from exact exponential moments. This spacing route agrees with
\[
\frac{3n-2}{n(n-1)}
\]
for every checked sample size in the unit-rate case.

The checker also verifies the exact positive difference of consecutive squared correlations and the limiting constant.

The finite computations are supplementary. The theorem for every integer \(n\ge2\) and every \(\lambda>0\) follows from the symbolic overlap calculation in `RESULT.md`.

Independent audit has not been performed.

Deterministic replay result: `VERIFY_OK conditional_exact=5 ustat_cov_checks=199 ustat_var_checks=398 spacing_checks=39 monotonicity_checks=199 limit_rho=0.9185586535436917`.
