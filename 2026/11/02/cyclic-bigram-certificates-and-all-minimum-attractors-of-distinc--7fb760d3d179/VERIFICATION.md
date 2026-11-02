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

# Verification record

The proof uses a constructive alignment argument for short factors and an overlapping-occurrence strip for long factors. It does not rely on computational extrapolation. The separate finite checker enumerates all single-position-per-letter candidates for 307 parameter families, builds literal factor-occurrence coverage masks, and compares their complete attractor truth values with the short-factor condition and a separately implemented exact inclusion–exclusion count.

Command: `python verify.py`

Observed output:

```text
VERIFY_OK families=307 candidate_sets=125015 distinct_factor_profiles=29362 literal_vs_local_and_IE=TRUE all_long_runs=TRUE all_singletons=TRUE
```

Checked values include alphabet sizes 2 through 5, periods 2 through 4, positive run lengths mostly 1 through 3, and word length at most 24. Binary cases test the boundary, but the theorem is asserted only for three or more distinct letters. Larger parameter choices are covered by the proof, not exhaustively searched. No external or independent audit has been performed.
