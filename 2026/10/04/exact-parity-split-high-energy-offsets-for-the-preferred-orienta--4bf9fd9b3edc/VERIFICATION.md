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

Run `python3 verify.py` in the same directory. The script uses only the Python standard library. It reconstructs the limiting sector coefficients from the displayed dodecahedral secular expression, verifies every claimed factor and its simplicity, evaluates the full displayed asymptotic secular expression at the predicted scaled offsets, and bisects representative finite-index roots of that displayed equation.

The exact proof does not depend on a finite enumeration. The numerical checks are consistency tests for the transcription and asymptotic scaling. The scientific conclusion rests on the algebraic factorization of the limiting sector polynomial together with simple-zero stability for the analytic secular determinant.

The verification does not classify branches with vanishing first scaled offset in even cells and does not establish next-order corrections. Independent audit status is not performed.
