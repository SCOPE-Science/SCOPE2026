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

# Reproduction checks and limits

Run `python verify.py` with Python 3 and NumPy. The source file is shipped inside this same package. The completed execution returned `PASS: 384994 independent finite checks`; the checker independently constructs each enumerated matrix residual and evaluates its singular values, rather than merely replaying the derived formulas. Rational enumerations check exact probabilities; derivative and Poisson tests are finite numerical cross-checks only.

The mathematical proof of the distribution and unique optimizers is in `RESULT.md`. Finite computations cannot certify the infinite-dimensional family or originality. No independent audit has been performed. The checker applies to exact projectors in double precision for numerical matrix comparisons; rounding tolerances are stated in source.
