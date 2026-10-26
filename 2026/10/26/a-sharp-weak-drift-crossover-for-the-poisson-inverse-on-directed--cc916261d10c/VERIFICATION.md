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

The provided `check.py` runs on Python 3 with no third-party dependencies. It computes a Green column by two separate methods: the stated rational closed formula and Gaussian elimination applied to the cyclic operator augmented by the mean projection. For 14 sizes and five rational biases per size, it checks equality, zero mean, source/off-source equations and the column maximum. Additional numeric comparisons test the weak- and strong-drift asymptotic profiles. On the packaged source it reports `CHECKS_PASSED 953`.

Finite-dimensional checks cannot prove an asymptotic statement. The weak-drift limit is proved by dominated convergence of Fourier coefficients with a summable quadratic bound; the strong-drift limit is proved by an explicit finite-error inequality. An unperformed independent audit is not an external certification.
