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

Exact verification uses `verify_klein.py` (SymPy) for the saturated elimination, degree-28 squarefree polynomial, factor degrees, contact-residue Euler tests, and resultant; `verify_rational.py` independently enumerates rational dual lines using Python standard library. Both scripts execute with assertions. The finite-field computation is exhaustive for the defined configuration, not evidence about other characteristics, twists, or publication-priority uniqueness.
