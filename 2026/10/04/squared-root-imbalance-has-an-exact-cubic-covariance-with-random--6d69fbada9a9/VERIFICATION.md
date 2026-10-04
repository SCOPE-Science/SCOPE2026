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

The theorem is analytic. The accompanying checker uses exact integer and rational arithmetic.

It enumerates every insertion permutation through \(n=9\), reconstructs the corresponding Quicksort comparison count, and records the first-pivot rank.

For every tested order it verifies the classical mean and variance of internal path length, the conditional mean given the root split, strict increase of that conditional mean across the support of squared root imbalance, the exact covariance, the exact imbalance variance, and the least-squares slope.

A separate exact-rational loop verifies the finite harmonic-sum reduction used in the proof for hundreds of values of \(n\). The asymptotic constant is checked numerically from the exact formula but is proved analytically from
\[
H_n^{(2)}\to\frac{\pi^2}{6}.
\]

Independent audit has not been performed.

Exact replay result: `VERIFY_OK permutations_checked=409112 covariance_checks=8 conditional_mean_checks=44 monotone_regression_checks=8 marginal_moment_checks=16 imbalance_moment_checks=16 slope_checks=7 harmonic_reduction_checks=796 asymptotic_checks=7`.
