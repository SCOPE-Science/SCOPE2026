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

# Reproducibility and limits

Run `python3 verify_gaussian.py` using standard Python. The test script checks rational row stochasticity, reversibility, nonzero modes, and the total-variation coefficient; 999 rational values of the Gaussian overlap identity and strict determinant positivity; the threshold polynomial with a rational bracket; the analytic derivative factor using finite differences as a check; and seven independent double-precision calculations from the full three-state Gaussian Gram matrix.

For a proof valid at every bandwidth, inspect `RESULT.md`, especially the Gaussian Fourier positivity argument, generalized Rayleigh quotient maximization, factored strictly positive derivative and Taylor expansions of the determinant. Exact-rational checks cover finitely many cases only; they cannot prove the global threshold, singular limit or uniqueness by themselves. The original motivating preprint and related matrix-conditioning literature are cited in `RESULT.md`. Independent validation has not been performed.
