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

The complete parameter-uniform argument is given in `RESULT.md`. A standalone standard-library checker is supplied as `check.py`; execute it with `python3 check.py`.

The checker independently constructs polynomial-coefficient representatives and evaluates their induced functions in the actual split square-zero ring for parameters `(q,d)=(2,1),(2,2),(2,3),(3,1)` (all polynomial functions, not sampled functions). It checks the composition-idempotent predicate, precise image subsets, the number of functions onto each image, and every rank coefficient. The respective idempotent counts are `21,49,129,604`. Separately, all `531441` affine normal-form functions for `(q,d)=(3,2)` are enumerated, yielding `5374` idempotents and `1330` possible images. The exact expected output terminates with `BOUNDARY_ARITHMETIC_OK 32 parameter pairs` and `ALL_EXACT_CHECKS_PASSED`.

Those finite checks do not constitute proof for arbitrary finite fields or dimensions; proof for all parameters depends on Hermite interpolation over finite fields, the square-zero evaluation formula, and an exact count of all choices satisfying the resulting necessary-and-sufficient idempotence equations. No independent audit has been performed. The originality comparison has an explicitly identified full-text access limitation for the 2001 near-ring work.
