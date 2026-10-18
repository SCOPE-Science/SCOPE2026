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

A proof is given in `RESULT.md` and rests on four exact steps: interval-factor overlap, a unique root of a strictly increasing quartic on a bounded half-angle range, unique upper-branch stationary orientation from an increasing cubic numerator, and the envelope calculation at the discontinuity.

The bundled standalone `verify.py` runs with Python 3's standard library and outputs `RECTANGLE_COVARIOGRAM_CHECK_OK comparisons=285` after evaluating 285 independent finite diagnostic comparisons across unequal aspect ratios, translation distances and angular samples. The numerical checks do not constitute an exhaustive verification of continuum angles, continuous aspect ratios or all possible distances; the analytic proof provides those quantifiers.

The square/hypercube case belongs to prior work and is excluded. No independent audit, publication-priority certification, or third-party verification has been performed.
