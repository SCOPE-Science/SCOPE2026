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

Run `python3 verify.py` with Python 3 and its standard library. The recorded execution ended `VERIFY_OK; exact assertions: 7820`.

The checker constructs the full directed-edge/visited-vertex state transition system, computes exact conditional first and second moments by rational linear equations, and compares with the stated closed formula for ten small bouquets. It separately checks the strict balancing inequality over bounded integer petal-length vectors. These computations provide strong finite consistency evidence but are not a substitute for the all-parameter proof. That proof appears in `RESULT.md` and uses petal excursions, geometric discovery stages, occupation-count covariance, and an exact positive coefficient.

The public artifacts assert no independent mathematical verification. Historical-priority checks are necessarily nonexhaustive.
