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

# Verification evidence and limits

The independently executable artifact `verify.py` uses the twelve maximal cones and eight primitive generators stated in the result. SymPy calculates all 18 toric wall relations symbolically in integer parameters, confirms the four affine certificate coordinates, and tests representative parameter values in the infinite wings. Running `python verify.py` produces four `VERIFY_OK` lines or raises an assertion.

The universal proof does not depend on bounded enumeration: the convex-hull certificates work for every integer parameter via an exhaustive inequality disjunction, and all wall degrees are symbolic formulas. The previously published hyperplane criterion is cited explicitly. No external or independent audit is represented by these checks.
