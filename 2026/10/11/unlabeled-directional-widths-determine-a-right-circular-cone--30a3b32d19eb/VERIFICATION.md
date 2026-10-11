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

# Verification and reproduction

Run `python3 verify.py` with Python 3.8 or newer; the script requires no additional package. The completed run printed `VERIFY_OK 11140 finite checks; analytic proof in RESULT.md`.

The verifier implements the projected width from the geometric support function independently from the inverse-image cumulative distribution. For 35 cone aspect ratios, including the two branch thresholds and their nearby perturbations, it compares a 180001-point axial-cosine grid to the inverse-image cumulative distribution at 121 interior thresholds; differentiates the distribution numerically at up to 70 noncritical points; and checks support bounds, exact reconstruction, and the distinct same-endpoints counterpart. A fixed pseudo-random seed makes the tests reproducible. The all-parameter density, endpoint formulas, inversion and sharp ambiguity are proved analytically in `RESULT.md`. Grid tests provide finite corroboration only; they are not exhaustive and do not certify mathematical independence or originality.
