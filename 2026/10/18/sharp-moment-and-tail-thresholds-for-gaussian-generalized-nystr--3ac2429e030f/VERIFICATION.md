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

Run `python verify.py` from the directory containing this document. Required third-party Python packages: NumPy and SciPy. A deterministic random seed is set directly in the program. Successful execution prints `PASS checks=16453 maximum_numerical_discrepancy=1.76e-08` (the count is deterministic; small floating-point residuals can vary by platform).

The script independently constructs Gaussian sketches, recomputes leave-one-right-out fits, compares them to normal-coordinate orthogonal decompositions and a fast square-matrix inverse relation, checks leave-pair/twin rank-one formulas using independently constructed random null vectors, and compares inverse chi-square first/second moments with numerical quadrature. All numeric checks passed in the stated execution, with floating-point tolerances specified in code.

The sharp moment and exact-law statements follow from the paper proof: orthogonal decomposition, multivariate Student coefficient density, chi-square lower-tail powers, spherical beta angles, and finite-sum moment inequalities. Simulations cannot establish infinite moments, the exact tail constants, or bibliographic novelty. Dependent pooled leave-out terms are not modeled as independent.

The result is specific to identity input and iid real Gaussian sketches. No independent audit has been performed.
