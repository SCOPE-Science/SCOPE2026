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

Run `python3 checker.py` with Python 3.9 or later. The file has no third-party dependencies. It independently constructs all tested cyclic rotations and checks all proper border lengths, compares to the claimed rule, and separately reconstructs necklace spectra and orbit counts. The tested maximum is thirty zeros; a finite test cannot establish the formulas for every circumference. The full all-length proof is in `RESULT.md`. No independent external audit has been performed.
