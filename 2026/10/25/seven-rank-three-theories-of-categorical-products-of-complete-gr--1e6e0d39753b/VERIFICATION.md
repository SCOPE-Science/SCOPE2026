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

Execute `python3 verify.py` from the directory containing the delivered artifacts. The program requires only Python's standard library and asserts seven distinct representative extension profiles, direct third-point signatures for 54 bounded coordinate vectors, an independent symbolic criterion on 494 vectors, and 28 direct recursive three-round EF games for the representative pairs plus eight cross-size games. Its recorded stdout is in `verification_output.txt`. Successful reproduction terminates in `VERIFY_OK`.

The mathematical proof of the infinite theorem is the coordinate construction and three-round back-and-forth argument in `RESULT.md`. The finite tests check for accidental formula, boundary, or implementation mistakes but do not prove the unrestricted assertion. A separate independent mathematical audit has not been performed.
