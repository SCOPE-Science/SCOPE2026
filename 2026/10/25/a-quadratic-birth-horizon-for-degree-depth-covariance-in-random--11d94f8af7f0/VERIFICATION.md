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

# Verification of exact degree–depth covariance

Run `python verify.py` with Python 3 standard library. The script checks the exact covariance of child counts and depths for every ordered vertex pair in all recursive trees of orders \(2\) through \(9\). It enumerates 46,233 trees in total, verifies the universal covariance decrement, and uses exact rational arithmetic to check transitions for source labels \(2\) through \(30\). The actual executable produces `VERIFY_OK` only when all checks pass.

The proof of the universal finite formula, the existence of a unique sign transition, and its quadratic asymptotic location is provided in `RESULT.md`. Enumeration cannot establish a statement for arbitrary order, and an asymptotic Euler–Maclaurin error estimate is not numerically certified by exhaustive testing.

Independent audit: not performed.
