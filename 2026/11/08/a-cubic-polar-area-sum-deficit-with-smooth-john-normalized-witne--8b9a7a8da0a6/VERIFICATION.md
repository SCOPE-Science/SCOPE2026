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

The analytic derivation is in `RESULT.md`. The independent standard-library numerical script `verify_area_sum.py` was executed from the actual source file and passed 122 assertions/checks. It compares primal circumscribed-polygon shoelace areas and polar-polygon shoelace areas with the exact closed forms for multiple angular frequencies and deformations. It also evaluates the smooth support-function area identity and the local cubic coefficient.

Run `python3 verify_area_sum.py` with Python 3. The finite tests are supplementary. No independent audit, formal proof certificate, or global cubic stability lower bound is claimed.
