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

The analytical proof consists of the exact binomial collision integral; the uniform \(u^{-3/2}\) Gaussian comparison; the binomial/Poisson coupling at fixed mesh distance; the summably bounded opposite-endpoint remainder; and a singularity-subtracted Riemann sum with the half-order zeta constant. It produces \(O(n^{-1/7})\) after cutoff balancing, uniformly over all positive integers \(n\) in the asymptotic sense. No optimized implied error constant or decimal interval certificate is asserted.

A standalone reproducible script `bernstein_collocation_check.py` uses Python's standard library only. It checks 12 exact-rational versus floating-point matrix energies, five independent Poisson collision comparisons, and the trend of six residual energies. Output from the packaged copy is `PASS` and a convergent sequence of residuals (approximately \(1.21145,1.23327,1.24946,1.26120,1.26963,1.27563\)). The finite checks do not establish the infinite theorem.

Scope: the real complete uniform-grid Bernstein collocation matrix in Euclidean coefficient norms; no individual singular-value, other mesh, or sharp error-rate assertion. The analytic proof is supplied in `RESULT.md`. Independent validation has not been performed.
