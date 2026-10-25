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

# Verification of the fourth-cumulant classification

Run `python3 verify.py` with Python 3.9 or later. This performs exact rational checks for five rate parameters, verifies the stated discriminant identity, reconstructs fourth cumulants independently from raw Gaussian-mixture moments, and tests explicit positive/negative/positive sign witnesses at a fixed rate.

The proof of positivity for every rate and the complete classification of roots are symbolic arguments in RESULT.md; a finite test suite alone would not establish either assertion. Gaussian conditional variances remain strictly positive for all allowed parameters, and no numerical root approximations are needed in the proof.
