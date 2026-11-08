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

# Reproducible mathematical verification

The exact theorem and definitions are in `RESULT.md`. The included `verify.py` checks two analytic representations of the characteristic function, the positive subordinator transform, stationary second/fourth coordinate moments, strict Bessel-profile signs for dimensions one through six, high-precision dimension-two small-radius ratios, and numerical radial integration of the proposed compound-Poisson density. Run `python verify.py` with NumPy, SciPy and mpmath. The checker returned `PASS: 393 computational diagnostic assertions` on the delivered sources before packaging.

The proof of every-dimensional necessity and sufficiency is the analytic Bessel identity and the polar Lévy monotonicity test. Finite samples or numerical quadrature cannot prove those assertions, nor do they provide independent audit or publication-priority certification. The source paper's stationary transform is known; the scalar marginal threshold and general subordination criteria are known. Independent scientific audit: not performed.
