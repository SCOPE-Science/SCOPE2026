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

Run `python check_spectrum.py` with Python 3.9 or later. The checker evaluates normalized Gegenbauer polynomials using exact rational recurrence, builds normalized roots without floating point, and compares direct Gram action with each stated eigenvalue on explicit independent-sector witnesses in 55 parameter cases. It separately checks 532 low-degree rational rank identities and the two exceptional zero levels. These are finite reproducibility checks; the all-degree proof is the Walsh-and-Johnson block reduction in RESULT.md. Independent external validation has not been performed.
