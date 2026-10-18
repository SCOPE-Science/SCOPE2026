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

Run `python check.py` from the extracted directory, using Python 3 with only the standard library. The script produces `VERIFY_OK 12000 exact arithmetic comparisons` on successful execution. The test was actually run on the enclosed source. It verifies the three exact logarithmic generator derivatives for rational input states, the tangent breakpoints and concavity polynomial, rational-grid inequalities for the envelope, the abstract two-point extremizers, and the strict exact example comparison.

The analytic invariant-measure argument is not replaced by these finite computations: its crucial step is applying generator invariance to a continuum of risk-coordinate test functions and invoking conditional expectation. The compact invariant-set conclusion then uses the usual time-average weak-limit argument. No numerical search for trajectories is asserted to certify recurrence exclusion. The motivating paper's separate supplementary PDF was not materially inspected; any equivalent claim there is an acknowledged originality risk.
