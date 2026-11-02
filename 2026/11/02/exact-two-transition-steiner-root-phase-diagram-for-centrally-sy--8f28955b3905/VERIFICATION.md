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

# Reproducibility and proof boundaries

Run `python3 verify_bicone.py` from the directory containing the extracted artifact. The program uses only the Python standard library for exact rational interval checks. SymPy, when available, provides optional symbolic algebra checks.

The program verifies strict signs of both transition functions at the rational aspect ratios in the theorem, the negative small-aspect limit of the cubic discriminant, and symbolic identities for the discriminant, both transition derivatives, and the stationary-point values. The program returns `FINAL_VERIFY_OK` if all implemented checks succeed; it was executed successfully from its actual packaged path.

The continuum claims require the explicit analytic identities and strict Minkowski inequality in `RESULT.md`. A finite list of signs alone cannot show uniqueness of zero crossings; that uniqueness comes from the globally positive derivative identities. Numerical aspect-ratio approximations are not used as proof.
