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

# Verification instructions

Run `python check.py` from the directory containing this file, using Python with SymPy, NumPy, and SciPy installed. The checker is standalone; it imports no local modules or datasets. Its recorded stdout is in `check_output.txt`.

The symbolic checks expand the exact differentiated Gegenbauer equation and derivative of the boundary product for several rational parameters and degrees. Root isolation corroborates the predicted finite counts. Independent numerical integration compares normalized cap integrals with their closed-form boundary products. A separate high-dimensional root comparison uses library Gegenbauer and Hermite zeros.

This is finite supporting verification only. The all-degree, all-dimensional conclusions follow analytically from the polar separation, norm recurrence, differentiated Gegenbauer equation, strict root interlacing, parity, and compact-limit domination spelled out in `RESULT.md`. Mathematical priority and independent audit have not been verified.
