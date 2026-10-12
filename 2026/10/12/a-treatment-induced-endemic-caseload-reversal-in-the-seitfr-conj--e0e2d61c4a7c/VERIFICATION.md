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

Run `python3 verify.py` in the same directory as the other files. It requires only Python 3 standard-library modules and prints `VERIFY_OK` upon successful completion.

The script recomputes the source SEITFR equilibrium relations with exact fractions at strictly positive treatment rates, checks all six original vector-field residuals, checks both derivative polynomials coefficient-by-coefficient, checks the explicit initial derivative condition, and compares the two positive-rate endemic fractions exactly. The continuum-wide sign conclusions and uniqueness of the clinical-caseload maximum follow from the written polynomial argument; finite substitution checks alone would not establish them. No observational or independent validation is asserted.
