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

Run `python3 verify.py` from the extracted package directory. The observed output was `VERIFY_OK: exact adjacent-sector integrals and sharp angular-energy bound`.

The script integrates the positive-quadrant adjacent-side distance constraint by composite Simpson quadrature for six distinct interior angles, independently compares with the sector/Jacobian prediction, and checks the angle-energy inequality for five alternating normal-gap sequences. The analytic proof covers every convex polygon; this finite verification checks numerical consistency only. There is no independent scientific audit.
