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

# Verification details
The all-length argument is the exact pair-of-embeddings identity in `RESULT.md`; it does not rely on a numerical recurrence. `verify_four_pattern_variances.py` recomputes the five overlap counts per orbit representative, verifies symmetry and coefficientwise ordering, and directly calculates moments over all \(2^n\) binary texts for \(4\le n\le11\). Execute `python3 verify_four_pattern_variances.py`. The test returned `VERIFY_OK`. The external independent audit has not been performed. Unindexed equivalent results are not ruled out by these checks.
