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

# Reproducibility

Run `python VERIFY.py` (standard Python 3 only) to confirm selected exact integer cases of the theorem, Catalan valuations and congruence comparisons. A successful run ends with `VERIFY_OK`. The checker is a consistency test for eight exponents; the complete proof for all positive exponents is contained in `RESULT.md` and relies on Kummer's theorem and explicit three-adic carry bounds. Neither this check nor the review constitutes independent certification.
