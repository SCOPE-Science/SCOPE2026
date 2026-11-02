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

The exact algebraic proof and the supplied `verify.py` reproduce the companion matrices, sharp endpoint energy relations, and the determinant certificate on the full scalar Schur interval. Execute `python verify.py` with a Python 3 standard-library interpreter. Replayed result: 2,932 rational identities and finite switching checks passed.

The infinite switching theorem follows from the proved Loewner matrix inequalities and their products; 2,401 finite switching tests are illustrative checks, not exhaustive validation of arbitrary sequences. Smooth-equation order two does not imply order two across discontinuous switched coefficients. No independent scientific verification has been undertaken.
