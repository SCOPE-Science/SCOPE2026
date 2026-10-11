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

# Reproducibility and verification

Execute `python verify.py` with Python 3 and SymPy; a successful run prints `VERIFY_OK`.

The checker independently simplifies the two-level fourth-moment expression, differentiates the one-variable rational function, checks its algebraic optimum and the irrationality-relevant product, tests equality witnesses for sizes from 2 through 27, and performs finite-dimensional sanity checks of the soft-threshold formula.

These finite tests and symbolic algebra are **not** a proof that a symmetric quartic is nonnegative on all real vectors in all dimensions. That step uses the published half-degree theorem of Riener, arXiv:1001.4464, Theorem 1.3. The exact global Lipschitz identification additionally uses the analytic piecewise-affine line-segment argument. The best-approximation exponent must be strictly between 1 and infinity, and all coordinates are real.

No independent scientific audit has been performed.
