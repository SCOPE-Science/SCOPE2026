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

# Verification and reproducibility

Run `python3 checker.py` with standard-library Python. It checks the two-moment formula against direct enumeration for nine independent rational cases with 3–6 agents over up to five updates, and checks the Perron-root equation on additional finite cases. Observed output: `EXACT_CHECKS_PASSED 145; enumerated_update_strings=14744; configs=9`.

The all-time and all-parameter results are proved analytically in `RESULT.md`. Finite tests alone would not establish either infinite-time asymptotic or uniqueness of the Perron mode. The proof makes the non-clipping hypothesis explicit; it does not claim extrapolation outside that neighborhood. The checker and file hashes provide reproducibility, not independent scientific validation.
