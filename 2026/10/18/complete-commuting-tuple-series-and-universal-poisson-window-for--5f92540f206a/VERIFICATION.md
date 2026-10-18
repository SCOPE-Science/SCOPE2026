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

Run `python3 brandt_commuting_checker.py` with Python 3 standard library only. The checker independently builds Brandt products and enumerates all commuting tuples up to selected lengths for three local groups and index sizes one through four. It compares all results to coefficients from the formal EGF derived by inclusion-exclusion. Its successful terminal line is `ALL_BRANDT_COMMUTING_COUNTS_PASSED 12`. This checker is exhaustive for its tested finite configurations, not a proof for arbitrarily large groups, tuple lengths, or the universal Poisson limit. The analytical proof in `RESULT.md` covers those statements. No independent audit or validation has been conducted.
