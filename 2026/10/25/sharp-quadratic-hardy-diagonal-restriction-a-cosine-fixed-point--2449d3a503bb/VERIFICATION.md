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

Run `python3 checker.py` after extracting the complete package. The standard-library script checks circle means, the optimal integrable endpoint, sample complex coefficients versus their symmetrizations, the scalar minimizers at seven exponents, and the Hilbert limit. It passed 848 deterministic assertions during direct execution.

The infinite family of coefficient inequalities is proved by symmetry reduction and convexity in `RESULT.md`; discrete numerical sampling is not a proof. The logarithmic slope is obtained by differentiation and exact Fourier coefficients, not a numerical fit. The operator norm is for quadratic homogeneous polynomials only. Independent audit is not performed.
