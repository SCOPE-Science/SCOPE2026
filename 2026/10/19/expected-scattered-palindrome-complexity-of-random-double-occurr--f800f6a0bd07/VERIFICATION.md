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

# Verification

Run `python verification/check_random_double_occurrence_mean.py` with Python 3.9 or newer. This uses no external package. All distinct palindromic subsequences are generated independently from positional masks; exact rational averages over all first-appearance-normalized double-occurrence words for \(q\le5\) are compared with the formula. Numerical asymptotic ratios at larger \(q\) are reported as illustration only.

The infinite proof relies on double counting, uniform restrictions, an exact probability generating function, a moment bound, and a logarithmic-product limit; finite enumeration and numerical ratios are not infinite certificates.
