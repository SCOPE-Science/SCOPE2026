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

# Verification procedure

Run `python checker.py` with Python 3's standard library. It must print `LATTICE_PERIOD_CHECK_OK cases=42` after checking all pairs of integer lattice points in each of 42 test polygons. The bounding rectangle used in the enumeration contains the full dilated parallelogram. Arithmetic uses exact integer inequalities and greatest common divisors, avoiding floating-point rounding.

The proof in `RESULT.md` covers all \(m\ge2\) and \(n\ge1\); the 42 finite checks are non-exhaustive across these infinite ranges. The least-period assertion is analytically verified by the pairwise distinct constituent slopes, not inferred from observed numerical sequences. No independent scientific audit has occurred.
