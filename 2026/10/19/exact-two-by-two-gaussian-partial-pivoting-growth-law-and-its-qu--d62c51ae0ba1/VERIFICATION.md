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

The complete analytic theorem, with its quantifiers and limits, is proved in `RESULT.md`. The accompanying `CHECK.py` uses only Python 3 standard-library modules.

Run `python3 CHECK.py` in a directory containing that file. Successful output ends with `GEPP_GROWTH_CHECK_OK`. It compares the explicitly integrated two-dimensional Rayleigh-angle formula against the one-dimensional primitive at six thresholds, compares three near-endpoint ratios to the analytic limit, and independently checks three thresholds using 160,000 seeded Gaussian matrices. The executed checks corroborate, but do not replace, the exact probability derivation and endpoint Taylor argument. The numerical atom is not a formally certified rounding interval.

Independent audit has not been performed. No statement about other dimensions, floating-point behavior, or earlier unindexed derivations is certified.
