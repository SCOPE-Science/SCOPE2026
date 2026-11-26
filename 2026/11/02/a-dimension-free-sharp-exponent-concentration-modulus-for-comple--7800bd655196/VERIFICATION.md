---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification and reproducibility

The analytic proof in `RESULT.md` computes the full norm by the maximum-modulus principle, an exact phase maximization, and a one-variable trigonometric maximization. It also derives a linear estimate for a single retained coordinate by the disk Schwarz–Pick bound. The general upper square-root estimate is the stated specialization of prior work.

Run `python3 checker.py` to check exact rational Pythagorean instances of the optimizing angle and error/deficit identity. These finite calculations are illustrative; sharpness as the deficit tends to zero and the uniform estimates follow from the proof.
