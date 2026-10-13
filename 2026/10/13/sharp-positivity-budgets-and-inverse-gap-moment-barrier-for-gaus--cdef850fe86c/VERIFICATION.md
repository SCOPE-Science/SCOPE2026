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

# Reproduction and limits

Install the two packages specified in `requirements.txt` and run `python verify.py` from this directory. It prints `VERIFY_OK` upon successful completion of 74 distinct algebraic/numerical checks, including exact-rational construction of the worst-case pair, independent Student/beta comparisons, a Gaussian Monte Carlo reconstruction, and numerical quadrature of the regularized spectral condition number. Independent review and external validation have not been performed.

All-parameter statements, limiting budgets, divergence of the first condition-number moment and the logarithmic prefactor are analytic results proved in `RESULT.md`; finite computations only check representative cases. No computation is represented as a proof of integrability or of infinite-dimensional coverage.
